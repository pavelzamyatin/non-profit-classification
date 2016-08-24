import webbrowser

file_name = input('Please type filename [by default segment-aa.txt]? ')
if len(file_name) == 0:
	file_name = 'segment-aa.txt'

start = input('Start from? ')

def classification(file_name, counter):
	''' Func for classification non-profit sites based on <...> '''
	try:

		f = open(file_name, 'r')
		site_list = f.read().splitlines()

		for x in range(counter, len(site_list), +1):
			url = site_list[counter]
			#webbrowser.open_new(url)
			print(url, counter)
			counter += 1

		f.close()	

	except Exception as e:
		print(e)


# --- TEST --- #

classification(file_name, int(start))