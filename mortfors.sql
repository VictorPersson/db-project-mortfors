\c ai0377
drop database if exists mortfors_fv;
create database mortfors_fv;

/* Tar bort DB tables */
drop table if exists Resenär;
drop table if exists Chaufför;
drop table if exists Tur;

\c mortfors_fv;

/* Tables */

create table Resenär
  (PersonID   int,
  Namn        varchar(30),
  Epost       varchar(30),
  Telefon     int,
  primary key(PersonID));

create table Chaufför
  (Personnummer   varchar(12),
  Namn            varchar(30),
  Adress          varchar(30),
  Hemtelefon      int,
  primary key(Personnummer));

create table Platser
  (Land       varchar(30),
  Stad        varchar (30),
  Hållplats   varchar(30),
  primary key(Hållplats));

create table Tur
  (ReseID       int,
  Personnummer  varchar(12),
  Datum         int,
  Avång         int,
  Ankomst       int,
  Kostnad       int,
  Platser       int,
  Från          varchar(30),
  Till          varchar(30),
  primary key(ReseID),
  foreign key(Personnummer) references Chaufför(Personnummer));

create table Bokning
  (ReseID     int,
  PersonID    int,
  Bokadplats  int,
  primary key(ReseID, PersonID),
  foreign key(ReseID) references Tur(ReseID),
  foreign key(PersonID) references Resenär(PersonID));

/* Insert satser */

insert into Resenär values
  (1, 'Victor', 'vp-96@hotmail.com', 070924058),
  (2, 'Felix', 'felix.m@gmail.com', 070666995),
  (3, 'Simon', 'simons.winter@brod.se', 070925158),
  (4, 'Josef', 'josef-stalin@marx.ussr', 011043222);

insert into Chaufför values
  (197202095123, 'Akilov', 'Kumla', 02123313),
  (196202124212, 'Pelle', 'Kattgränd 2', 07022512),
  (198401199182, 'Åse', 'Höganäsvägen 11', 07092633),
  (198909024123, 'Dipak', 'Likevägen 99', 070612534);

insert into Platser values
  ('Sverige', 'Malmö', 'Värnhem C'),
  ('Tyskland', 'Berlin', 'Münzstraße'),
  ('Sverige', 'Mörtfors', 'Stadshuset'),
  ('Frankrike', 'Paris', 'Rue dArcole');

insert into Tur values
  (001, 198401199182, 150518, 0930, 1100, 110, 162, 'Malmö', 'Berlin'),
  (002, 198401199182, 110618, 1330, 1530, 80, 82, 'Göteborg', 'Malmö'),
  (003, 198909024123, 020918, 0815, 1200, 50, 52, 'Mörtfors', 'Löddeköpinge'),
  (004, 198401199182, 090118, 2030, 2345, 100, 74, 'Berlin', 'Paris');

insert into Bokning values
  (001, 1, 2),
  (002, 2, 10),
  (003, 3, 6),
  (004, 4, 3);
