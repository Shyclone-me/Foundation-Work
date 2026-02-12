-- Insert student
INSERT INTO student_3nf (student_name, email)
VALUES ('Khushi', 'khushi@email.com'), ('Peina', 'peina@email.com');

-- Insert club
INSERT INTO club_3nf (club_name, club_room, club_mentor)
VALUES ('Robotics Club', 'Lab 204', 'Mr. Shyam');

-- Display students
SELECT * FROM student_3nf;

-- Display clubs
SELECT * FROM club_3nf;

-- Update Khushi's email
UPDATE student_3nf
SET email = 'khushi.updated@email.com'
WHERE student_name = 'Khushi';

-- Delete Khushi from student table
DELETE FROM student_3nf
WHERE student_id = 9;
