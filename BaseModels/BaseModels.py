from datetime import date, time
from pydantic import BaseModel
from typing import Optional


#Base Model For Meeting
class Meeting(BaseModel):
    id :Optional[int]
    hoster:int
    participants: str
    meeting_name:str
    date : date
    hour : time
    location: str
    meeting_link: str
    chatroom_id: Optional[int]


class Message(BaseModel):
    id : int
    username: Optional[str]
    chat_room_id: Optional[int]
    message: str
    user_id: Optional[int]
    date : date
    hour : time


class Users(BaseModel):
    user_id: Optional[int]
    username: Optional[str]
    email:str
    password:str