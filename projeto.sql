-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 19-Out-2021 às 00:36
-- Versão do servidor: 5.7.31
-- versão do PHP: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `projeto`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `dados`
--

DROP TABLE IF EXISTS `dados`;
CREATE TABLE IF NOT EXISTS `dados` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `cpf` varchar(15) NOT NULL,
  `pis` varchar(15) NOT NULL,
  `pais` varchar(100) NOT NULL,
  `estado` varchar(100) NOT NULL,
  `municipio` varchar(100) NOT NULL,
  `cep` varchar(13) NOT NULL,
  `logradouro` varchar(150) NOT NULL,
  `numero` varchar(12) NOT NULL,
  `complemento` varchar(150) NOT NULL,
  `email` varchar(100) NOT NULL,
  `senha` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `dados`
--

INSERT INTO `dados` (`id`, `nome`, `cpf`, `pis`, `pais`, `estado`, `municipio`, `cep`, `logradouro`, `numero`, `complemento`, `email`, `senha`) VALUES
(1, 'Edgar212', '17837866800', '12334566788', 'brrrrr', 'aaaaaa', 'aaaaaaa', '1231231', 'asdasdasdasdadsasd', '123', 'asdas11', 'edgar@hotmail.com', '123123123'),
(2, 'Augusto', '12313425611', '12389566723', 'ESTADOS UNIDOS', 'aaa', 'aaa', '1231231', 'aaaaaa', '1231', 'aaaa1', 'foa5064@hotmail.com', 'guga5064'),
(3, 'fabio', '7089122312', '7089122123', 'aaaaaa', 'aaaaaaaaaa', 'aaaaaaaaaa', '12312311', 'dasdasdas', '123123', 'aaaaa1', 'fabiorcost@hotmail.com', '123123123'),
(4, 'Olivia Oliveira Costa', '17837866800', '17867823411', 'Brasil', 'São paulo', 'Guarulhos', '7063150', 'Rua jesuino rabello', '369', '141b', 'otiene@hotmail.com', 'guga5064'),
(5, 'Fabio Costa', '08986322854', '12345678901', 'Brasil', 'São Paulo', 'São Paulo', '07063150', 'Rua Jesuíno Rabelo', '369', 'Apto. 141 Torre B', 'snow@hotmail.com', '123456'),
(6, 'test2', '01212312311', '01212312335', 'test1', 'test1', 'test1', '0123812', 'test1', '345', 'test1', 'testest1@hotmail.com', 'test1'),
(7, 'Leonardo Mateini da silva', '45789621466', '14578966511', 'Brasil', 'São Paulo', 'Guarulhos', '02328060', 'Rua bailao', '121', 'casa3', 'leonardo@hotmail.com', '123123123'),
(8, 'test2', '12312312311', '32132132122', 'test', 'test', 'test', '12312311', 'test', '123', 'test1', 'teest@hotmail.com', 'guga5064'),
(9, 'test4', '123123123123', '123123123123', 'test4', 'test4', 'test4', '12312122', 'test4', '12', 'test4', 'test4@hotmail.com', '123'),
(10, 'Caio vianna', '13423456711', '1234422311', 'Brasil ', 'Sao paulo', 'guarulhos', '07060150', 'Rua joão pannochia filho', '123', '', 'caio@hotmail.com', '123123123');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
