CREATE DEFINER=`root`@`localhost` PROCEDURE `getCust`()
BEGIN
	DECLARE done INT DEFAULT 0;
    DECLARE cname VARCHAR(50);
    DECLARE city VARCHAR(50);
    DECLARE country VARCHAR(50);
    DECLARE grd VARCHAR(50);
    DECLARE c1 CURSOR FOR SELECT CUST_NAME, WORKING_AREA, CUST_COUNTRY, GRADE
    from customer WHERE AGENT_CODE LIKE "A00%";
    DECLARE CONTINUE HANDLER for NOT FOUND SET done=1;
    CREATE table temptab (CUST_NAME varchar(50), WORKING_AREA varchar(50), CUST_COUNTRY varchar(50), GRADE varchar(30));
    OPEN c1;
    lbl: LOOP 
    
	fetch c1 into cname, city, country, grd;
        IF done=1 THEN LEAVE lbl;
        END IF;
			insert into temptab values(cname, city, country, grd);
    END LOOP lbl;
    
    select * from temptab;
    DROP TABLE IF exists temptab;
    close c1;
END