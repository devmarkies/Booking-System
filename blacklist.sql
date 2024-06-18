-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 24, 2023 at 11:44 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27


SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blacklist`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `id` int(11) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `username` varchar(25) DEFAULT NULL,
  `password` varchar(300) DEFAULT NULL,
  `access` varchar(50) DEFAULT NULL,
  `active` varchar(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`id`, `email`, `username`, `password`, `access`, `active`, `created_at`, `updated_at`) VALUES
(1, 'zhie@caz.com', 'admin', 'md5$NwyxdqHIIqAeB5Ki$1cb62af7ea75f50882327596a8dc0037', 'developer', '1', '2023-01-24 09:05:01', '2023-01-24 09:05:01');

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
  
--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('d41b719479c9');

-- --------------------------------------------------------

--
-- Table structure for table `booked`
--

CREATE TABLE `booked` (
  `id` int(11) NOT NULL,
  `name` varchar(500) DEFAULT NULL,
  `service` varchar(500) DEFAULT NULL,
  `contact_no` varchar(300) DEFAULT NULL,
  `booked_date` varchar(300) DEFAULT NULL,
  `is_confirm` varchar(300) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `contents`
--

CREATE TABLE `contents` (
  `id` int(11) NOT NULL,
  `name` varchar(500) DEFAULT NULL,
  `types` varchar(500) DEFAULT NULL,
  `content` varchar(300) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contents`
--

INSERT INTO `contents` (`id`, `name`, `types`, `content`, `created_at`, `updated_at`) VALUES
(1, 'Web Title', 'website', 'BlackList', '2023-01-24 09:05:01', '2023-01-24 09:05:01'),
(2, 'Web Icon', 'website', 'none', '2023-01-24 09:05:01', '2023-01-24 09:05:01'),
(3, 'Home Greeting', 'home', 'Hello! we are', '2023-01-24 09:05:01', '2023-01-24 09:05:01'),
(4, 'Home Ownwer', 'home', 'Blacklist Productions', '2023-01-24 09:05:01', '2023-01-24 09:05:01'),
(5, 'Home Position', 'home', 'Photography Catering Team', '2023-01-24 09:05:01', '2023-01-24 09:05:01'),
(6, 'Home Image', 'home', 'bitoy.jpg', '2023-01-24 09:05:01', '2023-01-24 09:05:01'),
(7, 'About Description', 'about', 'We in Blacklist Productions work very hard and passionately with our work\n\nWe strive to give you the best on what you look and image in your photos!, We desire to work with you now and give you the best experience we can provide!\n\nWORK WITH US NOW!', '2023-01-24 09:05:01', '2023-01-24 09:05:01'),
(8, 'About Image', 'about', 'logoofficial1.png', '2023-01-24 09:05:01', '2023-01-24 09:05:01');

-- --------------------------------------------------------

--
-- Table structure for table `pricing`
--

CREATE TABLE `pricing` (
  `id` int(11) NOT NULL,
  `service_id` varchar(500) DEFAULT NULL,
  `desc` varchar(500) DEFAULT NULL,
  `price` varchar(300) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `services`
--

CREATE TABLE `services` (
  `id` int(11) NOT NULL,
  `name` varchar(500) DEFAULT NULL,
  `desc` varchar(500) DEFAULT NULL,
  `image_p` varchar(300) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `pricing_id` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `services`
--

INSERT INTO `services` (`id`, `name`, `desc`, `image_p`, `created_at`, `updated_at`, `pricing_id`) VALUES
(1, 'PHOTOGRAPHY', 'Photography Workshops are a great way to pick up new skills and to fine-tune those we already have. They\'re also a great way to step out of our comfort zones and try something new.', 'photography.jpg', '2023-01-24 02:47:56', '2023-01-24 02:47:56', NULL),
(2, 'Workshop', 'Our team also offers photo workshops or photography training in various categories some listed below.\r\n-Fashion Photography Workshops\r\n-Food Photography Workshops\r\n-Portrait Photography Workshops\r\n-Street Photography Workshops', 'workshop.jpg', '2023-01-24 02:47:56', '2023-01-24 02:47:56', NULL),
(3, 'Photo Editing', 'Our Team also offers photo editing to bring your own home took or professionally taken photos to your full satisfaction.', 'videoediting.jpg', '2023-01-24 02:47:56', '2023-01-24 02:47:56', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `booked`
--
ALTER TABLE `booked`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `contents`
--
ALTER TABLE `contents`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pricing`
--
ALTER TABLE `pricing`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `services`
--
ALTER TABLE `services`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admins`
--
ALTER TABLE `admins`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `booked`
--
ALTER TABLE `booked`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `contents`
--
ALTER TABLE `contents`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `pricing`
--
ALTER TABLE `pricing`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `services`
--
ALTER TABLE `services`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
