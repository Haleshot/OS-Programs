# FCFS Algorithm with and without Arrival Time

# To Find - Turn Around Time and Wait Time and their respective average times

from tabulate import tabulate # For printing the result in a Tabular Format


def sorting_arrival(l):
    return l[1] # Returns the Second element of the list which is Arrival Time


def Turn_Around_Time(P, limit):
    # Declaring Variables for Calculating Total Turn Around Time
    total_tat = 0
    for i in range(limit):
        tat = P[i][3] - P[i][1]
        total_tat += tat # Formula For Turn Around Time -> Completion Time - Arrrival TIme
        P[i].append(tat) # Appending the Turn Around Time to the List

    avg_tat = total_tat/limit
    return avg_tat



def Waiting_Time(P, limit):
    # Declaring Variables for Calculating Total Waiting Time
    total_wt = 0

    for i in range(limit):
        wt = P[i][4] - P[i][2]
        total_wt += wt # Formula For Waiting Time -> Turn Around Time - Burst TIme
        P[i].append(wt) # Appending the Waiting Time to the List

    avg_wt = total_wt/limit
    return avg_wt
        

def Logic(P, limit):
    completion_time = 0
    exit_time = []

    

    
    



def main():
    run = True
    while(run):
        
        # Declaring arrays
        arrival_time = []
        burst_time = []
        limit_process = int(input("Enter the Number of Processes : "))
        
        print("\nDo you want to assume : \n1. Arrival Time as 0\n2. Input Arrival Time\n3. Exit\n")
        ch = int(input("Enter Your Choice : "))

        if ch == 1:
            for i in range(limit_process):
                arrival = 0
                burst = int(input("Enter the Burst Time for process {} : ".format(i)))
                arrival_time.append(arrival)
                burst_time.append(burst)

            Logic(arrival_time, burst_time, limit_process)
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 2:
            for i in range(limit_process):
                arrival = int(input("Enter the Arrival Time for process {} : ".format(i)))
                burst = int(input("Enter the Burst Time for process {} : ".format(i)))
                arrival_time.append(arrival)
                burst_time.append(burst)

            Logic(arrival_time, burst_time, limit_process)
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))
        
        elif ch == 3:
            exit(0)

        else:
            print("Invalid Choice!")
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))



main()
