def main():
    time = convert(input("What time is it? "))
    print(time)

    if 8 >= time >= 7:
        print("Breakfast time")
    elif 13 >= time >= 12:
        print("Lunch time")
    elif 19 >= time >= 18:
        print('Dinner time') 




def convert(time):
  hours, minutes = time.split(":")

  if minutes == "00":
    return int(hours)
  
  minutes = int(60/int(minutes))

  return float(f"{hours}.{minutes}")


if __name__ == "__main__":
    main()