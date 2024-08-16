--Email marketing content
-- id, contact_id, subject, body, created_at, sent_at
CREATE TABLE Emails (
    id INT PRIMARY KEY,
    contact_id INT REFERENCES Contacts(id),
    subject VARCHAR(255),
    body TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    sent_at TIMESTAMP
)