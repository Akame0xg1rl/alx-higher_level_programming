-- Script to create the table first_table in the current database if it doesn't already exist

-- Create the table only if it doesn't already exist
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);

