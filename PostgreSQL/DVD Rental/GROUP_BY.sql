-- SELECT
--   customer_id,
--   SUM(amount)
-- FROM
--   payment
-- GROUP BY
--   customer_id
-- ORDER BY
--   SUM(amount) ASC;

SELECT
  staff_id,
  COUNT(payment_id) payments_count
FROM
  payment
GROUP BY
  staff_id
ORDER BY
  payments_count;
