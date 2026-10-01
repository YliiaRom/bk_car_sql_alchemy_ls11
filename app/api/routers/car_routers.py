from fastapi import APIRouter,status,HTTPException
from sqlalchemy.exc import IntegrityError
from app.models.shemas import CarUpdate, CarCreate, CarBase,CarResponse
from app.services.car_service import create_car,get_cars,get_one_car, update_car,delete_car,get_car_by_filter
from app.dependencies import SessionDep

from app.models.models import BodyType 


router = APIRouter(prefix="/cars", tags=["car"])

@router.post('/add', response_model=CarResponse, status_code=status.HTTP_201_CREATED)
def create_new_car(db:SessionDep, payload:CarCreate)-> CarResponse:
  try:
    return create_car(db,payload)
  except IntegrityError:
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="car info incorrect")


@router.get("/", response_model=list[CarResponse])
def get_all_cars(db:SessionDep,body_type:BodyType | None = None,year:int | None =None, seller_name:str | None = None, is_available:bool | None =None, min_rating:int | None = None, limit:int=20,offset:int= 0):
  return get_car_by_filter(db, body_type,year,seller_name,is_available,min_rating,limit,offset)

@router.get("/{car_id}", response_model=CarResponse)
def get_car(db:SessionDep, car_id:int):
  car  = get_one_car(db, car_id)
  if car is  None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Сar Not Found")
  return car


@router.patch("/{car_id}", response_model=CarResponse, status_code=status.HTTP_200_OK)
def update_car_val(db:SessionDep, car_id:int, payload:CarUpdate):
  car = get_one_car(db,car_id)

  if car is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="car wit id not Found")
  try:
    return update_car(db,payload,car)
  except IntegrityError:
    db.rollback()
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="car not updated - Conflict")

@router.delete("/{car_id}")
def del_one_car(db:SessionDep, car_id:int):
  car = get_one_car(db,car_id)
  if car is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="car not found")
  
  delete_car(db,car)
      
