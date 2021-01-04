# RanugaD
print("RanugaD")
list_given = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def reverse_a_linked_list_way_one(list_to_reverse):
    new_list = []
    test_list = list_to_reverse.copy()
    while test_list != []:
        new_list.append(test_list[-1])
        test_list.remove(test_list[-1])
    print(new_list)
    return new_list


def reverse_a_linked_list_way_two(list_to_reverse):
    new_list = []
    test_list = list_to_reverse.copy()
    for _ in range(len(test_list)):
        new_list.append(test_list[-1])
        test_list.remove(test_list[-1])
    print(new_list)
    return new_list


reverse_a_linked_list_way_one(list_given)
print("\n\n")
reverse_a_linked_list_way_two(list_given)
print("\n\n")
print("RanugaD")
#RanugD-
