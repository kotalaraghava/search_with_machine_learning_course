import fasttext

model = fasttext.load_model("/workspace/datasets/fasttext/title_model_norm.bin")

synonms_list = []
with open("/workspace/datasets/fasttext/top_words.txt", "r") as w:
    for l in w:
        res = model.get_nearest_neighbors(l)
        li = [l.strip()]
        for v,w in res:
            if v > 0.75:
              li.append(w)
        # print(li, l)
        synonms_list.append(",".join(li))
        # break
print(synonms_list[0])

with open("/workspace/datasets/fasttext/synonyms.csv", "w") as w:
    for i in synonms_list:
        w.write(f"{i}\n")