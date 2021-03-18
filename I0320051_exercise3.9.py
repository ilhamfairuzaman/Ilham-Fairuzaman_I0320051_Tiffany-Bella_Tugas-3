# Mengupdate nilai pada tuple

tup1 = (12,34,56)
tup2 = ('abc','xyz')

# 'tup1[0] = 100' Akan menghasilkan error karena tuple unmutable

# Sehingga
tup3 = tup1 + tup2
print(tup3)