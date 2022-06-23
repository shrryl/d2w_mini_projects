from org.transcrypt.stubs.browser import *
import random

array = []

def gen_random_int(number, seed):
	random.seed(seed)
	mylist = list(range(number))
	random.shuffle(mylist)
	return mylist


def list_to_string(ls_int):
    # convert the items into one single string
    # the number should be separated by a comma
    # and a full stop should end the string.
	s = ''
	len_counter = 0

	for x in ls_int:
		s += str(x)
		len_counter += 1
		if len_counter<len(ls_int):
			s += ','
		else:
			s += '.'
	return s


def string_to_list(s):
	s = s.replace(".","")
	ls_str = s.strip().split(',')
	ls_int = [int(i) for i in ls_str]

	return ls_int


def insertion_sort(array):
	n = len(array)
	for outer_index in range(1,n):
		inner_index = outer_index  # start with the i-th element
		temporary = array[inner_index] # save its value

		# left number is bigger
		while (inner_index>0) and (temporary < array[inner_index - 1]):
			array[inner_index] = array[inner_index - 1] # bigger number will take its place
			inner_index = inner_index - 1  # index move to the left

		array[inner_index] = temporary # value moved to the left


def generate():
	global array

	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the global variable array
	array = gen_random_int(number, seed)

	# convert the items into one single string
	array_str = list_to_string(array)

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"
	document.getElementById("generate").innerHTML = array_str


def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the global variable array and
			copy it to a new list
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str

		list_tosort = array
		insertion_sort(list_tosort)
		array_str = list_to_string(list_tosort)

		document.getElementById("sorted").innerHTML = array_str

		OR
		get the random numbers from generate HTML id.
		Hint: use document.getElementById(id).innerHTML to get the numbers,
		remove the other characters and create a list of integers called sortedarray,
		sort the list using either bubble sort or insertion sort,
		create a single string containing the sorted numbers.
	'''
	generated_str = document.getElementById("generate").innerHTML

	sortedarray = string_to_list(generated_str)
	insertion_sort(sortedarray)
	array_str = list_to_string(sortedarray)

	document.getElementById("sorted").innerHTML = array_str


def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty.")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	str_tosort = value
	list_tosort = string_to_list(str_tosort)
	insertion_sort(list_tosort)
	array_str = list_to_string(list_tosort)

	document.getElementById("sorted").innerHTML = array_str
