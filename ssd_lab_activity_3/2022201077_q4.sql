USE COMPANY;
select d.Dname , d.Dnumber , count(*) as 'Number of location' from DEPT_LOCATIONS dp JOIN DEPARTMENT d on d.Dnumber = dp.Dnumber where dp.Dnumber in (select Dnumber from DEPARTMENT where Mgr_ssn in (select essn from DEPENDENT where sex = 'F'  group by essn having count(*) > 1)) group by dp.Dnumber;
