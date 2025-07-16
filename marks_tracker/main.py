import csv

def main():
    print('Welcome to the School report card')
    while True:
        print('Choose one of the following.\n1. Add a student\n2. View a student\n3. Quit')
        option = input('--> ')

        if option == '1':
            info = new_student()
            add_student(info)
        elif option == '2':
            view_student()
        elif option == '3':
            break
        else: 
            print('Invalid option.')
            continue

def new_student():
    while True:
        name = input('Enter name of the student: ')
        if not name.strip():
            print('Invalid name')
            continue

        id = input('Student ID: ')

        print('Enter marks for the following subjects')
        eng = input('English: ')
        math = input('Math: ')
        sci = input('Science: ')
        com = input('Computer: ')

        return {
            'name': name, 
            'id': id,
            'english': eng,
            'maths': math,
            'science': sci,
            'computer': com
        }

def add_student(info):
    with open('marks.csv', 'a') as file:
        fieldnames = ['name','id','english','maths','science','computer']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writerow(info)

    print('Student Added Successfully\n')

def view_student():
    while True:
        student = input('Name of student to view: ')
        if not student.strip():
            print('Invalid name')
            continue

        with open('marks.csv') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row['name'].strip() == student.strip():
                    print_report(**row)
                    break
            else: 
                print('No such student. Check and Try Again.\n') 
                continue

            break

def print_report(name, id, english, maths, science, computer):

    print("*" * 15)
    print(f"Marks for {name}:\n"
      f"  English : {english}\n"
      f"  Maths   : {maths}\n"
      f"  Science : {science}\n"
      f"  Computer: {computer}")
    print("*" * 15, "\n")


if __name__ == '__main__':
    main()