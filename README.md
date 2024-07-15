# Multiple-Traveling-Salesman-Problem

The Multiple Traveling Salesman Problem (mTSP) is a generalization of the Traveling Salesman Problem (TSP) in which more than one salesman is allowed. MTSP involves assigning M salesmen to N cities, and each city must be visited by a salesman while requiring a minimum total cost.

### Solution:
- Find centroid city (the city that has the lowest sum of distances to every other city).
- Calculate the Euclidean distance between each city and its distance from the centroid.
- Connect each city to centroid
- Begin with the city closest to the centroid and proceed to the farthest, connecting each city to its two nearest neighbors. Ensure that the connections between cities do not intersect with one another.
- Divide the number of cities (N) by the number of salesmen (M). Each salesman travel N / M cities.

### Results:
| Instance         | N | M | K | Optimal (in theory) solution  | Found solution |
| :---------------: | - | - | - | :---------------------: | :----------------: |
| 1 | 13 | 1 | 13 | 3071 | 3875 |
| 2 | 17 | 1 | 17 | 3948 | 4412 |
| 3 | 19 | 1 | 19 | 4218 | 4933 |
| 4 | 32 | 3 | 11 | 5841 | 5947 |
| 5 | 48 | 3 | 16 | 6477 | 6785 |
| 6 | 60 | 3 | 20 | 6786 | 7066 |
| 7 | 72 | 5 | 15 | 8618 | 10172 |
| 8 | 84 | 5 | 17 | 9565 | 8774 |
| 9 | 92 | 5 | 19 | 9586 | 10473 |

### How to run:
- Create virtual environment: `python3 -m venv .venv`
- Activate it:
  - For MACOS: `.venv/bin/activate`
  - For Windows: `.venv/Scripts/activate`
- Install dependencies:
`pip install -r requirements.txt`
- Run `main.py`

