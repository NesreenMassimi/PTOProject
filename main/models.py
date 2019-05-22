from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DATE, DATETIME, Float, BIGINT, Enum, TEXT, \
    CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, validates
from sqlalchemy import create_engine
engine = create_engine("mysql://root:16001700@localhost/PTO_system")
Base = declarative_base()


# Create your models here.



class User(Base) :
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True,autoincrement=True)
    email = Column(String(45),unique=True)
    hiring_date = Column(DATE)
    phone_number = Column(BIGINT)
    identity_number= Column(Integer,unique=True)
    role_id = Column(Integer,ForeignKey("role.id"),nullable=False)
    password = Column(String(45))
    created = Column(DATE)
    updated = Column(DATE)
    last_login = Column(DATETIME)
    name = Column(String(45))
    roles = relationship("Role",uselist=False,backref=backref("User"))


class TeamMembers(Base):

    __tablename__ = 'team_members'
    id = Column(Integer, primary_key=True,autoincrement=True)
    team_id = Column(Integer,ForeignKey("team.id"),nullable=False)
    member_id = Column(Integer,ForeignKey("id"),nullable=False)
    type = Column(Enum('employee','leader'))
    created = Column(DATE)
    updated = Column(DATE)
    Team = relationship('Team', back_populates="members")


class Team(Base):
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(45))
    created = Column(DATE)
    updated = Column(DATE)
    members = relationship('TeamMembers', back_populates="Team")


class Status(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True,autoincrement=True)
    created = Column(DATE)
    updated = Column(DATE)
    record_id = Column(Integer,ForeignKey("record.id"),nullable=False)
    status_type = Enum('approved','rejected','pending')


class Role(Base):

    __tablename__ = 'role'
    id= Column(Integer, primary_key=True,autoincrement=True)
    role_name = Column(String(45))
    created = Column(DATE)
    update = Column(DATE)


class Record(Base):

    __tablename__ = 'record'
    id = Column(Integer, primary_key=True,autoincrement=True)
    start_date = Column(DATE)
    end_date = Column(DATE)
    user =Column(Integer,ForeignKey("id"),nullable=False)
    type = Column(Enum('SICK', 'TRAVEL', 'MARRIAGE', 'FAMILY EVENT', 'OTHER'))
    note = Column(TEXT)
    created = Column(DATE)
    updated = Column(DATE)
    approved_by = Column(Integer,ForeignKey("id"),nullable=False)
    status = relationship("Status", backref=backref("Record"))
    __table_args__ = (
        CheckConstraint('start_date < end_date'),
    )


class Leaders(Base):

    __tablename__ = 'leaders'
    user = Column(Integer,ForeignKey("id"),nullable=False)
    user_leader_id1 = Column(Integer,ForeignKey("id"),nullable=False)
    id = Column(Integer, primary_key=True,autoincrement=True)
    created = Column(DATE)
    updated = Column(DATE)