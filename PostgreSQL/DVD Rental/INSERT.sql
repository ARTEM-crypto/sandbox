-- CREATE TABLE link (
--   ID SERIAL PRIMARY KEY,
--   url VARCHAR(255) NOT NULL,
--   name VARCHAR(255) NOT NULL,
--   description VARCHAR(225),
--   rel VARCHAR(50)
-- )

-- INSERT INTO link (url, name)
-- VALUES
--   ('http://www.postgresqltutorial.com',NULL);

-- INSERT INTO link (url, name)
-- VALUES
--  ('http://www.google.com','Google'),
--  ('http://www.yahoo.com','Yahoo'),
--  ('http://www.bing.com','Bing');

-- ALTER TABLE link ADD COLUMN last_update DATE;
-- ALTER TABLE link ALTER COLUMN last_update
-- SET DEFAULT CURRENT_DATE;

-- INSERT INTO link (url, name, last_update)
-- VALUES
--   ('http://www.facebook.com', 'Facebook', '2013-06-01')

-- INSERT INTO link (url, name, last_update)
-- VALUES
--   ('https://www.tumbur.com/', 'Tumbur', DEFAULT)

-- CREATE TABLE link_tmp (LIKE link);

-- INSERT INTO link_tmp
-- SELECT *
-- FROM link
-- WHERE
--   last_update IS NOT NULL;

INSERT INTO link (url, NAME, last_update)
VALUES
  ('http://www.vk.com','vk',DEFAULT),
  ('http://www.ok.com','ok',DEFAULT)
RETURNING id;
