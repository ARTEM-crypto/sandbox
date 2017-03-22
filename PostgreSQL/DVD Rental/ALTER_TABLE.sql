-- ALTER TABLE table_name ADD COLUMN new_column_name TYPE;
-- ALTER TABLE table_name DROP COLUMN column_name;
-- ALTER TABLE table_name RENAME COLUMN column_name TO new_column_name;
-- ALTER TABLE table_name ALTER COLUMN [SET DEFAULT value | DROP DEFAULT]
-- ALTER TABLE table_name ALTER COLUMN [SET NOT NULL| DROP NOT NULL]
-- ALTER TABLE table_name ADD CHECK expression;
-- ALTER TABLE table_name ADD CONSTRAINT constraint_name constraint_definition
-- ALTER TABLE table_name RENAME TO new_table_name;

-- CREATE TABLE link1(
--   link_id SERIAL PRIMARY KEY,
--   title VARCHAR(512) NOT NULL,
--   url VARCHAR(1024) NOT NULL UNIQUE
-- );

-- ALTER TABLE link1 ADD COLUMN active BOOLEAN;
-- ALTER TABLE link1 DROP COLUMN active;
-- ALTER TABLE link1 RENAME COLUMN title TO link_title;
-- ALTER TABLE link1 ADD COLUMN target varchar(10);
-- ALTER TABLE link1 ALTER COLUMN target SET DEFAULT '_blank';
-- INSERT INTO link1(link_title,url)VALUES('PostgreSQL Tutorial','http://www.postgresqltutorial.com/');
-- ALTER TABLE link1 ADD CHECK (target IN ('_self', '_blank', '_parent', '_top'));

ALTER TABLE link1 RENAME TO link11;
