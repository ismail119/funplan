from datetime import date, time
from pydantic import BaseModel
from typing import Optional


#Base Model For Meeting
class Meeting(BaseModel):
    id : Optional[int]
    hoster: int
    hoster_name: Optional[str]
    participants: str
    meeting_name:str
    date : date
    hour : time
    location: str
    meeting_link: str
    chatroom_id: Optional[int]


class Message(BaseModel):
    id : Optional[int]
    username: Optional[str]
    chat_room_id: Optional[int] #Posting
    message: str #Posting
    user_id: Optional[int] #Posting
    date : date #Posting
    hour : time #Posting


class Users(BaseModel):
    user_id: Optional[int]
    username: Optional[str]
    email:str
    password:str

class Participant(BaseModel):
    user_id: int
    username: str
