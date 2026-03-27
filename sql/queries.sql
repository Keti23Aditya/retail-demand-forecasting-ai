-- Total sales by product
SELECT Product, SUM(Sales) AS total_sales
FROM sales_data
GROUP BY Product;

-- Promotion effect
SELECT Promotion, AVG(Sales) AS avg_sales
FROM sales_data
GROUP BY Promotion;

-- Store performance
SELECT Store, SUM(Sales) AS total_sales
FROM sales_data
GROUP BY Store;