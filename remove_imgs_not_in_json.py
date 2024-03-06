import shutil
import os

# path = "o2pr/train/images/"
# file_name = "train_lists.csv"

path = "o2pr/test/images/"
file_name = "test_lists.csv"

name_lists_json = []
with open(file_name,'r') as f:
    content = f.read()
    rows = content.split('\n')
    for row in rows:
        name_lists_json.append(row)

name_lists_imgs = os.listdir(path)
print("original imgs lens",len(name_lists_imgs))
print("json imgs lens",len(name_lists_json))

names_tobe_del = list(set(name_lists_imgs)-set(name_lists_json))
print(len(names_tobe_del))

for file_del in names_tobe_del:
    path_del = path + file_del
    # shutil.rmtree(path_del)
    os.remove(path_del)
    # print(path_del)