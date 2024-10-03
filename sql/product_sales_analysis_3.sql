"""
Table: Sales

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to Product table.
Each row of this table shows a sale on the product product_id in a certain year.
Note that the price is per unit.
 

Table: Product

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the product name of each product.
 

Write a solution to select the product id, year, quantity, and price for the first year of every product sold.

Return the resulting table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+
Output: 
+------------+------------+----------+-------+
| product_id | first_year | quantity | price |
+------------+------------+----------+-------+ 
| 100        | 2008       | 10       | 5000  |
| 200        | 2011       | 15       | 9000  |
+------------+------------+----------+-------+
"""

ALTER TABLE Sales
DROP FOREIGN KEY sales_ibfk_1;

DROP TABLE IF EXISTS Product;

CREATE TABLE Product(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255)
);


DROP TABLE IF EXISTS Sales;

CREATE TABLE Sales (
    sale_id INT,
    product_id INT,
    year INT,
    quantity INT,
    price INT,
    PRIMARY KEY (sale_id, year),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);


INSERT INTO Product (product_id, product_name) VALUES
(100, 'Nokia'),
(200, 'Apple'),
(300, 'Samsung');

INSERT INTO Sales (sale_id, product_id, year, quantity, price) VALUES
(1, 100, 2008, 10, 5000),
(2, 100, 2009, 12, 5000),
(7, 200, 2011, 15, 9000);


--Get table with product_id and its first_year
SELECT 
    product_id,
    MIN(year) AS first_year
FROM 
    Sales 
GROUP BY 
    product_id;


--Use first_year subquery to filter
SELECT
    product_id,
    year AS first_year,
    quantity,
    price
FROM
    Sales
WHERE (product_id, year) IN (
    SELECT 
        product_id,
        MIN(year)
    FROM 
        Sales 
    GROUP BY 
        product_id
);


--Use CTE and join for the same results
WITH FirstYearSales AS (
    SELECT 
        product_id,
        MIN(year) AS first_year
    FROM 
        Sales 
    GROUP BY
        product_id
)

SELECT 
    s.product_id,
    f.first_year,
    s.quantity,
    s.price
FROM 
    Sales s 
JOIN 
    FirstYearSales f 
ON
    s.product_id = f.product_id AND s.year = f.first_year;