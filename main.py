def print_index_of_max(a_list):
	max_index = 0
	max_num = a_list[0]
	for index, i in enumerate(a_list):
		if (i > max_num):
			max_index = index
			max_num = i
	return max_index

if __name__ == "__main__":
	my_list = [1, 5, 7, 3, 10, 45, 7, -5]
	print(print_index_of_max(my_list))
