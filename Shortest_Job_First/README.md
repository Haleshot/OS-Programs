Characteristics of SJF Scheduling:
• Shortest Job first has the advantage of having a minimum average waiting time among 
all scheduling algorithms.
• It is a Greedy Algorithm.
• It may cause starvation if shorter processes keep coming. This problem can be solved using 
the concept of ageing.
• It is practically infeasible as Operating System may not know burst times and therefore 
may not sort them. While it is not possible to predict execution time, several methods can 
be used to estimate the execution time for a job, such as a weighted average of previous 
execution times.
• SJF can be used in specialized environments where accurate estimates of running time are 
available.

Algorithm:
• Sort all the processes according to the arrival time.
• Then select that process that has minimum arrival time and minimum Burst time.
• After completion of the process make a pool of processes that arrives afterward till the 
completion of the previous process and select that process among the pool which is having 
minimum Burst time.

Advantages -
• Reduces Average Time a lot.
• Better compared to FCFS.
• It helps in achieving an optimal Turn Around Time.
Disadvantages -
• It could cause starvation in some cases which can be solved by aging.
• Execution time of the process is a pre-requisite which is hard to predict.
• Cannot use this algorithm for short term CPU scheduling since it is hard to predict the CPU Burst 
Time


Calculating Average Waiting Time
For every scheduling algorithm, Average waiting time is a crucial parameter to judge it's 
performance. AWT or Average waiting time is the average of the waiting times of the processes 
in the queue, waiting for the scheduler to pick them for execution.
Example
In the following example, there are five jobs named as P1, P2, P3, P4 and P5. Their arrival time 
and burst time are given in the table below:

![image](https://user-images.githubusercontent.com/57552973/184400549-31fb2a38-12d9-434a-9b1a-0038bfdd2bc6.png)
![image](https://user-images.githubusercontent.com/57552973/184400622-95619498-fec1-44d1-82a9-0e9f1c61242f.png)





Output - 

![image](https://user-images.githubusercontent.com/57552973/184400016-9f123361-077e-43fb-a235-6b060f9ffea5.png)
![image](https://user-images.githubusercontent.com/57552973/184400117-82cfa672-932a-42f2-b524-fd9121506d84.png)
