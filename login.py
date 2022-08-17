import pymysql

# connect database
db = pymysql.connect(host='localhost', port=3306, user='root', password='Alex@0809', database='stu', charset='utf8')

# get cur
cur = db.cursor()


def register():
    name = input("please insert you username:")
    pwd = input("password:")
    sql = "select * from user where username='%s'"%name
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return False
    try:
        sql = "insert into user (username,password) values (%s,%s)"
        cur.execute(sql, [name, pwd])
        db.commit()
        return True
    except:
        db.rollback()
        return False
def login():
    name = input("please insert you username:")
    pwd = input("password:")
    sql = "select * from user where username='%s' and password='%s'" %(name,pwd)
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return True

while True:
    print("""==========
             1.register  2.login
             ===========
             """)
    cmd = input("insert you order:")
    if cmd == '1':
        if register():
            print("register succeed")
        else:
            print("unsucceed")

    elif cmd == '2':
        if login():
            print("login succeed")
            break
        else:
            print("login un succeed")

    else:
        print("can not do it")

cur.close()
db.close()
