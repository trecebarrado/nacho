-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-04-2020 a las 16:19:34
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
  `genero` varchar(255) NOT NULL,
  `tapa` varchar(10) NOT NULL,
  `coleccion` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tabla_comics`
--

INSERT INTO `tabla_comics` (`Id`, `titulo`, `autor`, `editorial`, `paginas`, `genero`, `tapa`, `coleccion`) VALUES
(1, 'Wilson', 'Daniel Clowes', 'La Cúpula', 98, 'Alternativo', 'Blanda', 0),
(2, 'Stock de coque', 'Hergé', 'Juventud', 68, 'Europeo', 'Dura', 0),
(3, 'La broma asesina', 'Alan Moore', 'DC Comics', 48, 'Superhéroes', 'Blanda', 0),
(4, 'V de Vendetta', 'Alan Moore', 'DC Comics', 300, 'Ciencia ficción', 'Blanda', 0),
(5, 'Freak Brothers nº 1', 'Gilbert Shelton', 'La Cúpula', 64, 'Alternativo', 'Blanda', 0),
(11, 'Animal Man', 'Grant Morrison', 'Vértigo', 680, 'Superhéroes', 'Blanda', 0),
(12, 'El gato Fritz', 'Robert Crumb', 'Víbora Comix', 96, 'Alternativo', 'Blanda', 0),
(13, 'Madman nº 3', 'Mike Allred', 'Norma', 64, 'Alternativo', 'Blanda', 1),
(25, 'Ronin', 'Frank Miller', 'DC Comics', 340, 'Histórico', 'Blanda', 1),
(26, 'Contrato con Dios', 'Will Eisner', 'Norma', 180, 'Alternativo', 'Dura', 0),
(27, 'MAUS', 'Art Spiegelman', 'Random House', 295, 'Histórico', 'Dura', 0),
(28, 'Pyongyang', 'Guy Delisle', 'Astiberri', 184, 'Alternativo', 'Blanda', 0),
(29, 'Ghost World', 'Daniel Clowes', 'La Cúpula', 84, 'Alternativo', 'Blanda', 0),
(31, 'Clandestine', 'Alan Davis', 'Marvel', 288, 'Superhéroes', 'Blanda', 1),
(37, 'Watchmen', 'Alan Moore', 'DC Comics', 416, 'Superhéroes', 'Dura', 0),
(57, 'Bola ocho nº 1', 'Daniel Clowes', 'La Cúpula', 48, 'Alternativo', 'Blanda', 1),
(58, 'Pussey!', 'Daniel Clowes', 'La Cúpula', 58, 'Alternativo', 'Blanda', 0);

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
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
