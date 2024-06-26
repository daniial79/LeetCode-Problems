SELECT 
    Department.Name AS Department, 
    Employee.Name AS Employee, 
    Employee.Salary AS Salary
FROM Department JOIN Employee ON Employee.DepartmentId = Department.Id
AND (Employee.departmentId, Employee.Salary) IN (
    SELECT e.departmentId, MAX(e.Salary) FROM Employee e 
    GROUP BY e.departmentId
)