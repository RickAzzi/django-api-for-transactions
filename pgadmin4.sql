--CREATE INDEX idx_client_id ON clients_client(client_id);
--CREATE INDEX idx_transaction_date ON clients_transaction(transaction_date);

/* CREATE MATERIALIZED VIEW client_summary AS
SELECT
    c.client_id,
    COUNT(t.transaction_id) AS total_transactions,
    SUM(CASE WHEN t.transaction_type = 'buy' THEN t.amount ELSE 0 END) AS total_buy_amount,
    SUM(CASE WHEN t.transaction_type = 'sell' THEN t.amount ELSE 0 END) AS total_sell_amount
FROM clients_client c
LEFT JOIN clients_transaction t ON c.client_id = t.client_id::text  -- Casting the transaction's client_id to text
GROUP BY c.client_id; */

--REFRESH MATERIALIZED VIEW client_summary;

SELECT * FROM client_summary;






