CREATE DEFINER=`root`@`localhost` PROCEDURE `SelectCustomers`(IN City varchar(35))
BEGIN
SELECT CUST_NAME FROM customer WHERE WORKING_AREA = City;
END
