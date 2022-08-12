One of the oldest, simplest, fairest and most widely used algorithm is round robin (RR). In the 
round robin scheduling, processes are dispatched in a FIFO manner but are given a limited amount 
of CPU time called a time-slice or a quantum. If a process does not complete before its CPU-time 
expires, the CPU is pre-empted and given to the next process waiting in a queue. The pre-empted 
process is then placed at the back of the ready list. Round Robin Scheduling is pre-emptive (at the 
end of time-slice) therefore it is effective in time sharing environments in which the system needs 
to guarantee reasonable response times for interactive users.
The only interesting issue with round robin scheme is the length of the quantum. Setting the 
quantum too short causes too many context switches and lower the CPU efficiency. On the other 
hand, setting the quantum too long may cause poor response time and approximates FCFS. In any 
event, the average waiting time under round robin scheduling is often quite long.

Round Robin scheduling algorithm is one of the most popular scheduling algorithm which can 
actually be implemented in most of the operating systems. This is the preemptive version of first 
come first serve scheduling. The Algorithm focuses on Time Sharing. In this algorithm, every 
process gets executed in a cyclic way. A certain time slice is defined in the system which is called 
time quantum. Each process present in the ready queue is assigned the CPU for that time quantum, if the execution of the process is completed during that time then the process will terminate else 
the process will go back to the ready queue and waits for the next turn to complete the execution.

Characteristics of Round-Robin Scheduling
Here are the important characteristics of Round-Robin Scheduling:
• Round robin is a pre-emptive algorithm
• The CPU is shifted to the next process after fixed interval time, which is called time 
quantum/time slice.
• The process that is preempted is added to the end of the queue.
• Round robin is a hybrid model which is clock-driven
• Time slice should be minimum, which is assigned for a specific task that needs to be 
processed. However, it may differ OS to OS.
• It is a real time algorithm which responds to the event within a specific time limit.
• Round robin is one of the oldest, fairest, and easiest algorithm.
• Widely used scheduling method in traditional OS

Calculating Average Waiting Time
For every scheduling algorithm, Average waiting time is a crucial parameter to judge its 
performance. AWT or Average waiting time is the average of the waiting times of the processes 
in the queue, waiting for the scheduler to pick them for execution.
Example
In the following example, there are five jobs named as P1, P2, P3, P4 and P5. Their arrival time 
and burst time are given in the table below.
Consider the set of 5 processes whose arrival time and burst time are given below - 
![image](https://user-images.githubusercontent.com/57552973/184402324-4eb1c003-61b4-4905-8fa7-f494b1d8646d.png)
![image](https://user-images.githubusercontent.com/57552973/184402354-6e6424c9-5d4d-441c-bb40-68b36cc9c91e.png)




Time Quantum is the time allocated to a process for which it is allowed to run/ be 
executed by the CPU. This helps in No starvation scenario since each process gets its 
time for execution due to cyclic nature of Round Robin due to the Time Quantum 
constraint.
• Hence, a process executes completely (for the entirety of its burst time), if its burst time 
is less than the Time Quantum. Otherwise, it executes till the Time Quantum limit and 
waits for its time to get executed for the remainder of its burst time.


Advantages -
• No starvation scenario since each process gets its time for execution due to cyclic nature 
of Round Robin.
• Every process gets executed by the CPU due to the Time Quantum constraint.
Disadvantages -
• If the Time Quantum is set too low, it lowers the efficiency of the CPU and increases 
overhead. Same scenario if the Time Quantum is set high (poor efficiency of execution 
for short processes).
• The Average waiting Time for processes for execution can get long is certain situations.

Output - 
![image](https://user-images.githubusercontent.com/57552973/184401859-8716a017-43ba-473d-bd6e-0ebbc64adea1.png)
![image](https://user-images.githubusercontent.com/57552973/184401921-ba6da456-fcdd-454f-b8f8-316066801d09.png)
![image](https://user-images.githubusercontent.com/57552973/184401942-102cc561-28b2-42b6-a962-ca385eb81c60.png)
