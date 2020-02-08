# Interview Questions from [Data Science Prep](https://datascienceprep.com/)
---

## [Probability] Unfair Coin: Facebook [Easy]

There is a fair coin (one side heads, one side tails) and an unfair coin (both sides tails). You pick one at random, flip it 5 times, and observe that it comes up as tails all five times.  Whatis the chance that you are flipping the unfair coin? 

### Solution 
Question 1 in the `pdf` file.

---

## [Coding] Sampling with weights: Lyft [Medium]

Say we are given a list of several categories
(for example, the strings: A, B, C, and D) and want to sample from a
list of such categories according to a particular weighting scheme.
Such an example would be: for 100 items total,
we want to see A 20% of the time, B 15% of the time, C 35% of the time,
and D 30% of the time. How do we simulate this?
What if we care about an arbitrary number of categories and about memory usage?

### Solution 
Code in `code/sampling_with_weights.py`

---

## [Probability] Flips until two heads: Lyft [Medium]

This problem was asked by Lyft.

What is the expected number of coin flips needed to get two consecutive heads?

### Solution 

Analytical solution in the Question 2 section in the `pdf` file. Empirical evaluation is [here.](https://github.com/adijo/data-science-prep/blob/master/code/expected_flips_two_heads.py)

---

## [Statistics] Drawing normally: Quora [Medium]

You are drawing from a normally distributed random variable X ~ N(0, 1) once a day. What is the approximate expected number of days until you get a value of more than 2?

### Solution
Analytical solution in the Question 3 section of the `pdf` file. Empirical evaluation is [here.](https://github.com/adijo/data-science-prep/blob/master/code/expected_days_normal_distribution.py)

---

## [SQL] Ad CTR: Facebook [Easy]
Assume you have the below events table on app analytics. Write a query to get the click-through rate per app in 2019.
```sqlite-sql
column_name	type
app_id	        integer
event_id	string ("impression", "click")
timestamp	datetime
```

### Solution
SQL query is [here.](https://github.com/adijo/data-science-prep/blob/master/code/ctr_calculation.sql)

---

## [Statistics] Is the coin biased?: Google [Medium]
A coin was flipped 1000 times, and 550 times it showed up heads. Do you think the coin is biased? Why or why not?

### Solution
Solution is in the Question 4 section of the `pdf` file. The computation is [here.](https://github.com/adijo/data-science-prep/blob/master/code/Is%20this%20coin%20biased%3F.ipynb)

