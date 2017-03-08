def find_max_min(num_list):

	""" find the minimum and maximum numbers in a list and return them in an Array in the format [min, max]"""

	my_list =[]

	maximum = max(num_list)
	minimum = min(num_list)

	my_list.append([minimum, maximum])
	return my_list
