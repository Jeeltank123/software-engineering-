CREATE DATABASE bank;
USE bank;
-- Create Bank table
CREATE TABLE Bank (
    branch_id INT PRIMARY KEY,
    branch_name VARCHAR(100),
    branch_city VARCHAR(100)
);

-- Create Account Holder table
CREATE TABLE Account_holder (
    acc_holder_id INT PRIMARY KEY,
    account_no VARCHAR(20),
    acc_holder_name VARCHAR(100),
    city VARCHAR(100),
    contact VARCHAR(15),
    date_created DATE,
    acc_status VARCHAR(20),   -- Active or Terminated
    acc_type VARCHAR(50),
    balance DECIMAL(12,2)
);

-- Create Loan table
CREATE TABLE Loan (
    loan_no INT PRIMARY KEY,
    branch_id INT,
    acc_holder_id INT,
    loan_amount DECIMAL(12,2),
    loan_type VARCHAR(50),
    FOREIGN KEY (branch_id) REFERENCES Bank(branch_id),
    FOREIGN KEY (acc_holder_id) REFERENCES Account_holder(acc_holder_id)
);

-- ============================================
-- Example Data Inserts
-- ============================================
INSERT INTO Bank VALUES
(1, 'Main Branch', 'Mumbai'),
(2, 'Central Branch', 'Delhi'),
(3, 'West Branch', 'Mumbai');

INSERT INTO Account_holder VALUES
(101, 'A1001', 'Jeel Tank', 'Mumbai', '9876543210', '2025-02-14', 'Active', 'Savings', 1000.00),
(102, 'A1002', 'Ravi Sharma', 'Mumbai', '9876500000', '2025-02-16', 'Active', 'Current', 500.00),
(103, 'A1003', 'Anjali Patel', 'Delhi', '9876511111', '2025-02-10', 'Active', 'Savings', 2000.00);

INSERT INTO Loan VALUES
(201, 1, 101, 50000, 'Home Loan'),
(202, 2, 103, 20000, 'Car Loan');

-- ============================================
-- 1. Transaction: Transfer $100 from Account A to Account B
-- Example: From Jeel Tank (A1001) → Ravi Sharma (A1002)
START TRANSACTION;

UPDATE Account_holder
SET balance = balance - 100
WHERE account_no = 'A1001';

UPDATE Account_holder
SET balance = balance + 100
WHERE account_no = 'A1002';

COMMIT;

-- ============================================
-- 2. Fetch details of account holders from the same city
SELECT *
FROM Account_holder a1
JOIN Account_holder a2 
    ON a1.city = a2.city 
   AND a1.acc_holder_id <> a2.acc_holder_id;

-- ============================================
-- 3. Fetch account number and name where account created after 15th of month
SELECT account_no, acc_holder_name
FROM Account_holder
WHERE DAY(date_created) > 15;

-- ============================================
-- 4. Display city name and count of branches
SELECT branch_city, COUNT(branch_id) AS Count_Branch
FROM Bank
GROUP BY branch_city;

-- ============================================
-- 5. Display account holder id, name, branch id, and loan amount (JOIN)
SELECT ah.acc_holder_id, ah.acc_holder_name, l.branch_id, l.loan_amount
FROM Account_holder ah
JOIN Loan l ON ah.acc_holder_id = l.acc_holder_id;
