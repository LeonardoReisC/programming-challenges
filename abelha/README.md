Maja is a bee. She lives in a bee hive with thousands of other bees. This bee hive consists of many
hexagonal honey combs where the honey is stored in.
But bee Maja has a problem. Willi told her where she can meet him, but because Willi is a male
drone and Maja is a female worker they have different coordinate systems.

|  |  |
|---------------------------|----------------------------|
| **Maja’s Coordinate System**<br>Maja who often flies directly to a special honey comb has laid an advanced two dimensional grid over the whole hive.<br>![Maja's Hive](../images/majas.png) | **Willi’s Coordinate System**<br>Willi who is more lazy and often walks around just numbered the cells clockwise starting from 1 in the middle of the hive.<br>![Willi's Hive](../images/willis.png) |

Help Maja to convert Willi’s system to hers. Write a program which for a given honey comb number
gives the coordinates in Maja’s system.

## Input

The input file contains one or more integers which represent Willi’s numbers. Each number stands on
its own in a separate line, directly followed by a newline. The honey comb numbers are all less than
100 000.

## Output

You should output the corresponding Maja coordinates to Willi’s numbers, each coordinate pair on a
separate line.

## Sample Input

```
1
2
3
4
5
```

## Sample Output

```
0 0
0 1
-1 1
-1 0
0 -1
```

***
