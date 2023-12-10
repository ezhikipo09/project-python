
CREATE TABLE tables (
    table_id INT PRIMARY KEY,
	reserved_by text,
    table_number INT ,
    is_reserved BOOLEAN
);

insert into tables (table_id, table_number, is_reserved) values (1, 1, false);
insert into tables (table_id, table_number, is_reserved) values (2, 2, false);
insert into tables (table_id, table_number, is_reserved) values (3, 3, false);
insert into tables (table_id, table_number, is_reserved) values (4, 4, false);
insert into tables (table_id, table_number, is_reserved) values (5, 5, false);
insert into tables (table_id, table_number, is_reserved) values (6, 6, false);
insert into tables (table_id, table_number, is_reserved) values (7, 7, false);
insert into tables (table_id, table_number, is_reserved) values (8, 8, false);
insert into tables (table_id, table_number, is_reserved) values (9, 9, false);
insert into tables (table_id, table_number, is_reserved) values (10, 10, false);

CREATE TABLE vip_rooms (
    room_id INT PRIMARY KEY,
	reserved_by text,
    room_number INT,
    is_reserved BOOLEAN
);

insert into vip_rooms (room_id, room_number, is_reserved) values (1, 1, false);
insert into vip_rooms (room_id, room_number, is_reserved) values (2, 2, false);
insert into vip_rooms (room_id, room_number, is_reserved) values (3, 3, false);
insert into vip_rooms (room_id, room_number, is_reserved) values (4, 4, false);
insert into vip_rooms (room_id, room_number, is_reserved) values (5, 5, false);
insert into vip_rooms (room_id, room_number, is_reserved) values (6, 6, false);
insert into vip_rooms (room_id, room_number, is_reserved) values (7, 7, false);
insert into vip_rooms (room_id, room_number, is_reserved) values (8, 8, false);
insert into vip_rooms (room_id, room_number, is_reserved) values (9, 9, false);
insert into vip_rooms (room_id, room_number, is_reserved) values (10, 10, false);

create table users(
	id serial primary key,
	user_id BIGINT,
	username text
);

CREATE TABLE IF NOT EXISTS reservations (
    id SERIAL PRIMARY KEY,
    user_id bigint,
    table_number bigint,
    vip_room_number bigint,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (table_number) REFERENCES tables (table_id),
    FOREIGN KEY (vip_room_number) REFERENCES vip_rooms (room_id)
);


drop table reservations
drop table vip_rooms
drop table tables
drop table users
SELECT * FROM users;
SELECT * FROM vip_rooms;
SELECT * FROM tables;
select * from reservations

