CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary) VALUES
(1, 'Frank', 'Engineering', 120000),
(2, 'Bob', 'Marketing', 90000),
(3, 'Charlie', 'Engineering', 110000),
(4, 'David', 'Sales', 80000),
(5, 'Eve', 'Finance', 100000),
(6, 'Alice', 'Engineering', 130000);
-- Do not modify above this line. --


SELECT name,
       CASE
           WHEN department = 'Engineering' THEN 'yes'
           ELSE 'no'
       END AS is_engineering
FROM employees
ORDER BY name ASC





