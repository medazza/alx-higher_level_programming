# 0x0E. SQL - More queries 

## How to Create a New MySQL User

To create a new MySQL user, you can use the following SQL command:
```sql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
```
Replace 'username' with the desired username and 'password' with the user's password. You can also specify a different host or IP address instead of 'localhost' if needed.

## How to Manage Privileges for a User to a Database or Table

MySQL uses the `GRANT` statement to manage user privileges. To grant privileges to a user, you can use the following syntax:
```sql
GRANT privilege_type ON database_name.table_name TO 'username'@'localhost';
```
Replace 'privilege_type' with the specific privilege you want to grant (e.g., SELECT, INSERT, UPDATE) and 'database_name.table_name' with the target database and table. Don't forget to replace 'username' and 'localhost' accordingly.

## What's a PRIMARY KEY

A PRIMARY KEY is a column or set of columns that uniquely identifies each row in a MySQL table. It enforces the uniqueness of values in the designated column(s) and ensures that they are not NULL. You can define a PRIMARY KEY during table creation, like this:
```sql
CREATE TABLE table_name (
    column_name INT PRIMARY KEY,
    ...
);
```

## What's a FOREIGN KEY

A FOREIGN KEY is a field in a MySQL table that is linked to the PRIMARY KEY of another table. It establishes a relationship between two tables, ensuring data integrity. You can define a FOREIGN KEY during table creation using the following syntax:
```sql
CREATE TABLE table_name (
    ...
    FOREIGN KEY (column_name) REFERENCES other_table(other_column),
    ...
);
```

## How to Use NOT NULL and UNIQUE Constraints

The NOT NULL constraint ensures that a column must have a value, preventing NULL values. The UNIQUE constraint enforces the uniqueness of values within a column. Here's how you can use them:
```sql
CREATE TABLE table_name (
    column1 INT NOT NULL,
    column2 VARCHAR(50) UNIQUE,
    ...
);
```

## How to Retrieve Data from Multiple Tables in One Request

To retrieve data from multiple tables in a single query, you can use SQL JOIN statements. For example, to retrieve data from 'table1' and 'table2' based on a common column 'id', you can use an INNER JOIN like this:
```sql
SELECT * FROM table1
INNER JOIN table2 ON table1.id = table2.id;
```

## What Are Subqueries

Subqueries are nested queries within a main query. They allow you to retrieve data from one query to use in another. For example, you can use a subquery to find the maximum value from a table and then use that result in your main query.

## What Are JOIN and UNION

JOIN is used to combine rows from two or more tables based on a related column between them. UNION, on the other hand, combines the result sets of two or more SELECT statements into a single result set.

## Author
* **AZZA MOHAMED** [AZZA](https://github.com/medazza)- ALX-Africa SE Student cohort 17