SELECT 
    Class
FROM Courses
GROUP BY Class
HAVING COUNT(Student) >= 5;