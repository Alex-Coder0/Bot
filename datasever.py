import datetime

def add_data(data):
	file = open(crypt() + ".data", "a")
	for i in range(len(data)):
		file.write(str(data[i]) + " ")

	x = datetime.datetime.now()
	x = x.strftime("%X")
	file.write(x)
	file.write("\n")
	file.close()


def find_user_info(firsname,lastname):
	try: 
		file = open(crypt() + ".data", "r")
		a = file.readlines()
		b = len(a)
		stats = []
		timer = datetime.datetime.strptime("0:0:0",'%H:%M:%S')
		for i in range(b):
			if str(firsname) in a[i] and str(lastname) in a[i]:
				j = a[i].split()
				stats.append(j)
		
		for i in range(len(stats)):
			if stats[i][4] == 's':
				try:
					ts = stats[i+1][6]
					te = stats[i][6]
					ts_d = datetime.datetime.strptime(ts, '%H:%M:%S')
					te_d = datetime.datetime.strptime(te, '%H:%M:%S')
					timer += ts_d - te_d
				except IndexError:
					te = stats[i][6]
					te_d = datetime.datetime.strptime(te, '%H:%M:%S')
					x = datetime.datetime.now()
					x = x.strftime("%X")
					x_d = datetime.datetime.strptime(x, '%H:%M:%S')
					timer = x_d-te_d
					print(timer)
					return 1, timer
		x = str(timer)

		return x[11:], 0
	except IOError:
		return "В файле нет записей", 0






def find_data(firsname,lastname):
	file1 = open(crypt() + ".data", "a")
	file1.close()
	file = open(crypt() + ".data", "r")
	a = file.readlines()
	b = len(a)
	stats = []
		
	for i in range(b):
		if str(firsname) in a[i] and str(lastname) in a[i]:
			j = a[i].split()
			stats.append(j)
	try:
		smokes = stats[len(stats)-1][2]
	except IndexError:
		smokes = 0
	try:
		eats = stats[len(stats)-1][3]
	except IndexError:
		eats = 0
		
	return smokes,eats
			



def crypt():
	x = datetime.datetime.now()
	years = x.year
	month = x.month
	days = x.day
	crypt = str(years) + str(days) + str(month)
	return crypt

# x = ["Alexander", "Smirnov", 0, 0, "s"]
# add_data(x)
# print(find_data("Alexander"))
