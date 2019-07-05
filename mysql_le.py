import pymysql

db = pymysql.connect(host="172.17.0.2", user="root", password="abc123456", database="zjh", charset='utf8' )

cursor = db.cursor()

sql = """CREATE TABLE sina (
         url  CHAR(100) NOT NULL,
         title CHAR(100)
          )"""

# sql = """CREATE TABLE wangyi (
#          url  CHAR(100) NOT NULL,
#          title CHAR(100)
#           )"""

# sql = """CREATE TABLE hupu (
#          url  CHAR(100) NOT NULL,
#          title CHAR(100)
#           )"""


sql = """CREATE TABLE souhu (
         url  CHAR(100) NOT NULL,
         title CHAR(100)
          )"""

cursor.execute(sql)

db.close()