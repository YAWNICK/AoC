#include <stdio.h>
#include <stdlib.h>

#define ROWBITS 7
#define ROWSEATBITS 3
#define ROWS (1 << ROWBITS)
#define ROWSEATS (1 << ROWSEATBITS)

int main() {
    FILE *fp;
    fp = fopen("input.txt", "r");
    if (fp == NULL) exit(EXIT_FAILURE);
    
    int maxSeatId = 0;  // keep track of current max Seat ID
    char seatString[ROWBITS + ROWSEATBITS + 1];  // + 1 for '\0'
    int seatIds[ROWS * ROWSEATS];  // store all Seat IDs for Part 2
    int seatIdsIndex = 0; // running index
    while (fscanf(fp, "%s", seatString) == 1) {
        char *seat = seatString;
        int seatId = 0;
        for (; *seat; seat++) {  // create Seat ID
            seatId <<= 1;
            seatId += *seat == 'F' || *seat == 'L' ? 0 : 1;
        }
        if (seatId > maxSeatId) maxSeatId = seatId;
        seatIds[seatIdsIndex++] = seatId;
    }
    printf("Part 1: %d\n", maxSeatId);

    // Part 2
    int mySeatId;
    // don't even consider front or back row
    for (mySeatId = ROWSEATS; mySeatId < ROWS * (ROWSEATS - 1); mySeatId++) {
        int neighbors = 0;  // counts taken neighbor seats
        int empty = 1;  // set it mySeatId is empty
        for (int iseatId = 0; iseatId < ROWS * ROWSEATS; iseatId++) {
            int seatId = seatIds[iseatId];
            if (mySeatId == seatId) {
                empty = 0;
                break;
            }
            if (seatId == mySeatId - 1 || seatId == mySeatId + 1) neighbors++;
        }
        if (neighbors == 2 && empty) break;
    }
    printf("Part 2: %d\n", mySeatId);
    return 0;
}
