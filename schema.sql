CREATE DATABASE waxgroove_db CHARACTER SET utf8mb4;

CREATE TABLE store_product (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(120) NOT NULL,
    artist VARCHAR(120) NOT NULL,
    genre VARCHAR(20) NOT NULL,
    price DECIMAL(8,2) NOT NULL,
    in_stock BOOL NOT NULL,
    created_at DATETIME(6) NOT NULL
);
