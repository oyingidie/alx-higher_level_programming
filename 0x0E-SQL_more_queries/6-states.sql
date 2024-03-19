-- create a new database 'hbtn_0d_usa' with table 'states' on MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT NOT NULL, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
