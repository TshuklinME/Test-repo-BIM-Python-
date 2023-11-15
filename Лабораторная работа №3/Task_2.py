# TODO Напишите функцию find_common_participants
def find_common_participants (str_1,str_2,separator=','):
    set_1=set(str_1.split(separator))
    set_2=set(str_2.split(separator))

    find = set_1.intersection(set_2)
    list_ = list(find)
    list_.sort()

    return list_


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group,participants_second_group,'|'))
