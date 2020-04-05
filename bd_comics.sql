-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-04-2020 a las 21:45:08
-- Versión del servidor: 10.1.13-MariaDB
-- Versión de PHP: 7.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_comics`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla_comics`
--

CREATE TABLE `tabla_comics` (
  `Id` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `autor` varchar(255) NOT NULL,
  `editorial` varchar(255) NOT NULL,
  `paginas` int(11) NOT NULL,
  `genero` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tabla_comics`
--

INSERT INTO `tabla_comics` (`Id`, `titulo`, `autor`, `editorial`, `paginas`, `genero`) VALUES
(1, 'Wilson', 'Daniel Clowes', 'La Cúpula', 96, 'Alternativo'),
(2, 'Stock de coque', 'Hergé', 'Juventud', 64, 'Europeo'),
(3, 'La broma asesina', 'Alan Moore', 'DC Comics', 48, 'Superhéroes'),
(4, 'V de Vendetta', 'Alan Moore', 'Vértigo', 304, 'Ciencia ficción'),
(5, 'Freak Brothers nº1', 'Gilbert Shelton', 'La Cúpula', 64, 'Alternativo'),
(9, '300', 'Frank Miller', 'Norma', 96, 'Histórico'),
(10, 'Agujero negro', 'Charles Burns', 'La Cúpula', 625, 'Alternativo'),
(11, 'Animal Man', 'Grant Morrison', 'Vértigo', 680, 'Superhéroes'),
(12, 'El gato Fritz', 'Robert Crumb', 'Víbora Comix', 96, 'Alternativo'),
(13, 'Madman nº1', 'Mike Allred', 'Norma', 64, 'Alternativo');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tabla_comics`
--
ALTER TABLE `tabla_comics`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tabla_comics`
--
ALTER TABLE `tabla_comics`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
