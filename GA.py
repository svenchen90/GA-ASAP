import random
import math

from constVariable import *
from asap_sort import ASAPSort
from patient import getPatients
from scheduler import scheduler

def GASort(array, max_iteration, m_rate, c_ratio, population):
	map = {p['id']: p for p in array}
	
	def produce(parents):
		if len(parents) == 0:
			print('error')
		parents = sorted(parents, key = lambda x: scheduler(toList(x), CAPACITY)[0])
		
		maxLengthCross = math.floor(len(parents) * c_ratio)
		
		offspring = []
		
		# crossover
		for p in parents:
			offspring.extend(crossover(list(parents[0]), list(p), random.randint(1, maxLengthCross)))
		
		# mutation
		for o in offspring:
			mutation(o)
		
		offspring = sorted(offspring, key = lambda x: scheduler(toList(x), CAPACITY)[0])
		
		offspring = offspring[:1]
		return offspring
	
	def fillParents(parents):
		while(len(parents) < population):
			temp = [ x for x in range(1, len(array)+1)]
			random.shuffle(temp)
			parents.append(temp)
	
	def toList(sequence):
		return [ map[id] for id in sequence]
	

		
	def arraySubstract(a1, a2):
		diff = []
		for i in a1:
			if i not in a2:
				diff.append(i)
		return diff
	
	def switchNumber(array, num1, num2):
		index1=-1
		index2=-1
		for index, x in enumerate(array):
			if x == num1:
				index1 = index
			elif x == num2:
				index2 = index
			
			if index1 != -1 and index2 != -1:
				break
				
		temp = array[index1]
		array[index1] = array[index2]
		array[index2] = temp
		
	
	def switchArray(array, start, end, subArray):
		diff = arraySubstract(subArray, array[start: end])

		if len(diff) == 0:
			return
		else:
			index = 0
			for i in range(start, end):
				if array[i] not in subArray:
					switchNumber(array, array[i], diff[index])
					index += 1
				
	def crossover(p1, p2, length):
		startPoint = random.randint(0, len(p1)-length)
		
		
		substring1 = p1[startPoint: startPoint+length]
		substring2 = p2[startPoint: startPoint+length]
		
		switchArray(p1, startPoint, startPoint+length, substring2)
		switchArray(p2, startPoint, startPoint+length, substring1)
		for i in range(startPoint, startPoint+length):
			p1[i] = substring2[i-startPoint]
			p2[i] = substring1[i-startPoint]
			
		return p1, p2
	
	def mutation(p1):
		if random.random() <= m_rate:
			index1 = random.randint(0, len(p1)-1)
			index2 = random.randint(0, len(p1)-1)
			temp = p1[index1]
			p1[index1] = p1[index2]
			p1[index2] = temp
	
	iterate = 0
	parents = [ASAPSort(array)[1]]
	while(iterate < max_iteration):
		fillParents(parents)
		parents = produce(parents)
		iterate += 1
	
	return toList(parents[0]), parents[0]