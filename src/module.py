from pydantic import BaseModel
from typing import List


class Input(BaseModel):
    plasma_glucose: float
    blood_work_result_1: float
    blood_pressure: float
    blood_work_result_2: float
    blood_work_result_3: float
    body_mass_index: float
    blood_work_result_4: float
    age: int 
    insurance: bool


class Inputs(BaseModel):
    all: List[Input]

    def return_dict_inputs(
            cls,
    ):
        return [ input.dict() for input in cls.all]
