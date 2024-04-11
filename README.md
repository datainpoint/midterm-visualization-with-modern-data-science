# midterm-visualization-with-modern-data-science

Midterm: Visualization with Modern Data Science.

## 01. Write a SQL statement that is able to show the number of rows for certain tables given `taiwan_election_2024.db`.

```
table_name	number_of_rows
candidates	331
districts	17795
parties	35
```

```python
answer_01 =\
"""
-- BEGIN SOLUTION

-- END SOLUTION
"""
```

## 02. Write a SQL statement that is able to show earliest and latest votes tallied time given `taiwan_election_2024.db`.

```
label	vote_tallied_at
earliest	2024-01-13 16:30:49
latest	2024-01-13 21:56:59
```

```python
answer_02 =\
"""
-- BEGIN SOLUTION

-- END SOLUTION
"""
```

## 03. Based on the previous query result, write a SQL statement that is able to find the corresponding polling places.

```
county	town	polling_place	vote_tallied_at
宜蘭縣	大同鄉	421	2024-01-13 16:30:49
新竹縣	竹北市	25	2024-01-13 21:56:59
```

```python
answer_03 =\
"""
-- BEGIN SOLUTION

-- END SOLUTION
"""
```

## 04. Write a SQL statement that is able to show the most votes received and the least votes received by a regional legislator candidate.

```
label	min_max_votes
maximun	158596
minimum	136
```

```python
answer_04 =\
"""
-- BEGIN SOLUTION

-- END SOLUTION
"""
```

## 05. Based on the previous query result, write a SQL statement that is able to show the information about the candidates.

```
legislator_region	party	name	sum_votes
新北市第1選舉區	中國國民黨	洪孟楷	158596
臺北市第8選舉區	興中同盟會	胡之壯	136
```

```python
answer_05 =\
"""
-- BEGIN SOLUTION

-- END SOLUTION
"""
```

## 06. Write a SQL statement that is able to show the top 15 regional legislators elected given `taiwan_election_2024.db`.

```
legislator_region	party	name	sum_votes
新北市第1選舉區	中國國民黨	洪孟楷	158596
臺中市第5選舉區	中國國民黨	黃健豪	134706
臺南市第3選舉區	民主進步黨	陳亭妃	132377
臺中市第7選舉區	民主進步黨	何欣純	132235
臺南市第5選舉區	民主進步黨	林俊憲	126248
新北市第11選舉區	中國國民黨	羅明才	123399
高雄市第8選舉區	民主進步黨	賴瑞隆	121064
高雄市第4選舉區	民主進步黨	林岱樺	121001
臺中市第4選舉區	中國國民黨	廖偉翔	119740
桃園市第4選舉區	中國國民黨	萬美玲	119430
臺中市第2選舉區	中國國民黨	顏寬恒	118962
新北市第2選舉區	民主進步黨	林淑芬	118544
高雄市第2選舉區	民主進步黨	邱志偉	117992
桃園市第1選舉區	中國國民黨	牛煦庭	116571
雲林縣第2選舉區	民主進步黨	劉建國	115376
```

```python
answer_06 =\
"""
-- BEGIN SOLUTION

-- END SOLUTION
"""
```

## 07. Write a SQL statement that is able to summarize the result of party legislators excluding the major three parties given `taiwan_election_2024.db`.

```
party	sum_votes
時代力量	353412
小民參政歐巴桑聯盟	128613
台灣綠黨	117298
台灣基進	95078
親民黨	69818
臺灣雙語無法黨	44852
台灣團結聯盟	43375
新黨	40288
司法改革黨	37615
制度救世島	19665
中華統一促進黨	17423
人民最大黨	11746
台灣維新	10300
```

```python
answer_07 =\
"""
-- BEGIN SOLUTION

-- END SOLUTION
"""
```

## 08. Write a SQL statement that is able to summarize the presidential votes received by each candidate for each county given `taiwan_election_2024.db`.

```
county	name	sum_votes
南投縣	侯友宜/趙少康	109163
南投縣	賴清德/蕭美琴	103279
南投縣	柯文哲/吳欣盈	74854
嘉義市	賴清德/蕭美琴	68199
嘉義市	侯友宜/趙少康	49507
嘉義市	柯文哲/吳欣盈	39950
嘉義縣	賴清德/蕭美琴	139510
嘉義縣	侯友宜/趙少康	85642
嘉義縣	柯文哲/吳欣盈	67382
基隆市	侯友宜/趙少康	84507
基隆市	賴清德/蕭美琴	76079
基隆市	柯文哲/吳欣盈	58195
宜蘭縣	賴清德/蕭美琴	119517
宜蘭縣	侯友宜/趙少康	77441
宜蘭縣	柯文哲/吳欣盈	70171
屏東縣	賴清德/蕭美琴	226110
屏東縣	侯友宜/趙少康	146789
屏東縣	柯文哲/吳欣盈	103028
彰化縣	賴清德/蕭美琴	282514
彰化縣	侯友宜/趙少康	244140
彰化縣	柯文哲/吳欣盈	214714
新北市	賴清德/蕭美琴	948818
新北市	侯友宜/趙少康	864557
新北市	柯文哲/吳欣盈	645105
新竹市	賴清德/蕭美琴	92679
新竹市	柯文哲/吳欣盈	91384
新竹市	侯友宜/趙少康	82326
新竹縣	侯友宜/趙少康	126016
新竹縣	柯文哲/吳欣盈	120985
新竹縣	賴清德/蕭美琴	93309
桃園市	賴清德/蕭美琴	476441
桃園市	侯友宜/趙少康	460823
桃園市	柯文哲/吳欣盈	413528
澎湖縣	賴清德/蕭美琴	19023
澎湖縣	侯友宜/趙少康	18052
澎湖縣	柯文哲/吳欣盈	12202
臺中市	賴清德/蕭美琴	641622
臺中市	侯友宜/趙少康	552556
臺中市	柯文哲/吳欣盈	513025
臺北市	賴清德/蕭美琴	587899
臺北市	侯友宜/趙少康	587258
臺北市	柯文哲/吳欣盈	366854
臺南市	賴清德/蕭美琴	570811
臺南市	侯友宜/趙少康	286867
臺南市	柯文哲/吳欣盈	262560
臺東縣	侯友宜/趙少康	54220
臺東縣	賴清德/蕭美琴	30131
臺東縣	柯文哲/吳欣盈	25590
花蓮縣	侯友宜/趙少康	87953
花蓮縣	賴清德/蕭美琴	43157
花蓮縣	柯文哲/吳欣盈	43047
苗栗縣	侯友宜/趙少康	131230
苗栗縣	柯文哲/吳欣盈	95637
苗栗縣	賴清德/蕭美琴	91798
連江縣	侯友宜/趙少康	3860
連江縣	柯文哲/吳欣盈	1651
連江縣	賴清德/蕭美琴	648
金門縣	侯友宜/趙少康	28005
金門縣	柯文哲/吳欣盈	13038
金門縣	賴清德/蕭美琴	4569
雲林縣	賴清德/蕭美琴	169516
雲林縣	侯友宜/趙少康	111633
雲林縣	柯文哲/吳欣盈	99470
高雄市	賴清德/蕭美琴	800390
高雄市	侯友宜/趙少康	478476
高雄市	柯文哲/吳欣盈	358096
```

```python
answer_08 =\
"""
-- BEGIN SOLUTION

-- END SOLUTION
"""
```

## 09. Based on the previous query result, write a SQL statement that is able to show the winner for each county.

```
county	winner	sum_votes
南投縣	侯友宜/趙少康	109163
嘉義市	賴清德/蕭美琴	68199
嘉義縣	賴清德/蕭美琴	139510
基隆市	侯友宜/趙少康	84507
宜蘭縣	賴清德/蕭美琴	119517
屏東縣	賴清德/蕭美琴	226110
彰化縣	賴清德/蕭美琴	282514
新北市	賴清德/蕭美琴	948818
新竹市	賴清德/蕭美琴	92679
新竹縣	侯友宜/趙少康	126016
桃園市	賴清德/蕭美琴	476441
澎湖縣	賴清德/蕭美琴	19023
臺中市	賴清德/蕭美琴	641622
臺北市	賴清德/蕭美琴	587899
臺南市	賴清德/蕭美琴	570811
臺東縣	侯友宜/趙少康	54220
花蓮縣	侯友宜/趙少康	87953
苗栗縣	侯友宜/趙少康	131230
連江縣	侯友宜/趙少康	3860
金門縣	侯友宜/趙少康	28005
雲林縣	賴清德/蕭美琴	169516
高雄市	賴清德/蕭美琴	800390
```

```python
answer_09 =\
"""
-- BEGIN SOLUTION

-- END SOLUTION
"""
```

## 10. Write a SQL statement that is able to show the winner for each town in Taipei City given `taiwan_election_2024.db`.

```
county	town	winner	sum_votes
臺北市	中山區	賴清德/蕭美琴	54448
臺北市	中正區	侯友宜/趙少康	34733
臺北市	信義區	侯友宜/趙少康	53076
臺北市	內湖區	侯友宜/趙少康	64781
臺北市	北投區	賴清德/蕭美琴	61151
臺北市	南港區	侯友宜/趙少康	26529
臺北市	士林區	賴清德/蕭美琴	71869
臺北市	大同區	賴清德/蕭美琴	34270
臺北市	大安區	侯友宜/趙少康	72954
臺北市	文山區	侯友宜/趙少康	70844
臺北市	松山區	侯友宜/趙少康	47452
臺北市	萬華區	賴清德/蕭美琴	43369
```

```python
answer_10 =\
"""
-- BEGIN SOLUTION

-- END SOLUTION
"""
```