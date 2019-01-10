
#include <iostream>
#include <unordered_set>

static const int MAX_NUMBER = 1000;

int solve1() {
    int sum = 0;

    for (int i = 3; i < MAX_NUMBER; ++i) {
        if (i % 3 == 0) {
            sum += i;
        } else if (i % 5 == 0) {
            sum += i;
        }
    }

    return sum;
}

int solve2() {
    int sum = 0;

    for (int multipleOf3 = 3; multipleOf3 < MAX_NUMBER; multipleOf3 += 3) {
        sum += multipleOf3;
    }

    for (int multipleOf5 = 5; multipleOf5 < MAX_NUMBER; multipleOf5 += 5) {
        if (multipleOf5 % 3 != 0) {
            sum += multipleOf5;
        }
    }

    return sum;
}

int solve3() {
    int sum = 0;
    int seqCounter = 0;
    const int SEQ_LENGTH = 5;

    for (int multipleOf3 = 3; multipleOf3 < MAX_NUMBER; multipleOf3 += 3) {
        sum += multipleOf3;

        if (seqCounter == 1) {
            sum += multipleOf3 - 1;
        } else if (seqCounter == 2 && multipleOf3 + 1 < 1000) {
            sum += multipleOf3 + 1;
        }
        seqCounter = (seqCounter + 1) % SEQ_LENGTH;
    }

    return sum;
}


int main() {
    std::cout << solve3() << std::endl;
    return 0;
}