#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXLINES 10000
#define MAXPWLEN 100

int part1(int res[][2], char *chars, char pws[][MAXPWLEN], int size);

int part2(int res[][2], char *chars, char pws[][MAXPWLEN], int size);

int main() {
     
    FILE *fp;

    fp = fopen("input.txt", "r");
    if (fp == NULL) exit(EXIT_FAILURE);
    int res[MAXLINES][2];
    char chars[MAXLINES];
    char pws[MAXLINES][MAXPWLEN];
    int cnt = 0;
    while (fscanf(fp, "%d-%d %c: %s", &res[cnt][0], &res[cnt][1], &chars[cnt], pws[cnt]) != EOF) {
        cnt++;
    }
    fclose(fp);
    printf("Part 1: %d\n", part1(res, chars, pws, cnt));
    printf("Part 2: %d\n", part2(res, chars, pws, cnt));

    return 0;
}

int part1(int res[][2], char *chars, char pws[][MAXPWLEN], int size) {
    int total = 0;
    for (int i_pw = 0; i_pw < size; i_pw++) {
        int cnt = 0;
        for (int i_c = 0; i_c < strlen(pws[i_pw]); i_c++) {
            if (pws[i_pw][i_c] == chars[i_pw]) cnt++;
        }
        if (res[i_pw][0] <= cnt && res[i_pw][1] >= cnt) total++;
    }
    return total;
}

int part2(int res[][2], char *chars, char pws[][MAXPWLEN], int size) {
    int total = 0;
    for (int i_pw = 0; i_pw < size; i_pw++) {
        int cnt = 0;
        for (int i_pos = 0; i_pos < 2; i_pos++) {
            if (pws[i_pw][res[i_pw][i_pos] - 1] == chars[i_pw]) cnt++;
        }
        if (cnt == 1) total++;
    }
    return total;
}
