import json
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

id_labels_path = "../../../finding/chexpert_labeled.csv"

# Create MultiLabelBinarizer object
mlb = MultiLabelBinarizer()


df = pd.read_json(path_or_buf="all.jsonl", lines=True)
df = df[['id', 'label']]
df['label'] = df['label'].apply(lambda x: [] if x == "''" or x == "" else list(map(lambda s: s.replace("'", ""), x.split("', '"))))
a = mlb.fit_transform(df['label'])
print(len(list(mlb.classes_)))
df = df[['id',]].join(pd.DataFrame(a,
                          columns=mlb.classes_,
                          index=df.index))

# df = df.loc[(df.drop('id', axis=1) == 1).any(axis=1)]
# df = df[df['No Finding'] == 0]

ids = set(df['id'])
df.to_csv(id_labels_path, index=False)

jsonObj1 = pd.read_json(path_or_buf="TrainBalanced.jsonl", lines=True)
jsonObj1["img"] = jsonObj1["img"].apply(lambda x: "/".join(x.rsplit("/", maxsplit=2)[1:]))
jsonObj1 = jsonObj1.rename(columns={"text": "report", "img": "image_path"})
jsonObj1 = jsonObj1[jsonObj1['id'].isin(ids)]
jsonObj1 = json.loads(jsonObj1.to_json(index=False, orient="records"))


jsonObj2 = pd.read_json(path_or_buf="Valid.jsonl", lines=True)
jsonObj2["img"] = jsonObj2["img"].apply(lambda x: "/".join(x.rsplit("/", maxsplit=2)[1:]))
jsonObj2 = jsonObj2.rename(columns={"text": "report", "img": "image_path"})
jsonObj2 = jsonObj2[jsonObj2['id'].isin(ids)]
jsonObj2 = json.loads(jsonObj2.to_json(index=False, orient="records"))

jsonObj3 = pd.read_json(path_or_buf="Test.jsonl", lines=True)
jsonObj3["img"] = jsonObj3["img"].apply(lambda x: "/".join(x.rsplit("/", maxsplit=2)[1:]))
jsonObj3 = jsonObj3.rename(columns={"text": "report", "img": "image_path"})
jsonObj3 = jsonObj3[jsonObj3['id'].isin(ids)]
jsonObj3 = json.loads(jsonObj3.to_json(index=False, orient="records"))

res = {
    'train': jsonObj1,
    'val': jsonObj2,
    'test': jsonObj3
}
with open("annotation.json", "w") as out:
    json.dump(res, out)


