-- MariaDB dump 10.19  Distrib 10.4.25-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: motel
-- ------------------------------------------------------
-- Server version	10.4.25-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client` (
  `Idclient` int(11) NOT NULL,
  `Cnom` varchar(30) DEFAULT NULL,
  `Cprenom` varchar(15) DEFAULT NULL,
  `Cusername` char(10) DEFAULT NULL,
  `Cpassword` char(32) DEFAULT NULL,
  `Cdateborn` date DEFAULT NULL,
  `Cadresse` varchar(50) DEFAULT NULL,
  `Cprofession` char(20) DEFAULT NULL,
  `Cpublic` tinyint(1) DEFAULT NULL,
  `Cnumtelfixe` varchar(15) DEFAULT NULL,
  `Cnumtelport` varchar(15) DEFAULT NULL,
  `Cemail` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Idclient`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES (0,'admin','minda','admin','25f9e794323b453885f5181f1b624d0b','0000-00-00','iciville','ing.info.',0,'0','0','admin.mail@Gmail.com'),(2,'pavard','arthur','glados','21e6721ad880a463156672c0a9654732','2022-12-31','0','ing.',0,'0','0','');
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `relation`
--

DROP TABLE IF EXISTS `relation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `relation` (
  `IdR` int(11) NOT NULL,
  `IdCA` int(11) DEFAULT NULL,
  `IdCB` int(11) DEFAULT NULL,
  `TagR` text DEFAULT NULL,
  PRIMARY KEY (`IdR`),
  KEY `IdCA` (`IdCA`),
  KEY `IdCB` (`IdCB`),
  CONSTRAINT `relation_ibfk_1` FOREIGN KEY (`IdCA`) REFERENCES `client` (`Idclient`),
  CONSTRAINT `relation_ibfk_2` FOREIGN KEY (`IdCB`) REFERENCES `client` (`Idclient`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `relation`
--

LOCK TABLES `relation` WRITE;
/*!40000 ALTER TABLE `relation` DISABLE KEYS */;
INSERT INTO `relation` VALUES (1,0,2,'admin'),(2,2,0,' ;admin;friend');
/*!40000 ALTER TABLE `relation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-14  1:40:32
