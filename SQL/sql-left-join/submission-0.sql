CREATE TABLE humans (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE pets (
    id INTEGER PRIMARY KEY,
    owner_id INTEGER REFERENCES humans(id),
    name TEXT
);

INSERT INTO humans (id, name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie'),
(4, 'David'),
(5, 'Eve');

INSERT INTO pets (id, owner_id, name) VALUES
(1, 1, 'Whiskers'),
(2, 2, 'Buddy'),
(3, 5, 'Max'),
(4, 5, 'Bella');
-- Do not modify above this line. --

select h.name as human_name, p.name as pet_name from humans h left join pets p on h.id = p.owner_id order by human_name, pet_name;




