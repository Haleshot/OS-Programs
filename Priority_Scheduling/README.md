# Priority Scheduling Algorithm

The Priority Scheduling algorithm assigns a priority number to each process, determining the order in which they are scheduled. The priority can be based on different criteria, depending on the system. Some systems consider a lower number to indicate higher priority, while others consider a higher number to indicate higher priority. The process with the highest priority among the available processes is given the CPU.

## Table of Contents
- [Introduction](#introduction)
- [Implementation](#implementation)
- [Advantages](#advantages)
- [Disadvantages](#disadvantages)
- [Calculating Average Waiting Time](#calculating-average-waiting-time)
- [Pictorial Representation](#pictorial-representation)
- [Output](#output)

## Introduction
The Priority Scheduling algorithm allows processes to be scheduled based on their assigned priority. The process with the highest priority is given the CPU first, followed by processes with lower priority. This algorithm helps determine the relative importance of each process based on its assigned priority.

## Implementation
To implement the Priority Scheduling algorithm, follow these steps:
1. Input the processes with their arrival time, burst time, and priority.
2. Schedule the first process based on the lowest arrival time. If multiple processes have the same arrival time, the one with the higher priority is scheduled first.
3. Schedule the remaining processes based on their arrival time and priority. If two processes have the same priority, sort them based on their process number.
4. Once all the processes have arrived, schedule them based on their priority.

## Advantages
- Helps understand the relative importance of each process due to the explicit mention of priority.
- Efficient algorithm for low-end machines with limited resources since the execution order is known beforehand.

## Disadvantages
- Ambiguity may arise while assigning priorities to each process.
- Processes with low priority may experience starvation if high priority processes utilize the CPU inefficiently or for extended periods.

## Calculating Average Waiting Time
Average waiting time (AWT) is a crucial parameter to evaluate the performance of any scheduling algorithm. AWT represents the average waiting time of processes in the queue, waiting for the scheduler to select them for execution.

Consider the following example, where five jobs (P1, P2, P3, P4, P5) have their arrival time and burst time given:

![Example Processes](https://user-images.githubusercontent.com/57552973/187022770-db1b78b4-8e11-4dd5-95ea-5fd8bb50da34.png)

To calculate the average waiting time, use the provided burst time and arrival time:

Average Waiting Time = 10.8

Turnaround Time = 8.2

## Pictorial Representation
The pictorial representation of the Priority Scheduling algorithm is shown below:

![Pictorial Representation](https://user-images.githubusercontent.com/57552973/187022777-05cf9d3c-99be-4293-9d87-ab3b385b88d2.png)

## Output
The output of the `.py` file implementing the Priority Scheduling algorithm is shown below:

![Priority Scheduling Output](https://user-images.githubusercontent.com/57552973/187023558-7bf20e79-c3c1-42dc-a522-071ce95356ff.png)

![Priority Scheduling Output 2](https://user-images.githubusercontent.com/57552973/187023575-e68fa250-580f-45d1-82fa-78b84c887ade.png)

Please refer to the [Priority Scheduling Repository](https://github.com/your-repo-link) for the complete code implementation.

For more information on scheduling algorithms and their analysis, please check the related files and code in this repository.