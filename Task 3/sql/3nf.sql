CREATE TABLE club_3nf (
    club_id INT AUTO_INCREMENT PRIMARY KEY,
    club_name VARCHAR(100) UNIQUE,
    club_room VARCHAR(50),
    club_mentor VARCHAR(100)
);

INSERT INTO club_3nf (club_name, club_room, club_mentor)
SELECT DISTINCT club_name, club_room, club_mentor
FROM club_members_1nf;

CREATE TABLE student_3nf (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    email VARCHAR(100)
);
INSERT INTO student_3nf
SELECT DISTINCT student_id, student_name, email
FROM club_members_1nf;

CREATE TABLE membership_3nf (
    membership_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    club_id INT,
    join_date DATE,
    FOREIGN KEY (student_id) REFERENCES student_3nf(student_id),
    FOREIGN KEY (club_id) REFERENCES club_3nf(club_id)
);

INSERT INTO membership_3nf (student_id, club_id, join_date)
SELECT 
    cm.student_id,
    c3.club_id,
    cm.join_date
FROM club_members_1nf cm
JOIN club_3nf c3 ON cm.club_name = c3.club_name;
