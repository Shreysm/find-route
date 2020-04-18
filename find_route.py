#Author:Shreyas Mohan+
#StudentID:1001669806

import operator
import sys

#Return the final path traversed from source to destination
def get_final_path(ele,explored,src,path):
	if ele==src:
		return path
	else:
		for i in explored:
			if ele==i[0]:
				ele=i[2]
				path.append((i))
				# return i
				# return path

	get_final_path(ele,explored,src,path)
#Implementation of Astar algorithm
def Astar(node,fringe,countnode):
	#Check if the node is present in the dictionary
	if node[0] in cities_dict:
		    #Iterate through each successors of the node
			for item in cities_dict[node[0]]:
				#print item[0]
				fringe2=[i[0] for i in fringe]
				explored2=[j[0]for j in explored]
				#print 'fringe2',fringe2
				#print 'explored2',explored2
				#If the node is already present in the fringe and explored,do not find successors of it
				if  not item[0] in fringe2 and not item[0] in explored2:
					item.extend((node[0],item[1]))
					item[1]=str(int(item[1])+int(h_dict[item[0]])+int(node[1]))
					fringe.append(item)
					#print('Appended Fringe',fringe)
				elif item[0] in explored2:
					countnode=countnode+1
					#print('countnode',countnode)
				fringe.sort(key=operator.itemgetter(1))
				#print fringe
	return fringe,countnode


print 'Assignment 1\n'
#python find_route.py input1.txt London Kassel
#python find_route.py input1.txt London Kassel h_kassel.txt
argCount=len(sys.argv) #Count the number of arguments
#stype=sys.argv[1]
ifile=sys.argv[1]
src=sys.argv[2]
dest=sys.argv[3]
#If 5 arguments,it is informed search,otherwise uninformed search
if argCount==5:
	print("Informed Search")
	hfile=sys.argv[4]
else:
	print("Uninformed Search")
	hfile='h_kassel1.txt' #h_kassel1.txt has heuristic values as 0 for each node

i=0
f=open(ifile, "r")
#Read the lines of inputfile
searchlines = f.readlines()
f.close()

SL=[]
for i, line in enumerate(searchlines):
    #Split the lines and store it in a list SL
	j=(line.split(' '))
	if j[0]=="END" and j[1]=="OF" and j[2]=="INPUT\n" :
		break
	temp=j[0]
	j[0]=j[1]
	j[1]=temp
	SL.append((' '.join(j)))

searchlines=searchlines+SL
for i in searchlines:
	if i=='\n':
		searchlines.remove('\n')
#cities_dict{Source:Destination,Distance}
cities_dict={}
for i, line in enumerate(searchlines):
    
    sl=(line.split(' '))
    
    #If node already present,append the value otherwise new key
    if sl[0] in cities_dict:
        cities_dict[sl[0]].append([sl[1],sl[2].splitlines()[0]])
    else:
        cities_dict[sl[0]]=[[sl[1],sl[2].splitlines()[0]]]

countnode=0  #Counter t determine the number of nodes expanded
h_dict={}
explored=[]
	
found_flag=False
f=open(hfile, "r")
searchlines = f.readlines()
f.close()

for i, line in enumerate(searchlines):
	sl=(line.split(' '))
	if sl[0]=="END" and sl[1]=="OF" and sl[2]=="INPUT\n" :
		break
	h_dict[sl[0]]=sl[1].splitlines()[0]

   	
fringe=[[src,str(0+int(h_dict[src])),'None','0']]
fringe.sort(key=operator.itemgetter(1))

while fringe :
	countnode=countnode+1
	#print('countnode',countnode)
	node=fringe.pop(0)
	explored.append(node)
	explored[-1][1],explored[-1][3]=explored[-1][3],explored[-1][1]
	#print('Node',node)
	#print('Explored',explored)
	if node[0]==dest:
		found_flag=True
		break
	else:
		fringe,countnode=Astar(node,fringe,countnode)



if found_flag:
	ele=explored[-1][2]
	# explored.pop(0)
	path=[explored.pop(-1)]
	get_final_path(ele,explored,src,path)
	# path.append(([src,0]))
	path=path[::-1]
	td=0
	pathstr=src
		
	for i,items in enumerate(path):
		td=td+int(items[1])
		pathstr=pathstr+' to '+items[0]+','+items[1]+' km\n'
		if i<(len(path)-1):
			pathstr=pathstr+items[0]

	print 'Distance:',str(td),'km'	
	print 'Route:',pathstr
	print 'Nodes Expanded:',countnode-1
else:
	print 'Distance: Infinity'	
	print 'Route: None'
	print 'Nodes Expanded:',countnode



	

    	
            
    
                    
                    
            
    

    
