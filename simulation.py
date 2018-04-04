from constVariable import *
from GA import GASort
from asap_sort import ASAPSort
from patient import getPatients
from scheduler import scheduler

import numpy as np
import matplotlib.pyplot as plt

# 
NUM_PATIENTS = [10,20,30,40,50,60,70,90,100]
y_asap = []
y_ga = []

ITERATION_TIMES = 10

for p_num in NUM_PATIENTS:
	sum_asap = 0.0
	sum_ga = 0.0
	for i in range(ITERATION_TIMES):
		p_list = getPatients(p_num,RELEASE_DAY_RANGE,DUE_DAY_RANGE,TREATMENT_DAY_RANGE,MAX_INTERUPT)	

		asap_list, asap_sequence = ASAPSort(p_list)
		ga_list, ga_sequence = GASort(p_list, MAX_ITERATION, MUTATION_RATE, CROSSOVER_RATE, POPULATION)
		# print(asap_sequence, ga_sequence)

		asap_tardiness = scheduler(asap_list, CAPACITY)[0]
		ga_tardiness = scheduler(ga_list, CAPACITY)[0]
		
		sum_asap += asap_tardiness
		sum_ga += ga_tardiness
		
	y_asap.append(sum_asap/ITERATION_TIMES)
	y_ga.append(sum_ga/ITERATION_TIMES)
	
	# if asap_tardiness[0] != 0:
		# print((asap_tardiness[0] - ga_tardiness[0])/asap_tardiness[0])
	# else:
		# print(0)
		
plt.plot(NUM_PATIENTS, y_asap)
plt.plot(NUM_PATIENTS, y_ga)
 
plt.show()