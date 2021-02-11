# Readme

## Use this SQL query:
### 1. CREATE DATABASE chatapp;
### 2. CREATE TABLE chats (id int NOT NULL AUTO_INCREMENT,sender varchar(10), receiver varchar(10), message varchar(500), time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id));
### 3. CREATE TABLE user (id int NOT NULL AUTO_INCREMENT,mobile varchar(10), pin int, created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id));