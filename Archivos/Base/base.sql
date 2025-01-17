-- MySQL Script generated by MySQL Workbench
-- mar 16 jul 2019 14:06:14 CDT
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
create database base;
USE base ;

-- -----------------------------------------------------
-- Table `mydb`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Usuario` (
  `idUsuario` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `contra` VARCHAR(45) NOT NULL,
  `tipo` VARCHAR(45) NOT NULL,
  `direccion` VARCHAR(45) NULL,
  `RFC` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idUsuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Proveedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Proveedor` (
  `idProveedor` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `RFC` VARCHAR(45) NOT NULL,
  `telefono` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idProveedor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Producto_inventario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Producto_inventario` (
  `idProducto_inventario` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `cantidad` INT(4) NOT NULL,
  `porcion` FLOAT NOT NULL,
  `descripcion` VARCHAR(45) NOT NULL,
  `fecha_elaboracion` DATE NOT NULL,
  `fecha_vencimiento` DATE NOT NULL,
  `idUsuario` INT NOT NULL,
  `idProveedor` INT NOT NULL,
  `precio` float NOT NULL,
  PRIMARY KEY (`idProducto_inventario`),
  INDEX (idUsuario), 
  foreign key(idUsuario) References Usuario(idUsuario),
  INDEX (idProveedor), foreign key (idProveedor) References Proveedor(idProveedor)
  )
  ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Producto_catalogo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Producto_catalogo` (
  idProducto_catalogo INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(45) NOT NULL,
  porcion FLOAT NOT NULL,
  descripcion VARCHAR(45) NOT NULL,
  idUsuario INT NOT NULL,
  idProveedor INT NOT NULL,
  precio VARCHAR(45) NOT NULL,
  PRIMARY KEY (idProducto_catalogo),
  INDEX (idUsuario), foreign key (idUsuario) references Usuario(idUsuario),
  INDEX (idProveedor), foreign key (idProveedor) references Proveedor(idProveedor)
  )
  
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Pedido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Pedido` (
  `idPedido` INT NOT NULL AUTO_INCREMENT,
  `idUsuario` INT NOT NULL,
  `total` FLOAT NOT NULL,
  PRIMARY KEY (`idPedido`, `Usuario_idUsuario`),
  INDEX (idUsuario), foreign key (idUsuario) references Usuario(idUsuario)) 
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`DetallePedido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`DetallePedido` (
  `idDetallePedido` INT NOT NULL AUTO_INCREMENT,
  `cantidad` VARCHAR(45) NOT NULL,
  `idPedido` INT NOT NULL,
  `idUsuario` INT NOT NULL,
  `idProducto_inventario` INT NOT NULL,
  PRIMARY KEY (`idDetallePedido`, `Pedido_idPedido`, `Pedido_Usuario_idUsuario`, `Producto_inventario_idProducto_inventario`),
  INDEX (idPedido), foreign key(idPedido) references Pedido (idPedido),
  INDEX (idUsuario), foreign key(idUsuario),references Usuario(idUsuario),
  INDEX (idProducto_inventario), foreign key (idProducto_inventario) references Producto_inventario(idProducto_invenatrio)
  )
  
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
