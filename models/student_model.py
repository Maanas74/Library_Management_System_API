from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from bson import ObjectId


class Address(BaseModel):
    city : str
    country : str

class Student(BaseModel):
    name : str = Field(...)
    age : int = Field(..., gt=0)
    address : Address
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True)
    

class Update_Student(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[Address] = None
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )


