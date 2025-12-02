import json
import sys

def build_index(obj_list, index):
    for obj in obj_list:
        index[obj["id"]] = obj
        if "values" in obj:
            build_index(obj["values"], index)

if len(sys.argv) < 4:
    print("Необходимо указать 3 файла")
    sys.exit(1)

filename_1 = sys.argv[1]
filename_2 = sys.argv[2]
filename_3 = sys.argv[3]

with open(filename_1, 'r') as f:
    values_json = json.load(f)

with open(filename_2, 'r') as f:
    tests_json = json.load(f)

index_values = {obj["id"]: obj for obj in values_json["values"]}


def fill_values(obj_list, index):
    for obj in obj_list:
        obj_id = obj["id"]
        if obj_id in index:
            obj["value"] = index[obj_id]["value"]
        if "values" in obj:
            fill_values(obj["values"], index)

fill_values(tests_json["tests"], index_values)

with open(filename_3, 'w', encoding='utf-8') as f:
    json.dump(tests_json, f, ensure_ascii=False, indent=4)
