CREATE TABLE IF NOT EXISTS client_rates (
    id INT PRIMARY KEY,
    client_id TEXT,
    rate REAL
);

INSERT INTO client_rates
VALUES
    (1, 'client1', 0.1),
    (2, 'client2', 0.12),
    (3, 'client3', 0.2),
    (4, 'client4', 0.15)