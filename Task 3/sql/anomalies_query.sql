
-- Inserion anomaly
INSERT INTO club_members_unf
(student_id, student_name, email, club_name, club_mentor, join_date)
VALUES
(NULL, NULL, NULL, 'Robotics Club', 'Mr. Kumar', NULL);


-- update anomaly
UPDATE club_members
SET club_mentor = 'Mr. Sharma'
WHERE club_name = 'Music Club'
LIMIT 1;

-- deletion anomaly
DELETE FROM club_members
WHERE club_name = 'Sports Club';
