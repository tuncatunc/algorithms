# Problem

## Description
Given an N X M matrix, where ai, j = 1 denotes the cell is not empty, ai, j = 0 denotes the cell is empty and ai, j = 2, denotes that you are standing at that cell. You can move vertically up or down and horizontally left or right to any cell which is empty. The task is to find the minimum number of steps to reach any boundary edge of the matrix. Print -1 if not possible to reach any of the boundary edges.

Note: There will be only one cell with value 2 in the entire matrix.

```
Input: matrix[] = {1, 1, 1, 0, 1}
                  {1, 0, 2, 0, 1} 
                  {0, 0, 1, 0, 1}
                  {1, 0, 1, 1, 0} 

Output: 2
Move to the right and then move 
upwards to reach the nearest boundary
edge. 

Input: matrix[] = {1, 1, 1, 1, 1}
                  {1, 0, 2, 0, 1} 
                  {1, 0, 1, 0, 1}
                  {1, 1, 1, 1, 1}
Output: -1 
```


## URL
https://www.geeksforgeeks.org/minimum-steps-to-reach-any-of-the-boundary-edges-of-a-matrix-set-2/