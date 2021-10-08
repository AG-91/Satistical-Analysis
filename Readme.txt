Introduction:

This code has to methods. First method csv_reader() takes the file name (which should be the correct directory path 
to the file ending with .csv) and returns a list of lists containing the data from the csv file. Second method stats(),
takes the parsed data (list of lists) and ends up printing mean, min, max, and standard deviaiton of each column of 
numeric dara along with corresponding headers. 


Discription of Methods:

	csv_reaser(file_name):
		- this function opens the csv file using  (with open()) and the file name with mode "r" and encoding "utf-8-sig" which was decided 
			after printing out the csv file without correct encoding, and searched online for correct encoding.
		- it will next iterate through the read csv file and append each row to an empty list called res while replacing 
			new line characters "\n" and qoutations " "" " at the same time
		- next it will loop through the list res and split the string after every comma using .split(',') and append the
			splitted strings to another list called lines
		- the function will return the list lines which is a list of lists

	stats(parsed_data):
		- this function takes the output from csv_reader() as input and first convert it to a NumPy array using np.array()
		- next, a variable called vector is defined to utilize the np.vectorize() method from NumPy library to convert the 
			strings to floats in order to perform the numerical procedures on them
		- arr_mean, arr_min, arr_max, and arr_std are variables created to calculates the mean, minimum, maximum, and
			standard deviation of the numeric values while skipping the date and time column using NumPy library
		- finally the method prints out the previous mentioned values along with the corresponding headers


Instructions to run the code:

in the (if __name__ == '__main__':) section of the .py file, do the following:

	- input the correct file directory path into the csv_reader() method and assign it to a variable like below example:
		- parsed_csv = csv_reader('weather-data/outside-temperature-1617.csv')
	- call the stats function with the variable from previous step as input (which is the parsed data) like below:
		- stats(parsed_csv)
	
The stats() function will print out the header, mean, minimum, maximum, and standard deviaiton values of the input file values.


References:

- Python Pool. 2021. [Solved] TypeError: Only Size-1 Arrays Can Be Converted To Python Scalars Error. 
	[online] Available at: <https://www.pythonpool.com/only-size-1-arrays-can-be-converted-to-python-scalars-error-solved/> [Accessed 17 March 2021].

- python, H. and Baraldi, M., 2021. How to split lines in a file and put data into a dictionary in python. [online] Stack Overflow. Available at: 
	<https://stackoverflow.com/questions/26680166/how-to-split-lines-in-a-file-and-put-data-into-a-dictionary-in-python> [Accessed 17 March 2021].

- GeeksforGeeks. 2021. Python | Removing newline character from string - GeeksforGeeks. [online] Available at: 
	<https://www.geeksforgeeks.org/python-removing-newline-character-from-string/> [Accessed 17 March 2021].

- GeeksforGeeks. 2021. numpy.mean() in Python - GeeksforGeeks. [online] Available at: 
	<https://www.geeksforgeeks.org/numpy-mean-in-python/> [Accessed 17 March 2021].

- 