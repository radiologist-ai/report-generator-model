import json
a = []
with open("Test.jsonl", "r") as f:
    a.extend(f.readlines())

with open("Train.jsonl", "r") as f:
    a.extend(f.readlines())

with open("Valid.jsonl", "r") as f:
    a.extend(f.readlines())

with open("all.jsonl", "w") as w:
    w.writelines(a)

print(len(a))
