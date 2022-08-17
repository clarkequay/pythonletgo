import pymysql

# connect database
db = pymysql.connect(host='localhost', port=3306, user='root', password='Alex@0809', database='stu', charset='utf8')

# get cur
cur = db.cursor()

sql="select * from class where sex='w';"
cur.execute(sql)

#get result
#one_row=cur.fetchone()
#rint(one_row)

many_row=cur.fetchmany(2)
print(many_row)

cur.close()
db.close()