import json
import sys

if len(sys.argv) < 4:
    print("Необходимо указать имя 3-х файлов в аргументе командной строки")
    sys.exit(1)

filename_1 = sys.argv[1]
with open(filename_1, "r") as f:
    values_json = json.load(f)

filename_2 = sys.argv[2]
with open(filename_2, "r") as f:
    tests = json.load(f)

def node(dict_test, dict_values):
    if dict_test["id"] in dict_values:
        dict_test["value"] = dict_values[dict_test["id"]]

    if "values" not in dict_test:
        return
    
    elif not dict_test["values"]:
        return
    
    else:
        for child in dict_test["values"]:
            node(child, dict_values)

values_map = {item["id"]: item["value"] for item in values_json}

for test_node in tests["tests"]:
    node(test_node, values_map)

filename_3 = sys.argv[3]
with open(filename_3, "w") as f:
    json.dump(tests, f)
