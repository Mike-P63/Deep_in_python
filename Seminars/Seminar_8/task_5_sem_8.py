# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import json
import os
import pickle

# def find_json(path):
#     for i in os.listdir(path):
#         if i.endswith('.json'):
#             *name, extention = i.split(".")
#             with open(i, 'r') as f:
#                 data = pickle.dumps(json.load(f))
#             with open('.'.join(name)+".pickle",'w') as f:
#                 pickle.dump(str(data), f)


# find_json("F:\Deep_in_python")

def find_json(path):
    for i in os.listdir(path):
        if i.endswith(".json"):
            *name, extention = i.split(".")
            with open(i, "r")as f:
                data = json.load(f)
            with open(".".join(name)+".pickle", "wb")as f:
                pickle.dump(data, f)


find_json("F:\Deep_in_python")