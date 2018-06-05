import os

dir_name = raw_input('Enter Dir Name: ')
parent_dir = raw_input('Enter Parent Dir: ')

mkdir = "hadoop fs -mkdir -p /data/" + parent_dir + "/" + dir_name
chown = "hadoop fs -chown -R hive:" + dir_name + " /data/" + parent_dir + "/" + dir_name
chmod = "hadoop fs -chmod -R 775 /data/" + parent_dir + "/" + dir_name

os.system(mkdir)
os.system(chown)
os.system(chmod)

# print "Created Dir and granted access to: " + dir_name

hadoop_ls = "hadoop fs -ls /data/" + parent_dir + " | " + "grep " + dir_name
list = os.system(hadoop_ls)
print list


