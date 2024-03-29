import os

import sys
from sqlalchemy import String, Integer, ForeignKey, Column, ForeignKeyConstraint,TIMESTAMP,Date,DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base= declarative_base()


class StatusType(Base):
    __tablename__= 'statustype'
    ststid=Column(Integer, primary_key=True,nullable=False)
    description=Column(String(225))
    entity=Column(String(25),nullable=False,unique=True)

    # @property
    # def serialize(self):
    #     return {'name':self.name,'id':self.id,}

class Status(Base):
    __tablename__='status'
    stsid=Column(Integer, primary_key=True,nullable=False)
    ststid=Column(Integer,ForeignKey("statustype.ststid"),nullable=False)
    name = Column(String(80), nullable=False)
    description=Column(String(225))
    # @property
    # def serialize(self):
    #     return{'id':self.id,'name':self.name,}

class FoodItem(Base):
    __tablename__='fooditem'
    fid=Column(Integer, primary_key=True,nullable=False)
    name = Column(String(80), nullable=False)
    stsid=Column(Integer,ForeignKey("status.stsid"),nullable=False)
    cfid=Column(Integer,ForeignKey("foodcategory.cfid"),nullable=False)
    price=Column(DECIMAL(5,2))
    description=Column(String(225))
    # @property
    # def serialize(self):
    #     return{'id':self.id,'name':self.name,}
class FoodCategory(Base):
    __tablename__='foodcategory'
    cfid=Column(Integer,nullable=False, primary_key=True)
    name = Column(String(80), nullable=False)
    stsid=Column(Integer,ForeignKey("status.stsid"),nullable=False)
    price=Column(DECIMAL(5,2))
    description=Column(String(225))
    # @property
    # def serialize(self):
    #     return{'id':self.id,'name':self.name,}

class EmployeeType(Base):
    __tablename__='employeetype'
    etid=Column(Integer,nullable=False, primary_key=True)
    name = Column(String(80), nullable=False)
    description=Column(String(225))
    # @property
    # def serialize(self):
    #     return{'id':self.id,'name':self.name,}
class Employee(Base):
    __tablename__='employee'
    eid=Column(Integer,nullable=False, primary_key=True)
    etid=Column(Integer, ForeignKey("employeetype.etid"),nullable=False)
    fname = Column(String(80), nullable=False)
    lname = Column(String(80), nullable=False)
    stsid=Column(Integer, ForeignKey("status.stsid"),nullable=False)
    price=Column(DECIMAL(5,2))
    # @property
    # def serialize(self):
    #     return{'id':self.id,'name':self.name,}

class Transaction(Base):
    __tablename__='transaction'
    tid=Column(Integer,nullable=False, primary_key=True)
    eid=Column(Integer, ForeignKey("employee.eid"),nullable=False)
    date=Column(Date,nullable=False)
    totalamt=Column(DECIMAL(10,1),nullable=False)
    stsid=Column(Integer, ForeignKey("status.stsid"),nullable=False)
    # @property
    # def serialize(self):
    #     return{'id':self.id,'name':self.name,}
 
class CustomerOrder(Base):
    __tablename__='customer_order'
    tid=Column(Integer,nullable=False,primary_key=True)
    eid=Column(Integer, ForeignKey("employee.eid"),nullable=False)
    qty=Column(Integer,nullable=False)
    amt=Column(Integer,nullable=False)
    stsid=Column(Integer, ForeignKey("status.stsid"),nullable=False)
    # @property
    # def serialize(self):
    #     return{'id':self.id,'name':self.name,}
class FoodCategoryHistory(Base):
    __tablename__='fchistory'
    cfid=Column(Integer,nullable=False,primary_key=True)
    name = Column(String(80), nullable=False)
    description=Column(String(225))
    fromdate=Column(Date)
    todate=Column(Date)
    stsid=Column(Integer, ForeignKey("status.stsid"),nullable=False)
    # @property
    # def serialize(self):
    #     return{'id':self.id,'name':self.name,}
 
    

engine=create_engine('sqlite:///ssds.db')
Base.metadata.create_all(engine)