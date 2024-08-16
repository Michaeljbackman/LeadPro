--Company thats using lead pro
-- For the tenant we want an ID, name, created_at, billing_type, primary_contact_id
CREATE TABLE Tenants (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    billing_type VARCHAR(50),
    primary_contact_id INT REFERENCES Contacts(id)
)

