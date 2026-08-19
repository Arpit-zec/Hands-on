SELECT 
    CASE
        WHEN get_salary = n THEN salary 
        ELSE NULL
    END AS getNthHighestSalary
FROM (
    SELECT 
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS get_salary
    FROM Employee 
    ) nthsalary where get_salary = n 
    LIMIT 1
