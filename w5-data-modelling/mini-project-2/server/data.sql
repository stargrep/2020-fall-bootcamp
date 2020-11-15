CREATE TABLE IF NOT EXISTS client_rates (
    id INT PRIMARY KEY,
    client_id TEXT,
    rate REAL
);

INSERT INTO client_rates
VALUES
    (1, 'Client1', 0.1),
    (2, 'Client2', 0.12),
    (3, 'Client3', 0.2),
    (4, 'Client4', 0.15)