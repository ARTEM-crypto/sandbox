-- DELETE FROM link
-- WHERE id = 10;

-- DELETE FROM link
-- USING link_tmp
-- WHERE link.id = link_tmp.id;

DELETE FROM link
RETURNING *;
