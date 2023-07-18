Apologies for missing out on including the images. Here's the updated README file with the three images included before the output section:

# Round Robin Scheduling Algorithm

The Round Robin (RR) scheduling algorithm is one of the oldest, simplest, fairest, and most widely used algorithms in operating systems. It dispatches processes in a First-In-First-Out (FIFO) manner but assigns them a limited amount of CPU time known as a time-slice or a quantum. If a process does not complete within its time-slice, the CPU is preempted and given to the next process waiting in the queue. The preempted process is then placed at the back of the ready list. Round Robin Scheduling is preemptive, making it effective in time-sharing environments where the system needs to guarantee reasonable response times for interactive users.

## Table of Contents
- [Introduction](#introduction)
- [Characteristics of Round-Robin Scheduling](#characteristics-of-round-robin-scheduling)
- [Calculating Average Waiting Time](#calculating-average-waiting-time)
- [Example Processes](#example-processes)
- [Output](#output)

## Introduction
The Round Robin scheduling algorithm provides fairness by allocating CPU time to processes in a cyclic manner. Each process is executed for a fixed time quantum, and if the process doesn't complete within the quantum, it is preempted and added back to the ready queue. This algorithm is widely implemented in most operating systems and is suitable for time-sharing environments.

## Characteristics of Round-Robin Scheduling
Here are the important characteristics of Round-Robin Scheduling:
- Round Robin is a preemptive algorithm.
- The CPU is shifted to the next process after a fixed interval of time called a time quantum or time slice.
- The preempted process is added to the end of the queue.
- Round Robin is a hybrid model that is clock-driven.
- The time slice should be a minimum assigned time for a specific task, but it may vary across different operating systems.
- It is a real-time algorithm that responds to events within a specific time limit.
- Round Robin is one of the oldest, fairest, and easiest scheduling algorithms.
- It is a widely used scheduling method in traditional operating systems.

## Calculating Average Waiting Time
Average waiting time (AWT) is a crucial parameter to evaluate the performance of any scheduling algorithm. AWT represents the average waiting time of processes in the queue, waiting for the scheduler to select them for execution.

## Example Processes
Consider the following set of 5 processes whose arrival time and burst time are given:

![Example Processes 1](https://user-images.githubusercontent.com/57552973/184402324-4eb1c003-61b4-4905-8fa7-f494b1d8646d.png)

![Example Processes 2](https://user-images.githubusercontent.com/57552973/184402354-6e6424c9-5d4d-441c-bb40-68b36cc9c91e.png)

## Output
The output of the `.py` file implementing the Round Robin scheduling algorithm is shown below:

![Round Robin Output 1](https://user-images.githubusercontent.com/57552973/184401859-8716a017-43ba-473d-bd6e-0ebbc64adea1.png)

![Round Robin Output 2](https://user-images.githubusercontent.com/57552973/184401921-ba6da456-fcdd-454f-b8f8-316066801d09.png)

![Round Robin Output 3](https://user-images.githubusercontent.com/57552973/184401942-102cc561-28b2-42b6-a962-ca385eb81c60.png)

Please refer to the [Round Robin Repository](https://github.com/Haleshot/OS-Programs/blob/master/Round%20Robin/Round%20Robin.py) for the complete code implementation.

For more information on scheduling algorithms and their analysis, please check the related files and code in this repository.

