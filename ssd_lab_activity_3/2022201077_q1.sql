USE COMPANY;
select CONCAT(Fname, ' ', Minit, ' ', Lname) AS 'Full name' , ssn, d.Dnumber, d.dname from EMPLOYEE e join DEPARTMENT d on e.dno = d.Dnumber where e.ssn in
(select Mgr_ssn from DEPARTMENT where Dnumber in (select dno from (select e.dno, sum(Hours) as hour from WORKS_ON join EMPLOYEE e on e.ssn = essn group by essn) o group by o.dno having min(hour) < 40)) ;