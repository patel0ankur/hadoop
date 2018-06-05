import os

port = "xxxx"
hostname = os.uname()[1]
enter_db = raw_input('Enter DB Name: ')
enter_rolename = raw_input('Enter Role Name: ')

beeline = "beeline -u " + "\"jdbc:hive2://" + hostname + ":" + port + "/default;principal=hive/_HOST@ABBVIENET.COM\"" + " -e " + "\"create database " + enter_db + "\""
#print beeline
os.system(beeline)

grant = "beeline -u " + "\"jdbc:hive2://" + hostname + ":" + port + "/default;principal=hive/_HOST@ABBVIENET.COM\"" + " -e " + "\"GRANT ALL ON DATABASE " + enter_db + " TO ROLE " + enter_rolename + "\""
#print grant
os.system(grant)
print "created db " + enter_db
print "Granted access to db " + enter_db

