CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);
-- Do not modify above this line. --
create index email_idx on users using hash (email);




-- Do not modify below this line. --
SELECT indexdef
FROM pg_indexes
WHERE tablename = 'users';
