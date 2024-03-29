create database mft;
-- table mft.person
-- salam
create table mft.person(
    id int primary key auto_increment,
    name varchar(30),
    family varchar(30),
    grade varchar(30)
);
-- table lesson
create table mft.lesson(
    id int primary key auto_increment,
    teacher_name varchar(40),
    name_lesson varchar(30),
    description varchar(100)
);
-- table entkhab dars
create table  choose_course(
    datetime_course date ,
    person_id int );

