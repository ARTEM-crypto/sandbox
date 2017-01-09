-- SELECT
--   first_name,
--   last_name,
--   email
-- FROM
--   customer;
--
-- SELECT DISTINCT ON (first_name),
--   last_name
-- FROM
--   customer
-- ORDER BY
--   first_name,
--   last_name;
--
-- CREATE TABLE t1 (
--   id serial NOT NULL PRIMARY KEY,
--   bcolor VARCHAR (25),
--   fcolor VARCHAR (25)
-- );
--
-- INSERT INTO t1 (bcolor, fcolor)
-- VALUES
--   ('red', 'red'),
--   ('red', 'red'),
--   ('red', NULL),
--   (NULL, 'red'),
--   ('red', 'green'),
--   ('red', 'blue'),
--   ('green', 'red'),
--   ('green', 'blue'),
--   ('green', 'green'),
--   ('blue', 'red'),
--   ('blue', 'green'),
--   ('blue', 'blue');
--
-- SELECT * FROM t1;
--
-- SELECT DISTINCT
--   bcolor
-- FROM
--   t1
-- ORDER BY
--   bcolor;
--
-- SELECT DISTINCT
--   bcolor,
--   fcolor
-- FROM
--   t1
-- ORDER BY
--   bcolor,
--   fcolor;

SELECT DISTINCT
  ON (bcolor) bcolor,
  fcolor
FROM
  t1
ORDER BY
  bcolor,
  fcolor;
