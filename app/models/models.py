from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Float, Numeric, Boolean, func, JSON, Text, Enum
from enum import Enum as PyEnum
import datetime

class BodyType(str, PyEnum):
    sedan = "sedan"
    crossover = "crossover"
    hatchback = "hatchback"
    wagon = "wagon"
    coupe = "coupe"
    convertible = "convertible"
    minivan = "minivan"
    pickup = "pickup"
    suv = "suv"



class Base(DeclarativeBase):
  pass

class Car(Base):
    __tablename__="cars"

    # * унікальний номер автомобіля
    id:Mapped[int] = mapped_column(Integer,primary_key=True)

    # * марка та модель автомобіля
    model:Mapped[str] = mapped_column(String(1000))

    # * ім`я виробника або дилера
    seller_name:Mapped[str] = mapped_column(String(500))

    # * він-код (VIN), як унікальний паспорт транспортного засобу
    vin:Mapped[str] = mapped_column(String(17),unique=True)

    # * тип кузова (наприклад, седан, кросовер, хетчбек)
    body_type:Mapped[BodyType] = mapped_column(Enum(BodyType))

    # * об'єм двигуна у літрах або потужність в к.с.
    engine_volume: Mapped[float] = mapped_column(Float)

    # * вартість автомобіля
    price:Mapped[float] = mapped_column(Numeric(10,2))

    # * оцінка від експертів чи покупців (може бути відсутня)
    rating:Mapped[int | None] = mapped_column(Integer,nullable=True)

    # * чи доступний автомобіль у наявності для продажу
    is_available:Mapped[bool] = mapped_column(Boolean, default=True)

    # * короткий опис комплектації або технічних характеристик
    description:Mapped[str] = mapped_column(Text)

    # * рік випуску автомобіля
    year:Mapped[int] = mapped_column(Integer)

    # * коли автомобіль був доданий в систему/базу
    created_at:Mapped[datetime.datetime] = mapped_column(server_default=func.now())

    # * список додаткових опцій чи міток (наприкл
    tags:Mapped[list[str]] = mapped_column(JSON)