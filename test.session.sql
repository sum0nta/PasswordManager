-- @block
CREATE TABLE Passwords(
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255),
    pass TEXT,
    website VARCHAR(255)
)
-- @block
INSERT INTO Passwords(email,pass,website)
VALUES ('xyz@bracu.ac.bd','ilikeapples12','https://www.bracu.ac.bd'),
    ('abc@bracu.ac.bd','ilikeoranges12','https://www.bracu.ac.bd'),
    ('mny@bracu.ac.bd','ilikedogs12','https://www.bracu.ac.bd');

-- @block
SELECT email,pass,website FROM Passwords
ORDER BY email ASC;