from constVariable import *
from GA import GASort
from asap_sort import ASAPSort
from patient import getPatients
from scheduler import scheduler

import time
import numpy as np
import matplotlib.pyplot as plt
import csv


for m in range(100):
	print(m)
	NUM_PATIENTS = [10,15,20,25,30,35,40,45,50]
	#NUM_PATIENTS = [10,20]
	y_asap = []
	y_ga = []
	timecost_asap = []
	timecost_ga = []

	ITERATION_TIMES = 10


	for p_num in NUM_PATIENTS:
		start_time_ga = time.time()
		sum_asap = 0.0
		sum_ga = 0.0
		for i in range(ITERATION_TIMES):
			p_list = getPatients(p_num,RELEASE_DAY_RANGE,DUE_DAY_RANGE,TREATMENT_DAY_RANGE,MAX_INTERUPT)	
			
			start_time_asap = time.time()
			asap_list, asap_sequence = ASAPSort(p_list)
			cost_asap = time.time() - start_time_asap
			
			ga_list, ga_sequence = GASort(p_list, MAX_ITERATION, MUTATION_RATE, CROSSOVER_RATE, POPULATION)
			# print(asap_sequence, ga_sequence)

			asap_tardiness = scheduler(asap_list, CAPACITY)[0]
			ga_tardiness = scheduler(ga_list, CAPACITY)[0]
			
			sum_asap += asap_tardiness
			sum_ga += ga_tardiness
			
		y_asap.append(sum_asap/ITERATION_TIMES)
		y_ga.append(sum_ga/ITERATION_TIMES)
		
		timecost_asap.append(cost_asap)
		timecost_ga.append((time.time() - start_time_ga))
		
	print(timecost_asap)
	print(timecost_ga)
		
		
		# if asap_tardiness[0] != 0:
			# print((asap_tardiness[0] - ga_tardiness[0])/asap_tardiness[0])
		# else:
			# print(0)




	line_up = plt.plot(NUM_PATIENTS, y_asap, '-x', label='ASAP')
	line_down = plt.plot(NUM_PATIENTS, y_ga, '-x', label='GA-ASAP')

	plt.legend()
	plt.xlabel('patients\' number')
	plt.ylabel('total tardiness')

	plt.show()

	line_up = plt.plot(NUM_PATIENTS, timecost_asap, '-x', label='ASAP')
	line_down = plt.plot(NUM_PATIENTS, timecost_ga, '-x', label='GA-ASAP')
	
	plt.legend()
	plt.xlabel('patients\' number')
	plt.ylabel('time cost (s)')
	plt.show()



	inprovement = [ ]
	for i, x in enumerate(y_ga):
		if y_asap[i] != 0:
			inprovement.append((y_asap[i] - x) / y_asap[i])
		else:
			inprovement.append(0)

	line_up = plt.plot(NUM_PATIENTS, inprovement, '-x')

	plt.legend()
	plt.xlabel('patients\' number')
	plt.ylabel('improvement (s)')
	plt.show()

	with open("data/tardiness_asap.txt", "a") as f:
		y_asap = [ str(x) for x in y_asap]
		s1=', '.join(y_asap)
		f.write(s1 + '\n')

	with open("data/tardiness_ga.txt", "a") as f:
		y_ga = [ str(x) for x in y_ga]
		s1=', '.join(y_ga)
		f.write(s1 + '\n')
		
	with open("data/timecost_asap.txt", "a") as f:
		timecost_asap = [ str(x) for x in timecost_asap]
		s1=', '.join(timecost_asap)
		f.write(s1 + '\n')
		
	with open("data/timecost_ga.txt", "a") as f:
		timecost_ga = [ str(x) for x in timecost_ga]
		s1=', '.join(timecost_ga)
		f.write(s1 + '\n')


