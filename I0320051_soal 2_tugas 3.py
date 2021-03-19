biodata = {'Nama':'Ilham Fairuzaman',
            'Hobi':['Menonton film','Membaca komik','Tidur'],
            'Sosmed':['@ilhamfairuzaman','@ilhamahmasa','Ilham Fairuzaman'],
            'Lagu':['Sufjan Steven','Iwan Fals','Pamungkas'],
            'Makanan':['Nasi goreng','Pisang goreng','Kebab']}
print('\nBiodata sebelum diproses :\n\n', biodata)
print('=========================')

# Mengubah salah satu hobi dan sosmed
biodata['Hobi'][1] = "Bermain Game"
biodata['Sosmed'][2] = "082137899006"

# Menghapus 2 makanan favorit
del biodata['Makanan'][1:]

# Menambah 1 hobi
biodata['Hobi'].append('Mendengarkan musik')

# Menampilkan dictionary
print('\nBiodata setelah diproses menjadi :\n\n', biodata)