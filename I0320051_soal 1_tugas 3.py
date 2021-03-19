# List 10 teman
temen = ['ojat','alam','hani','afnan','raka',
        'sasa','safri','yuki','rahmat','ilhum']

# Menampilkan isi list indeks 4 6 7
print('')
print('nama teman pada indeks ke-4 = ', temen[4])
print('nama teman pada indeks ke-6 = ', temen[6])
print('nama teman pada indeks ke-7 = ', temen[7])

# Mengganti nama teman pada indeks 3 5 9
print('')
temen[3] = 'mira'
temen[5] = 'hafiz'
temen[9] = 'nurki'
print(temen)

# Menambah 2 teman
print('')
temen.extend(['Ervizal','rama'])
print(temen)

# Menampilkan semua nama teman dengan loop
print('')
for i in temen:
    print('{}'.format(i))

# Menampilkan panjang list
print('')
print('panjang listnya yaitu = ',len(temen))