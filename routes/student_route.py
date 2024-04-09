from fastapi import APIRouter , status , HTTPException, Response
from config.connectDB import collection
from models.student_model import Student, Update_Student
from pymongo import ReturnDocument
from schema.schema_student import student_data
from bson import ObjectId


stu = APIRouter()

@stu.post(
    "/students/",    
    response_description="Add new student",
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
    )
async def adding_student(student : Student) -> dict: 
    new_student = collection.insert_one(student.model_dump(by_alias=True))
    return {"_id": str(new_student.inserted_id)}

@stu.get(
    "/students/",
    response_description="List all students",
    response_model_by_alias=False,
)
async def list_students(country: str = None, age: int = None):
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}
    students_list = []
    for student in collection.find(query):
        students_list.append(student_data(student))
    return students_list


@stu.get(
    "/students/{id}",
    response_description="Get a single student",
    response_model=Student,
    response_model_by_alias=False,
)
async def show_student(id: str):
    if (
        student := collection.find_one({"_id": ObjectId(id)})
    ) is not None:
        return student

    raise HTTPException(status_code=404, detail=f"Student {id} not found")


@stu.patch(
    "/students/{id}",
    response_description="Update a student",
    response_model_by_alias=False,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def update_student(id: str, student: Update_Student):
    student = {
        k: v for k, v in student.model_dump(by_alias=True).items() if v is not None
    }

    if len(student) >= 1:
        update_result = collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": student},
            return_document=ReturnDocument.AFTER,
        )
        if update_result is not None:
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(status_code=404, detail=f"Student {id} not found")

    if (collection.find_one({"_id": ObjectId(id)})) is not None:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=404, detail=f"Student {id} not found")


@stu.delete("/students/{id}", response_description="Delete a student")
async def delete_student(id: str):
    delete_result = collection.delete_one({"_id": ObjectId(id)})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_200_OK)

    raise HTTPException(status_code=404, detail=f"Student {id} not found")