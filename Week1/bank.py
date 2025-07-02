greeting = input("Greeting: ").casefold()

greetings = greeting.split(" ")

if "hello" in greetings[0]:
    print("$0")
elif "h" == greetings[0][0]:
    print("$20")
else:
    print("$100")

