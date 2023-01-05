# [[[1,2,3],2,[1,3]],[1,2,3]]


def index_all(list_numbers, item):

    index_list = []
    for index, value in enumerate(list_numbers):
        if value == item:
            index_list.append([index])
        elif isinstance(list_numbers[index], list):
            for i in index_all(list_numbers[index], item):                
                index_list.append([index] + i)
    
    return index_list

print(index_all([[[1,2,3],2,[1,3]],[1,2,3]],2))


