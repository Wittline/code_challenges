def sort_frequency(items):
    dict_freq = {}

    for item in items:
        if item in dict_freq:
            dict_freq[item] = dict_freq[item] + 1
        else:
            dict_freq[item] = 1

    swap = False
    for i in range(0, len(items)):
        for j in range(0, len(items) - i - 1):
            if items[j] > items[j+1]:
                items[j],  items[j+1] = items[j+1], items[j]
                swap = True
            if dict_freq[items[j]] > dict_freq[items[j+1]]:
                items[j],  items[j+1] = items[j+1], items[j]
                swap = True
            
        if not swap:
            return 
                    

    return items

sort_frequency( [7,7,5,5,2,3,5,1])