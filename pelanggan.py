import psycopg2

conn = psycopg2.connect(dbname='Bunga Florist', user='postgres', password='saptamabar', host='localhost', port=5432)
cur = conn.cursor()

def createpelanggan():
    query = f"SELECT * FROM pelanggan order by id_pelanggan desc"
    cur.execute(query)
    data = cur.fetchone()
    id_pelanggan = data[0]+1
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
    query = f"INSERT INTO pelanggan(id_pelanggan,nama_pelanggan, Alamat, no_telp,kecamatan_id_kecamatan,kelurahan_id_kelurahan) VALUES({id_pelanggan}, '{Nama}', '{Alamat}','{No_telp}',{Kecamatan},{kelurahan})"
    cur.execute(query, (id_pelanggan,Nama, Alamat, No_telp,Kecamatan,kelurahan) )
    conn.commit()
    query = f"SELECT * FROM pelanggan order by id_pelanggan desc"
    cur.execute(query)
    data = cur.fetchone()
    print(data)
    input('Enter untuk lanjut')

def updatepelanggan():
    readpelanggan()
    id_pelanggan = int(input('Masukan id pelanggan yang ingin di update : '))
    query_select = f'select * from pelanggan where id_pelanggan = {id_pelanggan}'
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
    query = f"UPDATE pelanggan SET id_pelanggan = {id_pelanggan}, nama_pelanggan = '{Nama}', Alamat= '{Alamat}', no_telp='{No_telp}',kecamatan_id_kecamatan={int(Kecamatan)},kelurahan_id_kelurahan={int(kelurahan)} where id_pelanggan = {id_pelanggan}"
    cur.execute(query)
    print('Tabel setelah update : ')
    readpelanggan()
    input('enter untuk lanjut')
    conn.commit()
    input('Enter untuk lanjut')


def deletepelanggan():
    readpelanggan()
    id_pelanggan = input('Masukkan id pelanggan yang ingin dihapus: ')
    query_delete = f"DELETE FROM pelanggan WHERE id_pelanggan = {id_pelanggan}"
    cur.execute(query_delete)
    input('Enter untuk lanjut')


def readpelanggan():
    query_select = "SELECT * FROM pelanggan order by id_pelanggan asc"
    cur.execute(query_select)
    data1 = cur.fetchall()
    for i in data1:
        print(i)
    input('Enter untuk lanjut')

