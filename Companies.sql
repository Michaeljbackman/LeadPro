-- Company info eg. Address, size, name, industry, description, tenant 
-- Creating a table --
CREATE TABLE Companies (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    address_line_1 VARCHAR(500),
    address_line_2 VARCHAR(500),
    city VARCHAR(255),
    state VARCHAR(255),
    zip_code VARCHAR(255),
    industry VARCHAR(100),
    tenant_id INT REFERENCES Tenants(id) ON DELETE CASCADE,
    description TEXT 
)
