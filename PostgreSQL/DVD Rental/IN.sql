-- SELECT
--   customer_id,
--   rental_id,
--   return_date
-- FROM
--   rental
-- WHERE
--   customer_id IN (1, 2)
-- ORDER BY
--   return_date DESC;

-- SELECT
--   customer_id,
--   rental_id,
--   return_date
-- FROM
--   rental
-- WHERE
--   customer_id NOT IN (1, 2)
-- ORDER BY
--   return_date DESC;

-- SELECT
--   customer_id
-- FROM
--   rental
-- WHERE
--   CAST (return_date AS DATE) = '2005-05-27'

SELECT
  first_name,
  last_name
FROM
  customer
WHERE
  customer_id IN (
    SELECT
      customer_id
    FROM
      rental
    WHERE
      CAST (rental_date AS DATE) = '2005-05-27'
  );
