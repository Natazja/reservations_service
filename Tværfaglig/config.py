# config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///reservations.db' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

