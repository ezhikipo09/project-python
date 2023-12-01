CREATE TABLE manager (
    manager_id INT PRIMARY KEY,
    name VARCHAR(255),
    phone_number VARCHAR(12)
);

insert into manager (manager_id , name, phone_number) values (1, 'Yehudi', '864-678-3584');
insert into manager (manager_id , name, phone_number) values (2, 'Jourdan', '204-931-2776');
insert into manager (manager_id , name, phone_number) values (3, 'Shayne', '998-355-0426');
insert into manager (manager_id , name, phone_number) values (4, 'Hallie', '477-628-2488');
insert into manager (manager_id , name, phone_number) values (5, 'Fania', '284-419-3993');
insert into manager (manager_id , name, phone_number) values (6, 'Karena', '377-512-1820');
insert into manager (manager_id , name, phone_number) values (7, 'Annamaria', '132-871-0907');
insert into manager (manager_id , name, phone_number) values (8, 'Elyssa', '140-481-5344');
insert into manager (manager_id , name, phone_number) values (9, 'Creigh', '359-517-1610');
insert into manager (manager_id , name, phone_number) values (10, 'Karlie', '299-655-9856');

CREATE TABLE restaurant (
    restaurant_id INT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    manager_id INT REFERENCES manager(manager_id)
);

insert into restaurant (restaurant_id , name, address, manager_id) values (1, 'Flavorsome Fusion', '4 Vidon Drive', 1);
insert into restaurant (restaurant_id , name, address, manager_id) values (2, 'Foodie''s Paradise', '87 Mockingbird Parkway', 2);
insert into restaurant (restaurant_id , name, address, manager_id) values (3, 'Culinary Delights', '200 Stone Corner Crossing', 3);
insert into restaurant (restaurant_id , name, address, manager_id) values (4, 'The Gourmet Grill', '5804 Di Loreto Crossing', 4);
insert into restaurant (restaurant_id , name, address, manager_id) values (5, 'Taste of Heaven', '3476 Stang Lane', 5);
insert into restaurant (restaurant_id , name, address, manager_id) values (6, 'Savory Bites', '46987 Londonderry Court', 6);
insert into restaurant (restaurant_id , name, address, manager_id) values (7, 'The Cozy Cafe', '1817 Hintze Center', 7);
insert into restaurant (restaurant_id , name, address, manager_id) values (8, 'Savory Bites', '5 Charing Cross Way', 8);
insert into restaurant (restaurant_id , name, address, manager_id) values (9, 'The Hungry Moose', '76781 Elgar Plaza', 9);
insert into restaurant (restaurant_id , name, address, manager_id) values (10, 'The Cozy Cafe', '8627 Hayes Circle', 10);

CREATE TABLE bartender (
    bartender_id INT PRIMARY KEY,
    name VARCHAR(255),
    phone_number VARCHAR(12),
    restaurant_id INT REFERENCES restaurant(restaurant_id)
);

insert into bartender (bartender_id, name, phone_number, restaurant_id) values (1, 'Huntley', '108-486-8331', 1);
insert into bartender (bartender_id, name, phone_number, restaurant_id) values (2, 'Clarice', '132-816-7137', 2);
insert into bartender (bartender_id, name, phone_number, restaurant_id) values (3, 'Stanford', '371-722-8819', 3);
insert into bartender (bartender_id, name, phone_number, restaurant_id) values (4, 'Suzy', '381-137-9613', 4);
insert into bartender (bartender_id, name, phone_number, restaurant_id) values (5, 'Corella', '634-440-6859', 5);
insert into bartender (bartender_id, name, phone_number, restaurant_id) values (6, 'Genovera', '347-232-3553', 6);
insert into bartender (bartender_id, name, phone_number, restaurant_id) values (7, 'Adorne', '696-578-6417', 7);
insert into bartender (bartender_id, name, phone_number, restaurant_id) values (8, 'Ransom', '231-707-9366', 8);
insert into bartender (bartender_id, name, phone_number, restaurant_id) values (9, 'Cornelius', '727-721-6174', 9);
insert into bartender (bartender_id, name, phone_number, restaurant_id) values (10, 'Liz', '400-122-1356', 10);

CREATE TABLE tables (
    table_id INT PRIMARY KEY,
    table_number INT,
    is_reserved BOOLEAN,
    restaurant_id INT REFERENCES restaurant(restaurant_id)
);

insert into tables (table_id, table_number, is_reserved, restaurant_id) values (1, 1, true, 1);
insert into tables (table_id, table_number, is_reserved, restaurant_id) values (2, 2, true, 2);
insert into tables (table_id, table_number, is_reserved, restaurant_id) values (3, 3, false, 3);
insert into tables (table_id, table_number, is_reserved, restaurant_id) values (4, 4, true, 4);
insert into tables (table_id, table_number, is_reserved, restaurant_id) values (5, 5, false, 5);
insert into tables (table_id, table_number, is_reserved, restaurant_id) values (6, 6, false, 6);
insert into tables (table_id, table_number, is_reserved, restaurant_id) values (7, 7, false, 7);
insert into tables (table_id, table_number, is_reserved, restaurant_id) values (8, 8, true, 8);
insert into tables (table_id, table_number, is_reserved, restaurant_id) values (9, 9, true, 9);
insert into tables (table_id, table_number, is_reserved, restaurant_id) values (10, 10, false, 10);

CREATE TABLE vip_rooms (
    room_id INT PRIMARY KEY,
    room_number INT,
    is_reserved BOOLEAN,
    restaurant_id INT REFERENCES restaurant(restaurant_id)
);

insert into vip_rooms (room_id, room_number, is_reserved, restaurant_id) values (1, 1, true, 1);
insert into vip_rooms (room_id, room_number, is_reserved, restaurant_id) values (2, 2, false, 2);
insert into vip_rooms (room_id, room_number, is_reserved, restaurant_id) values (3, 3, false, 3);
insert into vip_rooms (room_id, room_number, is_reserved, restaurant_id) values (4, 4, true, 4);
insert into vip_rooms (room_id, room_number, is_reserved, restaurant_id) values (5, 5, true, 5);
insert into vip_rooms (room_id, room_number, is_reserved, restaurant_id) values (6, 6, false, 6);
insert into vip_rooms (room_id, room_number, is_reserved, restaurant_id) values (7, 7, false, 7);
insert into vip_rooms (room_id, room_number, is_reserved, restaurant_id) values (8, 8, true, 8);
insert into vip_rooms (room_id, room_number, is_reserved, restaurant_id) values (9, 9, true, 9);
insert into vip_rooms (room_id, room_number, is_reserved, restaurant_id) values (10, 10, false, 10);

SELECT * FROM tables;
SELECT * FROM vip_rooms;