SELECT 
    employee_id,
    CASE 
        WHEN (SUBSTR(name, 1, 1) != "M") AND (MOD(employee_id, 2) = 1) THEN salary
        ELSE 0 
    END AS "bonus"
FROM employees
ORDER BY employee_id;