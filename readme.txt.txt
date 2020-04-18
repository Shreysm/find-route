Name : SHREYAS MOHAN
UTA ID : 1001669806
Programming Language : Python
Source Code:find_route.py
Additional files: input1.txt,h_kassel.txt,h_kassel1.txt

Structure of Code:

1. get_final_path(ele,explored,src,path) : It returns the final path traversed from Source to Destination.

2. Astar(node,fringe,countnode): It uses the A star algorithm to find the successor of the node and adds it to the fringe. It sorts based on the shortest distance to destiantion. Countnode is returned to calculate the numebr of nodes expanded.

3. main(): Accepts all the arguments that are passed and allocates them in to variables. It also handles all the operations for the program.

Program flow:

Read the arguements from command line and store it in variables.
if 5 arguements
    Read the heuristic file from user
else
     A dummy heuristic file(h_kassel1.txt) with values for all nodes as 0 is read.
(A star algorithm is used in this program for both 

Read the lines of input1.txt and store the source destiantion values in cities_dict{Src:[Destination,Distance]}

Sort the list and send it to the Astar method.
Calculate the path and display the rquired output.

Instructions:
1. Make sure that the source code and the .txt file are in the destination folder.
2. Open the terminal.
3. Change the current working directory to the destination folder.
4. Type the command in the following manner:

Uninformed Search
python find_route.py  <Input_File_Name> <Start_City> <Destination_City>
Example: python find_route.py input1.txt London Kassel.

Assignment 1

Uninformed Search
Distance: Infinity
Route: None
Nodes Expanded: 7

 
Informed Search

python find_route.py  <Input_File_Name> <Start_City> <Destination_City> <Heuristic_File_Name>
Example: python find_route.py input1.txt Bremen Kassel h_kassel.txt
 
Assignment 1

Informed Search
Distance: 297 km
Route: Bremen to Hannover,132 km
Hannover to Kassel,165 km

Nodes Expanded: 3









