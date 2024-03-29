create database mft;

create table mft.person(
    id int primary key auto_increment,
    name varchar(30),
    family varchar(30),
    grade varchar(50)
);
create table mft.lesson(
    id int primary key auto_increment,
    name varchar(30),
    teacher varchar(30),
    description varchar(50)
);
