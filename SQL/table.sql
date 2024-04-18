#CREATE DATABASE sae61;
USE sae61;
CREATE TABLE Utilisateurs (id int AUTO_INCREMENT, Nom varchar(45) NOT NULL, Prenom varchar(45) NOT NULL, identifiant varchar(45) NOT NULL, mail varchar(45) NOT NULL,password varchar(45) NOT NULL, PRIMARY KEY (id));
