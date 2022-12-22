from Database.dbConnection import getCursor,commit

def getInfoOfMeeting(meeting_id):
    query = "SELECT * FROM meetings WHERE meeting_id = %s" % meeting_id
    cursor = getCursor()
    try:
        cursor.execute(query)
    except:
        cursor.execute("rollback")
        cursor.execute(query)
    results = cursor.fetchall()[0]
    return results

def getMessagesFromChatroom(room_id):
    query = "SELECT message_id, user_name,message, message_hour, message_date, users.user_id FROM messages,users" \
            " WHERE messages.user_id = users.user_id and chat_room_id = %s" \
            " ORDER BY message_date DESC, message_hour DESC" % room_id
    cursor = getCursor()
    try:
        cursor.execute(query)
    except:
        cursor.execute("rollback")
        cursor.execute(query)
    results = cursor.fetchall()
    return results


def UserController(email,password):
    query = "SELECT user_id,user_name FROM users WHERE user_email = '%s' and user_password= '%s' " % (email, password)
    cursor = getCursor()

    try:
        cursor.execute(query)
    except:
        cursor.execute("rollback")
        cursor.execute(query)
    results = cursor.fetchall()
    if len(results)==0:
        return -1,"none"
    else:
        return results[0][0], str(results[0][1]).rstrip()

def insertUser(user):
    query = "INSERT INTO users(user_name,user_email,user_password) VALUES('%s','%s','%s')"\
            % (user.username,user.email,user.password)
    try:
        cursor = getCursor()
        cursor.execute(query)
        commit()
        return True
    except:
        return False


def insertMessage(message):
    query = "INSERT INTO messages(chat_room_id,message,user_id,message_date,message_hour) VALUES(%s,'%s',%s,'%s','%s')"\
            % (message.chat_room_id,message.message,message.user_id,message.date,message.hour)
    try:
        cursor = getCursor()
        cursor.execute(query)
        commit()
        return True
    except:
        return False


def DeleteMeeting(meetingId):
    query1 = "delete from meetings where meeting_id = %s" % meetingId
    cursor = getCursor()
    cursor.execute(query1)
    query2 = "delete from messages where chat_room_id = %s" %meetingId
    cursor.execute(query2)
    try:
        commit()
        return True
    except:
        print("delete error")
        return False


def AddMeetingWithLink(meetingLink,user_id):
    query = "update meetings set meeting_participants = CONCAT(meeting_participants ,%s,' ')" \
            " where meeting_link = '%s' " % (user_id,meetingLink)

    cursor = getCursor()
    cursor.execute(query)
    try:
        commit()
        return True
    except:
        print("insert link meeting error")
        return False




def GetParticipants(meeting_id):
    query= "select meeting_participants from meetings where meeting_id = %s" % meeting_id
    cursor = getCursor()
    try:
        cursor.execute(query)
    except:
        cursor.execute("rollback")
        cursor.execute(query)
    result1 = cursor.fetchall()
    myStringList = (result1[0][0]).split(' ')

    #O(n) ----
    myIntList = ""
    for participant_id in myStringList:
        try:
            if myIntList == "":
                myIntList += "{}".format((int(participant_id)))
            else:
                myIntList += ",{}".format((int(participant_id)))
        except:
            print("onemsiz")

    myTuple = "({})".format(myIntList)

    #---------

    query2 = "select user_id,user_name from users where user_id in {}".format(myTuple)
    cursor2 = getCursor()
    try:
        cursor2.execute(query2)
    except:
        cursor2.execute("rollback")
        cursor2.execute(query2)
    results = cursor2.fetchall()
    print("results {}".format(results))
    return results



def DeleteParticipant(participantId,meetingId):
    query = "update meetings set meeting_participants = replace(meeting_participants,'%s','')" \
            " where meeting_id=%s" %(participantId,meetingId)
    cursor = getCursor()
    cursor.execute(query)
    try:
        cursor = getCursor()
        cursor.execute(query)
        commit()
        return True
    except:
        return False



def insertMeeting(meeting):
    query = "INSERT INTO meetings(meeting_hoster,meeting_participants,meeting_name,meeting_date," \
            "meeting_hour,meeting_location,meeting_link) VALUES (%s,'%s ','%s','%s','%s','%s','%s')"\
            %(meeting.hoster,meeting.participants,meeting.meeting_name,meeting.date,meeting.hour,meeting.location,meeting.meeting_link)
    try:
        cursor = getCursor()
        cursor.execute(query)
        commit()
        return True
    except:
        return False

def getMeetings(user_id):
    query = " SELECT meeting_id,meeting_hoster,meeting_participants,meeting_name,meeting_date,meeting_hour,meeting_location " \
            ",meeting_link,meeting_chatroom_id,user_name  FROM meetings,users " \
            "WHERE meetings.meeting_hoster =users.user_id and meeting_participants " \
            "like '%s' order by meeting_date DESC" % "%{} %".format(user_id)
    cursor = getCursor()
    try:
        cursor.execute(query)
    except:
        cursor.execute("rollback")
        cursor.execute(query)
    results = cursor.fetchall()
    return results
