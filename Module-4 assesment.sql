CREATE DATABASE nobel;
USE nobel;
-- Create the table
CREATE TABLE Nobel_win (
    year INT,
    subject VARCHAR(50),
    winner VARCHAR(100),
    country VARCHAR(50),
    category VARCHAR(50)
);

-- Insert sample data
INSERT INTO Nobel_win (year, subject, winner, country, category) VALUES
(1965, 'Chemistry', 'Robert Burns Woodward', 'USA', 'Scientist'),
(1969, 'Physics', 'Murray Gell-Mann', 'USA', 'Scientist'),
(1970, 'Chemistry', 'Luis Federico Leloir', 'Argentina', 'Scientist'),
(1970, 'Physics', 'Hannes Alfvén', 'Sweden', 'Scientist'),
(1970, 'Medicine', 'Ulf von Euler', 'Sweden', 'Scientist'),
(1970, 'Economics', 'Paul Samuelson', 'USA', 'Economist'),
(1970, 'Literature', 'Aleksandr Solzhenitsyn', 'Russia', 'Writer'),
(1970, 'Peace', 'Norman Borlaug', 'USA', 'Scientist'),
(1970, 'Medicine', 'Bernard Katz', 'UK', 'Scientist'),
(1971, 'Chemistry', 'Gerhard Herzberg', 'Canada', 'Scientist'),
(1971, 'Peace', 'Willy Brandt', 'Germany', 'Politician'),
(1972, 'Physics', 'John Bardeen', 'USA', 'Scientist'),
(1973, 'Peace', 'Henry Kissinger', 'USA', 'Politician'),
(1974, 'Literature', 'Eyvind Johnson', 'Sweden', 'Writer'),
(1975, 'Chemistry', 'John Cornforth', 'Australia', 'Scientist'),
(1975, 'Economics', 'Leonid Kantorovich', 'Russia', 'Economist'),
(1975, 'Medicine', 'David Baltimore', 'USA', 'Scientist'),
(1976, 'Physics', 'Burton Richter', 'USA', 'Scientist'),
(1968, 'Economics', 'Jan Tinbergen', 'Netherlands', 'Economist'),
(1966, 'Peace', 'Louis Mountbatten', 'UK', 'Politician'); -- has 'Louis'

-- 1. Nobel prize winners of the year 1970
SELECT year, subject, winner
FROM Nobel_win
WHERE year = 1970;

-- 2. Nobel prize winners in Chemistry between 1965 and 1975
SELECT year, subject, winner, country
FROM Nobel_win
WHERE subject = 'Chemistry'
  AND year BETWEEN 1965 AND 1975;

-- 3. Winners whose first name matches with 'Louis'
SELECT year, subject, winner, country
FROM Nobel_win
WHERE winner LIKE 'Louis%';

-- 4. Nobel prize winners for subjects not starting with 'P'
SELECT year, subject, winner
FROM Nobel_win
WHERE subject NOT LIKE 'P%'
ORDER BY year DESC, winner ASC;

-- 5. Details of 1970 Nobel prize winners with special ordering
SELECT year, subject, winner, country, category
FROM Nobel_win
WHERE year = 1970
ORDER BY 
    CASE 
        WHEN subject IN ('Chemistry', 'Economics') THEN 2
        ELSE 1
    END,
    subject ASC;
