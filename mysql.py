import pymysql

# connect database
db = pymysql.connect(host='localhost', port=3306, user='root', password='Alex@0809', database='stu', charset='utf8')

# get cur
cur = db.cursor()

# implement
sql = "insert into class values(7,'Emma',17,'w',76.5,'2019-8-8');"

cur.execute(sql)
db.commit()
cur.close()
db.close()
