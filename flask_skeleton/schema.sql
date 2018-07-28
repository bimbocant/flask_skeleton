/*code to create the database*/
DROP TABLE IF EXISTS demotable;

CREATE TABLE demotable(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  demofield TEXT NOT NULL
);
