def main():
    try:
        n = int(input("Number: "))
    except ValueError:
        print("Invalid Number.")
    
    else:
        print(f"Square: {square(n)}")

def square(n):
    return n * n

if __name__ == "__main__":
    main()