CREATE TABLE users (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    username TEXT
);

INSERT INTO users (username) VALUES
  ('Alice'),
  ('Bob'),
  (NULL),
  ('Charlie'),
  (NULL);

-- Do not modify above this line. --
update users set username = 'anonymous' where username IS NULL;






-- Do not modify below this line. --
SELECT * FROM users;
