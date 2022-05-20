-- Base de datos: `cuentabancaria`
--creacion de la tabla tbl_cuenta
CREATE  OR REPLACE TABLE `tbl_cuenta` (
  `id` smallint(3) UNSIGNED NOT NULL,
  `username` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `password` char(102) COLLATE utf8_unicode_ci NOT NULL,
  `fullname` varchar(50) COLLATE utf8_unicode_ci NOT NULL, 
  `nrocuenta` varchar (50) COLLATE utf8_unicode_ci NOT NULL, 
  `nrocedula` varchar (50) COLLATE utf8_unicode_ci NOT NULL, 
  `tipocuenta` varchar (50) COLLATE utf8_unicode_ci NOT NULL, 
  `saldocuenta` INT (50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Cuenta bancaria''s data.';
-- Insert de datos para la tabla `tbl_cuenta`
INSERT INTO `tbl_cuenta` (`id`, `username`, `password`, `fullname`, `nrocuenta`,`nrocedula`,`tipocuenta`,`saldocuenta`) VALUES
(2, 'GERMIS', 'pbkdf2:sha256:260000$bZk2FTw9lEDDeHCc$200b49dc30740f1a805219a88a3b44e5109341c2012ece01a1a4861b42be3698', 'German Echavarria Estrada' ,'1234','	1234569','Ahorros',1200000),
(3, 'JUAND', 'pbkdf2:sha256:260000$duKPDoSJPd7dq1xE$d10118756958b83cdc76e6ea26064c763f9c788026c32c1f630c96265a739902', 'Juan Carloz Ramirez', '1235','654321','Ahorros',900000  ),
(4, 'Marta', 'pbkdf2:sha256:260000$E6cuYM0mkTfQDNw4$7f4258e60d9f1c0d9274b209252815e981056215ead62a03508e57188aed798c', 'Marta lopez Perez', '1236','987123','Ahorros',2000000 );
-- creacion de clave primaria
ALTER TABLE `tbl_cuenta`
  ADD PRIMARY KEY (`id`);
-- AUTO_INCREMENT de la tabla `tbl_cuenta`
ALTER TABLE `tbl_cuenta`
  MODIFY `id` smallint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;