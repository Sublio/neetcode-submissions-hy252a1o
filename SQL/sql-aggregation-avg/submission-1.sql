CREATE TABLE scores (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    score INTEGER,
    subject TEXT
);

INSERT INTO scores (score, subject) VALUES
(72, 'math'),
(88, 'math'),
(68, 'math'),
(80, 'science'),
(90, 'science'),
(60, 'science'),
(90, 'history'),
(85, 'history'),
(100, 'history');
-- Do not modify above this line. --
select  round(avg(score)) as average_math_score from scores where subject = 'math';




