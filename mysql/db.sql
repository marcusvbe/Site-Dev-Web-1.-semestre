CREATE DATABASE IF NOT EXISTS desafio4;

USE desafio4;

CREATE TABLE IF NOT EXISTS contatos (
    email VARCHAR(60), 
    assunto VARCHAR(60), 
    descricao VARCHAR(255));

INSERT INTO contatos (email, assunto, descricao) VALUES
    ('testedocker@example.com', 'Docker compose', 'Implementado');