-- SELECT
--   *
-- FROM
--  link;

-- UPDATE link
-- SET last_update = DEFAULT
-- WHERE
--   last_update IS NULL;

-- UPDATE link
-- SET rel = 'nofollow';

-- UPDATE link
-- SET description = name;

-- UPDATE link_tmp
-- SET rel = link.rel,
--     description = link.description,
--     last_update = link.last_update
-- FROM link
-- WHERE
--   link_tmp.id = link.id;

UPDATE link
SET description = 'Learn PostgreSQL fast and easy',
    rel = 'follow'
WHERE ID = 1
RETURNING
  id,
  description,
  rel;
