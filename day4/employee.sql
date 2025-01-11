-- Step 1: Create the Database
CREATE DATABASE studentdata;

-- Step 2: Use the Database
USE studentdata;

-- Step 3: Create the Students Table
CREATE TABLE students (
    PRN INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    cgpa DECIMAL(4, 2)
);

-- Step 4: Insert Data into Students Table
INSERT INTO students (PRN, FirstName, LastName, cgpa) 
VALUES 
    (1, 'Alice', 'Smith', 9.5),
    (2, 'Bob', 'Johnson', 8.3),
    (3, 'Akshaj', 'Chainani', 8.2),
    (4, 'Samuel', 'Jain', 8.3);

-- Step 5: Display All Records
SELECT * FROM students;

-- Step 6: Create a New Database and Switch to It
CREATE DATABASE capstonesql;
USE capstonesql;

-- Step 7: Create Employee Data Table
CREATE TABLE employeedata (
    Emp_id INT PRIMARY KEY,
    Emp_fullname VARCHAR(50),
    Emp_lastname VARCHAR(50),
    Emp_Dpt VARCHAR(50),
    Emp_salary DECIMAL(12, 2),
    joindate DATE
);

-- Step 8: Add Additional Columns to Employee Data
ALTER TABLE employeedata ADD COLUMN age INT, ADD COLUMN gender VARCHAR(10);

-- Step 9: Insert Data into Employee Data Table
INSERT INTO employeedata (Emp_id, Emp_fullname, Emp_lastname, Emp_Dpt, Emp_salary, joindate) 
VALUES 
    (1, 'Akshaj', 'Chainani', 'ROS Developer', 1000000, '2025-01-08'),
    (2, 'Apurva', 'Gosavi', 'HR', 1000000, '2025-01-08'),
    (3, 'Saachi', 'Parmar', 'Design', 1000000, '2025-01-08'),
    (4, 'Anushresth', 'Dube', 'Embedded Systems', 1000000, '2025-01-08'),
    (5, 'Ravi', 'Sharma', 'Marketing', 1200000, '2025-01-09'),
    (6, 'Priya', 'Verma', 'Finance', 1100000, '2025-01-09'),
    (7, 'Nikita', 'Jain', 'IT Support', 1050000, '2025-01-09');

-- Step 10: Update Age and Gender in Employee Data Table
UPDATE employeedata SET age = 20, gender = 'Male' WHERE Emp_id = 1;
UPDATE employeedata SET age = 28, gender = 'Male' WHERE Emp_id = 2;
UPDATE employeedata SET age = 30, gender = 'Female' WHERE Emp_id = 3;
UPDATE employeedata SET age = 32, gender = 'Female' WHERE Emp_id = 4;
UPDATE employeedata SET age = 35, gender = 'Male' WHERE Emp_id = 5;
UPDATE employeedata SET age = 27, gender = 'Female' WHERE Emp_id = 6;
UPDATE employeedata SET age = 33, gender = 'Male' WHERE Emp_id = 7;

-- Step 11: Select Data with Conditions
SELECT * FROM employeedata WHERE Emp_salary > 1000000;
SELECT * FROM employeedata WHERE age BETWEEN 25 AND 35;
SELECT * FROM employeedata ORDER BY Emp_salary DESC;

-- Step 12: Add an Index and Drop It
CREATE INDEX idx_dep ON employeedata(Emp_Dpt);
DROP INDEX idx_dep ON employeedata;

-- Step 13: Display All Employee Data
SELECT * FROM employeedata;

-- Step 14: Alter Employee Data Table Schema
ALTER TABLE employeedata MODIFY Emp_salary DECIMAL(15, 2);

-- Step 15: Drop Employee Data Table
DROP TABLE employeedata;

-- Step 16: Drop the Database
DROP DATABASE capstonesql;
