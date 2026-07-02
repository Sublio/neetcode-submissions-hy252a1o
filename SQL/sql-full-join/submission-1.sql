CREATE TABLE pokemon_types (
    id INTEGER PRIMARY KEY,
    name TEXT,
    weakness TEXT
);

CREATE TABLE pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type_id INTEGER
);

INSERT INTO pokemon_types (id, name, weakness) VALUES
(1, 'Fire', 'Water'),
(2, 'Water', 'Grass'),
(3, 'Grass', 'Fire'),
(4, 'Electric', 'Ground');

INSERT INTO pokemon (id, name, type_id) VALUES
(4, 'Charmander', 1),
(7, 'Squirtle', 2),
(3, 'Bulbasaur', 3),
(147, 'Dratini', 6),
(65, 'Alakazam', 7);
-- Do not modify above this line. --

select pt.name as type, p.name as pokemon, pt.weakness from pokemon_types pt full join pokemon p on pt.id=p.type_id order by type;