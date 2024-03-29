create database mft;
-- table mft.person
create table mft.person(
    id int primary key auto_increment,
    name varchar(30),
    family varchar(30),
    grade varchar(30)
);
-- salam
-- table lesson
create table mft.lesson(
    id int primary key auto_increment,
    teacher_name varchar(40),
    name_lesson varchar(30),
    description varchar(100)
);
-- table entkhab dars
create choose_course(
    datetime_coure date ,
    person_id int FOREIGN KEY REFERENCES mft.person (id),
    lesson_id int FOREIGN KEY REFERENCES mft.lesson (id))
);