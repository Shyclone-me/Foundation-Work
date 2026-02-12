SELECT 
    s.student_name AS "Student Name",
    c.club_name AS "Club Name",
    m.join_date AS "Join Date"
FROM membership_3nf m
JOIN student_3nf s ON m.student_id = s.student_id
JOIN club_3nf c ON m.club_id = c.club_id;
 