-- Create a database called CSR
CREATE DATABASE CSR;

-- Use the newly created CSR database
USE CSR;

-- Create the Profile table
CREATE TABLE Profile (
	emailAddress varchar(255),
	radius int,
	watchList varchar(255),
	PRIMARY KEY (emailAddress)
);

-- Create the User table
CREATE TABLE User (
	firstName TEXT NOT NULL,
	lastName TEXT NOT NULL,
	authority_registrationCode varChar(255),
	resident_registrationCode varChar(255),
	emailAddress varChar(255),
	password varChar(255) NOT NULL,
	PRIMARY KEY (emailAddress)
);

-- Create the ServiceRequest table
CREATE TABLE ServiceRequest (
	requestNumber varChar(255),
	creationDate DATE NOT NULL,
	completionDate DATE NOT NULL,
	requestType TEXT NOT NULL,
	status TEXT NOT NULL,
	priority INT,
	PRIMARY KEY (requestNumber)
);

-- Create the VehicleRequest table
CREATE TABLE VehicleRequest (
	requestNumber varChar(255),
	build TEXT,
	color TEXT,
	make TEXT,
	licensePlate varChar(255),
	PRIMARY KEY (requestNumber)
);

-- Create the Location table
CREATE TABLE Location (
	streetNumber INT,
	streetName varChar(255),
	zipCode INT,
	city TEXT,
	myState TEXT,
	id INT,
	PRIMARY KEY (streetNumber, streetName, zipCode)
);

-- Create the Alert table
CREATE TABLE Alert (
	requestNumber varChar(255),
	requestType TEXT NOT NULL,
	requestStatus TEXT NOT NULL,
	location INT NOT NULL,
	PRIMARY KEY (requestNumber)
);

-- Create the Notify table
CREATE TABLE Notify (
	emailAddress varChar(255),
	requestNumber varChar(255),
	PRIMARY KEY (emailAddress, requestNumber)
);

-- Create the Send table
CREATE TABLE Send (
	requestNumberA varChar(255),
	requestNumberB varChar(255),
	streetNumber INT,
	streetName varChar(255),
	zipCode INT,
	PRIMARY KEY (requestNumberA, requestNumberB)
);

-- Create the Provide table
CREATE TABLE Provide (
	emailAddress varChar(255),
	requestNumber varChar(255),
	streetNumber INT,
	streetName varChar(255),
	zipCode INT,
	PRIMARY KEY (emailAddress, requestNumber)
);

-- Create the Subscribe table
CREATE TABLE Subscribe (
	emailAddress varChar(255),
	requestNumber varChar(255),
	PRIMARY KEY (emailAddress, requestNumber)
);

-- Create the Submit table
CREATE TABLE Submit (
	emailAddress varChar(255),
	requestNumber varChar(255),
	PRIMARY KEY (emailAddress, requestNumber)
);

-- Create the Modify table
CREATE TABLE Modify (
	emailAddress varChar(255),
	requestNumber varChar(255),
	PRIMARY KEY (emailAddress, requestNumber)
);

-- Create the View table
CREATE TABLE View (
	emailAddress varChar(255),
	requestNumber varChar(255),
	PRIMARY KEY (emailAddress, requestNumber)
);

-- Create the Upvote table
CREATE TABLE Upvote (
	emailAddress varChar(255),
	requestNumber varChar(255),
	PRIMARY KEY (emailAddress, requestNumber)
);

/* Example of a row insertion
-- Insert the necessary data into the Profile table
INSERT INTO Profile (emailAddress, radius, watchList)
VALUES ('johndoe@gmail.com', 15, 'Lincoln Park');

-- Display everything in the table
SELECT *
FROM Profile;
*/

/*
-- Delete the data inside of the Profile table
TRUNCATE TABLE Profile;

-- Display everything in the table
SELECT *
FROM Profile;

-- Delete the Profile table
DROP TABLE Profile;

-- Delete the database
DROP DATABASE CSR;
*/