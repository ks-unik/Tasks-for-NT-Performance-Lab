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

with open(filename_1, 'r', encoding='utf-8') as f_1:
    values_json = json.load(f_1)

with open(filename_2, 'r', encoding='utf-8') as f_2:
    tests_json = json.load(f_2)

index_values = {}
build_index(values_json["values"], index_values)

index_tests = {}
build_index(tests_json["tests"], index_tests)

for id_value, obj_from_new in index_tests.items():
    if id_value in index_values:
        obj_from_values = index_values[id_value]
        for key, value in obj_from_new.items():
            if key not in obj_from_values or not obj_from_values[key]:
                obj_from_values[key] = value
    else:
        index_values[id_value] = obj_from_new

values_json["values"] = list(index_values.values())

with open(filename_3, 'w', encoding='utf-8') as f_3:
    json.dump(values_json, f_3, ensure_ascii=False, indent=4)
