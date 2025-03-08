from instance.database import db
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

## This is for show ticketing platform 

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    role = Column(String(120), nullable=False, default='user')
    created_at = Column(DateTime, default=datetime.utcnow)
    
class Theatre(db.Model):
    __tablename__ = 'theatres'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    place = Column(String(120), nullable=False)
    city = Column(String(120), nullable=False)
    capacity = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
class Show(db.Model):
    __tablename__ = 'shows'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    staring_time = Column(DateTime, nullable=False)
    ending_time = Column(DateTime, nullable=False)
    theatre_id = Column(Integer, ForeignKey('theatres.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    # theatre = relationship("Theatre", back_populates="shows")
    
class Booking(db.Model):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    show_id = Column(Integer, ForeignKey('shows.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    no_of_seats = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    # show = relationship("Show", back_populates="bookings")
    # user = relationship("User", back_populates="bookings")
    
class Ratings(db.Model):
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True)
    show_id = Column(Integer, ForeignKey('shows.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    rating = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    # show = relationship("Show", back_populates="ratings")
    # user = relationship("User", back_populates="ratings")


## This is for Quiz App

# class User(db.Model):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     full_name = Column(String(80), unique=True, nullable=False)
#     dob = Column(String(30), nullable=False)
#     qualification = Column(String(120), nullable=False) 
#     email = Column(String(120), unique=True, nullable=False)
#     password = Column(String(120), nullable=False)
#     role = Column(String(120), nullable=False, default='user')
#     created_at = Column(DateTime, default=datetime.utcnow)
    
# class Subject(db.Model):
#     __tablename__ = 'subjects'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(80), unique=True, nullable=False)
#     description = Column(String(120), nullable=False)

# class Chapter(db.Model):
#     __tablename__ = 'chapters'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(80), unique=True, nullable=False)
#     description = Column(String(120), nullable=False)
#     subject_id = Column(Integer, ForeignKey('subjects.id'))
#     # subject = relationship("Subject", back_populates="chapters")
    
# class Quiz(db.Model):
#     __tablename__ = 'quizzes'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(80), unique=True, nullable=False)
#     description = Column(String(120), nullable=False)
#     chapter_id = Column(Integer, ForeignKey('chapters.id'))
#     # chapter = relationship("Chapter", back_populates="quizzes")
    
# class Question(db.Model):
#     __tablename__ = 'questions'
#     id = Column(Integer, primary_key=True)
#     question = Column(String(80), unique=True, nullable=False)
#     option1 = Column(String(120), nullable=False)
#     option2 = Column(String(120), nullable=False)
#     option3 = Column(String(120), nullable=False)
#     option4 = Column(String(120), nullable=False)
#     answer = Column(String(120), nullable=False)
#     quiz_id = Column(Integer, ForeignKey('quizzes.id'))
#     # quiz = relationship("Quiz", back_populates="questions")
    
# class Score(db.Model):
#     __tablename__ = 'scores'
#     id = Column(Integer, primary_key=True)
#     quiz_id = Column(Integer, ForeignKey('quizzes.id'))
#     user_id = Column(Integer, ForeignKey('users.id'))
#     score = Column(Integer, nullable=False)
#     submitted_at = Column(DateTime, default=datetime.utcnow)
#     # quiz = relationship("Quiz", back_populates="scores")
#     # user = relationship("User", back_populates="scores")
    
    
## This is for Household Services Application

# class User(db.Model):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     full_name = Column(String(80), unique=True, nullable=False)
#     email = Column(String(120), unique=True, nullable=False)
#     password = Column(String(120), nullable=False)
#     role = Column(String(120), nullable=False, default='user')
#     pin_code = Column(Integer, nullable=False)
    
# class Service(db.Model):
#     __tablename__ = 'services'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(80), unique=True, nullable=False)
#     description = Column(String(120), nullable=False)
#     time_required = Column(Integer, nullable=False)
#     price = Column(Integer, nullable=False)
#     category = Column(String(120), nullable=False)
#     created_at = Column(DateTime, default=datetime.utcnow)
    
# class Service_Professionals(db.Model):
#     __tablename__ = 'service_professionals'
#     id = Column(Integer, primary_key=True)
#     full_name = Column(String(80), unique=True, nullable=False)
#     email = Column(String(120), unique=True, nullable=False)
#     password = Column(String(120), nullable=False)
#     role = Column(String(120), nullable=False, default='service_professional')
#     pin_code = Column(Integer, nullable=False)
#     service_type = Column(String(120), nullable=False)
#     experience = Column(Integer, nullable=False)
    
# class Service_Request(db.Model):
#     __tablename__ = 'service_requests'
#     id = Column(Integer, primary_key=True)
#     service_id = Column(Integer, ForeignKey('services.id'))
#     user_id = Column(Integer, ForeignKey('users.id'))
#     service_professional_id = Column(Integer, ForeignKey('service_professionals.id'))
#     address = Column(String(120), nullable=False)
#     pin_code = Column(Integer, nullable=False)
#     status = Column(String(120), nullable=False, default='pending')
#     created_at = Column(DateTime)
#     completed_at = Column(DateTime, nullable=True)
#     remarks = Column(String(120), nullable=True)
#     # service = relationship("Service", back_populates="service_requests")
#     # user = relationship("User", back_populates="service_requests")
#     # service_professional = relationship("Service_Professionals", back_populates="service_requests")
    
# class Service_Rating(db.Model):
#     __tablename__ = 'service_ratings'
#     id = Column(Integer, primary_key=True)
#     service_request_id = Column(Integer, ForeignKey('service_requests.id'))
#     user_id = Column(Integer, ForeignKey('users.id'))
#     rating = Column(Integer, nullable=False)
#     Service_Professional_id = Column(Integer, ForeignKey('service_professionals.id'))
    
