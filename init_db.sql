create database maintenance_db;

use maintenance_db;

CREATE TABLE IF NOT EXISTS machines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(255) NOT NULL,
    last_maintenance DATE NOT NULL,
    frequency INT NOT NULL
);

INSERT INTO machines (name, type, last_maintenance, frequency) VALUES
('Compressor A1', 'Air Compressor', '2025-07-01', 30),
('Boiler B2', 'Steam Boiler', '2025-06-15', 60),
('Pump C3', 'Hydraulic Pump', '2025-07-10', 45);

select * from machines;