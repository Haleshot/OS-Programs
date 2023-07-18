# Shortest Job First (SJF) Scheduling Algorithm

The Shortest Job First (SJF) scheduling algorithm is a non-preemptive scheduling algorithm that selects the process with the smallest burst time from the ready queue for execution. It aims to minimize the average waiting time among all scheduling algorithms. However, it may cause starvation if shorter processes keep arriving, which can be mitigated using the concept of aging. While it is practically infeasible for the operating system to know the exact burst times, SJF can be used in specialized environments where accurate estimates of running time are available.

## Table of Contents
- [Characteristics of SJF Scheduling](#characteristics-of-sjf-scheduling)
- [Algorithm](#algorithm)
- [Advantages](#advantages)
- [Disadvantages](#disadvantages)
- [Calculating Average Waiting Time](#calculating-average-waiting-time)
- [Example](#example)
- [Output](#output)

## Characteristics of SJF Scheduling
Here are the important characteristics of SJF Scheduling:
- Shortest Job First has the advantage of having a minimum average waiting time among all scheduling algorithms.
- It is a Greedy Algorithm.
- It may cause starvation if shorter processes keep coming. This problem can be solved using the concept of aging.
- It is practically infeasible as the operating system may not know the burst times and therefore may not sort them. However, there are methods to estimate the execution time for a job based on previous execution times.
- SJF can be used in specialized environments where accurate estimates of running time are available.

## Algorithm
The SJF scheduling algorithm follows these steps:
1. Sort all the processes according to their arrival time.
2. Select the process with the minimum arrival time and minimum burst time.
3. After completing the selected process, create a pool of processes that arrive afterward until the completion of the previous process. Select the process with the minimum burst time from this pool.

## Advantages
- Reduces the average waiting time significantly.
- Better compared to First-Come-First-Serve (FCFS) scheduling.
- Helps in achieving optimal turnaround time.

## Disadvantages
- It could cause starvation in some cases, which can be solved by using aging techniques.
- The execution time of a process is a prerequisite, which is hard to predict.
- Cannot be used for short-term CPU scheduling since predicting the CPU burst time is challenging.

## Calculating Average Waiting Time
Average waiting time (AWT) is a crucial parameter to evaluate the performance of any scheduling algorithm. AWT represents the average waiting time of processes in the queue, waiting for the scheduler to select them for execution.

## Example
Consider the following example with five jobs (P1, P2, P3, P4, and P5) having their arrival time and burst time given:

![Example Processes 1](https://user-images.githubusercontent.com/57552973/184400549-31fb2a38-12d9-434a-9b1a-0038bfdd2bc6.png)

![Example Processes 2](https://user-images.githubusercontent.com/57552973/184400622-95619498-fec1-44d1-82a9-0e9f1c61242f.png)

## Output
The output of the `.py` file implementing the SJF scheduling algorithm is shown below:

![SJF Output 1](https://user-images.githubusercontent.com/57552973/184400016-9f123361-077e-43fb-a235-6b060f9ffea5.png)

![SJF Output 2](https://user-images.githubusercontent.com/57552973/184400117-82cfa672-932a-42f2-b524-fd9121506d84.png)

Please refer to the [SJF Repository](https://github.com/your-repo-link) for the complete code implementation.

For more information on scheduling algorithms and their analysis, please check the related files and code in this repository.