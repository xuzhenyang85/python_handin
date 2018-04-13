# 30 cm Python

## Emil Rasmussen, Lasse Vistrup Rasmussen, Menja Holm Wettergren & Xu Zhen Yang

### Dataset

[ks-projects](https://github.com/mathiasjepsen/PythonDatasetAssignment/raw/master/ks-projects-201801.csv)

### Dependencies & how to run

The following dependencies should be installed in your system, either via `conda install` or `pip install`

```python
from collections import Counter
import statistics
import webget
import pandas as pd
import matplotlib.pyplot as plt
import os
```

Clone from git repository, `cd Den_4_april` and run the project from command promt with the command line:

`python handin_4_april.py`

Or by opening the run file in your chosen environment and running the file.

Our run.py file contains a webget that downloads the dataset upon running the file. 

Our answer to question 4 takes a while. Don't worry it has not crashed - give it time!

### Answers

#### Question 1

1. What main-category of project has the highest success rate?

The highest success rate of project is: Music : 24197

[Question 1](images/highest_succes_rate.png)

#### Question 2

2. For the main-category of project with highest success rate (question above), what is the main-category with the highest number of project proposals?
The highest number of project proposals is: Film & Video
[Question 2](images/highest_number_of_project_proposals.png)

#### Question 3

3. What is the median pledged amount (usd_pledged_real) of successfully funded projects?
The median pledged amount (usd_pledged_real) of successfully funded projects is: 5107.25

#### Question 4

3. What is the median pledged amount (usd_pledged_real) of successfully funded projects?
The median pledged amount (usd_pledged_real) of successfully funded projects is: 5107.25
[Question 4](images/number_of_success_project_more_than_5000.png)

#### Question 5

3. What is the median pledged amount (usd_pledged_real) of successfully funded projects?
The median pledged amount (usd_pledged_real) of successfully funded projects is: 5107.25
[Question 5](images/10k.png)
[Question 5](images/20k.png)
[Question 5](images/30k.png)
[Question 5](images/40k.png)
[Question 5](images/50k.png)
[Question 5](images/60k.png)
