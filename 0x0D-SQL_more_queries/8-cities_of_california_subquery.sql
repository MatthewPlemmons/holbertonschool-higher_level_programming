--  List all the cities of CA found in database.
SELECT id, name FROM hbtn_0d_usa.cities
WHERE state_id = (
      SELECT id FROM states WHERE name = 'California'
);
