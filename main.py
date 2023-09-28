from src.functions import get_executed_operations,get_operations,sort_by_date,finish_operation

all_operations = get_operations("src/operations.json")
filtered_operations = get_executed_operations(all_operations)
sorted_operations = sort_by_date(filtered_operations,5)
print(finish_operation(sorted_operations))
for operation in finish_operation(sorted_operations):
    print(operation)
