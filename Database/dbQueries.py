from Database.dbConnection import getCursor,commit

def getInfoOfMeeting(meeting_id):
    query = "SELECT * FROM meetings WHERE meeting_id = %s" % meeting_id
    cursor = getCursor()
    cursor.execute(query)
    results = cursor.fetchall()[0]
    return results

def getMessagesFromChatroom(room_id):
    query = "SELECT message_id, user_name,message, message_hour, message_date, users.user_id FROM messages,users" \
            " WHERE messages.user_id = users.user_id and chat_room_id = %s" \
            " ORDER BY message_date DESC, message_hour DESC" % room_id
    cursor = getCursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results


def UserController(email,password):
    query = "SELECT user_id,user_name FROM users WHERE user_email = '%s' and user_password= '%s' " % (email, password)
    cursor = getCursor()
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


def insertMeeting(meeting):
    print(meeting)
    query = "INSERT INTO meetings(meeting_hoster,meeting_participants,meeting_name,meeting_date," \
            "meeting_hour,meeting_location,meeting_link) VALUES (%s,'%s','%s','%s','%s','%s','%s')"\
            %(meeting.hoster,meeting.participants,meeting.meeting_name,meeting.date,meeting.hour,meeting.location,meeting.meeting_link)
    try:
        cursor = getCursor()
        print("1")
        cursor.execute(query)
        print("2")
        commit()
        print("3")
        return True
    except:
        return False

def getMeetings(user_id):
    query = " SELECT meeting_id,meeting_hoster,meeting_participants,meeting_name,meeting_date,meeting_hour,meeting_location " \
            ",meeting_link,meeting_chatroom_id,user_name  FROM meetings,users " \
            "WHERE meetings.meeting_hoster =users.user_id and meeting_participants " \
            "like '%s' order by meeting_date DESC" % "%{}%".format(user_id)
    cursor = getCursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results
