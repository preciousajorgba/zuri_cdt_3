from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import jwt
from passlib.context import CryptContext
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from jwt import PyJWTError

app = FastAPI()

# Replace with your actual secret key
SECRET_KEY = "ppeauli@j38kl78wj83uirnG0deuisG00d"
ALGORITHM = "HS256"

DATABASE_URL = "sqlite:///./task_3.db"  # SQLite database file

engine = create_engine(DATABASE_URL)

# Create a standard session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserCreate(BaseModel):
    username: str
    password: str

class UserInDB(BaseModel):
    id: int
    username: str
    

class Token(BaseModel):
    access_token: str
    token_type: str
    username: str
    id: int
    status_code: int  # Include a field for status code in the response model

def create_access_token(data: dict):
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Custom dependency for handling database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/signup", response_model=Token, status_code=201)  # Set the status_code for the endpoint
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    try:
        user_obj = User(username=user.username, password=pwd_context.hash(user.password))
        db.add(user_obj)
        db.commit()
        db.refresh(user_obj)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Username already taken")

    access_token = create_access_token({"sub": user_obj.id})
    # Include the status code in the response
    return {"access_token": access_token, "token_type": "bearer", "username": user_obj.username, "id": user_obj.id, "status_code": 201}

@app.get("/user", response_model=UserInDB, status_code=200)
async def get_user(id: int, token: str, db: Session = Depends(get_db)):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    if decoded_token.get("sub") != id:
        raise HTTPException(status_code=403, detail="Token does not match the provided user ID")

    user_obj = db.query(User).filter(User.id == id).first()
    if user_obj is None:
        raise HTTPException(status_code=404, detail="User not found")

    return UserInDB(id=user_obj.id, username=user_obj.username, status_code=200)
