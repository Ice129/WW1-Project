-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 03, 2025 at 05:20 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ww1 project`
--

-- --------------------------------------------------------

--
-- Table structure for table `biographyspreadsheet`
--

CREATE TABLE `biographyspreadsheet` (
  `id` int(11) NOT NULL,
  `surname` varchar(80) DEFAULT NULL,
  `forename` varchar(80) DEFAULT NULL,
  `regiment` varchar(70) DEFAULT NULL,
  `service_number` varchar(40) DEFAULT NULL,
  `biography_attachment` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bradfordmemorials`
--

CREATE TABLE `bradfordmemorials` (
  `id` int(11) NOT NULL,
  `surname` varchar(80) DEFAULT NULL,
  `forename` varchar(80) DEFAULT NULL,
  `regiment` varchar(70) DEFAULT NULL,
  `unit` varchar(40) DEFAULT NULL,
  `memorial` varchar(150) DEFAULT NULL,
  `memorial_location` varchar(150) DEFAULT NULL,
  `memorial_info` varchar(150) DEFAULT NULL,
  `memorial_postcode` varchar(32) DEFAULT NULL,
  `district` varchar(150) DEFAULT NULL,
  `photo_available` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `buriedinbradford`
--

CREATE TABLE `buriedinbradford` (
  `id` int(11) NOT NULL,
  `surname` varchar(80) DEFAULT NULL,
  `forename` varchar(80) DEFAULT NULL,
  `age` int(3) DEFAULT NULL,
  `medals` longtext DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `rank` varchar(40) DEFAULT NULL,
  `unit` varchar(40) DEFAULT NULL,
  `cemetery` varchar(150) DEFAULT NULL,
  `grave_ref` varchar(40) DEFAULT NULL,
  `info` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `memorialnames`
--

CREATE TABLE `memorialnames` (
  `id` int(11) NOT NULL,
  `surname` varchar(80) DEFAULT NULL,
  `forename` varchar(80) DEFAULT NULL,
  `memorial` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `newspaperreferences2025`
--

CREATE TABLE `newspaperreferences2025` (
  `id` int(11) NOT NULL,
  `surname` varchar(80) DEFAULT NULL,
  `forename` varchar(80) DEFAULT NULL,
  `rank` varchar(40) DEFAULT NULL,
  `address` varchar(150) DEFAULT NULL,
  `regiment` varchar(70) DEFAULT NULL,
  `unit` varchar(40) DEFAULT NULL,
  `article_comment` varchar(300) DEFAULT NULL,
  `newspaper_name` varchar(150) DEFAULT NULL,
  `newspaper_date` date DEFAULT NULL,
  `page_col` varchar(10) DEFAULT NULL,
  `photo_incl` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `rollofhonour`
--

CREATE TABLE `rollofhonour` (
  `id` int(11) NOT NULL,
  `surname` varchar(80) DEFAULT NULL,
  `forename` varchar(80) DEFAULT NULL,
  `address` varchar(150) DEFAULT NULL,
  `electoral_ward` varchar(35) DEFAULT NULL,
  `town` varchar(35) DEFAULT NULL,
  `rank` varchar(40) DEFAULT NULL,
  `regiment` varchar(70) DEFAULT NULL,
  `unit` varchar(40) DEFAULT NULL,
  `company` varchar(40) DEFAULT NULL,
  `age` int(3) DEFAULT NULL,
  `service_no` varchar(40) DEFAULT NULL,
  `other_regiment` varchar(70) DEFAULT NULL,
  `other_service_no` varchar(40) DEFAULT NULL,
  `medals` longtext DEFAULT NULL,
  `enlisted_date` date DEFAULT NULL,
  `discharged_date` date DEFAULT NULL,
  `death_date` date DEFAULT NULL,
  `misc_info_nroh` varchar(200) DEFAULT NULL,
  `cemetery_memorial` varchar(150) DEFAULT NULL,
  `cemetery_memorial_ref` varchar(40) DEFAULT NULL,
  `cemetary_memorial_country` varchar(56) DEFAULT NULL,
  `additional_cwgc_info` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `biographyspreadsheet`
--
ALTER TABLE `biographyspreadsheet`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bradfordmemorials`
--
ALTER TABLE `bradfordmemorials`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `buriedinbradford`
--
ALTER TABLE `buriedinbradford`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `memorialnames`
--
ALTER TABLE `memorialnames`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newspaperreferences2025`
--
ALTER TABLE `newspaperreferences2025`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rollofhonour`
--
ALTER TABLE `rollofhonour`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `biographyspreadsheet`
--
ALTER TABLE `biographyspreadsheet`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `bradfordmemorials`
--
ALTER TABLE `bradfordmemorials`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `buriedinbradford`
--
ALTER TABLE `buriedinbradford`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `memorialnames`
--
ALTER TABLE `memorialnames`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `newspaperreferences2025`
--
ALTER TABLE `newspaperreferences2025`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `rollofhonour`
--
ALTER TABLE `rollofhonour`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
