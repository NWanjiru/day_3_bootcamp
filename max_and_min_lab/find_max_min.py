def find_max_min(num_list):

	""" find the minimum and maximum numbers in a list and return them in an Array in the format [min, max]"""

	my_list =[]
	new_list+[]

	maximum = max(num_list)
	minimum = min(num_list)

	if minimum == maximum:
		new_list.append(len(num_list))
		return new_list

	my_list.append(minimum)
	my_list.append(maximum)
	return my_list
