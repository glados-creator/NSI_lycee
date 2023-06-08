create table CLIENT (
Idclient int,
Cnom varchar(30),
Cprenom varchar(15),
Cusername char(10),
Cpassword char(32),
Cdateborn date,
Cadresse varchar(50),
Cprofession char(20),
Cpublic bool,
Cnumtelfixe varchar(15),
Cnumtelport varchar(15),
Cemail varchar(50),
primary key (Idclient));

create table Relation (
IdR int,
IdCA int,
IdCB int,
TagR text,
primary key (IdR),
foreign key(IdCA) references CLIENT(Idclient),
foreign key(IdCB) references CLIENT(Idclient)
); 