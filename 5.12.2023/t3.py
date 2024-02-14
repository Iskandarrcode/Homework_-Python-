dt = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
mn = min(list(dt.values()))
mx = max(list(dt.values()))
for i in range(1, len(dt) + 1):
    if dt[i] == mn or dt[i] == mx:
        dt.pop(i)
print(dt)