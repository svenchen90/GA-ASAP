from constVariable import *
from GA import GASort
from asap_sort import ASAPSort
from patient import getPatients
from scheduler import scheduler


p_list = getPatients(NUM_PATIENTS,RELEASE_DAY_RANGE,DUE_DAY_RANGE,TREATMENT_DAY_RANGE,MAX_INTERUPT)	

asap_list, asap_sequence = ASAPSort(p_list)
ga_list, ga_sequence = GASort(p_list, MAX_ITERATION, MUTATION_RATE, CROSSOVER_RATE, POPULATION)
# print(asap_sequence, ga_sequence)

asap_tardiness = scheduler(asap_list, CAPACITY)
ga_tardiness = scheduler(ga_list, CAPACITY)
if asap_tardiness[0] != 0:
	print((asap_tardiness[0] - ga_tardiness[0])/asap_tardiness[0])
else:
	print(0)