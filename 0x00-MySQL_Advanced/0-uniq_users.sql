-- SQL script that creates a table users
use holberton;
CREATE TABLE IF NOT EXISTS `users` (
    `id` INTEGER AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255),
    PRIMARY KEY (`id`)
);
