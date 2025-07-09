while True:
    frac = input("Enter Fraction: ")

    try:
        x, y = frac.split("/")
    except ValueError:
        continue

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        continue

    
    else:
        try:
            pct = int ((x/y) * 100)
        except ZeroDivisionError:
            continue

        if pct < 0 or pct > 100:
            continue

        if pct == 0:
            print("E")
        elif pct == 100:
            print("F")
        else:
            print(f"{pct}%")
        break