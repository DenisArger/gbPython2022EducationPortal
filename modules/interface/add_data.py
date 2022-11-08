from modules.get_data import get_data
from modules.check_data import check_data

# Добавление данных
def add_data(filename, new_data):
    filename = "data/" + filename + ".txt"
    data = get_data(filename)
    if len(new_data) == len(data[0]):
        if check_data(data, new_data[0], 0) == "-1":
            data.append(new_data)
            with open(filename, "w", encoding="utf-8") as file:
                data = "\n".join(
                    [";".join(list(map(str, data[i]))) for i in range(len(data))]
                )
                file.write(data)
                print("Новая запись добавлена успешно")
        else:
            print("Данные с таким ключевым полем уже существуют в таблице")
    else:
        print("Неверный формат данных")
