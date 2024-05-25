import psycopg2

conn = psycopg2.connect(dbname='Bunga Florist', user='postgres', password='saptamabar', host='localhost', port=5432)
cur = conn.cursor()

def createPegawai():
    query = f"SELECT * FROM pegawai order by id_pegawai desc"
    cur.execute(query)
    data = cur.fetchone()
    id_pegawai = data[0]+1
    Nama = input("Masukan nama : ")
    Alamat = input('Masukan Alamat : ')
    No_telp = input('Masukan no telp :')
    query = f"SELECT * FROM kecamatan"
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(i)
    Kecamatan = int(input("Masukan ID kecamatan : "))
    query = f"SELECT * FROM kelurahan"
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(i)
    kelurahan = int(input('Masukan id kelurahan : '))
    query = f"INSERT INTO pegawai(id_pegawai,nama_pegawai, Alamat, no_telp,kecamatan_id_kecamatan,kelurahan_id_kelurahan) VALUES({id_pegawai}, '{Nama}', '{Alamat}','{No_telp}',{Kecamatan},{kelurahan})"
    cur.execute(query, (id_pegawai,Nama, Alamat, No_telp,Kecamatan,kelurahan) )
    conn.commit()
    query = f"SELECT * FROM pegawai order by id_pegawai desc"
    cur.execute(query)
    data = cur.fetchone()
    print(data)
    input('Enter untuk lanjut')

def updatePegawai():
    readPegawai()
    id_pegawai = int(input('Masukan id pegawai yang ingin di update : '))
    query_select = f'select * from pegawai where id_pegawai = {id_pegawai}'
    cur.execute(query=query_select)
    data = cur.fetchone()
    print(data)
    print(data[4])
    Nama = input('Masukan nama baru : ') or data[1]
    Alamat = input('Masukan alamat baru : ') or data[2]
    No_telp = input('Masukan no telp baru : ') or data[3]
    query = f"SELECT * FROM kecamatan"
    cur.execute(query)
    data_kecamatan = cur.fetchall()
    for i in data_kecamatan:
        print(i)
    Kecamatan = input('Masukan kecamatan baru :') or data[4]
    query = f"SELECT * FROM kelurahan"
    cur.execute(query)
    data_kelurahan = cur.fetchall()
    for i in data_kelurahan:
        print(i)
    kelurahan = input('Masukan kelurahan baru :') or data[5]
    print(Kecamatan)
    query = f"UPDATE pegawai SET id_pegawai = {id_pegawai}, nama_pegawai = '{Nama}', Alamat= '{Alamat}', no_telp='{No_telp}',kecamatan_id_kecamatan={int(Kecamatan)},kelurahan_id_kelurahan={int(kelurahan)} where id_pegawai = {id_pegawai}"
    cur.execute(query)
    print('Tabel setelah update : ')
    readPegawai()
    input('enter untuk lanjut')
    conn.commit()
    input('Enter untuk lanjut')


def deletePegawai():
    readPegawai()
    id_pegawai = input('Masukkan id pegawai yang ingin dihapus: ')
    query_delete = f"DELETE FROM pegawai WHERE id_pegawai = {id_pegawai}"
    cur.execute(query_delete)
    input('Enter untuk lanjut')


def readPegawai():
    query_select = "SELECT * FROM pegawai order by id_pegawai asc"
    cur.execute(query_select)
    data1 = cur.fetchall()
    for i in data1:
        print(i)
    input('Enter untuk lanjut')

