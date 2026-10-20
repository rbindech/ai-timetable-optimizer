# Timetabling benchmark — key results

| Dataset | Algorithm | Success | Success rate | Mean conflicts | Mean time (s) |
| --- | --- | --- | --- | --- | --- |
| 20 rooms | Genetic Algorithm | 5/5 | 100% | 0.00 | 1.38 |
| 20 rooms | Hill Climbing | 5/5 | 100% | 0.00 | 6.91 |
| 20 rooms | DFS + Backtracking | 5/5 | 100% | 0.00 | 0.22 |
| 15 rooms | Genetic Algorithm | 5/5 | 100% | 0.00 | 7.78 |
| 15 rooms | Hill Climbing | 4/5 | 80% | 0.20 | 12.10 |
| 15 rooms | DFS + Backtracking | 5/5 | 100% | 0.00 | 0.22 |
| 12 rooms | Genetic Algorithm | 3/5 | 60% | 0.60 | 22.02 |
| 12 rooms | Hill Climbing | 0/5 | 0% | 2.80 | 26.51 |
| 12 rooms | DFS + Backtracking | 0/5 | 0% | N/A | 30.00 |

*Mean time includes all runs, including unsuccessful ones. N/A means no complete timetable was returned; 999 is a failure marker, not a measured conflict count.*
