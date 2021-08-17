import pymysql.cursors

connection = pymysql.connect(host='3.35.70.166',
        user='user1',
        password='1234',
        db='aws',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Read a single record
        #sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        sql = 'SELECT count(*) FROM Apt_kr_0812'
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()


connection = pymysql.connect(host='3.35.70.166',
        user='user1',
        password='1234',
        db='aws',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Read a single record
        #sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        sql = 'SELECT * FROM Gagu_kr_0817 where year=2016'
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
