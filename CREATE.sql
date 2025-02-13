CREATE TABLE User (
id SERIAL PRIMARY KEY,
name VARCHAR(100) NOT NULL);

CREATE TABLE Word (
id SERIAL PRIMARY KEY,
name VARCHAR(100) NOT NULL)
User_id INTEGER REFERENCES Users(id);

CREATE TABLE Translate (
id SERIAL PRIMARY KEY,
title VARCHAR(100) NOT NULL,
year INTEGER);
Word_id INTEGER REFERENCES Word(id);