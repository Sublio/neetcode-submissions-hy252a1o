CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE posts (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    title TEXT,
    content TEXT
);

INSERT INTO users (id, name) VALUES
  (1, 'John Doe'),
  (2, 'Jane Doe'),
  (3, 'Jim Beam'),
  (4, 'John Smith');

INSERT INTO posts (id, user_id, title, content) VALUES
  (1, 1, 'My First Post', 'This is the content of my first post'),
  (2, 1, 'My Second Post', 'This is the content of my second post'),
  (3, 2, 'Janes Post', 'This is the content of my post. My name is Jane Doe.');
-- Do not modify above this line. --

select name from users u where not exists (
    select 1 from posts p where p.user_id = u.id
) order by name asc;




