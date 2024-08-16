import sqlalchemy
from sqlalchemy import create_engine, text

def create_tables():
    commands = (
        """
        CREATE TABLE Tenants (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            billing_type VARCHAR(50)
        )
        """,
        """
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
        """,
        """
        CREATE TABLE Contacts (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255),
            phone VARCHAR(50),
            company_id INT REFERENCES Companies(id),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE Emails (
            id INT PRIMARY KEY,
            contact_id INT REFERENCES Contacts(id),
            subject VARCHAR(255),
            body TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            sent_at TIMESTAMP
        )
        """
    )

    # Connect to the leadpro database
    engine = create_engine('postgresql://LeadPro:generateleads@localhost:5432/leadpro')

    with engine.connect() as connection:
        for command in commands:
            connection.execute(text(command))
        connection.commit()

def create_database():
    engine = create_engine('postgresql://LeadPro:generateleads@localhost:5432/postgres')

    # Check if database exists and create if it doesn't
    with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as connection:
        result = connection.execute(text("SELECT 1 FROM pg_database WHERE datname='leadpro'"))
        if result.fetchone() is None:
            connection.execute(text("CREATE DATABASE leadpro"))
            print("Database 'leadpro' created.")
        else:
            print("Database 'leadpro' already exists.")
        
if __name__ == '__main__':
    create_database()
    create_tables()