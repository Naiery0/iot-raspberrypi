CREATE DATABASE IF NOT EXISTS raspi;
USE raspi;

CREATE TABLE IF NOT EXISTS admin_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

INSERT INTO admin_user (username, password)
VALUES ('admin', 'admin');