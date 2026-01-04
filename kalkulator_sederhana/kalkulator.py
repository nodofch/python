print("="*30)
print("     <-- KALKULATOR -->")
print("="*30)

try:
    print(" ")
    angka1 = float(input("Masukkan angka pertama: "))
    operator = input("Masukkan operator [+, -, *, /]: ")
    angka2 = float(input("Masukkan angka kedua: "))

    if operator == "+":
        print(" ")
        print(f"Hasil dari >> {angka1} + {angka2} = ", angka1 + angka2)
    elif operator == "-":
        print(" ")
        print(f"Hasil dari >> {angka1} - {angka2} = ", angka1 - angka2)
    elif operator == "*":
        print(" ")
        print(f"Hasil dari >> {angka1} * {angka2} = ", angka1 * angka2)
    elif operator == "/":
        if angka2 != 0:
            hasil = angka1 / angka2
            print(" ")
            print(f"Hasil dari >> {angka1} / {angka2} = ", hasil)
        else:
            print(" ")
            print("Error: Tidak bisa membagi dengan angka 0.")

    else:
        print("")
        print("Error: Operator yang anda masukkan salah.")

except ValueError:
    print(" ")
    print("Error: Mohon masukkan angka yang valid.")

print(" ")
print("="*30)
