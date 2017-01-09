SELECT
 film_id,
 title
FROM
 film

EXCEPT

SELECT
  DISTINCT inventory.film_id,
  title
FROM
  inventory
INNER JOIN film ON film.film_id = inventory.film_id
ORDER BY title;
