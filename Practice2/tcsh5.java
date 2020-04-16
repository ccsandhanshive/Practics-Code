create table employee(emp_id int,ename varchar(20),sal int);

insert into employee values(1,'abc',50000);
insert into employee values(2,'pqr',60000);
insert into employee values(3,'xyz',90000);


select *
from employee;

select ename,sal
from employee;



select ename,sal,sal+1000
from emp;

select ename,sal,(sal+1000)*12
from emp;

select * from emp;

select ename,comm
from emp;


select ename,comm,sal+comm
from emp;

//aliases
select ename "Name",
sal*12 "annual salary"
from emp;






///listner.ora
///tnsnames.ora

1.distinct clause comes after select
2.there can be only one occurence of distinct in select

//!= or ^= or <> --means not equal to

//concatination operator

select ename || '  work as ' || job as discription
from emp

//where col optr value--- syntax

select ename,deptno
from emp
where deptno = 20

//display info for all manager
select * 
from emp
where job = 'MANAGER'

//display enames and their dates of joining but it should display only those employees who joined after the yr 81 ----dates are format specific
select ename,hiredate
from emp
where hiredate > '12/31/1981'

/*display all emp who do not report to 7839
select ename,mgr
from emp
where mgr != 7839 

//priority of 



//list all eployees working as managers earning less than 2500 
select ename,sal,job
from emp
where sal <2500 and job = 'MANAGER'

//display all employees who work as managers or clerk
select ename,job
from emp
where job='MANAGER' or job='CLERK'

//display records of emp who join between yr 81 to 82
select ename,hiredate
from emp
where hiredate between '1/1/1981' and '12/31/1982'

select ename, sal
from emp
where in 

//like
select ename,job
from emp
where job like 'SA^_%' escape '^'

//list names and commision of those emp who are not eligible for comm
select ename, comm
from emp
where comm is null


//order by clouse used for arranging data in asc /desc
//3 ways by which u can use order by clause
//1.order by column name
//2.order by column alias
//3.order by column number----column no. in select statement
//u can order on multiple columns

functions
    1.bulit in 
    2.user define 


//display ename,length of ename of only those employees having length 5
select ename,length(ename)
from emp
where length(ename) = 5


select ename,sal
from emp
where length(sal) = 4


select ename,round((sysdate-hiredate)/365,0)
from emp



// TO_CHAR display date in following format :22nd of Dec
select to_char(hiredate,'ddth " of " mon')
from emp

//list all employeee joining in apr
select ename,hiredate
from emp
where to_char(hiredate,'mon') = 'apr'

//TO_CHAR with number
select to_char(sal,'$9999.99')
from emp

//TO_NUMBER
select to_number ('$12,333.93','$99,999.99')
from dual

//TO_DATE
select to_date('06111111','mm/dd/yy')
from dual


//nvl()
select ename,sal,comm,sal+nvl(comm,0) total_salary
from emp

//avg of all commision
select avg(nvl(comm,0)) avg
from emp

//print 'no commision' in place where comm has null value%%%%%%%%%%%
select comm,to_number(nvl(comm,0),'no commision')
from emp

//nvl2
//nullif
//it compare to expression which is pass as paramtere if it is equal it will return null else return 1st expression

//coalesce(null,null,not null)

conditional expression
-case
-decode


select ename,job,sal,
case job when 'MANAGER' then 1.10*sal
         when 'PRESIDENT' then 1.15*sal
         when 'CLARK' then 1.20*sal
         else sal
end restored_sal
from emp


select ename,job,sal,
case when 'MANAGER' and deptno=30 then 1.10*sal
     when 'CLARK' and deptno=20 then 1.15*sal
     else sal
end restored_sal
from emp



/*/select ename,job,sal,
//decode(job ,'MANAGER', 1.10*sal
         when 'PRESIDENT' then 1.15*sal
         when 'CLARK' then 1.20*sal
         else sal
end restored_sal
from emp*/


grouped functions
count() || count(*) || count(distinct column)
min()
avg()
sum()

group by clouse
select deptno,sum(sal)
from emp
group by deptno
order by deptno

//if a non aggrgate column comes with aggregate column then include non col in grp by clouse to form a query
//the grp by col not necessrily to be in select stm


select deptno,job,sum(sal)
from emp
group by deptno,job

agrregate fun cannot be use with where clouse

//having clouse used with group by clouse
select deptno,count(ename)
from emp
group by deptno
having count(ename)>5


//find out min sal earned by each job
select job,min(sal)
from emp
group by job

////////////////join///////////

//inner join with aliases and where 
select ename, d.deptno,dname
from emp e
inner join dept d
on (e.deptno=d.deptno)
where e.sal>2000

//outer join
select ename, d.deptno,dname
from emp e
left outer join dept d
on (e.deptno=d.deptno)
where e.sal>2000

//cross join
select ename, d.deptno,dname
from emp e
cross join dept d

//natural join ---no need of aliases it will identify the joining column
select ename,deptno,dname
from emp 
natural join dept

//natual join using 'using' keyword
select ename,deptno,dname
from emp 
join dept
using(deptno)

//self join
select e.ename employee, m.ename manager
from emp e
inner join emp m
on(e.mgr=m.empno)


/////////////////////////sub query solving////////////////////


//display the name of employee who has max salary
select ename
from emp
where sal = (select max(sal)
       from emp)

//display name n salary of emplyee who earn more than that of jone's salary
select ename, sal
from emp
where sal > (select sal
             from emp
             where ename='JONES')


//display max sal earned in each dept 
select deptno,max(sal)
from emp
group by deptno
having max(sal)>3000

//display dept wise max sal display only those dept who earns sal more than that of dept 10's salary
select deptno 
from emp
where sal > (select max(sal)
             from emp
             where deptno=20)
or
select deptno,max(sal)
from emp
group by deptno
having max(sal)>(select max(sal) from emp where deptno=20)


//display employee number, manager,deptno where mgr is either of emp 7369/7499 and who belongs to dept of employe 7369/7499
select empno,mgr, deptno
from emp
where mgr in(select mgr 
            from emp
            where empno in(7369,7499))
and deptno in(select deptno
            from emp
            where empno in(7369,7499)) 

select empno,mgr,deptno
from emp
where (mgr,deptno) in (select mgr,deptno from emp where empno in(7369,7499))



create table emp_copy1
as
select * from emp

select * from dept_copy
select * from dept_copy

create table dept_copy
as
select * from dept

insert into dept_copy values(45,'MARKETING','PUNE')
insert into dept_copy(deptno) values(50)


//insert new row in emp_copy. emp_cpoy should get records from emp table.In emp_copy ,manager's id ,name,sal data sholud go
insert into emp_copy(empno,ename,sal)
select empno,ename,sal
from emp
where job='MANAGER'

update dept_copy
set loc='CHINCHWAD'
where deptno=10


update dept_copy
set loc='CHINCHWAD'
where deptno=10

//display ename,sal and deptno of employees belonging to accounting
select ename,sal,e.deptno
from emp_copy e ,dept_copy d
where dname='ACCOUNTING' and e.deptno=d.deptno

//update salary of emp_copy,update salaries of emp belonging to research
update emp_copy
set sal=sal+sal*0.1
where deptno =(select deptno
               from dept_copy
               where dname='RESEARCH')

//create product table -p_id, pname ,pdesc, ord_date, qty,rate

create table product(p_id number(2,0), pname varchar(10),pdesc varchar(50), ord_date date, qty number(2,0),rate number(5,2))

//to view
select * from user_tables

//add new col to product table called price,store
alter table product add(price number(5,2),store varchar(20))

//modify column
alter table tblenm
modify ()

ddl -delete truncate drop
drop table table_nm
select * from product



//creating table with constraints

create table student_details(Rollno number(3) constraint st_rn_pk primary key,
                             Name varchar(20) constraint st_nm_nn not null,
                             City varchar(20) default 'Pune',
                             Marks number(3),
                             Invoice_No char(3) constraint st_in_nn unique,
                             constraint st_mr_chk check(Marks between 0 and 100))

create table certificate_details(Rollno number(3), 
                                 date_of_certificate date constraint cd_dc_nn not null,
                                 Course char(10) , 
                                 constraint cd_co_ck check(Course in('Oracle','Java','XML')),
                                 constraint cd_fk foreign key(Rollno) references student_details(Rollno))

//system constaints
select constaint_name,column_name
from user_cons_column
where table_name='EMP'


//view object



//create a view based on dept_copy table. Insert a new record in dept table through this view
create or replace view v
as select deptno,dname
   from dept_copy
select * from v

//modify above view which restrict access to dept 30. no user should perform dml thruogh this view on dept other than 30
create or replace view v
as select deptno,dname
   from dept_copy
   where deptno=30
   with check option

insert into v values(30,'abc')

create sequence s
start with 5
increment by 3
maxvalue 15
minvalue 1
cycle
cache 3
 
select s.nextval
from dual

//when u r invoking seq 1st time use nextval 
//nextval gives next value and currval gives current value
//minvalue sholud be less than start value

insert into emp_copy(empno)
            values(s.nextval)

// alter sequence alter all the values but not start value of sequence
//drop sequence sequence_name


begin
dbms_output.put_line('hello world');
end;

declare
  x number(2);
  y number(2);
begin
  x:=15;
  y:=20;
  dbms_output.put_line(x+y);
end;

declare
  v_no number(4);
  v_salary number(4);
  v_name varchar(25);
begin
  select empno,ename,sal
  into v_no,v_name,v_salary
  from emp
  where empno=7369;
  dbms_output.put_line(v_no || v_name || v_salary);
end;


//////////////////////cursor/////////////////////
///when u want to fetch multiple rows we use cursor
sql% is implicit cursor
sql%rowcount -- tell how many rows affected by most recent sql statement

sql%found --  wheather query process or not.returns true or false

sql%notfound -- return true if not found

sql%isopen -- always evaluates to false because pl/sql closes implicit cursor immediately after they are execited




//////

declare
v_sal number(4);
begin 
 v_sal:=&v_sal;
 if v_sal < 1000 then
  dbms_output.put_line('C grade');
 elsif v_sal >=1000 and v_sal < 1500 then
   dbms_output.put_line('B grade');
 else
   dbms_output.put_line('A grade');
 --end if;
 end if;
 end;


//////iterative loops/////
basic loop ----
syntax LOOP
         stm;
         ...
         EXIT [when condition];
       END LOOP;

//in this i++ will not work

while loop



 
 
 declare 
 z number(10):=10;
 
 begin
  while z > 1 loop
   dbms_output.put_line(z);
   z:=z-1;
  end loop;
end;

///for loop
--counter variable in for loop is declare and initiated to its lower boundary.
   not needed to declare in declarative section
--it is constant value we can not modify it
--it only incremented by 1
--its value is not available outside the loop
--we can have same variable in declarative section which has differnt scope
--to iterate loop in reverse use reverse key word


/// explicit cursor
use to fetch multilple rows at a time 
into clause will not present in defining a cursor

declare
  cursor emp_cursor is
     select .....

open cursor_name;

fetch cursor_nm into variable name; -----with every fetch only one row fetch 

close cursor_name;





declare
v_nm varchar2(9);
v_job varchar2(10);
cursor a is select ename,job
            from emp
            order by ename desc;
begin
  open a;
    loop 
      fetch a into v_nm, v_job;
      exit when a%notfound;
      dbms_output.put_line(v_nm || ' ' ||v_job);
    --exit when sql%notfound;
    end loop;
    close a;
 end;



//
declare
cursor a is select ename,job
            from emp;
recemp a%rowtype;
begin
  open a;
    loop 
      fetch a into recemp;
      exit when a%notfound;
      dbms_output.put_line(recemp.ename || ' ' ||recemp.job);
    --exit when sql%notfound;
    end loop;
    close a;
 end;


 declare
 cursor c is select *
             from emp;
 record c%rowtype;
 begin
  open c;
  loop
   fetch c into record;
  exit when c%rowcount=5;
  end loop;
     dbms_output.put_line(record.ename || '  ' || record.job);
 close c;
 end;

///predefine exception
declare
 x number(2):=5;
 y number(2):=0;
 z number(2);
 begin
   z:=x/y;
   exception
   when zero_divide then
     dbms_output.put_line('divide by zero not allowed');
 end;


//non predefine exception

//function for trapping exception
--SQLCODE -returns the error number 
--SQLERRM -returns the error msg

 declare
 x number(8);
 sal_update exception;
 begin
 select sal
 into x
 from emp
 where ename='SMITH';
 x:=x*3;
 if x>2000 then
   raise sal_update;
 end if;
exception
  when sal_update then
  dbms_output.put_line('can not update');
end;


//procedure
 
 create or replace procedure demo
 is 
 begin
   dbms_output.put_line('hello world');
 end;
--calling procedure by 2 ways
execute demo;

--OR

begin
demo;
end;



 create or replace procedure demo2(p_number number)
 is 
 v_nm emp.ename%type;
 v_sal emp.sal%type;
 begin
   select ename,sal
   into v_nm,v_sal
   from emp
   where empno=p_number;
   dbms_output.put_line('employee name : '||v_nm || ' sal: '|| v_sal);
 end;
 
execute demo2(7499);


///modes in procedures
IN mode --default mode --values are passed into subprograms ---its read only ---procedure_nm(p_id in datatype)
OUT mode --values are passed from procedure to calling enviroment---it has to be a varialble---cant assign default value and cannot initialize
IN OUT mode --it has to be initialzed variable---pass to procedure and same variable will pass to calling envt after proccesing

//:v ---bind variable

--write a procedure which accepts empno and returns annual sal through another parameter

create or replace procedure annual_sal(en in number,ann_sal out number)
is
s number(9);
begin
 select sal 
 into s
 from emp
 where empno=en;
 ann_sal:=s*12;
end;

declare
s number(9);
begin
annual_sal(7499,s);
dbms_output.put_line(s);
end;


--function
create or replace function f1
return varchar2 is
begin
 return 'hello';
end;
 
--execution
declare
v varchar2(5);
begin
v:=f1;
dbms_output.put_line(v);
end;
 
 
 select f1 || ename
 from emp
 /////
 create or replace function tax(tsal number)
 return number is
 taxx number(10);
 begin
 taxx:=tsal*0.5;
 return taxx;
 end;
 
 declare
 taxq number(10);
 begin
 taxq:=tax(2000);
 dbms_output.put_line(taxq);
 end;
 
 select ename,sal,tax(sal) tax
 from emp;



  ----package specification
  create or replace package mypack is
     procedure mainp1;
     function mainf1 return varchar2;
  end;
 
----package body
create or replace package body mypack is
  procedure mainp1 is
    begin 
      dbms_output.put_line('Hi in procedure');
    end;
  function mainf1 return varchar2 is
    begin
      return('hello we are in function');
    end;
end;
--calling procedure of package
execute mypack.mainp1;                    
--calling function of package
declare
v varchar(50);
begin
  v:=mypack.mainf1;
  dbms_output.put_line(v);
end;


//////
create or replace package overpack
is
procedure o1(var varchar2);
procedure o1(var number);
end;

create or replace package body overpack 
is
 procedure o1(var varchar2) is
 begin
   dbms_output.put_line('hello, '||var||'!!');
 end;
 procedure o1(var number) is
 v number(5);
 begin
   v:=sqrt(var);
   dbms_output.put_line(v);
 end;
end;

execute overpack.o1(16);
begin
 overpack.o1(25);
end;

---to delete the package
drop package package_nm; ------delete both specification and body
--------



create or replace trigger before_demo
before insert on emp_copy
begin
 dbms_output.put_line('hello '||user||'is the user.before insert trigger');
end;

insert into emp_copy(empno,ename) values(546,'svx');

select * from emp_copy

///create a empty copy of emp table by name emp_history
when row from emp gets deleted,that emp eno,name,dept,sal,gets inserted in emp_history

create or replace trigger abd
before delete on emp_copy
for each row
begin
 insert into emp_history(empno,ename,deptno,sal) 
              values(:old.empno,:old.ename,:old.deptno,:old.sal);
end;
create table emp_history as
select * from emp_copy 
where 1=2

create table Inspection_details(Product_number varchar(9) constraint pd_pn_nn not null constraint pd_pn_unq unique ,
                       lower_limit number(5) constraint pd_ll_ck check(lower_limit =to_char(lower_limit,'999.99')),
                       Higher_limit number(5),
                       constraint pd_ck check(Higher_limit > lower_limit ))