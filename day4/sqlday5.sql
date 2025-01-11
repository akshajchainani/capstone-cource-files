-- Create department table
CREATE TABLE department (
    Department_ID INT AUTO_INCREMENT PRIMARY KEY,
    Department_Name VARCHAR(100) NOT NULL,
    Location VARCHAR(100) NOT NULL
);

-- Insert data into department table
INSERT INTO department (Department_Name, Location)
VALUES
    ('Software Engineer', 'New York'),
    ('HR Manager', 'Los Angeles'),
    ('Product Design', 'Chicago'),
    ('Embedded Systems', 'San Francisco'),
    ('Marketing', 'San Francisco'),
    ('Finance', 'Chicago'),
    ('IT Support', 'New York');

-- Select all data from department
SELECT * FROM department;

-- Select all data from emp
SELECT * FROM emp;

-- Left Join: Employee and Department
SELECT e.First_name, e.Emp_lastname, e.Emp_Dpt, d.Location
FROM emp e
LEFT JOIN department d
ON e.Emp_Dpt = d.Department_Name;

-- Right Join: Employee and Department
SELECT e.First_name, e.Emp_lastname, e.Emp_Dpt, d.Location
FROM emp e
RIGHT JOIN department d
ON e.Emp_Dpt = d.Department_Name;

-- Inner Join: Employees in the same department
SELECT e1.First_name AS Employee1, e2.First_name AS Employee2, e1.Emp_Dpt AS Department
FROM emp e1
INNER JOIN emp e2
ON e1.Emp_Dpt = e2.Emp_Dpt
WHERE e1.Emp_id != e2.Emp_id;

-- Aggregation: Count employees per department
SELECT d.Department_Name, COUNT(e.Emp_id) AS Number_of_Employees
FROM emp e
JOIN department d ON e.Emp_Dpt = d.Department_Name
GROUP BY d.Department_Name;

-- Employees with salaries above average in their department
SELECT e.First_name AS Employee_Name,
       e.Emp_lastname AS Employee_Lastname,
       e.Emp_Dpt AS Department,
       e.Monthly_salary AS Salary,
       d.Location AS Department_Location
FROM emp e
JOIN department d ON e.Emp_Dpt = d.Department_Name
WHERE e.Monthly_salary > (
    SELECT AVG(Monthly_salary)
    FROM emp
    WHERE Emp_Dpt = e.Emp_Dpt
)
ORDER BY e.Monthly_salary DESC;
