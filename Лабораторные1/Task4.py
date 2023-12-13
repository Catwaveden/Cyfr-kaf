users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
visits = {"Общее количество":0, "Уникальные посещения":0}
visits.update({"Общее количество": len(users)})
unique_users = len(set(users))
visits.update({"Уникальные посещения": unique_users})
print(visits)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
