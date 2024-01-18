import json
# TODO решите задачу
def task(data) -> float:
    with open(data, 'r') as file:
        dictionary_data = json.load(file)
    sum = 0
    for dictionary in dictionary_data:
        sum += dictionary.get("score") * dictionary.get("weight")
    return sum


print(f"{task('input.json'):.3f}")
