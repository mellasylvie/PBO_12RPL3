def luas_lingkaran():
    r = int(input('jari-jari :'))

    tanya = str(input("Apakah r kelipatan 7 ?(Y/N)"))
    if tanya == "Y" :
        luas = 22/7 * r * r
        return luas
    elif tanya == "N":
        luas = 3.14 * r * r
        return luas
    else :
        print("pilihan salah")

print("luas lingkaran", luas_lingkaran())
    