class biodata:
    count = 0
    def __init__(self,name,nim,tahun):
        self.nama = name
        self.nim = nim
        self.Angkatan = tahun
        biodata.count += 1
    def output(self):
        print('\nBerikut biodatamu')
        print(f'nama : {self.nama} \nNIM : {self.nim} \nTahun angkatan: {self.Angkatan}')
nama = input('Masukkan nama: ')
nim = input('Masukkan NIM: ')
Angkatan = input('Masukkan tahun angkatanmu: ')
mahasiswa = biodata(nama, nim, Angkatan)
mahasiswa.output()
print(f'\ntotal: %d' % biodata.count)