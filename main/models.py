from django.db import models
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey,DATE,DATETIME,Float
from sqlalchemy.ext.declarative import declarative_base
import pymysql
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
engine = create_engine("mysql://root:16001700@localhost/test")
Base = declarative_base()


# Create your models here.
