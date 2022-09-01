CREATE DEFINER=`root`@`localhost` PROCEDURE `addTwoNumber`(num1 int, num2 int, out res int)
BEGIN
	set res = num1 + num2;
END