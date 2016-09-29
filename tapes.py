#!/usr/bin/env python
# James McKelvie's 3foot7 tape changing script
# Tells James what tapes go where on a Friday and let's him know what to tell Wrangling

# Importing Modules

import sqlite3

# Declaring Global Variables

week1 = 103928
week2 = 103965
week3 = 104030
new_set = 0
empty_location = ''
active_set = 0
conn = sqlite3.connect('tapes.db')

# Declaring functions

def main():
	print ""
	print ""
	print "**********************************************************"
	print "***           The 3Foot7 Tape Changing Guide           ***"
	print "***                       v.1.0.2                      ***"
	print "**********************************************************"
	print "By James McKelvie"
	print ""
	report()

def report():
	global active_set

	query = conn.execute(" SELECT cases.ID \
		FROM locations \
		JOIN cases ON locations.cases_ID = cases.ID \
		WHERE locations.ID = 'P0001';")

	for row in query:
		print ""
		print "%s is the active set" % row[0]
		active_set = row[0]
	if active_set == week1:
		confirm(report2(week2))
	elif active_set == week2:
		confirm(report2(week3))
	elif active_set == week3:
		confirm(report2(week1))
	else:
		"something is up!"
		conn.close()
		exit()

def report2(nextset):
	global new_set, empty_location
	query = conn.execute("SELECT cases.ID, locations.locationDesc, locations.ID\
		FROM locations \
		JOIN cases ON locations.cases_ID = cases.ID \
		WHERE locations.cases_ID = %r;" % nextset)
	for row in query:
		new_set = row[0]
		empty_location = row[2]
		print ""
		print "you need to collect case # %s from %s and swap it with %s" % (row[0],row[1],active_set)
	return new_set

def confirm(newset):
	print "Preparing to update Database..."
	print "Setting %i as the active set and moving %i to %s" % (newset, active_set, empty_location)
	confirm = raw_input("Is this OK? ")
	if confirm == 'y' or confirm == 'Y' or confirm == 'yes':
		print "Updating..."
		update()
	else:
		print "No changes made"
		print "Closing connections and exiting"
		conn.close()

def update():
	conn.execute("UPDATE locations\
		SET cases_ID = %i\
		WHERE ID = 'P0001';" % new_set)
	conn.execute("UPDATE locations\
		SET cases_ID = %i\
		WHERE ID = '%s';" % (active_set, empty_location))
	print "Database updated as follows:"
	query = conn.execute("SELECT cases.ID, cases.caseDesc, locations.ID, locations.locationDesc \
		FROM locations\
		JOIN cases ON locations.cases_ID = cases.ID;")
	for row in query:
		print row
	print ""
	print "Tell Wrangling:"
	print "Shelf: %s" % empty_location
	print "OUT: %i" % new_set
	print "IN: %i" % active_set
	print ""
	conn.commit()
	conn.close()

if __name__ == '__main__':
	main()




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
