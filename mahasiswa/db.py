import psycopg2 as mc
class DBConnection:
    def __init__(self):
        self.name = 'umc'
        self.port = 5432
        self.user = 'maulana'
        self.password = '123'
        self.host = 'localhost'
        self.conn = None
        self.cursor = None
        self.result = None
        self.connected = False
        self.affected = 0
        self.connect()
        
    @property
    def connection_status(self):
        return self.connected

    @property
    def info(self):
        if(self.connected==True):
            self.cursor.execute('SELECT version();')
            # fetch result
            record = self.cursor.fetchone()
            a='PostgreSQL version = {}'.format(record)
            return a + "\n" + "Server is running on " + self.host + ' using port ' + str(self.port)
        else:
            return "Server is offline."

    
    def connect(self):
        try:           
            self.conn = mc.connect(host = self.host,
                                    port = self.port,
                                    database = self.name,
                                    user = self.user,
                                    password = self.password)

            self.connected = True
            self.cursor=self.conn.cursor()
        except mc.Error as e:
            self.connected = False
        return self.conn

    def disconnect(self):
        if(self.connected==True):
            self.conn.close
        else:
            self.conn = None

    def findOne(self, sql):
        self.connect()
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        a = self.cursor.rowcount
        if(a>0):
            self.result = res
        else:
            self.result = None
        return self.result

    def findAll(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        return self.result

    def insert(self, sql):
        self.connect()  
        self.cursor.execute(sql)
        self.conn.commit()
        self.affected = self.cursor.rowcount        
        return self.affected

    def update(self, sql, val):
        self.connect()  
        self.cursor.execute(sql, val)
        self.conn.commit()
        self.affected = self.cursor.rowcount        
        return self.affected

    def delete(self, sql):
        self.connect()  
        self.cursor.execute(sql)
        self.conn.commit()
        self.affected = self.cursor.rowcount        
        return self.affected


mydb = DBConnection()


"""#Menampilkan isi tabel mahasiswa
sql = "select * from mahasiswa limit 100"
hasil = mydb.findAll(sql)
print(hasil)"""


"""#Entry data ke mahasiswa
sql = "insert into mahasiswa(nim,nama,idfakultas,idprodi)values('4351','Hambali','1','2')"
hasil = mydb.insert(sql)
print(hasil)"""


"""#Cari data yang ada di tabel mahasiswa
nim = '4352'
sql = "select * from mahasiswa where nim = '"+nim+"'"
hasil = mydb.findOne(sql)
print(hasil)"""

"""#Ubah data yang ada di tabel mahasiswa
nim = '4352'
nama = 'Fachri'
idfk = '3'
idpr = '3'
val = (nama,idfk,idpr,nim)
sql = "UPDATE mahasiswa SET nama= %s, idfakultas= %s, idprodi= %s WHERE nim= %s"
hasil = mydb.update(sql, val)
print(hasil)"""

"""
#Hapus data yang ada di tabel mahasiswa berdasarkan nim
nim = '4352'
sql = "delete from mahasiswa where nim='"+nim+"'"
hasil = mydb.delete(sql)
print(hasil)"""