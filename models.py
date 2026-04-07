import uuid
from sqlalchemy import Column, String, Integer, Float, ForeignKey, JSON, DateTime, Text, Boolean
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    weight = Column(Float)
    activity_level = Column(String(50))
    fitness_goals = Column(JSON)
    health_conditions = Column(JSON)
    dietary_preferences = Column(JSON)
    target_weight = Column(Float)
    
    plans = relationship("Plan", back_populates="user", cascade="all, delete-orphan")
    progress_logs = relationship("ProgressLog", back_populates="user", cascade="all, delete-orphan")


class Plan(Base):
    __tablename__ = "plans"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    plan_type = Column(String(50), nullable=False) # e.g., 'workout', 'meal'
    plan_data = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="plans")


class ProgressLog(Base):
    __tablename__ = "progress_logs"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    plan_type = Column(String(50)) # e.g., 'workout', 'meal'
    feedback = Column(Text, nullable=True)
    perceived_difficulty = Column(String(50), nullable=True) # e.g., 'too hard', 'just right'
    weight_log = Column(Float, nullable=True)
    
    user = relationship("User", back_populates="progress_logs")


# Reference Tables for Exercises and Foods
class Exercise(Base):
    __tablename__ = "exercises"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    type = Column(String(50))
    level = Column(String(50))


class Food(Base):
    __tablename__ = "foods"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    type = Column(String(50)) # e.g., 'veg', 'non-veg'
    category = Column(String(50)) # e.g., 'breakfast'
    calories = Column(Integer)
