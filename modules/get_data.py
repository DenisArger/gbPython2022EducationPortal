# Получение данных из файла в виде списка
def get_data(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = [(string.replace("\n", "")).split(";") for string in file.readlines()]
    return data
