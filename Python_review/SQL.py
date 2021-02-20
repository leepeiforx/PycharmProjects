import pymssql

serverName = '127.0.0.1'

userName = 'sa'
passWord = '011235'

conn = pymssql.connect(serverName, userName, passWord,'tempdb')
cursor = conn.cursor()

cursor.execute("""
    IF OBJECT_ID('persons', 'U') IS NOT NULL
        DROP TABLE persons
    CREATE TABLE persons (
        id INT NOT NULL,
        name VARCHAR(100),
        salesrep VARCHAR(100),
        PRIMARY KEY(id)
    )
""")
# 插入三条测试数据
cursor.executemany(
    "INSERT INTO persons VALUES (%d, %s, %s)",
    [(1, 'John Smith', 'John Doe'),
     (2, 'Jane Doe', 'Joe Dog'),
     (3, 'Mike T.', 'Sarah H.')])
# 如果连接时没有设置autocommit为True的话，必须主动调用commit() 来保存更改。
conn.commit()
# 查询记录
cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
# 获取一条记录
row = cursor.fetchone()
# 循环打印记录(这里只有一条，所以只打印出一条)
while row:
    print("ID=%d, Name=%s" % (row[0], row[1]))
    row = cursor.fetchone()
# 连接用完后记得关闭以释放资源
conn.close()
