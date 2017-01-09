-- CREATE TABLE employees2 (
--   employee_id serial PRIMARY KEY,
--   employee_name VARCHAR (255) NOT NULL
-- );
--
-- CREATE TABLE keys (
--   employee_id INT PRIMARY KEY,
--   effective_date DATE NOT NULL,
--   FOREIGN KEY (employee_id) REFERENCES employees2 (employee_id)
-- );
--
-- CREATE TABLE hipos (
--   employee_id INT PRIMARY KEY,
--   effective_date DATE NOT NULL,
--   FOREIGN KEY (employee_id) REFERENCES employees2 (employee_id)
-- );
--
-- INSERT INTO employees2 (employee_name)
-- VALUES
--   ('Joyce Edwards'),
--   ('Diane Collins'),
--   ('Alice Stewart'),
--   ('Julie Sanchez'),
--   ('Heather Morris'),
--   ('Teresa Rogers'),
--   ('Doris Reed'),
--   ('Gloria Cook'),
--   ('Evelyn Morgan'),
--   ('Jean Bell');
--
-- INSERT INTO keys
-- VALUES
--   (1, '2000-02-01'),
--   (2, '2001-06-01'),
--   (5, '2002-01-01'),
--   (7, '2005-06-01');
--
-- INSERT INTO hipos
-- VALUES
--   (9, '2000-01-01'),
--   (2, '2002-06-01'),
--   (5, '2006-06-01'),
--   (10, '2005-06-01');

-- SELECT
--  employee_id
-- FROM
--  keys;

-- SELECT
--    employee_id
-- FROM hipos;

SELECT
  employee_id
FROM
  keys

INTERSECT

SELECT
  employee_id
FROM
  hipos

ORDER BY
  employee_id ASC;
