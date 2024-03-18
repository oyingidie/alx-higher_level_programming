-- convert database in my MySQL server to UTF8
-- also convert a table in the database & a field in the table
USE hbtn_0c_0
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
