def ASAPSort(p_list):
	sortedList = sorted(p_list, key = lambda x: (-x['cata'] , x['rd'], x['dd']))
		
	return sortedList,  [p['id'] for p in sortedList]