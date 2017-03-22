-- SELECT
--   film_id,
--   title,
--   rental_rate
-- FROM
--   film
-- WHERE
--   rental_rate < (
--     SELECT
--       AVG(rental_rate)
--     FROM
--       film
--   );

-- SELECT
--   film_id,
--   title
-- FROM
--   film
-- WHERE film_id IN (
--   SELECT
--     inventory.film_id
--   FROM
--     rental
--   INNER JOIN inventory ON inventory.inventory_id = rental.inventory_id
--   WHERE return_date BETWEEN '2005-05-29' and '2005-05-30'
-- );

SELECT
  first_name,
  last_name
FROM
  customer
WHERE EXISTS (
  SELECT 1 FROM payment
  WHERE payment.customer_id = customer.customer_id
);
