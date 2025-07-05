cost = 50
total = 0

while total < cost:
    print(f"Amount due: {cost - total}")
    amount = int(input("Insert coin: "))

    if amount in [25, 10, 5]:
        total += amount

print(f"Change due: {total - cost}")