from flask import Blueprint, request, jsonify, make_response
import json
from src import db


chaarg = Blueprint('chaarg', __name__)

# Get all events from the DB
@chaarg.route('/events', methods=['GET'])
def get_events():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT WE.EventId, WE.Public, WE.Semester, WE.Year, S.Name, ET.Type\
        FROM WeeklyEvent WE\
        JOIN Studio S on WE.HostedBy = S.StudioId\
        JOIN EventType ET on WE.TypeId = ET.TypeId')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(json.dumps(json_data, default=str)) # jsonify(json_data)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get all event sessions from the DB
@chaarg.route('/eventSessions', methods=['GET'])
def get_event_sessions():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT ES.EventId, ES.SessionNum, Public, DateTime, Name, Type, Title AS Location, Address,\
       Capacity, COUNT(SU.MemberID) as SignedUp,\
       (Capacity - COUNT(SU.MemberId)) AS RemainingSpots,\
       Waitlist\
        FROM EventSession ES\
        JOIN WeeklyEvent WE on ES.EventId = WE.EventId\
        JOIN Studio S on WE.HostedBy = S.StudioId\
        JOIN EventType ET on WE.TypeId = ET.TypeId\
        JOIN Location L on ES.LocatedAt = L.LocationId\
        LEFT JOIN SignUp SU on ES.EventId = SU.EventId and ES.SessionNum = SU.SessionNum\
        LEFT JOIN (SELECT W.EventId, W.SessionNum, COUNT(MemberId) as Waitlist\
                    FROM EventSession ES2\
                    JOIN Waitlist W on ES2.EventId = W.EventId and ES2.SessionNum = W.SessionNum\
                    GROUP BY ES2.EventId, ES2.SessionNum)\
            W2 ON W2.EventId = ES.EventId AND W2.SessionNum = ES.SessionNum\
        GROUP BY ES.EventId, ES.SessionNum;')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(json.dumps(json_data, default=str)) # jsonify(json_data)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get all event sessions from the DB for a specific event
@chaarg.route('/eventSessions/<eventId>', methods=['GET'])
def get_event_sessions_for_event(eventId):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT ES.EventId, ES.SessionNum, Public, DateTime, Name, Type, Title AS Location, Address,\
        CONCAT_WS(" ", I.FirstName, I.LastName) as Instructor,\
        Capacity, COUNT(SU.MemberID) as SignedUp,\
        (Capacity - COUNT(SU.MemberId)) AS RemainingSpots,\
        Waitlist\
        FROM EventSession ES\
        JOIN WeeklyEvent WE on ES.EventId = WE.EventId\
        JOIN Studio S on WE.HostedBy = S.StudioId\
        JOIN EventType ET on WE.TypeId = ET.TypeId\
        JOIN Location L on ES.LocatedAt = L.LocationId\
        LEFT JOIN Instructor I on ES.InstructedBy = I.InstructorId\
        LEFT JOIN SignUp SU on ES.EventId = SU.EventId and ES.SessionNum = SU.SessionNum\
        LEFT JOIN (SELECT W.EventId, W.SessionNum, COUNT(MemberId) as Waitlist\
                    FROM EventSession ES2\
                    JOIN Waitlist W on ES2.EventId = W.EventId and ES2.SessionNum = W.SessionNum\
                    GROUP BY ES2.EventId, ES2.SessionNum)\
            W2 ON W2.EventId = ES.EventId AND W2.SessionNum = ES.SessionNum\
        WHERE ES.EventId = {0}\
        GROUP BY ES.EventId, ES.SessionNum;'.format(eventId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(json.dumps(json_data, default=str)) # jsonify(json_data)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get all member names from the DB
@chaarg.route('/members', methods=['GET'])
def get_members():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT MemberId AS value, CONCAT_WS(" ", FirstName, LastName) AS label FROM Member')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get event information for specific event session
@chaarg.route('/eventInfo/<eventID>/<sessionNum>', methods=['GET'])
def get_event_info( eventID, sessionNum):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT *\
        FROM EventSession ES\
        JOIN WeeklyEvent WE on ES.EventId = WE.EventId\
        JOIN EventType ET on WE.TypeId = ET.TypeId\
        JOIN Instructor I on ES.InstructedBy = I.InstructorId\
        JOIN Location L on ES.LocatedAt = L.LocationId\
        JOIN Studio S on WE.HostedBy = S.StudioId\
        WHERE ES.EventId = {0} AND ES.SessionNum = {1};'.format( eventID, sessionNum))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(json.dumps(json_data, default=str))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get event information for specific event session, including a given member's sign-up and waitlist status
@chaarg.route('/memberSessionInfo/<memberID>/<eventID>/<sessionNum>', methods=['GET'])
def get_member_session_info( memberID, eventID, sessionNum):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT (Capacity - COUNT(SU.MemberId)) AS RemainingSpots,\
            SignedUpBool,\
            WaitlistBool\
        FROM EventSession ES\
        LEFT JOIN SignUp SU on ES.EventId = SU.EventId and ES.SessionNum = SU.SessionNum\
        LEFT JOIN\
            (SELECT SU2.MemberID, SU2.EventId, SU2.SessionNum, COUNT(*) as SignedUpBool FROM SignUp SU2 WHERE MemberId = {0} AND SU2.DeletedAt IS NULL GROUP BY EventId, SessionNum) MemberSignUp\
            ON ES.EventID = MemberSignUp.EventId AND ES.SessionNum = MemberSignUp.SessionNum\
        LEFT JOIN\
            (SELECT W.MemberID, W.EventId, W.SessionNum, COUNT(*) as WaitlistBool FROM Waitlist W WHERE MemberId = {0} AND W.DeletedAt IS NULL GROUP BY EventId, SessionNum) MemberWaitlist\
            ON ES.EventID = MemberWaitlist.EventId AND ES.SessionNum = MemberWaitlist.SessionNum\
        WHERE ES.EventId = {1} AND ES.SessionNum = {2}\
        GROUP BY ES.EventId, ES.SessionNum'.format(memberID, eventID, sessionNum))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(json.dumps(json_data, default=str))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get all reviews for a given studio
@chaarg.route('/reviews/<studioId>', methods=['GET'])
def get_reviews(studioId):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT Bolts, Comment, M.FirstName, M.LastName\
        FROM Review\
        JOIN WeeklyEvent WE on Review.EventId = WE.EventId\
        JOIN Member M on Review.MemberId = M.MemberId\
        WHERE WE.HostedBy = {0};'.format(studioId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(json.dumps(json_data, default=str))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get average rating for a given studio
@chaarg.route('/averageBolts/<studioId>', methods=['GET'])
def get_avg_bolts(studioId):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT AVG(Bolts) AS AverageBolts\
        FROM Review\
        JOIN WeeklyEvent WE on Review.EventId = WE.EventId\
        WHERE WE.HostedBy = {0}\
        GROUP BY HostedBy;'.format(studioId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(json.dumps(json_data, default=str))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get all event sessions, including a given member's sign-up and waitlist status
@chaarg.route('/allEvents/<memberID>', methods=['GET'])
def get_events_for_member(memberID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT ES.EventId, ES.SessionNum, DateTime, Name, Type, Title AS Location, Address,\
            (Capacity - COUNT(SU.MemberId)) AS RemainingSpots,\
            SignedUpBool,\
            WaitlistBool\
        FROM EventSession ES\
        JOIN WeeklyEvent WE on ES.EventId = WE.EventId\
        JOIN Studio S on WE.HostedBy = S.StudioId\
        JOIN EventType ET on WE.TypeId = ET.TypeId\
        JOIN Location L on ES.LocatedAt = L.LocationId\
        LEFT JOIN SignUp SU on ES.EventId = SU.EventId and ES.SessionNum = SU.SessionNum\
        LEFT JOIN\
            (SELECT SU2.MemberID, SU2.EventId, SU2.SessionNum, COUNT(*) as SignedUpBool FROM SignUp SU2 WHERE MemberId = {0} AND SU2.DeletedAt IS NULL GROUP BY EventId, SessionNum) MemberSignUp\
            ON ES.EventID = MemberSignUp.EventId AND ES.SessionNum = MemberSignUp.SessionNum\
        LEFT JOIN\
            (SELECT W.MemberID, W.EventId, W.SessionNum, COUNT(*) as WaitlistBool FROM Waitlist W WHERE MemberId = {0} AND W.DeletedAt IS NULL GROUP BY EventId, SessionNum) MemberWaitlist\
            ON ES.EventID = MemberWaitlist.EventId AND ES.SessionNum = MemberWaitlist.SessionNum\
        GROUP BY ES.EventId, ES.SessionNum'.format(memberID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(json.dumps(json_data, default=str))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get all sign-ups for a given event session
@chaarg.route("/signups/<eventID>/<sessionNum>", methods = ['GET'])
def get_signups(eventID, sessionNum):
    cursor = db.get_db().cursor()
    cursor.execute('SELECt * FROM SignUp SU\
        JOIN Member M ON M.MemberId = SU.MemberID\
        WHERE EventId = {0} AND SessionNum = {1} AND DeletedAt IS NULL'.format(eventID, sessionNum))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(json.dumps(json_data, default=str))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Sign up the given member for the given event session
@chaarg.route("/signup", methods = ['POST'])
def post_signup():
    memberId = request.form['memberId']
    eventId = request.form['eventId']
    sessionNum = request.form['sessionNum']
    cursor = db.get_db().cursor()
    cursor.execute('insert into SignUp (MemberId, EventId, SessionNum) values ({0}, {1}, {2})'.format(memberId, eventId, sessionNum))
    cursor.connection.commit()
    return "Success", 201

# Remove a sign up for the given user for the given event session
@chaarg.route("/deleteSignUp", methods = ['PATCH'])
def delete_signup():
    memberId = request.form['memberId']
    eventId = request.form['eventId']
    sessionNum = request.form['sessionNum']
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE SignUp SET DeletedAt = CURRENT_TIMESTAMP WHERE MemberId = {0} AND EventId = {1} AND SessionNum = {2}'.format(memberId, eventId, sessionNum))
    cursor.connection.commit()
    return "Success", 201

# Get all waitlist entries for a given event session
@chaarg.route("/waitlistEntries/<eventID>/<sessionNum>", methods = ['GET'])
def get_waitlist_entries(eventID, sessionNum):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Waitlist W\
        JOIN Member M ON M.MemberId = W.MemberID\
        WHERE EventId = {0} AND SessionNum = {1} AND DeletedAt IS NULL'.format(eventID, sessionNum))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(json.dumps(json_data, default=str))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Add the given member to the waitlist for the given event
@chaarg.route("/waitlist", methods = ['POST'])
def post_waitlist():
    memberId = request.form['memberId']
    eventId = request.form['eventId']
    sessionNum = request.form['sessionNum']
    cursor = db.get_db().cursor()
    cursor.execute('insert into Waitlist (MemberId, EventId, SessionNum) values ({0}, {1}, {2})'.format(memberId, eventId, sessionNum))
    cursor.execute('UPDATE Waitlist W, (SELECT MAX(Position) + 1 AS NextPosition FROM Waitlist WHERE EventId = {1} AND SessionNum = {2} AND DeletedAt IS NULL) W1\
        SET W.Position = W1.NextPosition\
        WHERE MemberId = {0} AND EventId = {1} AND SessionNum = {2};'.format(memberId, eventId, sessionNum))
    cursor.connection.commit()
    return "Success", 201

# Give the given member from the waitlist a ticket to the event, by removing them from the waitlist and adding them as a sign-up
@chaarg.route("/ticket", methods = ['PATCH'])
def ticket_waitlist_entry():
    memberId = request.form['memberId']
    eventId = request.form['eventId']
    sessionNum = request.form['sessionNum']
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE Waitlist W, (SELECT Position FROM Waitlist WHERE MemberId = {0} AND EventId = {1} AND SessionNum = {2} ) W1\
        SET W.Position = W.Position - 1\
        WHERE W.Position > W1.Position AND EventId = {1} and SessionNum = {2} AND DeletedAt IS NULL AND Ticketed IS FALSE;'.format(memberId, eventId, sessionNum))
    cursor.execute('UPDATE Waitlist W\
        SET W.DeletedAt = CURRENT_TIMESTAMP, W.Ticketed = 1\
        WHERE MemberId = {0} AND EventId = {1} AND SessionNum = {2}'.format(memberId, eventId, sessionNum))
    cursor.execute('insert into SignUp (MemberId, EventId, SessionNum) values ({0}, {1}, {2})'.format(memberId, eventId, sessionNum))
    cursor.connection.commit()
    return "Success", 201

# Remove the given member from the waitlist for the given event session
@chaarg.route("/deleteWaitlist", methods = ['PATCH'])
def delete_waitlist():
    memberId = request.form['memberId']
    eventId = request.form['eventId']
    sessionNum = request.form['sessionNum']
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE Waitlist W, (SELECT Position FROM Waitlist WHERE MemberId = {0} AND EventId = {1} AND SessionNum = {2} ) W1\
        SET W.Position = W.Position - 1\
        WHERE W.Position > W1.Position AND EventId = {1} and SessionNum = {2} AND DeletedAt IS NULL AND Ticketed IS FALSE;'.format(memberId, eventId, sessionNum))
    cursor.execute('UPDATE Waitlist SET DeletedAt = CURRENT_TIMESTAMP WHERE MemberId = {0} AND EventId = {1} AND SessionNum = {2}'.format(memberId, eventId, sessionNum))
    cursor.connection.commit()
    return "Success", 201

# Toggle the publicity boolean for the given event
@chaarg.route("/togglePublic", methods=['PATCH'])
def toggle_public():
    eventId = request.form['eventId']
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE WeeklyEvent\
        SET Public = !Public\
        WHERE EventId = {0};'.format(eventId))
    cursor.connection.commit()
    return "Success", 201

# add a new event to the db
@chaarg.route("/addEvent", methods=['POST'])
def add_event():
    semester = request.form['semester']
    year = request.form['year']
    public = request.form['public']
    typeId = request.form['typeId']
    hostedBy = request.form['hostedBy']
    cursor = db.get_db().cursor()
    cursor.execute("INSERT into WeeklyEvent (Semester, Year, Public, TypeId, HostedBy) values ('{0}', {1}, {2}, {3}, {4})".format(semester, year, public, typeId, hostedBy))
    cursor.connection.commit()
    return "Success", 201

# get all event types from the db
@chaarg.route("/eventTypes", methods=['GET'])
def get_event_types():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT TypeId as value, Type as label FROM EventType')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# get all studios from the db
@chaarg.route("/studios", methods=['GET'])
def get_studios():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT StudioId as value, Name as label FROM Studio')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get the instructors at a given studio
@chaarg.route("/instructorsByStudio/<studioId>", methods=['GET'])
def get_instructors(studioId):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT InstructorId as value, CONCAT_WS(" ", FirstName, LastName) AS label FROM Instructor WHERE InstructorAt = {0}'.format(studioId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get the locations for a given studio 
@chaarg.route("/locationsByStudio/<studioId>", methods=['GET'])
def get_locations(studioId):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT L.LocationId as value, CONCAT_WS(", ", L.Title, L.Address) AS label FROM Location L JOIN StudioLocation SL on L.LocationId = SL.LocationId WHERE StudioId = {0}'.format(studioId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get the studio information for a given event
@chaarg.route("/studioByEventId/<eventId>", methods=['GET'])
def get_studio_by_event(eventId):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Studio JOIN WeeklyEvent WE on Studio.StudioId = WE.HostedBy WHERE WE.EventId = {0}'.format(eventId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get the next incrememnted session number for an event
@chaarg.route("/nextSessionNum/<eventId>", methods=['GET'])
def get_next_session_num(eventId):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT MAX(SessionNum) + 1 AS NextSessionNum FROM EventSession WHERE EventId = {0}'.format(eventId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Add a new event session to the db
@chaarg.route("/addEventSession", methods=['POST'])
def add_event_session():
    # insert into EventSession (EventId, SessionNum, Capacity, Date, Time, InstructedBy, LocatedAt) values (1, 1, 40, '2024-03-10', '16:15', 4, 1);
    eventId = request.form['eventId']
    sessionNum = request.form['sessionNum']
    capacity = request.form['capacity']
    datetime = str(request.form['datetime'])
    datetime_formatted = datetime[0:10] + ' ' + datetime[11:19]
    instructedBy = request.form['instructedBy']
    locatedAt = request.form['locatedAt']
    cursor = db.get_db().cursor()
    if(instructedBy != ''):
        cursor.execute("insert into EventSession (EventId, SessionNum, Capacity, DateTime, InstructedBy, LocatedAt) values ({0}, {1}, {2}, '{3}', {4}, {5})".format(eventId, sessionNum, capacity, datetime_formatted, instructedBy, locatedAt))
    else:
        cursor.execute("insert into EventSession (EventId, SessionNum, Capacity, DateTime, LocatedAt) values ({0}, {1}, {2}, '{3}', {4})".format(eventId, sessionNum, capacity, datetime_formatted, locatedAt))
    cursor.connection.commit()
    return "Success", 201