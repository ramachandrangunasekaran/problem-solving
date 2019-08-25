# PROBLEM SOLVING

## Problem Statement

A manufacturer purchases delicate components that must be shipped in expensive custom containers. The supplier agrees to provide a free container of the components in return for the return of a number of shipping containers. Determine the maximum number of containers the manufacturer can purchase, assuming each container is immediately emptied and returned for credit.

**For example,**  start with a budget n=4 units of currency to buy containers at cost = 1 unit each. The number of empty containers to return for a free full container is m = 2. First, buy 4 containers for the entire budget. Turn in those 4 containers for 2 more. Turn in those 2 containers for one more. At this point, there are not enough funds or containers to receive another. In total, 4 + 2 + 1 = 7 containers were received. 

## Function Description
Complete the function maximumContainers in the editor below. For each test case the function must print an integer, the maximum number of containers the manufacturer can obtain, each on a new line. No return value is expected.
 
maximumContainers has the following parameter(s):
    **scenarios:** a string array where each string contains three space-separated integers, n, cost, and m, the starting budget, the price of a full container, and the number of containers that can be turned in for a full container, respectively.
 
```
Constraints
1 ≤ t ≤ 103
2 ≤ n ≤ 105
1 ≤ cost ≤ n
2 ≤ m ≤ n
```

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.
 
The first line contains an integer t, the number of test cases.
Each of the next t lines contains three space-separated integers, n, cost, and m.

### Sample Case 0
```
Sample Input 0
3
10 2 5
12 4 4
6 2 2
 
Sample Output 0
6
3
5
```
#### Explanation 0

There are 3 test cases:

Spend 10 units currency on 5 containers at 2 units each. Turn in 5 containers for another one.
Spend 12 units on 3 containers at 4 units. There aren't enough containers to turn in.
Spend 6 units on 3 containers at 2 units. Turn in 2 of the containers for a 4th container leaving 1 old and 1 new container. Turn those 2 in for 1 more container.

### Sample Case 1
```
Sample Input 1
2
8 4 2
7 2 3
 
Sample Output 1
3
4
```

#### Explanation 1
 
There are 2 test cases:

Spend 8 units currency on 2 containers at 4 units each. Turn in 2 containers for another one.
Spend 6 units on 3 containers at 2 units. Turn in 3 containers for another one. 1 unit of currency is left over.


#### To Run the solution:

```
python runner.py

```