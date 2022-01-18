def print_index_of_max(a_list):
	max_index = 0
	max_num = a_list[0]
	for index, i in enumerate(a_list):
		i = int(i)
		if (i > max_num):
			max_index = index
			max_num = i
	return max_index

if __name__ == "__main__":
	my_int_str = input("Please enter a list of integers separated by spaces")
	my_list = my_int_str.split()
	print(print_index_of_max(my_list))
