salary = [4000,3000,1000,2000]

def oylik(salary):
    count = 0
    sum = 0
    salary.remove(max(salary))
    salary.remove(min(salary))
    for i in salary:
        sum += i
        count += 1
    return sum / count

print(oylik(salary))