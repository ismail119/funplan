from typing import Optional
from fastapi import FastAPI
from BaseModels.BaseModels import Meeting, Message, Users,Participant
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
                                 chatroom_id = result[8],
                                 hoster_name = result[9]
                            )
        all_meetings.append(temp_meeting)

    # Converting tuple to json model our result
    return all_meetings


@app.get('/allMessages')
async def allMessages(room_id:Optional[int]=None):
    results = getMessagesFromChatroom(room_id)
    room_messages = list()
    for message in results:
        temp_message = Message(
            id = message[0],
            username = message[1],
            message = message[2],
            hour = message[3],
            date = message[4],
            user_id = message[5]
        )
        room_messages.append(temp_message)
    return room_messages




# Get all meetings
@app.get('/userControl')
async def userControl(email: str, password:str):
    id, name  = UserController(email,password)
    return {
            "id": id,
            "username":name
            }

# Post New User into database
@app.post('/newUser')
async def addUser(new_user: Optional[Users]=None):
    result = insertUser(new_user)
    return result


@app.post('/newMessage')
async def addMessage(new_message: Optional[Message]=None):
    result = insertMessage(new_message)
    return result


@app.delete('/deleteParticipants')
async def deleteParticipant(participantId: Optional[int],meetingId:Optional[int]):
    result = DeleteParticipant(participantId,meetingId)
    return result

@app.put('/logout')
async def logout(user_id:int,meeting_id:int):
    result = DeleteParticipant(user_id, meeting_id)
    return result


@app.delete('/deleteMessage')
async  def deleteMessage(messageId:Optional[int]=None):
    result = DeleteMessage(messageId)
    return result


@app.delete('/deleteMeeting')
async def deleteMeeting(meetingId: Optional[int]):
    result = DeleteMeeting(meetingId)
    return result

@app.put('/changePassword')
async def changePassword(oldPassword:str, newPassword:str,user_id:int):
    result = ChangePassword(user_id,oldPassword,newPassword)
    return result


@app.put('/addMeetingWithLink')
async def addMeetingWithLink(meetingLink:Optional[str]=None,user_id:Optional[int]=None):
    result = AddMeetingWithLink(meetingLink,user_id)
    return result


@app.get('/participants')
async def getParticipants(meeting_id: Optional[int]):
    results = GetParticipants(meeting_id)
    participants = list()
    for participant in results:
        temp_participant = Participant(
            user_id = participant[0],
            username = participant[1]
        )
        participants.append(temp_participant)

    return participants

# Post New Meeting into database
@app.post('/newMeeting')
async def addMeeting(new_meeting: Optional[Meeting]=None):
    result = insertMeeting(new_meeting)
    print("result : {}".format(result) )
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
