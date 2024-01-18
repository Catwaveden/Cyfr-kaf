# TODO Напишите функцию find_common_participants
def find_common_participants(group_1, group_2, separator = ","):
    group_1_set = set(group_1.split(separator))
    group_2_set = set(group_2.split(separator))
    common_participants = list(group_1_set.intersection(group_2_set))
    common_participants.sort()
    return common_participants



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group, participants_second_group, "|")