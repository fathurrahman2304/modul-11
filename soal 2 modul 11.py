class OOP:
    def __init__(self,n,m):
        self._name = n 
        self._nilai = m 
    def get_nama(self):
        return self._name
    def get_nilai(self):
        return self._nilai
    def set_nama(self,n):
        self._name = n
    def set_nilai(self,m):
        self._nilai = m
    def output(self):
        print(f'\nNama : {self.get_nama()} \nNilai : {self.get_nilai()}')
# -----------------------------------------------------------------------------
nama = None
nilai = None
while True:
    print('\n===== PROGRAM OOP ===== \n1.Mendeklarasikan objek \n2.Menampilkan objek \n3.Mengubah objek \n4.Menghapus objek \n5.Keluar dari program')
    mode = int(input('Masukkan pilihan berupa angka (1/2/3/4/5): '))
    memanggil_class = OOP(nama,nilai)
    if mode == 1:
        nama = input('\nMasukkan Nama : ')
        nilai = int(input('Masukkan Nilai : '))
        memanggil_class.set_nama(nama)
        memanggil_class.set_nilai(nilai)
        print('\nData berhasil ditambahkan')
    elif mode == 2:
        memanggil_class.output()
    elif mode == 3:
        ubah = input('Apa yang ingin diubah (Nama/Nilai): ').upper()
        if ubah == 'NAMA':
            nama = input('\nMasukkan Nama : ')
            memanggil_class.set_nama(nama)
            print('Data berhasil nama diubah')
        elif ubah == 'NILAI':
            nilai = int(input('\nMasukkan Nilai : '))
            memanggil_class.set_nilai(nilai)
            print('Data berhasil nilai diubah')
        else:
            print('Inputan harus Nama/Nilai')
    elif mode == 4:
        nama = memanggil_class.set_nama(None)
        nilai = memanggil_class.set_nilai(None)
        print('\nData berhasil dihapus')
    elif mode == 5:
        break
    else:
        print('Inputan harus (1/2/3/4/5)')
        continue