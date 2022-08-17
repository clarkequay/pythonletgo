import pymysql

# connect database
db = pymysql.connect(host='localhost', port=3306, user='root', password='Alex@0809', database='stu', charset='utf8')

# get cur
cur = db.cursor()

# with open('image.jpg','rb') as f:
#     data=f.read()
# try:
#     sql = "update class set image=%s where name='Abby';"
#     cur.execute(sql,[data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)
sql="select image from class where name='Abby'"
cur.execute(sql)
data=cur.fetchone()
with open('cat.jpg','wb') as f:
    f.write(data[0])
cur.close()
db.close()