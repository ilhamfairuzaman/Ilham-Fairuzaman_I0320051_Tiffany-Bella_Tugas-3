biodata = {'Nama':'Ilham Fairuzaman',
            'Hobi':{1:'Menonton film',2:'Membaca komik',3:'Tidur'},
            'Sosmed':{1:'@ilhamfairuzaman',2:'@ilhamahmasa',3:'Ilham Fairuzaman'},
            'Lagu1':{1:'Sufjan Steven',2:'Iwan Fals',3:'Noah'},
            'Makanan':{1:'Nasi goreng',2:'Pisang goreng',3:'Kebab'}}
print('\nBiodata sebelum diproses :\n', biodata)

# Mengubah salah satu hobi
biodata['Hobi'] = {1:'Menonton film',2:'Main game',3:'Dengerin musik'}
biodata['Sosmed'] = {1:'082137899006',2:'@ilhamahmasa',3:'Ilham Fairuzaman'}

# Menghapus 2 makanan favorit
biodata['Makanan'] = 'Nasi goreng'

# Menambah 1 hobi
biodata['Hobi'] = {1:'Menonton film',2:'Main game',3:'Dengerin musik',4:'Baca komik'}

# Menampilkan dictionary
print('\nBiodata setelah diproses menjadi :\n', biodata)
