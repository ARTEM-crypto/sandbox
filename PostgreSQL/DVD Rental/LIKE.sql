-- ~~   is equivalent to LIKE
-- ~~*  is equivalent to ILIKE
-- !~~  is equivalent to NOT LIKE
-- !~~* is equivalent to NOT ILIKE

SELECT
  first_name,
  last_name
FROM
  customer
WHERE
  first_name LIKE 'Jen%';
-- 'foo'   LIKE 'foo'   -- true
-- 'foo'   LIKE 'f%'    -- true
-- 'foo'   LIKE '_o_'   -- true
-- 'bar'   LIKE 'b_'    -- false
-- 'hello' LIKE '%ll%'  -- true
-- 'hello' LIKE '_ell%' -- true

/* PostgreSQL provides the ILIKE operator that acts like the LIKE operator.
   In addition, the ILIKE operator matches value case-insensitively */
