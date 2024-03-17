create table product(
    pid int primary key auto_increment,
    pname varchar(20),
    pprice float
);

create table ordercli(
    oid int primary key auto_increment,
    otime bigint, -- timestamp
    oconfirmed bool
);

create table product_ordercli(
    poid int primary key auto_increment,
    pid int,
    pnum int,
    oid int,
    foreign key (pid) references product(pid),
    foreign key (oid) references ordercli(oid)
);

create table sessions(
    sid int primary key auto_increment,
    oid int,
    status int,
    foreign key (oid)references ordercli(oid)
);

insert into product(pname, pprice) values
('product1', 1),
('product2', 2),
('product3', 3),
('product4', 4),
('product5', 5),
('product6', 6);

drop table if exists sessions;
drop table if exists product_ordercli;
drop table if exists ordercli;
drop table if exists product;
