from typing import Optional
from fastapi import FastAPI
from BaseModels.BaseModels import Meeting, Messages, Users
from Database.dbQueries import *

app = FastAPI()

# Get Specific meeting information
@app.get("/meeting")
async def meetings(meeting_id: Optional[int] = None):
    try:
        meeting_info = getInfoOfMeeting(meeting_id) #Get Data from database

        #Converting tuple to json model our result
        meetingModel = Meeting(id=meeting_info[0],hoster=meeting_info[1],
                               participants=meeting_info[2],meeting_name=meeting_info[3],
                               date=meeting_info[4],hour=meeting_info[5],location=meeting_info[6],
                               meeting_link = meeting_info[7],chatroom_id=meeting_info[8])

        return {meeting_id : meetingModel}

    except:
        print("Data not found")


# Get Specific Chatroom's messages
@app.get("/chatroom")
async def chatrooms(room_id: Optional[int] = None):
    try:
        messages_info = getMessagesFromChatroom(room_id)  # Get Data from database

        messages = list()
        for message_info in messages_info:
            messagesModel = Messages(id=message_info[0], chat_room_id=message_info[1],
                                     message=message_info[2], user_id=message_info[3],
                                     date=message_info[4], hour=message_info[5])
            messages.append(messagesModel)

        # Converting tuple to json model our result

        return {"messages" : messages}

    except:
        print("Data not found")


# Get all meetings
@app.get('/allMeetings')
async def getAllMeetings(user_id: Optional[int] = None):
    results = getMeetings(user_id)
    all_meetings = list()
    for result in results:
        temp_meeting = Meeting(id=result[0], hoster=result[1],
                                 participants=result[2], meeting_name=result[3],
                                 date=result[4], hour=result[5],
                                 location=result[6],meeting_link = result[7],
                                 chatroom_id = result[8]
                            )
        all_meetings.append(temp_meeting)
        print(all_meetings)
    # Converting tuple to json model our result

    return {"meetings_of_user": all_meetings}



# Post New User into database
@app.post('/newUser')
async def addUser(new_user: Optional[Users]=None):
    result = insertUser(new_user)
    return result

    """
           {
             "username": "string",
             "email": "string",
             "password": "string"
           }
    """


# Post New Meeting into database
@app.post('/newMeeting')
async def addMeeting(new_meeting: Meeting):
    result = insertMeeting(new_meeting)
    return result

    """
        {
          "hoster": int,
          "participants": "string",
          "meeting_name": "string",
          "date": "string",
          "hour": "string",
          "location": "string",
          "meeting_link": "string"
         }
    """

