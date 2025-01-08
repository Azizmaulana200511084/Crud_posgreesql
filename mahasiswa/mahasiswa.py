from db import DBConnection as mydb
class Mahasiswa:
    def __init__(self):
        self.__idmhs= None
        self.__nim= None
        self.__nama= None
        self.__idfakultas= None
        self.__idprodi= None
        self.conn= None
        self.affected= None
        self.result= None
    @property
    def idmhs(self):
        return self.__idmhs
    
    @property
    def nim(self):
        return self.__nim

    @nim.setter
    def nim(self, value):
        self.__nim = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def idfakultas(self):
        return self.__idfakultas

    @idfakultas.setter
    def idfakultas(self, value):
        self.__idfakultas = value

    @property
    def idprodi(self):
        return self.__idprodi

    @idprodi.setter
    def idprodi(self, value):
        self.__idprodi = value

    def simpan(self):
        self.conn= mydb()
        val = (self.__nim,self.__nama,self.__idfakultas,self.__idprodi)
        sql = "INSERT INTO mahasiswa (nim,nama,idfakultas,idprodi) VALUES" + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nim,self.__nama,self.__idfakultas,self.__idprodi, id)
        sql = "UPDATE mahasiswa SET nim=%s nama=%s, idfakultas=%s, idprodi=%s WHERE idmhs=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNIM(self, nim):
        self.conn = mydb()
        val = (self.__nama,self.__idfakultas,self.__idprodi, nim)
        sql = "UPDATE mahasiswa SET nama=%s, idfakultas=%s, idprodi=%s WHERE nim=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM mahasiswa WHERE idmhs='"+ str(id) +"'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNIM(self, nim):
        self.conn = mydb()
        sql = "DELETE FROM mahasiswa WHERE nim='"+ str(nim) +"'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql = "SELECT * FROM mahasiswa WHERE idmhs='"+ str(id) +"'"
        self.result = self.conn.findOne(sql)
        self.__nim = self.result[1]
        self.__nama = self.result[2]
        self.__idfakultas = self.result[3]
        self.__idprodi = self.result[4]
        self.conn.disconnect
        return self.result

    def getByNIM(self, nim):
        a=str(nim)
        b=a.strip()
        self.conn = mydb()
        sql = "SELECT * FROM mahasiswa WHERE nim='"+ b +"'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nim = self.result[1]
            self.__nama = self.result[2]
            self.__idfakultas = str(self.result[3])
            self.__idprodi = str(self.result[4])
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nim = ''
            self.__nama = ''
            self.__idfakultas = ''
            self.__idprodi = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM mahasiswa"
        self.result = self.conn.findAll(sql)
        return self.result

mhs = Mahasiswa()

# Read
'''result = mhs.getAllData()
print(result)'''

# Create
'''mhs.nim = '2657'
mhs.nama = 'Robin'
mhs.idfakultas = 3
mhs.idprodi = 7
hasil = mhs.simpan()
print(hasil)'''

# Search
'''nim = '2657'
hasil = mhs.getByNIM(nim)
print(hasil)'''

# Update
'''nim = '2657'
mhs.nama = 'Labirin'
mhs.idfakultas = 8
mhs.idprodi = 3
hasil = mhs.updateByNIM(nim)
print(hasil)'''

# Delete
'''nim = '2657'
hasil = mhs.deleteByNIM(nim)
print(hasil)'''