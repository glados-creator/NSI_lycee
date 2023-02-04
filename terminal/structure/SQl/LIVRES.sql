-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le :  jeu. 08 sep. 2022 à 14:46
-- Version du serveur :  10.4.11-MariaDB
-- Version de PHP :  7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `idkdemo_2`
--

-- --------------------------------------------------------

--
-- Structure de la table `LIVRES`
--

CREATE TABLE `livres` (
  `id` int(11) NOT NULL,
  `titre` char(30) COLLATE utf8_bin DEFAULT NULL,
  `auteur` char(15) COLLATE utf8_bin DEFAULT NULL,
  `ann_publi` int(11) DEFAULT NULL,
  `note` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Déchargement des données de la table `LIVRES`
--

INSERT INTO `LIVRES` (`id`, `titre`, `auteur`, `ann_publi`, `note`) VALUES
(1, '1984', 'Orwell', 1949, 10),
(2, 'Dune', 'Herbert', 1965, 8),
(3, 'Fondation', 'Asimov', 1951, 9),
(4, 'Le meilleur des mondes', 'Huxley', 1931, 7),
(5, 'Fahrenheit 451', 'Bradbury', 1953, 7),
(6, 'Ubik', 'K,Dick', 1969, 9),
(7, 'Chroniques martiennes', 'Bradbury', 1950, 8),
(8, 'La nuit des temps', 'Barjavel', 1968, 7),
(9, 'Blade Runner', 'K,Dick', 1968, 8),
(10, 'Les Robots', 'Asimov', 1950, 9),
(11, 'La Planète des singes', 'Boulle', 1963, 8),
(12, 'Ravage', 'Barjavel', 1943, 8),
(13, 'Le Maître du Haut Château', 'K,Dick', 1962, 8),
(14, 'Le monde des Ā', 'Van Vogt', 1945, 7),
(15, 'La Fin de l’éternité', 'Asimov', 1955, 8),
(16, 'De la Terre à la Lune', 'Verne', 1865, 10);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `LIVRES`
--
ALTER TABLE `LIVRES`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
