yil = int(input("Yil kiriting: "))
if yil % 100 == 0:
    print(f"{yil // 100} asr")
else:
    print(f"{yil // 100 + 1} asr")