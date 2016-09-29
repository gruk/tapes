# tapes
# MANUAL #

# Make sure you have sqlite3 installed 
# Make sure you have  pysqlite installed
# In the same direcetory as this script, create a database 'tapes.db' with the queries below:
# Following that run the script

# DATABASE QUERIES:

# sqlite3 tapes.db

# CREATE TABLE cases(
# ID int PRIMARY KEY,
# caseDesc string
# );
# CREATE TABLE locations(
# ID string PRIMARY KEY,
# cases_ID int,
# locationDesc string
# );

# INSERT INTO cases(
# ID, caseDesc)
# VALUES(
# 103928, 'BackupSet1');

# INSERT INTO cases(
# ID, caseDesc)
# VALUES(
# 103965, 'BackupSet2');

# INSERT INTO cases(
# ID, caseDesc)
# VALUES(
# 104030, 'BackupSet3');


# INSERT INTO locations(
# ID, cases_ID, locationDesc)
# VALUES(
# 'P0001', 103928, 'Portsmouth Plant Room Tape Library');

# INSERT INTO locations(
# ID, cases_ID, locationDesc)
# VALUES(
# 'V0332', 104030, 'Top Shelf PRPP Vault');

# INSERT INTO locations(
# ID, cases_ID, locationDesc)
# VALUES(
# 'V0342', 103965, 'Bottom Shelf PRPP Vault');
