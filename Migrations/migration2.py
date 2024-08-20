from sqlalchemy import create_engine, text

def seed_data():
    engine = create_engine('postgresql://LeadPro:generateleads@localhost:5432/leadpro')

    commands = (
        """
        INSERT INTO Tenants (id, name, billing_type) 
        VALUES 
        (1, 'Default Tenant', 'monthly'),
        (2, 'Tech Startup', 'annual'),
        (3, 'Marketing Agency', 'quarterly')
        """,
        """
        INSERT INTO Companies (id, name, address_line_1, city, state, zip_code, industry, tenant_id, description) 
        VALUES 
        (1, 'Example Company', '123 Main St', 'Anytown', 'CA', '12345', 'Technology', 1, 'A leading tech company'),
        (2, 'Innovative Solutions', '456 Tech Ave', 'Silicon Valley', 'CA', '94000', 'Software', 2, 'Cutting-edge software solutions'),
        (3, 'Creative Marketing', '789 Ad Lane', 'New York', 'NY', '10001', 'Marketing', 3, 'Full-service marketing agency')
        """,
        """
        INSERT INTO Contacts (id, name, email, phone, company_id) 
        VALUES 
        (1, 'John Doe', 'john@example.com', '555-1234', 1),
        (2, 'Jane Smith', 'jane@innovative.com', '555-5678', 2),
        (3, 'Mike Johnson', 'mike@creative.com', '555-9012', 3),
        (4, 'Sarah Lee', 'sarah@example.com', '555-3456', 1),
        (5, 'Tom Brown', 'tom@innovative.com', '555-7890', 2)
        """,
        """
        INSERT INTO Emails (id, contact_id, subject, body, sent_at)
        VALUES 
        (1, 1, 'Meeting Request', 'Can we schedule a meeting next week?', '2023-05-01 10:00:00'),
        (2, 2, 'Project Update', 'Here's the latest update on our ongoing project.', '2023-05-02 14:30:00'),
        (3, 3, 'Campaign Proposal', 'Attached is our proposal for your new marketing campaign.', '2023-05-03 09:15:00')
        """
    )

    with engine.begin() as connection:
        for command in commands:
            try:
                connection.execute(text(command))
                print(f"Data inserted successfully.")
            except Exception as e:
                print(f"Error inserting data: {str(e)}")

if __name__ == '__main__':
    seed_data()