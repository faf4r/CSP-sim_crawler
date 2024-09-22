## 问题描述
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">创造一个世界只需要定义一个初状态和状态转移规则。</span><span lang="EN-US"><o:p></o:p></span></p>
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">宏观世界的物体运动规律始终跟物体当前的状态有关，也就是说只要知道物体足够多的状态信息，例如位置、速度等，我们就能知道物体之后任意时刻的状态。</span><span lang="EN-US"><o:p></o:p></span></p>
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">现在小</span><span lang="EN-US">M</span><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">创造了一个简化的世界。</span><span lang="EN-US"><o:p></o:p></span></p>
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">这个世界中，时间是离散的，物理规律是线性的：世界的初始状态可以用一个</span><i><span lang="EN-US">m</span></i><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">维向量</span><b><i><span lang="EN-US">b</span></i></b><sup><span lang="EN-US">(0)</span></sup><span style="font-family:宋体;mso-ascii-font-family:
&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">表示，状态的转移方式用</span><i><span lang="EN-US">m</span></i><span lang="EN-US">&times;</span><i><span lang="EN-US">m</span></i><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">的矩阵</span><b><i><span lang="EN-US">A</span></i></b><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">表示。</span><span lang="EN-US"><o:p></o:p></span></p>
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">若已知这个世界当前的状态是</span><b><i><span lang="EN-US">b</span></i></b><span style="font-family:宋体;mso-ascii-font-family:
&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">，那么下一时刻就等于</span><b><i><span lang="EN-US">b</span></i></b><span style="font-family:宋体;mso-ascii-font-family:
&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">左乘状态转移矩阵</span><b><i><span lang="EN-US">A</span></i></b><span style="font-family:宋体;mso-ascii-font-family:
&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">，即</span><b><i><span lang="EN-US">Ab</span></i></b><span style="font-family:宋体;mso-ascii-font-family:
&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">。</span><span lang="EN-US"><o:p></o:p></span></p>
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">这个世界中，物体的状态也是离散的，也就是说可以用整数表示。再进一步，整数都可以用二进制编码拆分为有限位</span><span lang="EN-US">0</span><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">和</span><span lang="EN-US">1</span><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">。因此，这里的矩阵</span><b><i><span lang="EN-US">A</span></i></b><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">和向量</span><b><i><span lang="EN-US">b</span></i></b><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">的每个元素都是</span><span lang="EN-US">0</span><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">或</span><span lang="EN-US">1</span><span style="font-family:
宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">，矩阵乘法中的加法运算视为异或运算（</span><b><span lang="EN-US">xor</span></b><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">），乘法运算视为与运算（</span><b><span lang="EN-US">and</span></b><span style="font-family:宋体;mso-ascii-font-family:
&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">）。</span><span lang="EN-US"><o:p></o:p></span></p>
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">具体地，设矩阵</span><b><i><span lang="EN-US">A</span></i></b><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">第</span><i><span lang="EN-US">i</span></i><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">行第</span><i><span lang="EN-US">j</span></i><span style="font-family:宋体;mso-ascii-font-family:
&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">列的元素为</span><i><span lang="EN-US">a<sub>i</sub></span></i><sub><span lang="EN-US">, <i>j</i></span></sub><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">，向量</span><b><i><span lang="EN-US">b</span></i></b><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">的第</span><i><span lang="EN-US">i</span></i><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">个元素为</span><i><span lang="EN-US">b<sub>i</sub></span></i><span style="font-family:宋体;
mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">。那么乘法</span><b><i><span lang="EN-US">Ab</span></i></b><span style="font-family:宋体;mso-ascii-font-family:
&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">所得的第</span><span lang="EN-US">k</span><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">个元素为</span><span lang="EN-US"><o:p></o:p></span></p>
<p class="NOI0"><span lang="EN-US">(<i>a<sub>k</sub></i><sub>,1</sub> <b>and</b> <i>b</i><sub>1</sub>) <b>xor</b> (<i>a<sub>k</sub></i><sub>,2</sub> <b>and</b> <i>b</i><sub>2</sub>) <b>xor</b> </span><span lang="EN-US" style="font-family:&quot;Cambria Math&quot;,&quot;serif&quot;;mso-bidi-font-family:&quot;Cambria Math&quot;">⋯</span><span lang="EN-US"> <b>xor</b> (<i>a<sub>k</sub></i><sub>,<i><u>m</u></i></sub> <b>and</b> <i>b<sub>m</sub></i>)<o:p></o:p></span></p>
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">矩阵和矩阵的乘法也有类似的表达。</span><span lang="EN-US"><o:p></o:p></span></p>
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">小</span><span lang="EN-US">M</span><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">发现，这样的矩阵运算也有乘法结合律，例如有</span><b><i><span lang="EN-US">A</span></i></b><span lang="EN-US">(<b><i>Ab</i></b>)=(<b><i>AA</i></b>)<b><i>b</i></b>=<b><i>A</i></b><sup>2</sup><b><i>b</i></b></span><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">。</span><span lang="EN-US"><o:p></o:p></span></p>
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">为了保证自己创造的世界维度不轻易下降，小</span><span lang="EN-US">M</span><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">保证了矩阵</span><b><i><span lang="EN-US">A</span></i></b><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">可逆，也就是说存在一个矩阵</span><b><i><span lang="EN-US">A</span></i></b><sup><span lang="EN-US">-1</span></sup><span style="font-family:宋体;mso-ascii-font-family:
&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">，使得对任意向量</span><b><i><span lang="EN-US">d</span></i></b><span style="font-family:宋体;mso-ascii-font-family:
&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">，都有</span><b><i><span lang="EN-US">A</span></i></b><sup><span lang="EN-US">-1</span></sup><b><i><span lang="EN-US">Ad</span></i></b><span lang="EN-US">=<b><i>d</i></b></span><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">。</span><span lang="EN-US"><o:p></o:p></span></p>
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">小</span><span lang="EN-US">M</span><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">想了解自己创造的世界是否合理，他希望知道这个世界在不同时刻的状态。</span><span lang="EN-US"><o:p></o:p></span></p>
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">具体地，小</span><span lang="EN-US">M</span><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">有</span><i><span lang="EN-US">n</span></i><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">组询问，每组询问会给出一个非负整数</span><i><span lang="EN-US">k</span></i><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">，小</span><span lang="EN-US">M</span><span style="font-family:
宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">希望你帮他求出</span><b><i><span lang="EN-US">A</span></i></b><i><sup><span lang="EN-US">k</span></sup><b><span lang="EN-US">b</span></b></i><span style="font-family:宋体;mso-ascii-font-family:
&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">。</span><span lang="EN-US"><o:p></o:p></span></p>

## 输入格式
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">输入第一行包含一个整数</span><i><span lang="EN-US">m</span></i><span style="font-family:宋体;mso-ascii-font-family:
&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">，表示矩阵和向量的规模。</span><span lang="EN-US"><o:p></o:p></span></p>
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">接下来</span><i><span lang="EN-US">m</span></i><span style="font-family:宋体;mso-ascii-font-family:
&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">行，每行包含一个长度为</span><i><span lang="EN-US">m</span></i><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">的</span><span lang="EN-US">01</span><span style="font-family:
宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">串，表示矩阵</span><b><i><span lang="EN-US">A</span></i></b><span style="font-family:宋体;mso-ascii-font-family:
&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">。</span><span lang="EN-US"><o:p></o:p></span></p>
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">接下来一行，包含一个长度为</span><i><span lang="EN-US">m</span></i><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">的</span><span lang="EN-US">01</span><span style="font-family:
宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">串，表示初始向量</span><b><i><span lang="EN-US">b</span></i></b><sup><span lang="EN-US">(0)</span></sup><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">。（</span><b><i><span lang="EN-US">b</span></i></b><sup><span lang="EN-US">(0)</span></sup><span style="font-family:宋体;mso-ascii-font-family:
&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">是列向量，这里表示它的转置）</span><span lang="EN-US"><o:p></o:p></span></p>
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">注意：</span><span lang="EN-US">01</span><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">串两个相邻的数字之间均没有空格。</span><span lang="EN-US"><o:p></o:p></span></p>
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">接下来一行，包含一个正整数</span><i><span lang="EN-US">n</span></i><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">，表示询问的个数。</span><span lang="EN-US"><o:p></o:p></span></p>
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">最后</span><i><span lang="EN-US">n</span></i><span style="font-family:宋体;mso-ascii-font-family:
&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">行，每行包含一个非负整数</span><i><span lang="EN-US">k</span></i><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">，表示询问</span><b><i><span lang="EN-US">A</span></i></b><i><sup><span lang="EN-US">k</span></sup><b><span lang="EN-US">b</span></b></i><sup><span lang="EN-US">(0)</span></sup><span style="font-family:宋体;mso-ascii-font-family:
&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">。</span><span lang="EN-US"><o:p></o:p></span></p>
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">注意：</span><i><span lang="EN-US">k</span></i><span style="font-family:宋体;mso-ascii-font-family:
&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">可能为</span><span lang="EN-US">0</span><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">，此时是求</span><b><i><span lang="EN-US">A</span></i></b><sup><span lang="EN-US">0</span></sup><b><i><span lang="EN-US">b</span></i></b><sup><span lang="EN-US">(0)</span></sup><span lang="EN-US"> =<b><i>b</i></b><sup>(0)</sup></span><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">。</span><span lang="EN-US"><o:p></o:p></span></p>

## 输出格式
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">输出</span><i><span lang="EN-US">n</span></i><span style="font-family:宋体;mso-ascii-font-family:
&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">行，每行包含一个</span><span lang="EN-US">01</span><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">串，表示对应询问中</span><b><i><span lang="EN-US">A</span></i></b><i><sup><span lang="EN-US">k</span></sup><b><span lang="EN-US">b</span></b></i><sup><span lang="EN-US">(0)</span></sup><span style="font-family:宋体;mso-ascii-font-family:
&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">的结果。</span><span lang="EN-US"><o:p></o:p></span></p>
<p class="NOI0"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;">注意：</span><span lang="EN-US">01</span><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:
&quot;Times New Roman&quot;">串两个相邻的数字之间不要输出空格。</span><span lang="EN-US"><o:p></o:p></span></p>


## 样例输入
```
3
110
011
111
101
10
0
2
3
14
1
1325
6
124124
151
12312
```
## 样例输出
```
101
010
111
101
110
010
100
101
001
100
```
## 评测用例规模与约定

本题使用10个评测用例来测试你的程序。

对于评测用例1，m = 10，n = 100，k &le; $10^3$。

对于评测用例2，m = 10，n = 100，k &le; $10^4$。

对于评测用例3，m = 30，n = 100，k &le; $10^5$。

对于评测用例4，m = 180，n = 100，k &le; $10^5$。

对于评测用例5，m = 10，n = 100，k &le; $10^9$。

对于评测用例6，m = 30，n = 100，k &le; $10^9$。

对于评测用例7，m = 180，n = 100，k &le; $10^9$。

对于评测用例8，m = 600，n = 100，k &le; $10^9$。

对于评测用例9，m = 800，n = 100，k &le; $10^9$。

对于评测用例10，m = 1000，n = 100，k &le; $10^9$。