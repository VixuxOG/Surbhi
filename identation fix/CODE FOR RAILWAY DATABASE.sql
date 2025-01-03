CREATE DATABASE railwaydata;

USE railwaydata;

CREATE TABLE passenger (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    total INT,
    date DATE
);

CREATE TABLE train (
    train_name VARCHAR(100),
    boogie_type VARCHAR(20)
);

CREATE TABLE reservation (
    pnr_no INT,
    passenger_id INT,
    train_id INT,
    available_seats INT
);

drop database railwaydata
