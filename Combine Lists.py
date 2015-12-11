list3=[]
if list1==[] or list2==[]:
	list3=[]
	return list3
elif len(list1)>len(list2):
	for i in range(len(list2)):
		list3+=[list1[i]]+[list2[i]]
	list3+=list1[i+1:]
	return list3

else:
	for i in range(len(list1)):
		list3+=[list1[i]]+[list2[i]]
	list3=list3+list2[i+1:]
	return list3
