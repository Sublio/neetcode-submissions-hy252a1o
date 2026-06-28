create table orders(
    id integer primary key,
    items text[],
    total_price integer
);






-- Do not modify below this line --
INSERT INTO orders (id, items, total_price) 
    VALUES (1, ARRAY['apple', 'banana'], 100),
          (2, ARRAY['orange', 'grape'], 200),
          (3, ARRAY['watermelon', 'pineapple'], 300);

SELECT * FROM orders;
