#include <stdio.h>
#include <stdlib.h>

int part1(int *nums, int size);

int part2(int *nums, int size);

int main(int argc, char *argv[]) {
    
    FILE *fp;
    int numLines = 200;

    fp = fopen("input.txt", "r");
    if (fp == NULL) exit(EXIT_FAILURE);
    
    int nums[numLines];
    int i = 0;
    while (fscanf(fp, "%d", &nums[i]) != EOF) i++;

    printf("Part 1: %d\n", part1(nums, numLines));
    printf("Part 2: %d\n", part2(nums, numLines));
    
    return 0;
}

int part1(int *nums, int size){
    for (int i = 0; i < size; i++) {
        for (int j = i + 1; j < size; j++) {
            if (nums[i] + nums[j] == 2020) {
                return nums[i] * nums[j];
            }
        }
    }
    return -1;
}

int part2(int *nums, int size) {
    for (int i = 0; i < size; i++) {
        for (int j = i + 1; j < size; j++) {
            for (int k = j + 1; k < size; k++) {
                if (nums[i] + nums[j] + nums[k] == 2020) {
                    return nums[i] * nums[j] * nums[k];
                }
            }
        }
    }
    return -1;
}
