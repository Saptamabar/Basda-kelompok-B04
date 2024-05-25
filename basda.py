import psycopg2
from pegawai import createPegawai,readPegawai,updatePegawai,deletePegawai
from pelanggan import createpelanggan,readpelanggan,updatepelanggan,deletepelanggan
import os
# from pelanggan import main_pelanggan

conn = psycopg2.connect(dbname='Bunga Florist', user='postgres', password='saptamabar', host='localhost', port=5432)
cur = conn.cursor()

def main():
    print('Selamat datang!!')
    print('Apa yang ingin anda lakukan ?')
    print('1. CRUD Pegawai')
    print('2. CRUD Pelanggan')
    print('3. Keluar')
    pilihan = input('Masukan Pilihan : ')
    if pilihan == "1":
        main_pegawai()
    elif pilihan == '2':
        main_pelanggan()
    elif pilihan == '3':
        cur.close()
        conn.close()
        exit()

def main_pegawai():
    os.system('cls')
    print('1. Create pegawai')
    print('2. Read pegawai')
    print('3. Update pegawai')
    print('4. Delete pegawai')
    print('5. Kembali')
    pilihan = input('Masukan Pilihan anda : ')
    if pilihan == '1':
        os.system('cls')
        createPegawai()
        os.system('cls')
        main_pegawai()
    elif pilihan == '2':
        os.system('cls')
        readPegawai()
        os.system('cls')
        main_pegawai()
    elif pilihan == '3':
        os.system('cls')
        updatePegawai()
        os.system('cls')
        main_pegawai()
    elif pilihan == '4':
        os.system('cls')
        deletePegawai()
        os.system('cls')
        main_pegawai()
    elif pilihan == '5':
        os.system('cls')
        main()
    else:
        input('masukan pilihan yang benar\ntekan enter untuk lanjut')

def main_pelanggan():
    os.system('cls')
    print('1. Create pelanggan')
    print('2. Read pelanggan')
    print('3. Update pelanggan')
    print('4. Delete pelanggan')
    print('5. Kembali')
    pilihan = input('Masukan Pilihan anda : ')
    if pilihan == '1':
        os.system('cls')
        createpelanggan()
        os.system('cls')
        main_pelanggan()
    elif pilihan == '2':
        os.system('cls')
        readpelanggan()
        os.system('cls')
        main_pelanggan()
    elif pilihan == '3':
        os.system('cls')
        updatepelanggan()
        os.system('cls')
        main_pelanggan()
    elif pilihan == '4':
        os.system('cls')
        deletepelanggan()
        os.system('cls')
        main_pelanggan()
    elif pilihan == '5':
        os.system('cls')
        main()
    else:
        input('masukan pilihan yang benar\ntekan enter untuk lanjut')

main()