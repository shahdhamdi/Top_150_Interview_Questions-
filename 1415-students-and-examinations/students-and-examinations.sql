# Write your MySQL query statement below
SELECT S.student_id, S.student_name, SJ.subject_name, COUNT(E.subject_name) AS attended_exams
FROM Students S
CROSS JOIN Subjects SJ 
left join Examinations E ON S.student_id= E.student_id AND SJ.subject_name= E.subject_name
GROUP BY  S.student_id, subject_name
order by S.student_id, SJ.subject_name