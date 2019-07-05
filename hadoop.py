import os
import pyhdfs
import  hdfs

def main():
  cmd = "/usr/local/hadoop/bin/hdfs dfs -put  a.html /home/"
  os.system(cmd)
if __name__ == "__main__":
  main()