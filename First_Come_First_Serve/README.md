# First-Come-First-Serve (FCFS) Algorithm

The First-Come-First-Serve (FCFS) algorithm is the simplest scheduling algorithm in operating systems. It dispatches processes based on their arrival time, placing them on the ready queue. FCFS is a non-preemptive scheduling discipline, which means that once a process has the CPU, it will run to completion.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Calculating Average Waiting Time](#calculating-average-waiting-time)
- [Output](#output)

## Introduction
The FCFS scheduling algorithm is fair in terms of both formal and human sense of fairness. However, it has a drawback in that long jobs make short jobs wait, and unimportant jobs make important jobs wait. This algorithm is more predictable compared to most other schemes as it offers time.

## Features
- Simple and easy to understand code.
- Predictable behavior.
- Not suitable for scheduling interactive users as it cannot guarantee good response time.
- Often embedded within other scheduling schemes rather than used as a standalone master scheme in modern operating systems.

## Calculating Average Waiting Time
Average waiting time (AWT) is an important parameter to evaluate the performance of any scheduling algorithm. AWT represents the average waiting time of processes in the queue, waiting for the scheduler to select them for execution. The lower the average waiting time, the better the scheduling algorithm.

Consider the following processes with their respective burst times:

| Process | Burst Time |
|---------|------------|
| P1      | 24         |
| P2      | 3          |
| P3      | 3          |
| P4      | 6          |

Using the FCFS scheduling algorithm, we can calculate the average waiting time as follows:

```
Average Waiting Time = (0 + 24 + 27 + 30) / 4 = 20.25
```

Pictorial representation is:
[Pictorial Representation](https://user-images.githubusercontent.com/57552973/184399363-d5f003ce-8698-4e7e-bc81-c6eeb1d2abad.png)

## Output
The output of the `.py` file implementing the FCFS algorithm is shown below:

![FCFS Output](https://user-images.githubusercontent.com/57552973/187034305-6e0b4810-3da7-4f65-8fa4-a5be5488e97a.png)
![FCFS Output 2](https://user-images.githubusercontent.com/57552973/187034211-f5e90a8a-ff3c-4ea4-8f5d-eb01219821f7.png)

Please refer to the [FCFS Repository](https://github.com/Haleshot/OS-Programs/blob/master/First_Come_First_Serve/First_Come_First_Serve.py) for the complete code implementation.

For more information on scheduling algorithms and their analysis, please check the related files and code in this repository.
