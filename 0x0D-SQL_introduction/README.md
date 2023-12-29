# 0x0D. SQL - Introduction

## What’s a Database
A database is a structured collection of data, typically organized for efficient retrieval and management.

## What’s a Relational Database
A relational database is a type of database that stores and manages data in a structured manner using tables with rows and columns. It allows you to define relationships between data elements.

## What does SQL stand for
SQL stands for Structured Query Language. It is a standard programming language for managing and querying relational databases.

## What’s MySQL
MySQL is an open-source relational database management system (RDBMS) that uses SQL. It's known for its reliability, speed, and ease of use.

# Working with MySQL

## How to Create a Database in MySQL
To create a database in MySQL, you can use the `CREATE DATABASE` statement. For example:
```sql
CREATE DATABASE mydatabase;
```

## What Does DDL and DML Stand For
- DDL: Data Definition Language. It includes commands to define, modify, and remove database structures, such as tables and indexes.
- DML: Data Manipulation Language. It includes commands to manipulate data within the database, like inserting, updating, and deleting records.

## How to CREATE or ALTER a Table
To create a table, you can use the `CREATE TABLE` statement. For example:
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE
);
```
To alter a table, use the `ALTER TABLE` statement.

## How to SELECT Data from a Table
To retrieve data from a table, you use the `SELECT` statement. For example:
```sql
SELECT * FROM users;
```

## How to INSERT, UPDATE, or DELETE Data
- To insert data, use `INSERT INTO`.
- To update data, use `UPDATE`.
- To delete data, use `DELETE FROM`.

## What Are Subqueries
Subqueries are queries nested within other queries. They can be used to retrieve data for complex conditions or calculations. For example:
```sql
SELECT name FROM employees WHERE department_id = (SELECT id FROM departments WHERE name = 'HR');
```

## How to Use MySQL Functions
MySQL provides a wide range of built-in functions for tasks like string manipulation, math operations, and date handling. Example:
```sql
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM employees;
```

# Additional Resources

- [MySQL Documentation](https://dev.mysql.com/doc/)

## Author
* **AZZA MOHAMED** [AZZA](https://github.com/medazza)- ALX-Africa SE Student cohort 17