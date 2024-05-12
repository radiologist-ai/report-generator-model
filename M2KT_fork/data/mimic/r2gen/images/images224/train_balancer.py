import json

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

# Найдите максимальное количество объектов среди всех классов
max_count = max(class_counts.values())

# Создайте новый список для дублированных объектов
new_data = []

# Дублируйте объекты для каждого класса, чтобы сделать количество объектов равным максимальному
for obj in data:
    duplications = []
    flag = False
    for label in obj['label'].replace("'", "").split(", "):
        # Определяем, сколько раз нужно продублировать объект
        if label in ['Pleural Effusion', '', 'Support Devices']:
            flag = True
        duplications.append(max_count // class_counts[label])
    if flag:
        flag = False
        new_obj = obj.copy()
        new_data.append(new_obj)
        continue
    for _ in range(sum(duplications) // len(duplications)):
        new_obj = obj.copy()
        new_data.append(new_obj)

# Запишите новые данные в JSON файл
with open('TrainBalanced.jsonl', 'w') as f:
    f.writelines(list(map(lambda x: json.dumps(x, ensure_ascii=False) + "\n", new_data)))

