import psycopg2 as db
con = None
connected = None
cursor = None
def connect():
    global connected
    global con
    global cursor
    try:
        con = db.connect(
        host='localhost', 
        database="umc",
        port=5432,
        user="maulana",
        password="123"
        )
        cursor = con.cursor()
        connected = True
    except:
        connected = False
    return cursor
def disconnect():
    global connected
    global con
    global cursor
    if (connected == True):
        cursor.close()
        con.close()
    else:
        con = None
        connected = False
def Tampil(sql):
    a = connect()
    a.execute(sql)
    record= a.fetchall()
    return record
sql = "select * from mahasiswa"
a = Tampil(sql)
print("koneksi berhasil")
disconnect()