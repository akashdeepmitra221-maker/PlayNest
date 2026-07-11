-- ---------------------------------------------------------------------------
-- Run this file in MySQL Workbench (or `mysql -u root -p < schema.sql`)
-- to set up the database used by the Flask app.
-- ---------------------------------------------------------------------------

CREATE DATABASE IF NOT EXISTS auth_app_db;
USE auth_app_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,   -- stores a hashed password, never plain text
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
