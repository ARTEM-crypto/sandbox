-- SELECT
--   customer_id,
--   SUM (amount)
-- FROM
--   payment
-- GROUP BY
--   customer_id
-- HAVING
--   SUM (amount) > 200;
--
SELECT
  store_id,
  COUNT (customer_id) custmer_count
FROM
  customer
GROUP BY
  store_id
HAVING
  COUNT (customer_id) > 300;
