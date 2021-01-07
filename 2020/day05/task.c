#include <stdio.h>
#include <stdlib.h>

#define ROWBITS 7
#define ROWSEATBITS 3
#define ROWS (1 << ROWBITS)
#define ROWSEATS (1 << ROWSEATBITS)

int getSeatId(char *seatString);

int part1(int *seatIds, int size);

int part2(int *seatIds, int size);

int main() {
    FILE *fp;
    fp = fopen("input.txt", "r");
    if (fp == NULL) exit(EXIT_FAILURE);

    int seatIds[ROWS * ROWSEATS];  // holds all seat IDs
    int seatIdsCnt = 0;
    char seatString[ROWBITS + ROWSEATBITS + 1];  // + 1 for '\0'
    while (fscanf(fp, "%s", seatString) == 1) {
        seatIds[seatIdsCnt++] = getSeatId(seatString);
    }
    printf("Part 1: %d\n", part1(seatIds, seatIdsCnt));
    printf("Part 2: %d\n", part2(seatIds, seatIdsCnt));
    return 0;
}

// the binary space partitioning
int getSeatId(char *seatString) {
    int seatId = 0;
    for (; *seatString; seatString++) {
        seatId <<= 1;
        seatId += *seatString == 'F' || *seatString == 'L' ? 0 : 1;
    }
    return seatId;
}

int part1(int *seatIds, int size) {
    int maxSeatId = *seatIds;
    for (int i = 1; i < size; i++) {
        if (seatIds[i] > maxSeatId) maxSeatId = seatIds[i];
    }
    return maxSeatId;
}

int part2(int *seatIds, int size) {
    int mySeatId;
    // dont't consider front and back row
    for (mySeatId = ROWSEATS; mySeatId < ROWS * (ROWSEATS - 1); mySeatId++) {
        int empty = 1;  // set it mySeatId is empty
        int neighbors = 0;  // counts occupied neighbors
        for (int iSeatId = 0; iSeatId < size; iSeatId++) {
            int seatId = seatIds[iSeatId];
            if (seatId == mySeatId) {
                empty = 0;
                break;
            }
            if (seatId == mySeatId - 1 || seatId == mySeatId + 1) neighbors++;
        }
        if (empty && neighbors == 2) break;
    }
    return mySeatId;
}
