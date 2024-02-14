import heapq

ls = (22, 32, 5, 6, 27, 28, 9, 10, 11)

heapq.heapify(list(ls))

print(heapq.nsmallest(1, ls))
print(heapq.nlargest(1, ls))