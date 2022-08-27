In Priority scheduling, there is a priority number assigned to each process.
In some systems, the lower the number, the higher the priority. While, in the others, the higher the number, the higher will be the priority.
The Process with the higher priority among the available processes is given the CPU.


Implementation –  
First input the processes with their arrival time, burst time and priority. 
First process will schedule, which have the lowest arrival time, if two or more processes will have lowest arrival time, then whoever has higher priority will schedule first. 

Now further processes will be schedule according to the arrival time and priority of the process. (Here we are assuming that lower the priority number having higher priority). If two process priority are same then sort according to process number. 
Note: In the question, They will clearly mention, which number will have higher priority and which number will have lower priority. 
Once all the processes have been arrived, we can schedule them based on their priority. 

Advantages - 
  Helps us understand the relative importance of each process due to explicit mention of priority to each process. 
  Efficient algorithm for low end machines with limited resources since the order of execution is known beforehand. 

Disadvantages – 
  Some ambiguity maybe present while assigning the priority for each process. 
  It could lead to starvation for processes having low priority compared to others (if high priority processes utilize the CPU inefficiently or for long periods of time).
  

The processes with higher priority are executed first followed by the processes with lower priority. 
Consider the set of 5 processes whose arrival time and burst time are given below- 

![image](https://user-images.githubusercontent.com/57552973/187022770-db1b78b4-8e11-4dd5-95ea-5fd8bb50da34.png)

![image](https://user-images.githubusercontent.com/57552973/187022777-05cf9d3c-99be-4293-9d87-ab3b385b88d2.png)

Calculating Average Waiting Time 

For every scheduling algorithm, Average waiting time is a crucial parameter to judge it's performance. AWT or Average waiting time is the average of the waiting times of the processes in the queue, waiting for the scheduler to pick them for execution. 
Example 
In the following example, there are five jobs named as P1, P2, P3, P4 and P5. Their arrival time and burst time are given in the table below.

![image](https://user-images.githubusercontent.com/57552973/187022642-2365ee58-e22d-4b2f-8bfc-1762ae44af74.png)

Average Waiting time = 10.8 

Turnaround time = 8.2 

Output of the .py File - 
![image](https://user-images.githubusercontent.com/57552973/187023558-7bf20e79-c3c1-42dc-a522-071ce95356ff.png)
![image](https://user-images.githubusercontent.com/57552973/187023575-e68fa250-580f-45d1-82fa-78b84c887ade.png)


