def hitung_frekuensi_karakter(string):
    """Menghitung frekuensi setiap karakter dalam sebuah string."""
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Input string dari pengguna
string_input = input("Masukkan sebuah string: ")

# Hitung frekuensi karakter
frekuensi_karakter = hitung_frekuensi_karakter(string_input)

# Tampilkan hasil
print("Frekuensi karakter dalam string:")
for char, count in frekuensi_karakter.items():
    print(f"Karakter '{char}': {count}")
