#include <stdio.h>
#include <stdlib.h>

#define MAXLINES 10000

int part1(int *nums, int size);

int part2(int *nums, int size);

int main(int argc, char *argv[]) {
    
    FILE *fp;

    fp = fopen("input.txt", "r");
    if (fp == NULL) exit(EXIT_FAILURE);
    
    int nums[MAXLINES];
    int cnt = 0;
    while (fscanf(fp, "%d", &nums[cnt]) != EOF) cnt++;

    printf("Part 1: %d\n", part1(nums, cnt));
    printf("Part 2: %d\n", part2(nums, cnt));
    
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
