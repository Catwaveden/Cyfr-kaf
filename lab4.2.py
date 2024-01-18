# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as file_csv:
        reader = csv.DictReader(file_csv, delimiter=",")
        data = list(reader)
        # TODO считать содержимое csv файла

    with open(OUTPUT_FILENAME, 'w') as file_json:
        json.dump(data, file_json, indent=4)
        # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
