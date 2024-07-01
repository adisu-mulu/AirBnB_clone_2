--- creating user if not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hbnb_dev_pwd';
--- creating database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
--- granting all privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
--- granting select privileges
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
