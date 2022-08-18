USE COMPANY;
select  essn , count(*) as 'NumberOfProject' from WORKS_ON where essn in (select mgr_ssn from DEPARTMENT where Dnumber in (select Dnum from PROJECT where Pname = "ProductY")) group by essn;
