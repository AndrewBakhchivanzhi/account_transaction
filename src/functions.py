import json
def get_operations(filename):
    with open(filename, "r", encoding='utf-8') as file:
        return json.load(file)

all_operations = get_operations("operations.json")

def get_executed_operations(some_operations):
    executed_operation = []
    for operation in some_operations:
        for key in operation:
            if operation[key] == "EXECUTED":
                executed_operation.append(operation)
    return executed_operation

filtered_operations = get_executed_operations(all_operations)

def sort_by_date(some_operations,last_list):
    sort_operation = sorted(some_operations, key=lambda operation: operation["date"], reverse=True)
    return sort_operation[:last_list]

sorted_operations = sort_by_date(filtered_operations,5)

def finish_operation(some_operations):
    for operation in some_operations:
        def date(some_date):
            only_date = some_date[:10]
            splitted_date = only_date.split('-')
            return '.'.join(splitted_date[::-1])
        if 'from' in operation:
            var_1 = operation["from"]
            var_2 = operation["to"]
            if var_1.lower().startswith("счет"):
                from1 = var_1.split()
                from_ = f"**{from1[-1][-4:]}"
            else:
                from1 = var_1.split()
                from_ = f"{from1[-1][:4]} {from1[-1][4:6]}** **** {from1[-1][-4:]}"
            if var_2.lower().startswith("счет"):
                to1 = var_2.split()
                to = f"**{to1[-1][-4:]}"
            else:
                to1 = var_2.split()
                to = f"{to1[-1][:4]} {to1[-1][4:6]}** **** {to1[-1][-4:]}"
            print(f"""{date(operation['date'])} {operation["description"]}
{" ".join(from1[:-1])} {from_} -> {" ".join(to1[:-1])} {to}
{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}
""")
        else:
            var_2 = operation["to"]
            if var_2.lower().startswith("счет"):
                to1 = var_2.split()
                to = f"**{to1[-1][-4:]}"
            else:
                to1 = var_2.split()
                to = f"{to1[-1][:4]} {to1[-1][4:6]}** **** {to1[-1][-4:]}"
            print(f"""{date(operation['date'])} {operation["description"]}
{" ".join(to1[:-1])} {to}
{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}
""")

finish_operation(sorted_operations)
