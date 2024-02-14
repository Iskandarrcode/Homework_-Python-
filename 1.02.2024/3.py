def number_phone(n):
    num1 = ["88", "90", "91", "93", "94", "97"]
    if len(n) != 18:
        return False
    if n[:6] != "(998) ":
        return False
    if n[6:8] not in num1:
        return False
    if n[8] != "-" and n[12] != "-" and n[15] != "-":
        return False
    else:
        return True
    


n = input("Phone number:_(998) 9-123-45-67:\n\n")
print(number_phone(n))