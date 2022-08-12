# FCFS Algorithm with and without Arrival Time

# To Find - Turn Around Time and Wait Time and their respective average times


def Logic(at, bt, n):

    # Array for Turn Around Time
    turn_at = [0] * n

    # Array for Waiting Time
    wait_t = [0] * n
    wait_t[0] = 0 # Initializing first value of CPU start as zero.

    # Array for Exit/ Completion Time
    exit_t = [0] * n
    exit_t[0] = 0 # Initializing first value of completion Time start as zero.
    

    print("\nProcess Number\t\tArrival Time\t\tBurst Time\t\tWaiting Time\t\tTurn Around Time\t\tCompletion Time\n")



    for i in range(1, n):
        exit_t[i] = exit_t[i - 1] + bt[i - 1]
        wait_t[i] = exit_t[i] - at[i] # Formula for Waiting Time

        if(wait_t[i] < 0):
            wait_t = 0

    total_wt = 0
    total_tat = 0

    for i in range(n):
        turn_at[i] = wait_t[i] + bt[i] # Formula for Turn Around Time

    for i in range(n):
        total_wt += wait_t[i]
        total_tat += turn_at[i]
        compl_time = turn_at[i] + at[i]
        p = "P" + str(i + 1)
        print(p, "\t\t\t\t", at[i], "\t\t", bt[i], "\t\t\t", wait_t[i], "\t\t\t", turn_at[i], "\t\t\t\t" , compl_time)


    avg_wait_t = total_wt/n 
    avg_turn_at = total_tat/n
    
    print("Average Waiting Time is = ", round(avg_wait_t, 2))
    print("Average Turn Around Time is = ", round(avg_turn_at, 2))

    
    



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
