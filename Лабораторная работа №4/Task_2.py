# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(input_file, output_file) -> None:

    # TODO считать содержимое csv файла
    with open(input_file) as in_f:
        lines = [line for line in csv.DictReader(in_f)]

    # TODO Сериализовать в файл с отступами равными 4
    with open(output_file, 'w') as out_f:
        json.dump(lines, out_f, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME,OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")