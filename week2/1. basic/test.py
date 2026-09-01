import heapq
patients1 = [
        ("김철수", 3),
        ("이영희", 1),
        ("박민수", 2)
        ]
i = []
pro = []

for j , k in patients1:
    heapq.heappush(i,(k,j))

while i != []:

    result = heapq.heappop(i)
    pro.append(result[1]) 
    print(f"처리: {result[1]} (우선순위: {result[0]})")

print(pro)