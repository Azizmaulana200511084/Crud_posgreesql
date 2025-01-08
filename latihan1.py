import psycopg2 as db

try:
    con = db.connect(
    host='localhost', 
    database="umc",
    port=5432,
    user="maulana",
    password="123"
    )
    cursor = con.cursor()
    sql = "select * from mahasiswa limit 100"
    cursor.execute(sql)
    record = cursor.fetchall()
    print("koneksi berhasil")
    
except:
    print("koneksi gagal.")