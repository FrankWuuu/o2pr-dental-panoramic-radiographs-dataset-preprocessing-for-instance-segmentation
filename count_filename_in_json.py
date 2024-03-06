import json

# json_name = 'train.json'  # path to Dataset and code test.json
# csv_dst = 'train_lists.csv'

json_name = 'test.json' # path to Dataset and code test.json
csv_dst = 'test_lists.csv'

with open(json_name) as json_file:
    labelbox_data = json.load(json_file)

file_names = []

print(len(labelbox_data['images']))

for image in labelbox_data['images']:
    file_name = image['file_name']
    file_names.append(file_name)

with open(csv_dst,'w') as f:
    for r in file_names:
        f.write(r+"\n")