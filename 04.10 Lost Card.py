n = int(input("Enter Number of Cards: "))
sum_cards = 0
for i in range(1, n + 1):
    sum_cards += i
for i in range(n - 1):
    sum_cards -= int(input("Enter Card: "))
print("Missing Card:",sum_cards)