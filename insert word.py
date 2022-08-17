import re

import pymysql

f = open('words.txt')
# connect database
db = pymysql.connect(host='localhost', port=3306, user='root', password='Alex@0809', database='dict', charset='utf8')

# get cur
cur = db.cursor()
sql = "insert into words(word,mean) values(%s,%s)"

for line in f:
    tup = re.findall(r"(\S+)\s+(.*)", line)[0]
    try:
        cur.execute(sql, tup)
        db.commit()
    except:
        db.rollback()

f.close()
cur.close()
db.close()
