\c ai0377
drop database if exists mortfors_fv;
create database mortfors_fv;

  /* Felix är en horkattunge */
drop table if exists Resenär;
drop table if exists Chaufför;
drop table if exists Tur;

\c mortfors_fv;

create table Resenär
  (PersonID   int,
  namn        varchar(30),
  Epost       varchar(30),
  Telefon     int,
  primary key(PersonID));

create table Chaufför
  (personnummer int,
  namn          varchar(30),
  Adress        varchar(30),
  hemtelefon    int,
  primary key(personnummer));

create table Tur
  (ReseID       int,
  personnummer  int,
  datum         int,
  Avång         int,
  Ankomst       int,
  Kostnad       int,
  Platser       int,
  från          varchar(30),
  till          varchar(30),
  primary key(reseID),
  foreign key(personnummer) references Chaufför(personnummer));

create table Bokning
(reseID int,
PersonID  int,
Bokadplats int,
primary key(ReseID, PersonID),
foreign key(ReseID) references Tur(ReseID),
foreign key(PersonID) references Resenär(PersonID));

create table Platser
(Land varchar(30),
Stad varchar (30),
Hållplats varchar(30),
primary key(Hållplats));
