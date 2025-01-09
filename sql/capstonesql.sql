-- Step 1: Create the database
CREATE DATABASE emp;

-- Step 2: Use the database
USE emp;

-- Step 3: Create the table
CREATE TABLE emp (
    Emp_id INT PRIMARY KEY,
    Emp_fullname VARCHAR(50),
    Emp_lastname VARCHAR(50),
    Emp_Dpt VARCHAR(50),
    Emp_salary DECIMAL(12, 2),
    joindate DATE,
    age INT,
    gender VARCHAR(10)
);

-- Step 4: Insert data into the table
INSERT INTO emp (Emp_id, Emp_fullname, Emp_lastname, Emp_Dpt, Emp_salary, joindate, age, gender) 
VALUES 
    (1, 'John', 'Doe', 'Software Engineer', 900000, '2025-01-10', 25, 'Male'),
    (2, 'Alice', 'Smith', 'HR Manager', 950000, '2025-01-10', 30, 'Female'),
    (3, 'Bob', 'Johnson', 'Product Design', 980000, '2025-01-10', 28, 'Male'),
    (4, 'Eva', 'Williams', 'Embedded Systems', 1000000, '2025-01-10', 35, 'Female'),
    (5, 'James', 'Brown', 'Marketing', 1100000, '2025-01-10', 40, 'Male'),
    (6, 'Sophia', 'Davis', 'Finance', 1050000, '2025-01-10', 32, 'Female'),
    (7, 'William', 'Miller', 'IT Support', 1020000, '2025-01-10', 29, 'Male');

-- Step 5: Select all data
SELECT * FROM emp;

-- Step 6: Select specific column
SELECT Emp_fullname FROM emp;

-- Step 7: Count total employees
SELECT COUNT(*) AS total_employees FROM emp;

-- Step 8: Select rows with conditions
SELECT * FROM emp WHERE Emp_salary > 1000000;
SELECT * FROM emp WHERE age > 25;
SELECT * FROM emp WHERE age BETWEEN 25 AND 30;
SELECT * FROM emp WHERE YEAR(joindate) = 2025;

-- Step 9: Update table data
UPDATE emp SET Emp_salary = 950000 WHERE Emp_id = 1;
UPDATE emp SET joindate = '2020-01-10' WHERE Emp_id = 1;

-- Step 10: Order data by salary
SELECT * FROM emp ORDER BY Emp_salary ASC;

-- Step 11: Aggregate functions
SELECT MAX(Emp_salary) AS max_salary, AVG(Emp_salary) AS average_salary FROM emp;

-- Step 12: Rename columns
ALTER TABLE emp CHANGE Emp_fullname First_name VARCHAR(50);
ALTER TABLE emp CHANGE Emp_salary Monthly_salary DECIMAL(12, 2);

-- Step 13: Filter with distinct values
SELECT DISTINCT Emp_Dpt FROM emp;

-- Step 14: Additional filtering and LIKE patterns
SELECT * FROM emp WHERE First_name LIKE 'J%';
SELECT * FROM emp WHERE Emp_Dpt != 'HR Manager';

-- Step 15: Drop the table and database
DROP TABLE emp;
DROP DATABASE emp;
