--People
-- id, name, email, phone, tenant_id, company_id, created_at
CREATE TABLE Contacts (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(50),
    tenant_id INT REFERENCES Tenants(id) ON DELETE CASCADE,
    company_id INT REFERENCES Companies(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
