import json
# Run this script split the training video .json to train/val/test.
# When evaluate change the input json name.
loader = json.load(open('./data/videodatainfo_2017_ustc.json', 'r'))
print(loader['videos'][0]["split"])
for ind, _ in enumerate(loader['videos'][6500:7000]):
    loader['videos'][ind+6500]['split'] = 'val';
for ind, _ in enumerate(loader['videos'][7000:9999]):
    loader['videos'][ind+7000]['split'] = 'test';
print(loader['videos'][6501]['split'])
print(loader['videos'][9000]['split'])
json.dump(loader,open('./data/split_train_videodatainfo.json','w+'))
split_loader = json.load(open('./data/split_train_videodatainfo.json', 'r'))
print("check if the split change")
print(loader['videos'][2]["split"])
print(loader['videos'][6551]['split'])
print(loader['videos'][9030]['split'])