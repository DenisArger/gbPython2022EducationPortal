from modules.read_data import read_data


def student_interface():
    while True:
        print("")
        print("Меню студента")
        print("")
        print("1 - Прсмотреть домашние задания")
        print("0 - Выход")
        choise = input("Введите команду: ")
        if choise == "1":
            print(
                read_data(
                    "hometasks",
                    "all",
                )
            )
        if choise == "0":
            break
