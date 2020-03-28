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
Code is [here.](https://github.com/adijo/data-science-prep/blob/master/code/sampling_with_weights.py)

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

---

## [Probability] Rolls to see all sides: Facebook [Medium]
What is the expected number of rolls needed to see all 6 sides of a fair die?

### Solution
Solution is in the Question 5 section of the `pdf` file.
 
--- 

## [Statistics] Picking between two dice games: Facebook [Hard]
There are two games involving dice that you can play. In the first game, you roll two die at once and get the dollar amount equivalent to the product of the rolls. In the second game, you roll one die and get the dollar amount equivalent to the square of that value. Which has the higher expected value and why?

### Solution
Solution is in the Question 6 section of the `pdf` file.

---
## [Probability] Fair odds from unfair coin: Airbnb [Medium]
Say you are given an unfair coin, with an unknown bias towards heads or tails. How can you generate fair odds using this coin?

### Solution 
Solution is in the Question 7 section of the `pdf` file. Code is [here.](https://github.com/adijo/data-science-prep/blob/master/code/unfair_coin.py)

---
## [Probability] Ant Collision: Facebook [Medium]
Three ants are sitting at the corners of an equilateral triangle. Each ant randomly picks a direction and starts moving along the edge of the triangle. What is the probability that none of the ants collide? Now, what if it is k ants on all k corners of an equilateral polygon?

### Solution 
Solution is in the Question 8 section of the `pdf` file.

---
## [Coding] Generating integer partitions: Stripe [Medium]
Write a program to generate the partitions for a number `n`. A partition for `n` is a list of positive integers that sum up to `n.` For example: if `n = 4`, we want to return the following partitions: `[1,1,1,1], [1,1,2], [2,2], [1,3]`, and `[4]`. Note that a partition`[1,3]` is the same as `[3,1]` so only the former is included.

### Solution
Code is [here.](https://github.com/adijo/data-science-prep/blob/master/code/integer_partitions.py)

---

## [ML] Classification Metrics: Uber [Medium]
Say you need to produce a binary classifier for fraud detection. What metrics would you look at, how is each defined, and what is the interpretation of each one?

### Solution
Question 9 of the `pdf` file.

---

## [Statistics] Simulating a standard normal distribution: Uber [Hard]
Say you are given a random Bernoulli trial generator. How would you generate values from a standard normal distribution?

### Solution
Code is [here.](https://github.com/adijo/data-science-prep/blob/master/code/Standard%20Normal%20From%20Bernoulli.ipynb)

---

## [Coding] Correlation by hand: Robinhood [Medium]
This problem was asked by Robinhood.

Write a program to calculate correlation (without any libraries except for math) for two lists X and Y.

### Solution
Code is [here.](https://github.com/adijo/data-science-prep/blob/master/code/correlation.py)

---

## [Probability] Flipping game: Facebook [Easy]
You and your friend are playing a game. The two of you will continue to toss a coin until the sequence HH or TH shows up. If HH shows up first, you win. If TH shows up first, your friend wins. What is the probability of you winning?

### Solution
Question 10 of the `pdf` file.

--- 

## [Probability] First to roll side k: Lyft [Medium]
A and B are playing the following game: a number k from 1-6 is chosen, and A and B will toss a die until the first person sees the side k, and that person gets $100. How much is A willing to pay to play first in this game?

### Solution
Question 11 of the `pdf` file.

