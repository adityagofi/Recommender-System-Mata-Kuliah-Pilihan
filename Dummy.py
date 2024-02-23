import pandas as pd

# Contoh DataFrame
data = {
    'Nama': ['John', 'Alice', 'Bob'],
    'A': [10, 20, 30],
    'B': [5, 10, 15],
    'C': [3, 6, 9]
}

df = pd.DataFrame(data)

# Menambahkan kolom 'Total' yang berisi total dari setiap baris
df['Total'] = df[['A', 'B', 'C']].sum(axis=1)

# Mengurutkan DataFrame berdasarkan kolom 'Total' dari yang terbesar ke yang terkecil
df = df.sort_values(by='Total', ascending=False)

# Mengatur ulang indeks DataFrame
df = df.reset_index(drop=True)

print(df)
