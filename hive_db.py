import os

#Enter Hive Server Details
port = "xxxx"
hostname = os.uname()[1]
enter_db = input('Enter DB Name: ')
enter_rolename = input('Enter Role Name: ')


#Create DBs using beeline
beeline = "beeline -u " + "\"jdbc:hive2://" + hostname + ":" + port + "/default;principal=hive/_HOST@ABBVIENET.COM\"" + " -e " + "\"create database " + enter_db + "\""
#print beeline
os.system(beeline)

#Grant All permission on DBs to Role 
grant = "beeline -u " + "\"jdbc:hive2://" + hostname + ":" + port + "/default;principal=hive/_HOST@ABBVIENET.COM\"" + " -e " + "\"GRANT ALL ON DATABASE " + enter_db + " TO ROLE " + enter_rolename + "\""
#print grant
os.system(grant)

#Print details
print "created db " + enter_db
print "Granted access to db " + enter_db

