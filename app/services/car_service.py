from app.models.models import Car
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.shemas import CarCreate,CarResponse,CarUpdate

from app.models.models import BodyType

def create_car(session:Session, payload:CarCreate)-> Car:
  car = Car(**payload.model_dump())

  session.add(car)
  session.commit()
  session.refresh(car)

  return car

def get_cars(session:Session)->list[Car]:
  stmt = select(Car)
  return session.scalars(stmt).all()


def get_one_car(session:Session,car_id:int)-> Car | None:
  stmt = select(Car).where(Car.id == car_id)
  car  = session.scalars(stmt).first()

  if car is None:
    return None

  else:
    return car

def update_car(session:Session, payload: CarUpdate, car:Car)->Car:
  car_modify = payload.model_dump(exclude_unset=True)

  for field,value in car_modify.items():
    setattr(car,field,value)

  session.commit()
  session.refresh(car)
  return car


def delete_car(session:Session, car:Car) -> None:

  session.delete(car)
  session.commit()



def get_car_by_filter(session:Session,  body_type:BodyType | None = None,year:int | None =None, seller_name:str | None = None, is_available:bool | None =None, min_rating:int | None = None, limit:int=20,offset:int= 0):
  stmt = select(Car)

  if body_type is not None:
    stmt = stmt.where(Car.body_type == body_type)

  if year is not None:
    stmt = stmt.where(Car.year == year)

  if seller_name is not None:
    stmt = stmt.where(Car.seller_name == seller_name)

  if is_available is not None:
    stmt = stmt.where(Car.is_available == is_available)

  if min_rating is not None:
    stmt = stmt.where(Car.rating >= min_rating)

  stmt = stmt.order_by(Car.id).limit(limit).offset(offset)

  return list(session.scalars(stmt).all())

  # перелік машин з фільтрами за роком -випуску, body_type- типом кузоваб  seller_name-ім'ям виробника, is_available-за наявністтю, більше вказанногг рейтінгу
  
  