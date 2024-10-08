


**时间限制：** 1.0 秒 


**空间限制：** 512 MB






## 题目背景

独立硬盘冗余阵列（RAID, Redundant Array of Independent Disks）是一种现代常用的存储技术。它以一定形式，将数据分散、冗余地存储在多个磁盘上，从而当部分磁盘不可用时，仍然能保证数据的完整性。RAID 分为多种级别，提供了丰富的冗余性和性能的搭配方案选择。本题中，我们主要研究一种十分常见的 RAID 级别—— RAID5。

### RAID5 基本算法

RAID5 可以提供一块硬盘的冗余度，即阵列中至多允许有一块硬盘故障而不丢失数据。RAID5 的基本原理是异或运算（$\oplus$）。考虑数 $$a_1, a_2, \dots, a_{n}$$
今令 $$p = a_1 \oplus a_2 \oplus \dots \oplus a_{n} = \bigoplus_{i=1}^{n}{a_i}$$
易知 $$a_k = p \oplus \bigoplus_{i=1\dots n, I\not=k}{a_i}$$
上式意味着，在 $p$ 与 $a_1 \dots a_{n}$ 这 $(n+1)$ 个数中，由任意 $n$ 个可以推知其余的一个，这便是 RAID5 的基本原理。

由此，一种朴素的 $(n+1)$ 块盘的存储方案是：将数据分块存放在前 $n$ 块盘中，然后在第 $(n+1)$ 块盘中存储前 $n$ 块盘上相应位置处数据的异或结果。这种方案的确可以实现 1 块硬盘的冗余度，但是很显然，如果所有的硬盘都没有发生故障，当读取数据时，最后一块盘完全不会被利用起来，在性能上较为浪费。因此现行 RAID5 的存储方式采取了条带（stripe）化的方式，将被存储的数据均匀分布在所有磁盘上，从而提高了读写的性能。

### 硬盘及其组织

现代的硬盘可以被看作是一种能**按块**随机读写的持久化存储装置。大多数硬盘每块的大小是 512 字节或 4096 字节，硬盘上所有的块，从 0 开始连续编号。每次对硬盘的读写，都应该以块为单位，在读写时，传入被读写的块的编号，一次读写一整个块。

RAID 装置，可以将多个硬盘组织成一定的存储结构。在上层软件看起来，被组织后的存储结构好像一整块大硬盘。因此上层软件向 RAID 发送的读写指令里面的块的编号，应当被 RAID 装置进行适当地转换，反映到对具体某个硬盘或某几个硬盘的操作上。

### 条带化与数据布局

在 RAID5 中，一个重要的参数是条带大小。**条带**是指连续、等大的数据块，是 RAID5 进行数据布局的基本单元。例如，假设某硬盘有 1024 个块，条带大小是 8 个块，那么这个硬盘一共被分为 128 个条带，编号在 $[0,8)$ 的块在第一个条带上，编号 $[8,16)$ 的块在第二个条带上，依次类推。一般地，如果将条带也从 0 开始编号，且条带大小为 $s$ 个块，那么编号为 $b$ 的块所在的条带编号是 $\lfloor\frac{b}{s}\rfloor$。

对于有 $(n+1)$ 块硬盘的 RAID5 存储，我们利用每块硬盘上编号为 $k$ 的条带，存储编号为 $[kn, (k+1)n)$ 的条带（共 $n$ 个）。这 $n$ 个条带具体的存储方法是：先按一定规则，选中某个硬盘作为校验盘，存储这 $n$ 个条带的异或和，然后再按一定顺序，将这 $n$ 个条带存入其余的硬盘中。选中校验盘的规则是：随着 $k$ 递增，从最后一块盘开始，依次递减地选取校验盘，直到第一块盘为止，然后重新从最后一块盘开始。存入数据条带的顺序是：从被选中的校验盘的下一块盘开始，依次存入数据条带，直到最后一块盘为止，然后从第一块盘开始，依次存入其余的数据条带，直到被选中的校验盘的上一块盘为止。

我们以 $n=3$ 为例，示意性地给出条带的布局情况。

 <img src="attachments/CSP201903-3-0.png" alt="img" align="middle" width="40%"/> 

## 题目描述

传说中，每个成功的运维背后，都坏着一打 RAID 阵列。有一天，汉东省政法大学丁香学生公寓楼下的外卖又被偷了！正在调取监控录像的关键时刻，汉东省政法大学监控中心的 RAID5 阵列发生了故障！老师拿来了一摞同一个型号的“圆邪”牌硬盘，找到了你。作为成功的运维，你能不能帮忙恢复里面的数据呢？为了不辱使命，你立刻使用搜猫搜索得知，该型号硬盘的块大小是 4 字节。当你正打算撸起袖子加油码代码的时候，电话响了，老师焦急的声音从听筒里传来：“哎呀呀，我好像把硬盘的顺序弄乱了……”

## 输入格式

从标准输入读入数据。

输入的第一行包含三个正整数 $n$（$n \geq 2$）、$s$ 和 $l$，表示阵列中硬盘的数目、阵列的条带大小（单位：块）和现存的硬盘数目。

接下来的 $l$ 行，每行包含由空格分开的一个非负整数和一个不含空格，长度相等且为 8 的整数倍的字符串。该整数为从零开始的这个硬盘的顺序号。该字符串仅包含数字 `0`～`9` 和大写字母 `A`～`F`，每两个字符构成一个 16 进制数字，表示一个字节的硬盘内容。输入硬盘集合保证：向该硬盘集合补充若干适当内容的硬盘，即可使它们恰好组成一个合法的、数据没有差错的 RAID5 阵列。输入数据保证：阵列的条带大小能整除每块硬盘的大小。

接下来的一行包含一个正整数 $m$，表示读取操作的数目。

接下来的 $m$ 行，每行表示一个读取操作，包括一个非负整数 $b_i$，表示要读取的块的编号。

## 输出格式

输出到标准输出。

输出包含 $m$ 行。

对于每一个读操作，产生一行输出。如果该读操作能进行，或能由现存的硬盘数据推算出来，则输出长度为 8 的字符串，该字符串仅包含数字 `0`～`9` 和大写字母 `A`～`F`，每两个字符构成一个 16 进制数字，表示读取到的数据块的内容。如果该读操作由于下列情形之一无法进行，则输出一个减号（`-`）：

* 阵列不完整，且被读取的块所在的硬盘缺失，且该数据无法由现存的硬盘数据推算出来；
* 指定的块超出阵列总长度。








## 样例1输入

```plain
2 1 2
0 000102030405060710111213141516172021222324252627
1 000102030405060710111213141516172021222324252627
2
0
1

```



## 样例1输出

```plain
00010203
04050607
```


## 样例1解释

由题意，给出的 RAID5 阵列由两块盘组成，条带大小是 1 块（4 字节）长，并给出了两块盘的数据。注意到当 RAID5 的阵列中只有两块盘时，有 $p = a_1$，因此两块盘中数据是相同的，都是 RAID 阵列中的内容，因此可以任取一块盘进行读取操作。








## 样例2输入

```plain
3 2 2
0 000102030405060710111213141516172021222324252627
1 A0A1A2A3A4A5A6A7B0B1B2B3B4B5B6B7C0C1C2C3C4C5C6C7
2
2
5
```



## 样例2输出

```plain
A0A1A2A3
A0A0A0A0
```


## 样例2解释

由题意，给出的 RAID5 阵列由三块盘组成，条带大小是 2 块（8 字节）长，并给出了 0 号、1 号盘的数据，缺失 2 号盘，因此整个 RAID5 阵列的布局情况如图所示。

 <img src="attachments/CSP201903-3-1.png" alt="img" align="middle" width="40%"/> 

图中，用虚线隔开的长方形表示一个块，连续的两个长方形组成的正方形表示一个条带。当读取编号为 2 的块时，该数据位于编号为 1 的盘的编号为 0 的块，因此结果是 `A0A1A2A3`；当读取编号为 5 的块时，该数据位于编号为 2 的盘的编号为 3 的块，该盘缺失，因此需要用其余两块盘相应位置处的数据进行异或运算得到 `14151617` $\oplus$ `B4B5B6B7` $=$ `A0A0A0A0`。

## 子任务

 
	


<table class="table table-bordered"><thead><tr><th rowspan="1">子任务编号</th><th rowspan="1">$n$</th><th rowspan="1">$s$</th><th rowspan="1">$l$</th><th rowspan="1">$m$</th><th rowspan="1">$b_i$</th><th rowspan="1">每块硬盘数据长度</th><th rowspan="1">输入硬盘是否有序</th></tr></thead><tbody><tr><td rowspan="1">1</td><td rowspan="1">$2\leq n \leq 2$</td><td rowspan="5">$< 10^{3}$</td><td rowspan="3">$=n$</td><td rowspan="5">$< 10^{3}$</td><td rowspan="1">$< 2^{31}$</td><td rowspan="4">$< 10^{1}\mathrm{KiB}$</td><td rowspan="3">有序</td></tr><tr><td rowspan="1">2,3</td><td rowspan="1">$2\leq n \leq 10$</td><td rowspan="1">不超出总容量</td></tr><tr><td rowspan="1">4,5</td><td rowspan="3">$2\leq n \leq 10^{3}$</td><td rowspan="3">$< 2^{31}$</td></tr><tr><td rowspan="1">6,7</td><td rowspan="1">$n-1 \leq l \leq n$</td><td rowspan="2">无序</td></tr><tr><td rowspan="1">8,9,10</td><td rowspan="1">$l \leq n$</td><td rowspan="1">$< 40.0\mathrm{KiB}$</td></tr></tbody></table> 
