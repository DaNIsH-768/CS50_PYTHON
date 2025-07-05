def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s.isalnum():
        return False
    
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False
    
    number_started =  False
    for i in range(len(s)):
        # check if s[i] is a number
        if s[i].isdigit():
            if not number_started:
                number_started = True
                # check if first number != 0
                if s[i] == '0':
                    return False
        
        # check if a letter comes after number
        elif number_started:
            return False

    return True





main()