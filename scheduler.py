#from patient import getPatients

def scheduler(p_list, capacity):
	# schedule = [ [] for i in range(capacity) ];
	utilization = []
	
	def findAvaliableSlots(startD, realseD, dueD, treatmentD, maxInterupt):
		availableD = 0
		finishD = -1
		for i in range(startD ,startD+treatmentD+maxInterupt):
			if i < len(utilization):
				if utilization[i] < capacity:
					availableD += 1
			else:
				availableD += 1
			if availableD == treatmentD:
				finishD = i
				break
				
		
		if availableD == treatmentD:
			index = startD
			while(availableD > 0):
				if index < len(utilization):
					if utilization[index] < capacity:
						utilization[index] += 1
						availableD -= 1
				else:
					utilization.append(1);
					availableD -= 1
				index += 1
			return startD - dueD, finishD - startD + 1 - treatmentD
		else:
			return findAvaliableSlots(startD+1, realseD, dueD, treatmentD, maxInterupt)
	
	
	tardiness = 0
	tardiness_weighted = 0.0
	for index, patient in enumerate(p_list):
		localTardiness, localInterupt = findAvaliableSlots(patient['rd'], patient['rd'], patient['dd'],patient['td'],patient['mi'])
		tardiness += max(0, localTardiness) + localInterupt
		tardiness_weighted += (max(0, localTardiness) + localInterupt)/patient['td']
	
	return tardiness, tardiness_weighted, utilization
	
	return tardiness, utilization
	
		
# p_list = getPatients(2,10,10, 30, 10)
# scheduler(p_list, 3)