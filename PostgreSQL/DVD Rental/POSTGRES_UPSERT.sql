-- CREATE TABLE customers (
--   customer_id SERIAL PRIMARY KEY,
--   name VARCHAR UNIQUE,
--   email VARCHAR NOT NULL,
--   active BOOL NOT NULL DEFAULT TRUE
-- );

-- INSERT INTO customers (name, email)
-- VALUES
--   ('IBM', 'contact@ibm.com'),
--   (
--     'Microsoft',
--     'contact@microsoft.com'
--   ),
--   (
--     'Intel',
--     'contact@intel.com'
--   );

-- EXPLAIN (analyze, format yaml) INSERT INTO customers (name, email)
-- VALUES
--   (
--     'Microsoft',
--     'hotline@microsoft.com'
--   )
-- ON CONFLICT ON CONSTRAINT customers_name_key
-- DO NOTHING;

-- EXPLAIN (analyze, format yaml) INSERT INTO customers (name, email)
-- VALUES
--  (
--    'Microsoft',
--    'hotline@microsoft.com'
--  )
-- ON CONFLICT (name)
-- DO NOTHING;

INSERT INTO customers (name, email)
VALUES
  (
    'Microsoft',
    'hotline@microsoft.com'
  )
ON CONFLICT (name)
DO
  UPDATE
    SET email = EXCLUDED.email || ';' || customers.email;
