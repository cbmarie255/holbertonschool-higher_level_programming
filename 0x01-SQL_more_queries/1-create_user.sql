-- Creates a MySQL server user who has al privileges, a password, and should not fail if the user exists.
-- User: user_0d_1; Password: user_0d_1_pwd;
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
