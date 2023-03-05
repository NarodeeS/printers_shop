from pydantic import BaseModel, Field


class CreateWorkerSchema(BaseModel):
    name: str = Field(max_length=50)
    surname: str = Field(max_length=50)
    login: str = Field(max_length=50)
    mobile_number: int
    email: str = Field(max_length=255)
    position_code: int
    
    class Config:
        orm_mode = True
    

class ReturnWorkerSchema(CreateWorkerSchema):
    id: int


class CreatePrinterSchema(BaseModel):
    manufacturer:str 
    printer_name: str 
    paper_weight: int
    colors_number: int 
    resolution:str  
    print_speed: int
    cartridge_count: int 
    tray_capacity: int 
    paper_format: str
    category_id: str
    amount: int 
    price: int


class ReturnCategorySchema(BaseModel):
    id: str
    name: str
    