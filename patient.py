import random

def getPatients(num, rd_range, dd_range, td_range, mi_range):
	list = []
	for i in range(num):
		id = i + 1;
		releaseDay = random.randint(1,rd_range)
		dueDay = random.randint(releaseDay,dd_range)
		treatmentDay = random.randint(1,td_range)
		maxInterupt = random.randint(0,mi_range)
		catagory = random.choice([0, 1])
		
		
		list.append({'id': id, 'rd': releaseDay, 'dd': dueDay, 'td': treatmentDay, 'mi': maxInterupt, 'cata': catagory});
	return list
	
# print(getPatients(100,10,10, 30, 10))