-- Create Database 
CREATE DATABASE stock_project;

-- Create a table for gold data
CREATE TABLE gold_history (
    Date DATE,
    Open DOUBLE PRECISION,
    High DOUBLE PRECISION,
    Low DOUBLE PRECISION,
    Close DOUBLE PRECISION,
    Volume INT,
    Dividends DOUBLE PRECISION,
    StockSplits DOUBLE PRECISION
);

-- check the column that we make before
SELECT * FROM gold_history;


-- create a table for GOLD_company_price
CREATE TABLE GOLD_stock_data(
    Date DATE,
    Open FLOAT,
    High FLOAT,
    Low FLOAT,
    Close FLOAT,
    Adj_Close FLOAT,
    Volume INT
);

-- check the column for GOLD_compnay_price
SELECT * from GOLD_stock_data;

-- create table for kgc data 
CREATE TABLE kgc_stock_data(
    Date DATE,
    Open FLOAT,
    High FLOAT,
    Low FLOAT,
    Close FLOAT,
    Adj_Close FLOAT,
    Volume INT
);

-- check kgc data
SELECT * from kgc_stock_data;


-- create table for nem data
CREATE TABLE nem_stock_data(
    Date DATE,
    Open FLOAT,
    High FLOAT,
    Low FLOAT,
    Close FLOAT,
    Adj_Close FLOAT,
    Volume INT
);

-- check nem data
SELECT * from nem_stock_data

-- create table for rgld data
CREATE TABLE rgld_stock_data(
    Date DATE,
    Open FLOAT,
    High FLOAT,
    Low FLOAT,
    Close FLOAT,
    Adj_Close FLOAT,
    Volume INT
);

-- check name data
SELECT * from rgld_stock_data


-- create table sand
CREATE TABLE sand_stock_data(
    Date DATE,
    Open FLOAT,
    High FLOAT,
    Low FLOAT,
    Close FLOAT,
    Adj_Close FLOAT,
    Volume INT
);

-- check sand data
SELECT * from sand_stock_data



