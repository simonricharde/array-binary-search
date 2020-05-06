def binary_search(input_list, search_key):
    mid_number = 0
    low_number = 0
    high_number = get_length(input_list) - 1

    while low_number <= high_number:
		mid_number = (high_number + low_number) / 2
			
		if search_key == input_list[mid_number]:
			return mid_number
		elif search_key < input_list[mid_number]:
			high_number = mid_number - 1
		elif search_key > input_list[mid_number]:
			low_number = mid_number + 1
    return -1



def get_length(input_list):
    list_counter=0
    for items in input_list: 
        list_counter = list_counter +1
    return list_counter
