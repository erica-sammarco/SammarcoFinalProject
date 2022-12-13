-- Erica Sammarco
-- Project Phase 2
-- CHAARG Database Creation + Mock Data

CREATE DATABASE CHAARG;
GRANT ALL PRIVILEGES ON CHAARG.* TO 'webapp'@'%';
flush PRIVILEGES;

USE CHAARG;

CREATE TABLE Member (
    MemberId INT AUTO_INCREMENT NOT NULL,
    FirstName VARCHAR(30),
    LastName VARCHAR(30),
    Pronouns VARCHAR(12),
    Email VARCHAR(50),
    Phone CHAR(10),
    ChinstaUsername VARCHAR(30),
    PRIMARY KEY (MemberId)
);

-- MOCK MEMBER DATA
insert into Member (MemberId, FirstName, LastName, Pronouns, Email, Phone, ChinstaUsername) values (1, 'Annemarie', 'Kembrey', 'she/her', 'akembrey0@mediafire.com', '9268314346', 'akembrey0');
insert into Member (MemberId, FirstName, LastName, Pronouns, Email, Phone, ChinstaUsername) values (2, 'Gwendolyn', 'Hedling', 'she/her', 'ghedling1@mysql.com', '7982132171', 'ghedling1');
insert into Member (MemberId, FirstName, LastName, Pronouns, Email, Phone, ChinstaUsername) values (3, 'Keelia', 'Reilingen', 'she.her', 'kreilingen2@ted.com', '8858701174', 'kreilingen2');
insert into Member (MemberId, FirstName, LastName, Pronouns, Email, Phone, ChinstaUsername) values (4, 'Henderson', 'Gullan', 'he/him', 'hgullan3@usnews.com', '7031949795', 'hgullan3');
insert into Member (MemberId, FirstName, LastName, Pronouns, Email, Phone, ChinstaUsername) values (5, 'Aubert', 'Pettyfer', 'she/they', 'apettyfer4@marriott.com', '7741049643', 'apettyfer4');
insert into Member (MemberId, FirstName, LastName, Pronouns, Email, Phone, ChinstaUsername) values (6, 'Toddie', 'Morrant', 'she/he/they', 'tmorrant5@time.com', '6479825043', 'tmorrant5');
insert into Member (MemberId, FirstName, LastName, Pronouns, Email, Phone, ChinstaUsername) values (7, 'Kari', 'Whitham', 'she/they', 'kwhitham6@dagondesign.com', '2224084817', 'kwhitham6');
insert into Member (MemberId, FirstName, LastName, Pronouns, Email, Phone, ChinstaUsername) values (8, 'Annabela', 'Skarin', 'they/them', 'askarin7@patch.com', '4923620765', 'askarin7');
insert into Member (MemberId, FirstName, LastName, Pronouns, Email, Phone, ChinstaUsername) values (9, 'Gusti', 'Bowling', 'she/her', 'gbowling8@google.co.uk', '7914999225', 'gbowling8');
insert into Member (MemberId, FirstName, LastName, Pronouns, Email, Phone, ChinstaUsername) values (10, 'Duncan', 'Greenhalf', 'they/them', 'dgreenhalf9@istockphoto.com', '1965844119', 'dgreenhalf9');
insert into Member (MemberId, FirstName, LastName, Pronouns, Email, Phone, ChinstaUsername) values (11, 'Herold', 'Fleetham', 'he/him', 'hfleethama@harvard.edu', '2746958425', 'hfleethama');
insert into Member (MemberId, FirstName, LastName, Pronouns, Email, Phone, ChinstaUsername) values (12, 'Abbot', 'Shadwick', 'she/her', 'ashadwickb@huffingtonpost.com', '6428037640', 'ashadwickb');
insert into Member (MemberId, FirstName, LastName, Pronouns, Email, Phone, ChinstaUsername) values (13, 'Morrie', 'Basillon', 'she/her', 'mbasillonc@google.co.uk', '2937437793', 'mbasillonc');
insert into Member (MemberId, FirstName, LastName, Pronouns, Email, Phone, ChinstaUsername) values (14, 'Fowler', 'Rapi', 'she/her', 'frapid@phoca.cz', '5133125964', 'frapid');
insert into Member (MemberId, FirstName, LastName, Pronouns, Email, Phone, ChinstaUsername) values (15, 'Brina', 'Renault', 'she/her', 'brenaulte@boston.com', '8355854056', 'brenaulte');
insert into Member (MemberId, FirstName, LastName, Pronouns, Email, Phone, ChinstaUsername) values (16, 'Gabby', 'Gheerhaert', 'she/her', 'ggheerhaertf@google.ru', '4057880866', 'ggheerhaertf');
insert into Member (MemberId, FirstName, LastName, Pronouns, Email, Phone, ChinstaUsername) values (17, 'Corly', 'Beville', 'she/her', 'cbevilleg@goodreads.com', '9175948724', 'cbevilleg');
insert into Member (MemberId, FirstName, LastName, Pronouns, Email, Phone, ChinstaUsername) values (18, 'Sal', 'Roycroft', 'she/her', 'sroycrofth@europa.eu', '2095330318', 'sroycrofth');
insert into Member (MemberId, FirstName, LastName, Pronouns, Email, Phone, ChinstaUsername) values (19, 'Lindy', 'Isaq', 'she/her', 'lisaqi@vk.com', '2028416132', 'lisaqi');
insert into Member (MemberId, FirstName, LastName, Pronouns, Email, Phone, ChinstaUsername) values (20, 'Elsi', 'Harcase', 'she/her', 'eharcasej@constantcontact.com', '7202600584', 'eharcasej');
--

CREATE TABLE EventType (
    TypeId INT AUTO_INCREMENT NOT NULL,
    Type VARCHAR(30),
    PRIMARY KEY (TypeId)
);

-- MOCK EVENT TYPE DATA
insert into EventType (TypeId, Type) values (1, 'Spin');
insert into EventType (TypeId, Type) values (2, 'HIIT');
insert into EventType (TypeId, Type) values (3, 'Pilates');
insert into EventType (TypeId, Type) values (4, 'Yoga Flow');
insert into EventType (TypeId, Type) values (5, 'Hot Yoga');
insert into EventType (TypeId, Type) values (6, 'Social');
insert into EventType (TypeId, Type) values (7, 'Dance');
insert into EventType (TypeId, Type) values (8, 'Boxing');

--

CREATE TABLE Studio (
    StudioId INT AUTO_INCREMENT NOT NULL,
    Name VARCHAR(30),
    PRIMARY KEY (StudioId)
);

-- MOCK STUDIO DATA
insert into Studio (StudioId, Name) values (1, 'Tekfly');
insert into Studio (StudioId, Name) values (2, 'Katz');
insert into Studio (StudioId, Name) values (3, 'Meedoo');
insert into Studio (StudioId, Name) values (4, 'Topiczoom');
insert into Studio (StudioId, Name) values (5, 'Skibox');
insert into Studio (StudioId, Name) values (6, 'Skalith');
insert into Studio (StudioId, Name) values (7, 'Miboo');
insert into Studio (StudioId, Name) values (8, 'Quire');
insert into Studio (StudioId, Name) values (9, 'Gabspot');
insert into Studio (StudioId, Name) values (10, 'Voonder');
--

CREATE TABLE Location (
    LocationId INT AUTO_INCREMENT NOT NULL,
    Title VARCHAR(30),
    Address VARCHAR(40),
    City VARCHAR(20) DEFAULT 'Boston',
    State VARCHAR(20) DEFAULT 'Massachusetts',
    PostalCode CHAR(5),
    Country VARCHAR(20) DEFAULT 'USA',
    CommuteInfo TEXT,
    PRIMARY KEY (LocationId)
);

-- MOCK LOCATION DATA
insert into Location (LocationId, Title, Address, City, State, PostalCode, Country, CommuteInfo) values (1, 'Chatterpoint', '71012 Scott Hill', 'Boston', 'Massachusetts', '02199', 'USA', 'Vivamus vel nulla eget eros elementum pellentesque. Quisque porta volutpat erat.');
insert into Location (LocationId, Title, Address, City, State, PostalCode, Country, CommuteInfo) values (2, 'Ntag', '24 Petterle Point', 'Boston', 'Massachusetts', '02115', 'USA', 'Vivamus vestibulum sagittis sapien.');
insert into Location (LocationId, Title, Address, City, State, PostalCode, Country, CommuteInfo) values (3, 'Dazzlesphere', '1 Mesta Way', 'Boston', 'Massachusetts', '02115', 'USA', 'Maecenas pulvinar lobortis est. Phasellus sit amet erat.');
insert into Location (LocationId, Title, Address, City, State, PostalCode, Country, CommuteInfo) values (4, 'Eadel', '036 Bartillon Way', 'Boston', 'Massachusetts', '02115', 'USA', null);
insert into Location (LocationId, Title, Address, City, State, PostalCode, Country, CommuteInfo) values (5, 'Katz', '8 Dapin Lane', 'Boston', 'Massachusetts', '02115', 'USA', 'Vestibulum sed magna at nunc commodo placerat. Praesent blandit. Nam nulla.');
insert into Location (LocationId, Title, Address, City, State, PostalCode, Country, CommuteInfo) values (6, 'Yambee', '6733 Pine View Avenue', 'Boston', 'Massachusetts', '02121', 'USA', null);
insert into Location (LocationId, Title, Address, City, State, PostalCode, Country, CommuteInfo) values (7, 'Fliptune', '920 Sherman Hill', 'Boston', 'Massachusetts', '02115', 'USA', 'In hac habitasse platea dictumst. Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem. Integer tincidunt ante vel ipsum.');
insert into Location (LocationId, Title, Address, City, State, PostalCode, Country, CommuteInfo) values (8, 'Tagchat', '69 Bluestem Way', 'Boston', 'Massachusetts', '02110', 'USA', 'Cras in purus eu magna vulputate luctus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.');
insert into Location (LocationId, Title, Address, City, State, PostalCode, Country, CommuteInfo) values (9, 'Wikivu', '526 Rieder Court', 'Boston', 'Massachusetts', '02199', 'USA', 'Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.');
insert into Location (LocationId, Title, Address, City, State, PostalCode, Country, CommuteInfo) values (10, 'Fivebridge', '80 South Alley', 'Boston', 'Massachusetts', '02110', 'USA', 'Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.');
insert into Location (LocationId, Title, Address, City, State, PostalCode, Country, CommuteInfo) values (11, '440 Egan', '20 Forsyth Street', 'Boston', 'Massachusetts', '02115', 'USA', 'On campus!');
--

CREATE TABLE Instructor (
    InstructorId INT AUTO_INCREMENT NOT NULL,
    FirstName VARCHAR(30),
    LastName VARCHAR(30),
    InstructorAt INT,
    PRIMARY KEY (InstructorId),
    CONSTRAINT fk_1
        FOREIGN KEY (InstructorAt) REFERENCES Studio (StudioId)
);

-- MOCK INSTRUCTOR DATA
insert into Instructor (InstructorId, FirstName, LastName, InstructorAt) values (1, 'Noell', 'Akid', 3);
insert into Instructor (InstructorId, FirstName, LastName, InstructorAt) values (2, 'Alistair', 'Du Fray', 1);
insert into Instructor (InstructorId, FirstName, LastName, InstructorAt) values (3, 'Brittany', 'Cumberland', 2);
insert into Instructor (InstructorId, FirstName, LastName, InstructorAt) values (4, 'Frances', 'Tolumello', 2);
insert into Instructor (InstructorId, FirstName, LastName, InstructorAt) values (5, 'Ashbey', 'Cicchinelli', 6);
insert into Instructor (InstructorId, FirstName, LastName, InstructorAt) values (6, 'Vinny', 'Vidgen', 10);
insert into Instructor (InstructorId, FirstName, LastName, InstructorAt) values (7, 'Dewain', 'Sisselot', 10);
insert into Instructor (InstructorId, FirstName, LastName, InstructorAt) values (8, 'Orin', 'Reddan', 10);
insert into Instructor (InstructorId, FirstName, LastName, InstructorAt) values (9, 'Kendra', 'Aingell', 7);
insert into Instructor (InstructorId, FirstName, LastName, InstructorAt) values (10, 'Ignaz', 'Gosforth', 4);
insert into Instructor (InstructorId, FirstName, LastName, InstructorAt) values (11, 'Yolanthe', 'MacDonnell', 7);
insert into Instructor (InstructorId, FirstName, LastName, InstructorAt) values (12, 'Mari', 'Suttling', 2);
insert into Instructor (InstructorId, FirstName, LastName, InstructorAt) values (13, 'Matthias', 'Ugo', 6);
insert into Instructor (InstructorId, FirstName, LastName, InstructorAt) values (14, 'Sean', 'Racine', 3);
insert into Instructor (InstructorId, FirstName, LastName, InstructorAt) values (15, 'Shelly', 'Cosh', 1);
--

CREATE TABLE WeeklyEvent (
    EventId INT AUTO_INCREMENT NOT NULL,
    Week INT,
    Semester VARCHAR(10),
    Year SMALLINT,
    Public BOOLEAN DEFAULT FALSE,
    TypeId INT NOT NULL,
    HostedBy INT,
    PRIMARY KEY (EventId),
    CONSTRAINT fk_2
        FOREIGN KEY (TypeId) REFERENCES EventType (TypeId),
    CONSTRAINT fk_3
        FOREIGN KEY (HostedBy) REFERENCES Studio (StudioId)
);

-- MOCK WEEKLY EVENT DATA
insert into WeeklyEvent (EventId, Week, Semester, Year, Public, TypeId, HostedBy) values (1, 9, 'Spring', 2024, true, 5, 8);
insert into WeeklyEvent (EventId, Week, Semester, Year, Public, TypeId, HostedBy) values (2, 6, 'Spring', 2024, true, 3, 5);
insert into WeeklyEvent (EventId, Week, Semester, Year, Public, TypeId, HostedBy) values (3, 5, 'Fall', 2022, false, 1, 1);
insert into WeeklyEvent (EventId, Week, Semester, Year, Public, TypeId, HostedBy) values (4, 15, 'Fall', 2023, false, 5, 1);
insert into WeeklyEvent (EventId, Week, Semester, Year, Public, TypeId, HostedBy) values (5, 19, 'Spring', 2024, true, 5, 1);
insert into WeeklyEvent (EventId, Week, Semester, Year, Public, TypeId, HostedBy) values (6, 2, 'Fall', 2022, true, 1, 5);
insert into WeeklyEvent (EventId, Week, Semester, Year, Public, TypeId, HostedBy) values (7, 5, 'Fall', 2023, true, 8, 6);
insert into WeeklyEvent (EventId, Week, Semester, Year, Public, TypeId, HostedBy) values (8, 13, 'Fall', 2023, false, 1, 10);
insert into WeeklyEvent (EventId, Week, Semester, Year, Public, TypeId, HostedBy) values (9, 16, 'Fall', 2022, false, 1, 2);
insert into WeeklyEvent (EventId, Week, Semester, Year, Public, TypeId, HostedBy) values (10, 1, 'Summer', 2024, true, 4, 3);
insert into WeeklyEvent (EventId, Week, Semester, Year, Public, TypeId, HostedBy) values (11, 18, 'Spring', 2024, false, 7, 9);
insert into WeeklyEvent (EventId, Week, Semester, Year, Public, TypeId, HostedBy) values (12, 8, 'Summer', 2022, true, 5, 9);
insert into WeeklyEvent (EventId, Week, Semester, Year, Public, TypeId, HostedBy) values (13, 15, 'Spring', 2024, false, 5, 3);
insert into WeeklyEvent (EventId, Week, Semester, Year, Public, TypeId, HostedBy) values (14, 15, 'Spring', 2023, true, 5, 9);
insert into WeeklyEvent (EventId, Week, Semester, Year, Public, TypeId, HostedBy) values (15, 6, 'Fall', 2023, true, 3, 6);
--

CREATE TABLE StudioLocation (
    LocationId INT NOT NULL,
    StudioId INT NOT NULL,
    PRIMARY KEY (LocationId, StudioId),
    CONSTRAINT fk_4
        FOREIGN KEY (LocationId) REFERENCES Location (LocationId),
    CONSTRAINT fk_5
        FOREIGN KEY (StudioId) REFERENCES Studio (StudioId)
);

insert into StudioLocation (LocationId, StudioId) values (1, 4);
insert into StudioLocation (LocationId, StudioId) values (2, 9);
insert into StudioLocation (LocationId, StudioId) values (3, 2);
insert into StudioLocation (LocationId, StudioId) values (4, 2);
insert into StudioLocation (LocationId, StudioId) values (5, 5);
insert into StudioLocation (LocationId, StudioId) values (6, 8);
insert into StudioLocation (LocationId, StudioId) values (7, 3);
insert into StudioLocation (LocationId, StudioId) values (8, 10);
insert into StudioLocation (LocationId, StudioId) values (9, 2);
insert into StudioLocation (LocationId, StudioId) values (10, 4);
insert into StudioLocation (LocationId, StudioId) values (11, 1);
insert into StudioLocation (LocationId, StudioId) values (11, 2);
insert into StudioLocation (LocationId, StudioId) values (11, 3);
insert into StudioLocation (LocationId, StudioId) values (11, 4);
insert into StudioLocation (LocationId, StudioId) values (11, 5);
insert into StudioLocation (LocationId, StudioId) values (11, 6);
insert into StudioLocation (LocationId, StudioId) values (11, 7);
insert into StudioLocation (LocationId, StudioId) values (11, 8);
insert into StudioLocation (LocationId, StudioId) values (11, 9);
insert into StudioLocation (LocationId, StudioId) values (11, 10);

CREATE TABLE Review (
    EventId INT NOT NULL,
    MemberId INT NOT NULL,
    Bolts SMALLINT,
    Comment TEXT,
    PRIMARY KEY (EventId, MemberId),
    CONSTRAINT bolt_num
        CHECK (Bolts BETWEEN 0 AND 5),
    CONSTRAINT fk_6
        FOREIGN KEY (EventId) REFERENCES WeeklyEvent (EventId),
    CONSTRAINT fk_7
        FOREIGN KEY (MemberId) REFERENCES Member (MemberId)
);

-- MOCK REVIEW DATA
insert into Review (EventId, MemberId, Bolts, Comment) values (9, 16, 0, 'Sed sagittis.');
insert into Review (EventId, MemberId, Bolts, Comment) values (9, 15, 2, 'Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo.');
insert into Review (EventId, MemberId, Bolts, Comment) values (5, 2, 0, 'Phasellus in felis.');
insert into Review (EventId, MemberId, Bolts, Comment) values (12, 5, 1, 'In eleifend quam a odio. In hac habitasse platea dictumst. Maecenas ut massa quis augue luctus tincidunt. Nulla mollis molestie lorem.');
insert into Review (EventId, MemberId, Bolts, Comment) values (3, 20, 5, 'Suspendisse potenti. Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum.');
insert into Review (EventId, MemberId, Bolts, Comment) values (13, 6, 2, 'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque.');
insert into Review (EventId, MemberId, Bolts, Comment) values (8, 12, 0, 'Suspendisse ornare consequat lectus.');
insert into Review (EventId, MemberId, Bolts, Comment) values (14, 16, 1, 'Donec posuere metus vitae ipsum. Aliquam non mauris. Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet.');
insert into Review (EventId, MemberId, Bolts, Comment) values (13, 12, 3, 'Integer tincidunt ante vel ipsum. Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat. Praesent blandit. Nam nulla.');
insert into Review (EventId, MemberId, Bolts, Comment) values (15, 3, 4, 'Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem.');
insert into Review (EventId, MemberId, Bolts, Comment) values (7, 15, 1, 'Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.');
insert into Review (EventId, MemberId, Bolts, Comment) values (6, 9, 5, 'Nulla facilisi. Cras non velit nec nisi vulputate nonummy.');
insert into Review (EventId, MemberId, Bolts, Comment) values (10, 17, 2, 'Nulla tellus.');
insert into Review (EventId, MemberId, Bolts, Comment) values (15, 7, 2, 'Morbi ut odio.');
insert into Review (EventId, MemberId, Bolts, Comment) values (15, 5, 3, 'Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.');
insert into Review (EventId, MemberId, Bolts, Comment) values (2, 17, 1, 'Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus. Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst. Maecenas ut massa quis augue luctus tincidunt.');
insert into Review (EventId, MemberId, Bolts, Comment) values (2, 18, 1, 'Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam. Suspendisse potenti. Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum.');
insert into Review (EventId, MemberId, Bolts, Comment) values (13, 7, 0, 'Vivamus in felis eu sapien cursus vestibulum. Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.');
insert into Review (EventId, MemberId, Bolts, Comment) values (1, 14, 5, 'Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam. Suspendisse potenti. Nullam porttitor lacus at turpis.');
insert into Review (EventId, MemberId, Bolts, Comment) values (1, 17, 2, 'Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue.');
--

CREATE TABLE EventSession (
    EventId INT NOT NULL,
    SessionNum INT NOT NULL,
    Capacity INT,
    DateTime DATETIME,
    InstructedBy INT,
    LocatedAt INT NOT NULL,
    PRIMARY KEY (EventId, SessionNum),
    CONSTRAINT fk_8
        FOREIGN KEY (EventId) REFERENCES WeeklyEvent (EventId),
    CONSTRAINT fk_9
        FOREIGN KEY (InstructedBy) REFERENCES Instructor (InstructorId),
    CONSTRAINT fk_10
        FOREIGN KEY (LocatedAt) REFERENCES Location (LocationId)
);

-- MOCK EVENT SESSION DATA
insert into EventSession (EventId, SessionNum, Capacity, DateTime, InstructedBy, LocatedAt) values (1, 1, 40, '2024-03-10 16:15:00', 4, 1);
insert into EventSession (EventId, SessionNum, Capacity, DateTime, InstructedBy, LocatedAt) values (1, 2, 40, '2024-03-10 17:15:00', 4, 1);
insert into EventSession (EventId, SessionNum, Capacity, DateTime, InstructedBy, LocatedAt) values (1, 3, 40, '2024-03-10 18:15:00', 4, 1);
insert into EventSession (EventId, SessionNum, Capacity, DateTime, InstructedBy, LocatedAt) values (2, 1, 35, '2024-02-21 16:00:00', 4, 1);
insert into EventSession (EventId, SessionNum, Capacity, DateTime, InstructedBy, LocatedAt) values (3, 1, 29, '2022-10-03 19:00:00', 12, 4);
insert into EventSession (EventId, SessionNum, Capacity, DateTime, InstructedBy, LocatedAt) values (4, 1, 40, '2023-09-04 18:20:00', 4, 4);
insert into EventSession (EventId, SessionNum, Capacity, DateTime, InstructedBy, LocatedAt) values (6, 1, 42, '2022-11-17 16:30:00', 5, 3);
insert into EventSession (EventId, SessionNum, Capacity, DateTime, InstructedBy, LocatedAt) values (6, 2, 29, '2021-11-17 19:45:00', 15, 11);
insert into EventSession (EventId, SessionNum, Capacity, DateTime, InstructedBy, LocatedAt) values (7, 2, 34, '2023-10-26 20:30:00', 8, 1);
insert into EventSession (EventId, SessionNum, Capacity, DateTime, InstructedBy, LocatedAt) values (7, 1, 25, '2023-10-26 17:30:00', 14, 4);
insert into EventSession (EventId, SessionNum, Capacity, DateTime, InstructedBy, LocatedAt) values (8, 2, 39, '2023-12-12 20:30:00', 8, 2);
insert into EventSession (EventId, SessionNum, Capacity, DateTime, InstructedBy, LocatedAt) values (9, 1, 27, '2022-08-21 18:15:00', 1, 6);
insert into EventSession (EventId, SessionNum, Capacity, DateTime, InstructedBy, LocatedAt) values (13, 1, 50, '2024-05-24 15:02:00', 10, 3);
insert into EventSession (EventId, SessionNum, Capacity, DateTime, InstructedBy, LocatedAt) values (14, 1, 3, '2023-05-24 15:00:00', 10, 3);
--

CREATE TABLE SignUp (
    SignUpId INT NOT NULL AUTO_INCREMENT,
    MemberId INT NOT NULL,
    EventId INT NOT NULL,
    SessionNum INT NOT NULL,
    Attended BOOLEAN DEFAULT FALSE,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    DeletedAt DATETIME,
    PRIMARY KEY (SignUpId),
    CONSTRAINT fk_11
        FOREIGN KEY (MemberId) REFERENCES Member (MemberId),
    CONSTRAINT fk_12
        FOREIGN KEY (EventId, SessionNum) REFERENCES EventSession (EventId, SessionNum)
);

-- MOCK SIGN UP DATA
insert into SignUp (MemberId, EventId, SessionNum) values (10, 13, 1);
insert into SignUp (MemberId, EventId, SessionNum) values (11, 1, 1);
insert into SignUp (MemberId, EventId, SessionNum) values (17, 1, 3);
insert into SignUp (MemberId, EventId, SessionNum) values (8, 13, 1);
insert into SignUp (MemberId, EventId, SessionNum) values (17, 6, 2);
insert into SignUp (MemberId, EventId, SessionNum) values (11, 13, 1);
insert into SignUp (MemberId, EventId, SessionNum) values (16, 1, 2);
insert into SignUp (MemberId, EventId, SessionNum) values (10, 8, 2);
insert into SignUp (MemberId, EventId, SessionNum) values (7, 7, 2);
insert into SignUp (MemberId, EventId, SessionNum) values (2, 7, 1);
insert into SignUp (MemberId, EventId, SessionNum) values (15, 2, 1);
insert into SignUp (MemberId, EventId, SessionNum) values (12, 1, 1);
insert into SignUp (MemberId, EventId, SessionNum) values (6, 7, 2);
insert into SignUp (MemberId, EventId, SessionNum) values (10, 3, 1);
insert into SignUp (MemberId, EventId, SessionNum) values (15, 13, 1);
insert into SignUp (MemberId, EventId, SessionNum) values (20, 13, 1);
insert into SignUp (MemberId, EventId, SessionNum) values (17, 8, 2);
insert into SignUp (MemberId, EventId, SessionNum) values (12, 7, 1);
insert into SignUp (MemberId, EventId, SessionNum) values (5, 2, 1);
insert into SignUp (MemberId, EventId, SessionNum) values (1, 14, 1);
insert into SignUp (MemberId, EventId, SessionNum) values (2, 14, 1);
insert into SignUp (MemberId, EventId, SessionNum) values (3, 14, 1);
--

CREATE TABLE Waitlist (
    WaitlistId INT NOT NULL AUTO_INCREMENT,
    MemberId INT NOT NULL,
    EventId INT NOT NULL,
    SessionNum INT NOT NULL,
    Position INT,
    Ticketed BOOLEAN DEFAULT FALSE,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    DeletedAt DATETIME,
    PRIMARY KEY (WaitlistId),
    CONSTRAINT fk_13
        FOREIGN KEY (MemberId) REFERENCES Member (MemberId),
    CONSTRAINT fk_14
        FOREIGN KEY (EventId, SessionNum) REFERENCES EventSession (EventId, SessionNum)
);

-- MOCK WAITLIST DATA
insert into Waitlist (MemberId, EventId, SessionNum, Position) values (4, 14, 1, 1);
insert into Waitlist (MemberId, EventId, SessionNum, Position) values (5, 14, 1, 2);
insert into Waitlist (MemberId, EventId, SessionNum, Position) values (6, 14, 1, 3);
insert into Waitlist (MemberId, EventId, SessionNum, Position, Ticketed) values (17, 8, 2, 1, TRUE);
insert into Waitlist (MemberId, EventId, SessionNum, Position, Ticketed) values (12, 7, 1, 1, TRUE);
insert into Waitlist (MemberId, EventId, SessionNum, Position, Ticketed) values (5, 2, 1, 1, TRUE);
