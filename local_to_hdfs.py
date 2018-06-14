import shutil
import os
from os import listdir
from os.path import isfile, join
import subprocess
import shlex

#Dirs details
SOURCE_DIR = "/home/moscftpprod/srcfile/"
BACKUP_DIR = "/mnt/disk_c/srcfile_bkp/"
HDFS_DIR = "/HDFS_DIR/"

#kinit for authentication
cmd = "kinit -kt datalake.keytab datalake/(hostname)"
subprocess.call(shlex.split(cmd))

#Filter .temp files 
cpfiles = [file for file in listdir(SOURCE_DIR) if isfile(join(SOURCE_DIR, file)) and ".temp" not in os.path.basename(
    file) and "DroppedOnTime" not in os.path.basename(file) and "OnTimeDeparture" not in os.path.basename(
    file) and "InboundDelivery" not in os.path.basename(file)]

#Copying file from source to backup and hdfs dirs	
for file in cpfiles:
    cmd = "hadoop fs -put -f " + SOURCE_DIR + file + " " + HDFS_DIR
    subprocess.call(shlex.split(cmd))
    shutil.move(SOURCE_DIR + file, BACKUP_DIR)
