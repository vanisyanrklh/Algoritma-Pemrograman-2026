# Program penjumlahan matriks 2x2
# Algoritma dan Pemrograman | S1 Pendidikan Matematika FKIP Untirta | 2026/2027 Ganjil

def tambah_matriks(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            C[i][j] = A[i][j] + B[i][j]
    return C

# Input dari pengguna
print("Masukkan elemen matriks A (2x2):")
A = [[int(input(f"A[{i}][{j}]: ")) for j in range(2)] for i in range(2)]

print("Masukkan elemen matriks B (2x2):")
B = [[int(input(f"B[{i}][{j}]: ")) for j in range(2)] for i in range(2)]

# Proses dan Output
C = tambah_matriks(A, B)
print("Hasil penjumlahan matriks C adalah:")
for row in C:
    print(row)

# Test case tambahan
print("Test Case 1:", tambah_matriks([[1,2],[3,4]], [[5,6],[7,8]]))  # [[6,8],[10,12]]
print("Test Case 2:", tambah_matriks([[2,0],[1,-3]], [[-2,4],[3,5]])) # [[0,4],[4,2]]
