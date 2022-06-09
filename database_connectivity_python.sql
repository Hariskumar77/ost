create database python_database;
use  python_database;
create table student_data(Name varchar(20),Regno int primary key not null,Age varchar(10),Gender varchar(10),Community varchar(5),Mobile int(10),Email varchar(20),CGPA varchar(10));
insert into student_data values("HARISKUMAR",1918111,"21","Male","BC",638245168,"hk@gmail.com","8.8");
insert into student_data values ("KAVINKUMAR",1911167,"22","Male","BC",987643333,"kk@gmail.com","9.0"),
("SIVAKUMAR",1918168,"21","Male","BC",638245168,"sk@gmail.com","8.5");
select*from student_data;
