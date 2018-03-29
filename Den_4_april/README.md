# 30 cm Python

## Emil Rasmussen, Lasse Vistrup Rasmussen, Menja Holm Wettergren & Xu Zhen Yang

### Dataset

[55000+ Song lyrics dataset](https://github.com/KasperOnFire/ImpossibleTechnology/blob/master/Datasets/songdata.csv)

### Dependencies & how to run

The following dependencies should be installed in your system, either via `conda install` or `pip install`

```python
import pandas
import matplotlib
import webget
from collections import Counter
import numpy
import os
```

Clone from git repository, `cd Den_4_april` and run the project from command promt with the command line:

`python handin_4_april.py`

Or by opening the run file in your chosen environment and running the file.

Our run.py file contains a webget that downloads the dataset upon running the file. 

Our answer to question 4 takes a while. Don't worry it has not crashed - give it time!

### Images

#### Question 1

![Question 1](img/top5.png)

#### Question 2

![Question 2](img/repeated_words.png)



### Questions

Question 1: What is the most used words in the songs?

Question 2: How many times are each word repeated in a song? (Or perhaps - what song repeats the top 4 repeated words the most? - finds the most repetitive song)

Question 3: What song uses the word "X" the most time? (X meaning a specific word, choose your own!)

Question 4: What is the average number of words per song?

Question 5: Show the distribution of number of words in the songs. (Example: how many songs have 5-10 words, 10-20 words)

### Answers

1. The most used words in the songs is: the, and the amount is: 446872, see image 1.

2. Each word repeated in a song are: 
[('she', 9), ('could', 8), ('and', 7), ('me', 7), ('my', 5), ('that', 4), ("she's", 4), ('just', 4), ('kind', 4), ('of', 4), ('girl', 4), ('ever', 4), ('what', 4), ('i', 4), ('do', 4), ('her', 3), ('the', 3), ('be', 3), ('look', 2), ('at', 2), ('face', 2), ('a', 2), ('when', 2), ('makes', 2), ('feel', 2), ('fine', 2), ('who', 2), ('believe', 2), ('mine', 2), ('without', 2), ("i'm", 2), ('blue', 2), ('if', 2), ('leaves', 2), ('we', 2), ('go', 2), ('for', 2), ("it's", 1), ('wonderful', 1), ('it', 1), ('means', 1), ('something', 1), ('special', 1), ('to', 1), ('way', 1), ('smiles', 1), ('sees', 1), ('how', 1), ('lucky', 1), ('can', 1), ('one', 1), ('fellow', 1), ('walk', 1), ('in', 1), ('park', 1), ('holds', 1), ('squeezes', 1), ('hand', 1), ("we'll", 1), ('on', 1), ('walking', 1), ('hours', 1), ('talking', 1), ('about', 1), ('all', 1), ('things', 1), ('plan', 1)]
See image 2.

3. You choiced word: the. The song: Bando. Amount: 127

4. 
The average number of words is: 2.283582089552239
The average number of words is: 3.7681159420289854
The average number of words is: 2.8363636363636364

5. 
Total amount of words: 57650
Songs have 0-100 words: 3715
Songs have 100-200 words: 26429
Songs have 200-300 words: 17785
Songs have 300-400 words: 6008
Songs have 400-500 words: 1923
Songs have 500-600 words: 1020
Songs have 600-700 words: 603
Songs have 700-800 words: 167