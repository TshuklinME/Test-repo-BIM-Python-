# TODO решите задачу
import json

def task() -> float:
    name = 'input.json'
    with open(name) as i:
        data = json.load(i)

    sum_ = sum(([item['score'] * item ['weight'] for item in data]))
    return round(sum_, 3)

print(task())
