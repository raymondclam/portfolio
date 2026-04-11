-- This creates the structure
CREATE TABLE tech_portfolio (
    id INTEGER PRIMARY KEY,
    project_name TEXT,
    status TEXT
);

-- This adds your first real data
INSERT INTO tech_portfolio (project_name, status) 
VALUES ('Python File Organizer', 'Completed');

-- This shows us the result
SELECT * FROM tech_portfolio;