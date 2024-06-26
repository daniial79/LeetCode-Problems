SELECT
    customer_number
FROM (
    SELECT
        customer_number,
        COUNT(order_number) AS order_quantity
    FROM Orders
    GROUP BY customer_number
    ORDER BY order_quantity DESC
) AS T
LIMIT 1;