# Euler 001 - Multiples of 3 and 5

## Problem Description
Find the original problem [here](https://projecteuler.net/problem=1).

> If we list all the natural numbers below 10 that are multiples of 3 or 5 we get 3, 5, 6, and 9. The sum of these multiples is 23.
> Find the sum of all the multiples of 3 or 5 below 1000.

## Simplifying/Clarifying the Problem
One thing to keep in mind is the duplicity of some numbers. For instance, 15 is multiple of
3 and 5 but 15 should not be counted twice.

## The Solutions

### Solution 1
The first really simple solution that I came up with is to iterate over all of the natural numbers between 0 and 1000.
For every number, I check if the number is divisible by 3 or 5 and, if so, add the number to the sum. This gives us a small and simple loop.

```c++
    int sum = 0;

    for (int i = 3; i < 1000; ++i) {
        if (i % 3 == 0) {
            sum += i;
        } else if (i % 5 == 0) {
            sum += i;
        }
    }

    return sum;
```

I used an `else if` instead of an `if` when checking for multiples of 5 in order to not double count numbers that are divisible by both 3 and 5, such as 15.

This algorithm is small and compact. It has a time complexity of O(N) where N is the number of natural numbers in between 0 and the max number. However, I can do better.
This algorithm does a lot of unnecessary work. It is easy to compute the multiples of a number so there is no need to check the numbers in between. I use this idea in my next solution.

### Solution 2
To reduce the unnecessary work, I can iterate over the multiples of 3 and then iterate over the multiples of 5. 

```c++
    int sum = 0;

    for (int multipleOf3 = 3; multipleOf3 < 1000; multipleOf3 += 3) {
        sum += multipleOf3;
    }

    for (int multipleOf5 = 5; multipleOf5 < 1000; multipleOf5 += 5) {
        if (multipleOf5 % 3 != 0) {
            sum += multipleOf5;
        }
    }

    return sum;
```

This algorithm has a complexity of O(a+b) where 'a' is the number of multiples of 3 between 0 and the max number and 'b' is the
number of multiples of 5 between 0 and the max number. Since there are fewer multiples of 3 and 5 than natural numbers in a range, a+b < N.
So I have reduced the unnecessary work which has improved the complexity. But now I am doing a little bit of duplicate work. While iterating over the multiples of 5 I revisit numbers that were multiples of 3, hence the additional `if` statement. Is there a way to be even better?

### Solution 3
In the previous solution I iterate over two sets of numbers. One way to improve this is to derive one set from the other. Can I derive the multiples of 5 from the multiples of 3? Let's take a look at the pattern of the two sets.

| Multiples of 3 | Multiples of 5 |
|:--------------:|:--------------:|
| 3              |                |
|                | 5              |
| 6              |                |
| 9              |                |
|                | 10             |
| 12             |                |
| 15             | 15             |
| 18             |                |
|                | 20             |
| 21             |                |
| 24             |                |
|                | 25             |
| 27             |                |
| 30             | 30             |

The table is spaced out so that the numbers are in order. Looking at this table we can see that we start with a multiple of 3, then a multiple of 5, two multiples of 3, a multiple of 5, a multiple of 3, and then a shared multiple. After 15, it is evident that this pattern repeats. A repeating pattern suggests that I can derive one set from the other. The table below shows one of the ways that you could do this.

| Multiple3 of 3 | Corresponding Multiple of 5 |
|:--------------:|:--------------------------:|
| 3  | N/A |
| 6  | -1  |
| 9  | +1  |
| 12 | N/A |
| 15 | N/A |

What this table says is that if we are at 6, or more generally the second multiple of 3 from the above pattern, then I can subtract 1 to get a multiple of 5. Additionally, if I am at the third multiple of 3 then I can add 1 to get another multiple of 5. All other multiples of 3 have no corresponding multiple of 5 or is itself a multiple of 5.

Using this pattern I can now generate all multiples of 5. I still have to be careful to make sure that the generated multiple of five is still within the exceptable range.

```c++
    int sum = 0;
    int seqCounter = 0;
    int seqLength = 5;

    for (int multipleOf3 = 3; multipleOf3 < 1000; multipleOf3 += 3) {
        sum += multipleOf3;

        if (seqCounter == 1) {
            sum += multipleOf3 - 1;
        } else if (seqCounter == 2 && multipleOf3 + 1 < 1000) {
            sum += multipleOf3 + 1;
        }
        seqCounter = (seqCounter + 1) % seqLength;
    }
```

`seqCounter` and `seqLength` are variables that help me deterime where I am in the pattern. Now we have an algorithm that does not visit unnecessary numbers and does not revisit numbers. The time complexity of this solution is O(a) where 'a' is the number of multiples of 3 between 0 and the max number.

Despite achieving my goal, this solution is the ugliest due to its multiple conditions to check for and the added code for keeping track of the sequence. Personally, I prefer solution 2 as it is easier to read and understand and has an acceptable runtime complexity for the purposes of the problem.