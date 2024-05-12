import json


def a(s: str):
    with open(s, 'r') as f:
        reports = json.load(f)

    n = 0
    unique = {}

    for r in reports:
        if (r['prediction'] not in unique):
            unique[r['prediction']] = 0
        unique[r['prediction']] += 1
        n += 1

    return [(u, u / n) for u in unique.values()], n, len(unique)

resss = []

for i in range(1, 51):
    s1 = rf"D:\Py\M2KT\results\iu_xray\V12_resnet101_labelloss_rankloss_7th_try_20240309-232709\Enc2Dec-{i}_0_test_generated.json"
    s2 = rf"D:\Py\M2KT\results\iu_xray\V12_resnet101_labelloss_rankloss_7th_try_20240309-232709\Enc2Dec-{i}_0_val_generated.json"
    q, w, e = a(s1)
    resss.append((i,"test",q,w,e))
    print(f"{i}\ttest\t{q}\t{w}\t{e}")
    print("--"*60)
    q, w, e = a(s2)
    resss.append((i,"val",q,w,e))
    print(f"{i}\tval\t{q}\t{w}\t{e}")
    print("##"*60)

resss.sort(key=lambda x: -x[-1])
for i, split, distr, n, len_unique in resss[:5]:
    print(f"{i}\t{split}\t{distr}\t{n}\t{len_unique}")
    print("_"*120)