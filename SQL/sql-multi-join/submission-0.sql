CREATE TABLE teams (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE players (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    team_id INTEGER REFERENCES teams(id)
);

CREATE TABLE contracts (
    id INTEGER PRIMARY KEY,
    player_id INTEGER REFERENCES players(id),
    salary INTEGER
);

INSERT INTO teams (id, name) VALUES
  (1, 'Lakers'),
  (2, 'Celtics'),
  (3, 'Bucks');

INSERT INTO players (id, name, team_id) VALUES
  (1, 'LeBron James', 1),
  (2, 'Anthony Davis', 1),
  (3, 'Kobe Bryant', 1),
  (4, 'Magic Johnson', 1),
  (5, 'Larry Bird', 2),
  (6, 'Kevin Garnett', 2),
  (7, 'Paul Pierce', 2),
  (8, 'Giannis Antetokounmpo', 3),
  (9, 'Khris Middleton', 3),
  (10, 'Jrue Holiday', 3);

INSERT INTO contracts (id, player_id, salary) VALUES
  (1, 1, 30000000),
  (2, 2, 25000000),
  (3, 3, 35000000),
  (4, 4, 15000000),
  (5, 5, 40000000),
  (6, 6, 19000000),
  (7, 7, 60000000),
  (8, 8, 27000000),
  (9, 9, 20000000),
  (10, 10, 25000000);
-- Do not modify above this line. --
select p.name as player_name, t.name as team_name, c.salary from players p join teams t on t.id = p.team_id
join contracts c on p.id=c.player_id order by c.salary desc;






