CREATE DEFINER=`root`@`localhost` PROCEDURE `getCustomerAndGrade`()
BEGIN
	select CUST_NAME, GRADE from customer where OPENING_AMT + RECEIVE_AMT > 10000;
END