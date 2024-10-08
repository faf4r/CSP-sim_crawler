

## 问题描述



小明在玩一个电脑游戏，游戏在一个n&times;m的方格图上进行，小明控制的角色开始的时候站在第一行第一列，目标是前往第n行第m列。

方格图上有一些方格是始终安全的，有一些在一段时间是危险的，如果小明控制的角色到达一个方格的时候方格是危险的，则小明输掉了游戏，如果小明的角色到达了第n行第m列，则小明过关。第一行第一列和第n行第m列永远都是安全的。

每个单位时间，小明的角色必须向上下左右四个方向相邻的方格中的一个移动一格。

经过很多次尝试，小明掌握了方格图的安全和危险的规律：每一个方格出现危险的时间一定是连续的。并且，小明还掌握了每个方格在哪段时间是危险的。

现在，小明想知道，自己最快经过几个时间单位可以达到第n行第m列过关。



## 输入格式



输入的第一行包含三个整数n, m, t，用一个空格分隔，表示方格图的行数n、列数m，以及方格图中有危险的方格数量。

接下来t行，每行4个整数r, c, a, b，表示第r行第c列的方格在第a个时刻到第b个时刻之间是危险的，包括a和b。游戏开始时的时刻为0。输入数据保证r和c不同时为1，而且当r为n时c不为m。一个方格只有一段时间是危险的（或者说不会出现两行拥有相同的r和c）。



## 输出格式



输出一个整数，表示小明最快经过几个时间单位可以过关。输入数据保证小明一定可以过关。



## 样例输入
```
3 3 3
2 1 1 1
1 3 2 10
2 2 2 10
```
## 样例输出
```
6
```
## 样例说明

第2行第1列时刻1是危险的，因此第一步必须走到第1行第2列。
第二步可以走到第1行第1列，第三步走到第2行第1列，后面经过第3行第1列、第3行第2列到达第3行第3列。

## 评测用例规模与约定

前30%的评测用例满足：0 &lt; n, m &le; 10，0 &le; t &lt; 99。

所有评测用例满足：0 &lt; n, m &le; 100，0 &le; t &lt; 9999，1 &le; r &le; n，1 &le; c &le; m，0 &le; a &le; b &le; 100。

&nbsp;