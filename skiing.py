

num_slopes = 10
slopes = [["L", 360, 1500, 2000], 
         ["L", 480, 1200, 1800], 
         ["L", 720, 900, 1400], 
         ["S", 302.4, 2000, 1500, 4.2], 
         ["S" ,468, 2000, 1200, 5.2], 
         ["S", 1716, 2000, 900, 14.3], 
         ["S", 2016, 2000, 1400, 11.2], 
         ["S", 423, 1400, 900, 4.7], 
         ["S", 554.4, 1800, 900, 7.7], 
         ["S", 1098, 1800, 900, 6.1]]



highest_point = 0
lowest_point = 10000


for x in range(num_slopes):
    if slopes[x][0] == "S":
        if slopes[x][2] >= highest_point:
            highest_point = slopes[x][2]


for x in range(num_slopes):
    if slopes[x][0] == "S":
        if slopes[x][3] <= lowest_point:
            lowest_point = slopes[x][3]


def checkEnd(x):
    if x == lowest_point:
        return "end"
    else:
        return "continue"
            
def pathfinder(x, total_time, count):
    a_time = 0                                      #introduces a new time var for the branching out times
    for n in range(num_slopes):   
        count += 1           
        print(count)
        if slopes[x][3] == slopes[n][2]:            #runs code if the end height of the first slope is equal to the start of the next slope or lift
            a_time = slopes[n][1]  
            if checkEnd(slopes[n][3]) == "end":
                return a_time + total_time
            elif count != num_slopes:
                return pathfinder(n, total_time + a_time, count)
            else:
                return "deadend"

time_list = [] 
num_start = 0   
   
for x in range(num_slopes):                                 #runs for the number of slopes
    total_time = 0
    if slopes[x][2] == highest_point: 
        total_time += slopes[x][1]
        if checkEnd(slopes[x][3]) == "end":
            time_list.append(total_time)                      #adds time for the first slope to the total time
        else:    
            g = pathfinder(x, total_time, 0)
            if g == "deadend":
                time_list.append(1000000) 
            else:
                time_list.append(g) 

time_list.sort()
print(time_list[0])

