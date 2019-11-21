from sqlalchemy.schema import Sequence
#id_seq is required for auto id generation(cx_Oracle)
id_seq = Sequence('id_seq')



import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random 

engine = create_engine('oracle+cx_oracle://mustafa:1234@24.133.185.104:1521/XE')
Base = declarative_base()
Base.metadata.create_all(engine)

class User(Base):
    __tablename__ = 'USER'
    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    username = Column(String(255))
    password = Column(String(255))
    fname = Column(String(255))
    mname = Column(String(255))
    lname = Column(String(255))
    registerdate = Column(String(255))#Column(DateTime(timezone=True))

class Recipe(Base):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    direction = Column(String(255))
    fat = Column(Integer())
    date = Column(DateTime(timezone=True))
    calories = Column(Integer())
    description = Column(String(255))
    protein = Column(Integer())
    rating = Column(Integer())
    title = Column(String(255))
    ingredientList = Column(String(255))
    ingredientDescription = Column(String(255))
    sodium = Column(Integer())
    categoryName = Column(String(255))

class Menu(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True)
    uId = Column(Integer())
    recipeList = Column(String(255))
    name = Column(String(255))


class Category(Base):
    __tablename__ = 'category'
    name = Column(String(255), primary_key=True)

class Ingredient(Base):
    __tablename__ = 'ingredient'
    name = Column(String(255), primary_key=True)

class MenuRate(Base):
    __tablename__ = 'menurate'
    id = Column(Integer, primary_key=True)
    menuId = Column(Integer())
    uId = Column(Integer())
    rate = Column(Integer())



Base.metadata.create_all(engine)


def add_User(email,username,password,fname,mname,lname,registerdate):
    for i in range(5):
        st_id = random.randint(1,2**24)
        
        try:
            Session = sessionmaker(bind=engine)
            session = Session()
            admin = User(id=st_id,email=email,username=username,password=password,fname=fname,mname=mname,lname=lname,registerdate=registerdate)
            session.add(admin)
            session.commit()
            break
        except:
            continue    




def add_Ingredient(name):
    for i in range(5):
        st_id = random.randint(1,2**24)
        
        try:
            Session = sessionmaker(bind=engine)
            session = Session()
            admin = Ingredient(name=name)
            session.add(admin)
            session.commit()
            break
        except:
            continue    

