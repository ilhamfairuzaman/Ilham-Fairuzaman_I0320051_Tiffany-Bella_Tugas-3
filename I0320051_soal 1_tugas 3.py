# List 10 teman
temen = ['ojat','alam','hani','afnan','raka',
        'sasa','safri','yuki','rahmat','ilhum']

# Menampilkan isi list indeks 4 6 7
print('')
print(temen[4])
print(temen[6])
print(temen[7])

# Mengganti nama teman pada indeks 3 5 9
print('')
temen[3] = 'mira'
temen[5] = 'hafiz'
temen[9] = 'nurki'
print(temen)

# Menambah 2 teman
print('')
temen.append('ervizal')
temen.append('rama')
print(temen)

# Menampilkan semua nama teman dengan loop
print('')
for i in temen:
    print('{}'.format(i))

# Menampilkan panjang list
print('')
print('panjang listnya yaitu = ',len(temen))