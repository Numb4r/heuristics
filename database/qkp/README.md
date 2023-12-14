# 0-1 Quadratic Knapsak Problem

This package contains the randomly generated (QKP) instances solved in the two following references:
- Alain Billionnet and Eric Soutif, "Using a Mixed Integer Programming Tool for Solving the 0-1 Quadratic Knapsack Problem", INFORMS J. on Comput vol. 16(2): 188-197, 2004.
- Alain Billionnet and Eric Soutif,"An exact method for the 0-1 Quadratic Knapsack Problem based on Lagrangian Decomposition", European J. of Operational Research vol. 157(3): 565-575, 2004.

## Instance format

Given the following parameters:
- `n`: the number of objects.
- `c[i]`: the individual profit for the i-th object (linear coefficients).
- `c[i][j]`: the profit for the pair of objects `i` and `j` (quadratic coefficients).
- `a[i]`: the weight of the i-th object.
- `b`: the capacity of the knapsack.

Each (QKP) instance correspond to a file containing the following informations:

```
instance_name
n
p[1] p[2] p[3] p[4] ... p[n]
p[1][2] p[1][3] p[1][4] ... p[1][n]
p[2][3] p[2][4] ... p[2][n]
p[3][4] ... p[3][n]
... 
p[n-1][n]

constraint_type
b
a[1] a[2] a[3] a[4] ... a[n]

comments
```

The `constraint_type` defines the type of constraints. It is `0` if the constraints are of type <= or `1` if the constraints are an equality constraints. Since we are considering QKP instances, it is always `0`.

The `comments` are some comments about the instance.


## Example of an instance

Here is an example of an instance with 10 objects:

```
r_10_100_13
10
91 78 22 4 48 85 46 81 3 26
55 23 35 44 5 91 95 26 40
92 11 20 43 71 83 27 65
7 57 33 38 57 63 82
100 87 91 83 44 48
69 57 79 89 21
9 40 22 26
50 6 7
71 52
17

0
145
34 33 12 3 43 26 10 2 48 39

Comments

Density : 100.00 %
Seed : 13
```
