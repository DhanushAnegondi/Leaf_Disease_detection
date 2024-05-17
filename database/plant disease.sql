/*
SQLyog Community Edition- MySQL GUI v6.07
Host - 5.5.30 : Database - plant_disease
*********************************************************************
Server version : 5.5.30
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

create database if not exists `plant_disease`;

USE `plant_disease`;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

/*Table structure for table `diseases` */

DROP TABLE IF EXISTS `diseases`;

CREATE TABLE `diseases` (
  `Dis_Name` varchar(60) DEFAULT NULL,
  `Remedies` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `diseases` */

insert  into `diseases`(`Dis_Name`,`Remedies`) values ('Apple_Black_rot','	Burn or Bury them'),('Corn_commonrust','	Spray fungicide on Crop'),('Grape_Leaf_blight','	Apply Dormant Spray'),('Apple___healthy','	Your Crop is Healthy'),('Corn_healthy','	Your Crop is Healthy'),('Grape___healthy','	Your Crop is Healthy');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
