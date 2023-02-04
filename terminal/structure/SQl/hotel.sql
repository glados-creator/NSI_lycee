-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le :  jeu. 15 sep. 2022 à 13:49
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
-- Base de données :  `hotel`
--

-- --------------------------------------------------------

--
-- Structure de la table `chambre`
--

CREATE TABLE `chambre` (
  `idch` int(11) NOT NULL,
  `numch` int(11) NOT NULL,
  `prixch` int(11) NOT NULL,
  `idh` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `chambre`
--

INSERT INTO `chambre` (`idch`, `numch`, `prixch`, `idh`) VALUES
(1, 100, 50, 1),
(2, 100, 75, 4),
(3, 102, 40, 5),
(4, 103, 130, 3),
(5, 23, 45, 1),
(6, 200, 80, 6),
(7, 220, 80, 6);

-- --------------------------------------------------------

--
-- Structure de la table `client`
--

CREATE TABLE `client` (
  `idc` int(11) NOT NULL,
  `nomc` varchar(25) DEFAULT NULL,
  `prenomc` varchar(20) DEFAULT NULL,
  `num_c` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `client`
--

INSERT INTO `client` (`idc`, `nomc`, `prenomc`, `num_c`) VALUES
(1, 'hunt', 'victor', NULL),
(2, 'adam', 'martine', NULL),
(3, 'lois', 'anne', NULL);

-- --------------------------------------------------------

--
-- Structure de la table `hotel`
--

CREATE TABLE `hotel` (
  `idh` int(11) NOT NULL,
  `nomh` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `hotel`
--

INSERT INTO `hotel` (`idh`, `nomh`) VALUES
(1, 'Hotel du Nord'),
(2, 'Hotel Ibis'),
(3, 'Hotel de Paris'),
(4, 'Hotel du lac'),
(5, 'Hotel du Vieux'),
(6, 'Hotel de Lyon');

-- --------------------------------------------------------

--
-- Structure de la table `reservation`
--

CREATE TABLE `reservation` (
  `idresa` int(11) NOT NULL,
  `dateresa` date NOT NULL,
  `idch` int(11) DEFAULT NULL,
  `idc` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `reservation`
--

INSERT INTO `reservation` (`idresa`, `dateresa`, `idch`, `idc`) VALUES
(1, '0000-00-00', 3, 3),
(2, '0000-00-00', 4, 2),
(3, '0000-00-00', 2, 3),
(4, '0000-00-00', 1, 1),
(5, '0000-00-00', 5, 3),
(6, '0000-00-00', 5, 2);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `chambre`
--
ALTER TABLE `chambre`
  ADD PRIMARY KEY (`idch`),
  ADD KEY `idh` (`idh`);

--
-- Index pour la table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`idc`);

--
-- Index pour la table `hotel`
--
ALTER TABLE `hotel`
  ADD PRIMARY KEY (`idh`);

--
-- Index pour la table `reservation`
--
ALTER TABLE `reservation`
  ADD PRIMARY KEY (`idresa`),
  ADD KEY `idc` (`idc`),
  ADD KEY `idch` (`idch`);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `chambre`
--
ALTER TABLE `chambre`
  ADD CONSTRAINT `chambre_ibfk_1` FOREIGN KEY (`idh`) REFERENCES `hotel` (`idh`);

--
-- Contraintes pour la table `reservation`
--
ALTER TABLE `reservation`
  ADD CONSTRAINT `reservation_ibfk_1` FOREIGN KEY (`idc`) REFERENCES `client` (`idc`),
  ADD CONSTRAINT `reservation_ibfk_2` FOREIGN KEY (`idch`) REFERENCES `chambre` (`idch`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
