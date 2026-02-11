CREATE TABLE student_2nf (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO student_2nf
SELECT DISTINCT student_id, student_name, email
FROM club_members_1nf;

CREATE TABLE club_2nf (
    club_name VARCHAR(100) PRIMARY KEY,
    club_room VARCHAR(50),
    club_mentor VARCHAR(100)
);

INSERT INTO club_2nf
SELECT DISTINCT club_name, club_room, club_mentor
FROM club_members_1nf;

CREATE TABLE membership_2nf (
    student_id INT,
    club_name VARCHAR(100),
    join_date DATE,
    PRIMARY KEY (student_id, club_name),
    FOREIGN KEY (student_id) REFERENCES student_2nf(student_id),
    FOREIGN KEY (club_name) REFERENCES club_2nf(club_name)
);

INSERT INTO membership_2nf
SELECT DISTINCT student_id, club_name, join_date
FROM club_members_1nf;
