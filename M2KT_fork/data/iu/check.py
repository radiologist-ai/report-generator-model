import json

# Загрузите ваш JSON файл
with open('TrainBalanced.jsonl', 'r') as f:
    data = list(map(json.loads, f.readlines()))

# Создайте словарь для подсчета количества объектов для каждого класса
class_counts = {}

# Подсчитайте количество объектов для каждого класса
for obj in data:
    for label in obj["label"].replace("'", "").split(", "):
        if label not in class_counts:
            class_counts[label] = 0
        class_counts[label] += 1

print(class_counts)

# Загрузите ваш JSON файл
with open('Train.jsonl', 'r') as f:
    data = list(map(json.loads, f.readlines()))

# Создайте словарь для подсчета количества объектов для каждого класса
class_counts = {}

# Подсчитайте количество объектов для каждого класса
for obj in data:
    for label in obj["label"].replace("'", "").split(", "):
        if label not in class_counts:
            class_counts[label] = 0
        class_counts[label] += 1

print(class_counts)