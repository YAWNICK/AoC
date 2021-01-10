#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

#define MAXQS 26  // for 26 letters in the alphabet
// Character offset: lowercase letters go from 97 ('a') to 122 ('z')
#define COFF 97

int main() {
    FILE *fp;
    fp = fopen("input.txt", "r");
    if (fp == NULL) exit(EXIT_FAILURE);
    
    int total1 = 0;  // Part 1
    int total2 = 0;  // Part 2
    // The lower 26 bits of qs1 and qs2 represent all possible questions
    // If the bit is set the question is counted for the current group
    uint32_t qs1 = 0;  // start with all zeros
    uint32_t qs2 = ~0;   // start with all ones
    char answers[MAXQS + 2];  // + 2 for '\n\0'
    while (fgets(answers, MAXQS + 2, fp) != NULL) {
        // input.txt must end with an empty line, or else the last group
        // will not be added to the total
        if (*answers == '\n') {  // end of group
            for (int i = 0; i < MAXQS; i++) {  // add counted Qs to total
                total1 += (qs1 & 1);
                total2 += (qs2 & 1);
                qs1 >>= 1;
                qs2 >>= 1;
            }
            qs1 = 0;
            qs2 = ~0;
            continue;
        }
        // handle answered questions
        char *answer = answers;
        uint32_t p2mask = 0;
        for (; *answer != '\n'; answer++) {
            qs1 |= (1 << (*answer - COFF));
            p2mask |= (1 << (*answer - COFF));
        }
        qs2 &= p2mask;
    }
    printf("Part 1: %d\n", total1);
    printf("Part 2: %d\n", total2);
    return 0;
}
