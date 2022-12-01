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


class Messages(BaseModel):
    id :int
    chat_room_id:int
    message: str
    user_id:int
    date : date
    hour : time


class Users(BaseModel):
    user_id: Optional[int]
    username:str
    email:str
    password:str