from flask import Blueprint, request, jsonify, make_response
import json
from src import db


chaarg = Blueprint('chaarg', __name__)

# This is a base route
# we simply return a string.  
@chaarg.route('/')
def home():
    return ('<h1>Hello from the CHAARG app!!</h1>')

# Get all events from the DB
# @chaarg.route('/events', methods=['GET'])
# def get_events():
    # cursor = db.get_db().cursor()
    # cursor.execute('SELECT ES.EventId, ES.SessionNum, Date, Time, Name, Type, Title AS Location, Address, (Capacity - COUNT(MemberId)) AS RemainingSpots\
    #     FROM EventSession ES\
    #     JOIN WeeklyEvent WE on ES.EventId = WE.EventId\
    #     JOIN Studio S on WE.HostedBy = S.StudioId\
    #     JOIN EventType ET on WE.TypeId = ET.TypeId\
    #     JOIN Location L on ES.LocatedAt = L.LocationId\
    #     JOIN SignUp SU on ES.EventId = SU.EventId and ES.SessionNum = SU.SessionNum\
    #     GROUP BY ES.EventId, ES.SessionNum')
    # row_headers = [x[0] for x in cursor.description]
    # json_data = []
    # theData = cursor.fetchall()
    # for row in theData:
    #     json_data.append(dict(zip(row_headers, row)))
    # the_response = make_response(json.dumps(json_data, default=str)) # jsonify(json_data)
    # the_response.status_code = 200
    # the_response.mimetype = 'application/json'
    # return the_response

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


# Get sign up for event, if it exists
@chaarg.route('/memberSignUp/<memberID>/<eventID>/<sessionNum>', methods=['GET'])
def get_signup(memberID, eventID, sessionNum):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM SignUp WHERE MemberId = {0} AND EventId = {1} AND SessionNum = {2}'.format(memberID, eventID, sessionNum))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# SELECT * FROM SignUp WHERE MemberId = 1 AND EventId = 14 AND SessionNum = 1;

# Get all events for a given member from the DB
@chaarg.route('/memberEvents/<memberID>', methods=['GET'])
def get_member_events(memberID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT ES.EventId, ES.SessionNum, Date, Time, Name, Type, Title AS Location, Address, (Capacity - COUNT(MemberId)) AS RemainingSpots\
        FROM EventSession ES\
        JOIN WeeklyEvent WE on ES.EventId = WE.EventId\
        JOIN Studio S on WE.HostedBy = S.StudioId\
        JOIN EventType ET on WE.TypeId = ET.TypeId\
        JOIN Location L on ES.LocatedAt = L.LocationId\
        JOIN SignUp SU on ES.EventId = SU.EventId and ES.SessionNum = SU.SessionNum\
        WHERE MemberId = {0}\
        GROUP BY ES.EventId, ES.SessionNum'.format(memberID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(json.dumps(json_data, default=str)) # jsonify(json_data)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get all events with information for the member with particular memberID
@chaarg.route('/allEvents/<memberID>', methods=['GET'])
def get_events_for_member(memberID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT ES.EventId, ES.SessionNum, Date, Time, Name, Type, Title AS Location, Address,\
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

@chaarg.route("/signup", methods = ['POST'])
def post_signup():
    memberId = request.form['memberId']
    eventId = request.form['eventId']
    sessionNum = request.form['sessionNum']
    cursor = db.get_db().cursor()
    cursor.execute('insert into SignUp (MemberId, EventId, SessionNum) values ({0}, {1}, {2})'.format(memberId, eventId, sessionNum))
    cursor.connection.commit()
    return "Success", 201

@chaarg.route("/deleteSignUp", methods = ['PATCH'])
def delete_signup():
    memberId = request.form['memberId']
    eventId = request.form['eventId']
    sessionNum = request.form['sessionNum']
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE SignUp SET DeletedAt = CURRENT_TIMESTAMP WHERE MemberId = {0} AND EventId = {1} AND SessionNum = {2}'.format(memberId, eventId, sessionNum))
    cursor.connection.commit()
    return "Success", 201


@chaarg.route("/waitlist", methods = ['POST'])
def post_waitlist():
    memberId = request.form['memberId']
    eventId = request.form['eventId']
    sessionNum = request.form['sessionNum']
    cursor = db.get_db().cursor()
    cursor.execute('insert into Waitlist (MemberId, EventId, SessionNum) values ({0}, {1}, {2})'.format(memberId, eventId, sessionNum))
    cursor.connection.commit()
    return "Success", 201

@chaarg.route("/deleteWaitlist", methods = ['PATCH'])
def delete_waitlist():
    memberId = request.form['memberId']
    eventId = request.form['eventId']
    sessionNum = request.form['sessionNum']
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE Waitlist SET DeletedAt = CURRENT_TIMESTAMP WHERE MemberId = {0} AND EventId = {1} AND SessionNum = {2}'.format(memberId, eventId, sessionNum))
    cursor.connection.commit()
    return "Success", 201

@chaarg.route("/getWaitlist", methods=['GET'])
def get_waitlist():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Waitlist')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(json.dumps(json_data, default=str))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response