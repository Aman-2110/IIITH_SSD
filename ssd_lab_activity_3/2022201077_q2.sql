USE COMPANY;
select CONCAT(Fname, ' ', Minit, ' ', Lname) AS 'Full name' , ssn , Dno , NumberSub from EMPLOYEE e JOIN 
(select Super_ssn , count(*) as 'NumberSub' from EMPLOYEE group by Super_ssn) as tab on tab.Super_ssn = e.ssn order by NumberSub;