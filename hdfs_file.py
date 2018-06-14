import os

#make dir and assign ownership and permission
dir_name = input('Enter Dir Name: ')
parent_dir = input('Enter Parent Dir: ')

mkdir = "hadoop fs -mkdir -p /data/" + parent_dir + "/" + dir_name
chown = "hadoop fs -chown -R hive:" + dir_name + " /data/" + parent_dir + "/" + dir_name
chmod = "hadoop fs -chmod -R 775 /data/" + parent_dir + "/" + dir_name

os.system(mkdir)
os.system(chown)
os.system(chmod)

# print "Created Dir and granted access to: " + dir_name

#List created dirs
hadoop_ls = "hadoop fs -ls /data/" + parent_dir + " | " + "grep " + dir_name
list = os.system(hadoop_ls)
print(list)


