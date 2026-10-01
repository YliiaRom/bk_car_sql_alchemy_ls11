from datetime import datetime
from pydantic import BaseModel, Field,ConfigDict
from app.models.models import BodyType


class CarBase(BaseModel):
    # * унікальний номер автомобіля
    # id:Mapped[int] = mapped_column(Integer,primary_key=True)


    # * марка та модель автомобіля
    # model:Mapped[str] = mapped_column(String(1000))
    model:str = Field(max_length=1000, examples=["RAW-4"])

    # * ім`я виробника або дилера
    # seller_name:Mapped[str] = mapped_column(String(500))
    seller_name:str = Field(max_length=500, examples=["toyota"])

    # * він-код (VIN), як унікальний паспорт транспортного засобу
    # vin:Mapped[str] = mapped_column(String(17),unique=True)
    vin:str = Field(max_length=17, examples=["WVWZZ1JZXW000001"])

    # * тип кузова (наприклад, седан, кросовер, хетчбек)
    # body_type:Mapped[BodyType] = mapped_column(Enum(BodyType))
    body_type:BodyType

    # * об'єм двигуна у літрах або потужність в к.с.
    # engine_volume: Mapped[float] = mapped_column(Float)
    engine_volume:float = Field(examples=[2.5])

    # * вартість автомобіля
    # price:Mapped[float] = mapped_column(Numeric(10,2))
    price:float = Field(examples=[100000.00])

    # * оцінка від експертів чи покупців (може бути відсутня)
    # rating:Mapped[int | None] = mapped_column(Integer,nullable=True)
    rating:int | None = Field(default=None, ge=0)

    # * чи доступний автомобіль у наявності для продажу
    # is_available:Mapped[bool] = mapped_column(Boolean, default=True)
    is_available:bool = Field(default=True)

    # * короткий опис комплектації або технічних характеристик
    # description:Mapped[str] = mapped_column(Text)
    description:str = Field(max_length=5000, examples=["короткий опис комплектації або технічних характеристик (5000 символів)"])

    # * рік випуску автомобіля
    # year:Mapped[int] = mapped_column(Integer)
    year:int = Field(ge=1900, examples=[2000])

    # * коли автомобіль був доданий в систему/базу
    # created_at:Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    # created_at:datetime | None = None



    # * список додаткових опцій чи міток (наприкл
    # tags:Mapped[list[str]] = mapped_column(JSON)
    tags:list[str] | None = Field(max_length=12, examples=[["#car"]])


class CarCreate(CarBase):
    pass

class CarUpdate(CarBase):
     # * унікальний номер автомобіля
    # id:Mapped[int] = mapped_column(Integer,primary_key=True)


    # * марка та модель автомобіля
    # model:Mapped[str] = mapped_column(String(1000))
    model:str | None = Field(default=None)

    # * ім`я виробника або дилера
    # seller_name:Mapped[str] = mapped_column(String(500))
    seller_name:str| None = Field(default=None, max_length=500)

    # * він-код (VIN), як унікальний паспорт транспортного засобу
    # vin:Mapped[str] = mapped_column(String(17),unique=True)
    vin:str | None = Field(default=None, max_length=17)

    # * тип кузова (наприклад, седан, кросовер, хетчбек)
    # body_type:Mapped[BodyType] = mapped_column(Enum(BodyType))
    body_type:BodyType | None = None

    # * об'єм двигуна у літрах або потужність в к.с.
    # engine_volume: Mapped[float] = mapped_column(Float)
    engine_volume:float| None = Field(default=None)

    # * вартість автомобіля
    # price:Mapped[float] = mapped_column(Numeric(10,2))
    price:float | None = Field(default=None)

    # * оцінка від експертів чи покупців (може бути відсутня)
    # rating:Mapped[int | None] = mapped_column(Integer,nullable=True)
    rating:int | None = None

    # * чи доступний автомобіль у наявності для продажу
    # is_available:Mapped[bool] = mapped_column(Boolean, default=True)
    is_available:bool | None = Field(default=None)

    # * короткий опис комплектації або технічних характеристик
    # description:Mapped[str] = mapped_column(Text)
    description:str | None = Field(default=None, max_length=5000)

    # * рік випуску автомобіля
    # year:Mapped[int] = mapped_column(Integer)
    year:int | None = Field(default=None, ge=1900)

    # * коли автомобіль був доданий в систему/базу
    # created_at:Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    # created_at:datetime | None = None



    # * список додаткових опцій чи міток (наприкл
    # tags:Mapped[list[str]] = mapped_column(JSON)
    tags:list[str] | None = Field(default=None, max_length=12) 


class CarResponse(CarBase):
    id:int
    created_at:datetime

    model_config = ConfigDict(from_attributes=True)