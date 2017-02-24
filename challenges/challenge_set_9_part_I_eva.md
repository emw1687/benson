1. Which customers are from the UK?
```SQL
SELECT CustomerName
FROM Customers
WHERE Country = 'UK';
```
2. What is the name of the customer who has the most orders?
```SQL
SELECT CustomerName, COUNT(*) AS Order_Count
FROM Customers
JOIN Orders ON Customers.CustomerID = Orders.CustomerID
GROUP BY CustomerName
ORDER BY Order_Count DESC;
```

3. Which supplier has the highest average product price?
```SQL
SELECT SupplierName, AVG(Price) AS Mean_Price
FROM Products
JOIN Suppliers ON Products.SupplierID = Suppliers.SupplierID
GROUP BY SupplierName
ORDER BY Mean_Price DESC;
```

4. How many different countries are all the customers from? (Hint: consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)
```SQL
SELECT COUNT(DISTINCT Country)
FROM Customers;
```

5. What category appears in the most orders?
```SQL
SELECT CategoryName, COUNT(*) AS Product_Count
FROM Categories
JOIN Products on Categories.CategoryID = Products.CategoryID
JOIN OrderDetails on Products.ProductID = OrderDetails.ProductID
GROUP BY CategoryName
ORDER BY Product_Count DESC;
```

6. What was the total cost for each order?
```SQL
SELECT OrderID, SUM(Price*Quantity) AS Total_Cost
FROM Products
JOIN OrderDetails on Products.ProductID = OrderDetails.ProductID
GROUP BY OrderID;
```

7. Which employee made the most sales (by total price)?
```SQL
SELECT FirstName, LastName, SUM(Price*Quantity) AS Total_Cost
FROM Employees
JOIN Orders on Employees.EmployeeID = Orders.EmployeeID
JOIN OrderDetails on Orders.OrderID = OrderDetails.OrderID
JOIN Products on OrderDetails.ProductID = Products.ProductID
GROUP BY FirstName, LastName
ORDER BY Total_Cost DESC;
```

8. Which employees have BS degrees? (Hint: look at the LIKE operator.)
```SQL
SELECT FirstName, LastName
FROM Employees
WHERE Notes LIKE '%BS%';
```

9. Which supplier of three or more products has the highest average product price? (Hint: look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)
```SQL
SELECT SupplierName, AVG(Price) AS Avg_Price, COUNT(*) AS Num_Products
FROM Suppliers
JOIN Products ON Suppliers.SupplierID = Products.SupplierID
GROUP BY SupplierName
HAVING Num_Products >= 3
ORDER BY Avg_Price DESC;
```
