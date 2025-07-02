def main():
    text = input("Enter your text: ")
    convert(text)


def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    print(text)

main()