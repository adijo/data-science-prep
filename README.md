# Interview Questions from [Data Science Prep](https://datascienceprep.com/)

## [Probability] Unfair Coin: Facebook [Easy]

There is a fair coin (one side heads, one side tails) and an unfair coin (both sides tails). You pick one at random, flip it 5 times, and observe that it comes up as tails all five times.  Whatis the chance that you are flipping the unfair coin? 

## Solution 
Question 1 in the `pdf` file.

## [Coding] Sampling with weights: Lyft [Medium]

Say we are given a list of several categories
(for example, the strings: A, B, C, and D) and want to sample from a
list of such categories according to a particular weighting scheme.
Such an example would be: for 100 items total,
we want to see A 20% of the time, B 15% of the time, C 35% of the time,
and D 30% of the time. How do we simulate this?
What if we care about an arbitrary number of categories and about memory usage?

## Solution 
Code in `code/sampling_with_weights.py` 

## [Probability] Flips until two heads: Lyft [Medium]

This problem was asked by Lyft.

What is the expected number of coin flips needed to get two consecutive heads?

## Solution 3

Analytical solution in the Question 2 section in the `pdf` file. Empirical evaluation in `code/expected_flips_two_heads.py.`



