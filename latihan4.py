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

def Entry():
    global connected
    global con
    global cursor
    xnim = input("Masukan Nim: ")
    xnama = input("Masukan Nama Lengkap: ")
    xidfk = input("Masukan ID FAKULTAS (1 ... 5): ")
    xidpr = input("Masukan ID Prodi (1 ... 10): ")
    a = connect()
    sql = "insert into mahasiswa (nim, nama, idfakultas, idprodi) values ('"+xnim+"', '"+xnama+"', '"+xidfk+"', '"+xidpr+"')"
    a.execute(sql)
    con.commit()
    print("Entry is done.")
def Cari():
    global connected
    global con
    global cursor
    xnim = input("Masukan NIM yang di cari: ")
    a = connect()
    sql = "select * from mahasiswa where nim='"+xnim+"'"
    a.execute(sql)
    record = a.fetchall()
    print(record)
    print("Search is done.")
Cari()