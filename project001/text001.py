#coding=utf-8
schema = {
    "china": {
        "shanghai": [
            {"name": "person1", "age": 10, "data": [77, 87, 99]},
            {"name": "person2", "age": 20, "data": [67, 67, 85]},
            {"name": "person3", "age": 30, "data": [76, 78, 96]}
        ],
        "shenzhen": [
            {"name": "person11", "age": 11, "data": [77, 87, 99]},
            {"name": "person22", "age": 22, "data": [67, 67, 85]},
            {"name": "person33", "age": 33, "data": [76, 78, 96]}
        ]
    }
}


def analyze_data(data, result):
    if isinstance(data, dict):
        for k, v in data.items():
            analyze_data(v, result + ".get(\"%s\")" % str(k))
    elif isinstance(data, (list, tuple)):
        for i in range(len(data)):
            analyze_data(data[i], result + "[%s]" % i)
    else:
        print(result + "=" + str(data))


analyze_data(schema, result="schema")
