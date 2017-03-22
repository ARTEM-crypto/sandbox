-- CREATE TABLE account(
--   user_id SERIAL PRIMARY KEY,
--   username VARCHAR(50) UNIQUE NOT NULL,
--   password VARCHAR(50) NOT NULL,
--   email VARCHAR(350) UNIQUE NOT NULL,
--   created_on TIMESTAMP NOT NULL,
--   last_login TIMESTAMP
-- );

-- CREATE TABLE role(
--   role_id SERIAL PRIMARY KEY,
--   role_name VARCHAR(255) UNIQUE NOT NULL
-- );

CREATE TABLE accaunt_role(
  user_id INTEGER NOT NULL,
  role_id INTEGER NOT NULL,
  grant_date TIMESTAMP WITHOUT TIME ZONE,
  PRIMARY KEY (user_id, role_id),
  CONSTRAINT account_role_role_id_fkey FOREIGN KEY (role_id)
    REFERENCES role (role_id) MATCH SIMPLE
    ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT account_role_user_id_fkey FOREIGN KEY (user_id)
    REFERENCES account (user_id) MATCH SIMPLE
    ON UPDATE NO ACTION ON DELETE NO ACTION
);
