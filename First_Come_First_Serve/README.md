First-Come-First-Serve algorithm is the simplest scheduling algorithm. Processes are dispatched 
according to their arrival time on the ready queue. Being a non-pre-emptive discipline, once a 
process has a CPU, it runs to completion. The FCFS scheduling is fair in the formal sense or human 
sense of fairness but it is unfair in the sense that long jobs make short jobs wait and unimportant 
jobs make important jobs wait.
 
FCFS is more predictable than most of other schemes since it offers time. FCFS scheme is not 
useful in scheduling interactive users because it cannot guarantee good response time. The code 
for FCFS scheduling is simple to write and understand. One of the major drawback of this scheme 
is that the average time is often quite long. The First-Come-First-Served algorithm is rarely used 
as a master scheme in modern operating systems but it is often embedded within other schemes.

Calculating Average Waiting Time
For every scheduling algorithm, Average waiting time is a crucial parameter to judge it's 
performance. AWT or Average waiting time is the average of the waiting times of the processes 
in the queue, waiting for the scheduler to pick them for execution.
Lower the Average Waiting Time, better the scheduling algorithm.
Consider the processes P1, P2, P3, P4 given in the below table, arrives for execution in the same 
order, with Arrival Time 0, and given Burst Time, let's find the average waiting time using the 
FCFS scheduling algorithm

![image](https://user-images.githubusercontent.com/57552973/184399363-d5f003ce-8698-4e7e-bc81-c6eeb1d2abad.png)


Output of the .py file - 
![image](https://user-images.githubusercontent.com/57552973/187034211-f5e90a8a-ff3c-4ea4-8f5d-eb01219821f7.png)

