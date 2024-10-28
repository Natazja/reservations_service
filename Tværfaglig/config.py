# config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///reservations.db'  # Skift til en anden SQL-database om nødvendigt
    SQLALCHEMY_TRACK_MODIFICATIONS = False

