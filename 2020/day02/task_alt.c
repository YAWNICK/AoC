#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXLINES 10000
#define MAXPWLEN 100

typedef struct _Pw {
    int lo;
    int hi;
    char letter;
    char pw[MAXPWLEN];
} Pw;

int part1(Pw *pw, int size);

int part2(Pw *pw, int size);

int main() {
    
    FILE *fp;
    fp = fopen("input.txt", "r");
    if (fp == NULL) exit(EXIT_FAILURE);

    Pw pws[MAXLINES];
    int cnt = 0;
    while (fscanf(fp, "%d-%d %c: %s", &pws[cnt].lo, &pws[cnt].hi, &pws[cnt].letter, pws[cnt].pw) != EOF) {
        cnt++;
    }

    printf("Part 1: %d\n", part1(pws, cnt));
    printf("Part 2: %d\n", part2(pws, cnt));
    return 0;
}

int part1(Pw *pw, int size) {
    int total = 0;
    for (int i = 0; i < size; i++) {
        int cnt = 0;
        for (int c = 0; c < strlen(pw->pw); c++){
            if (pw->pw[c] == pw->letter) cnt++;
        }
        if (cnt >= pw->lo && cnt <= pw->hi) total++;
        pw++;
    }
    return total;
}

int part2(Pw *pw, int size) {
    int total = 0;
    for (int i = 0; i < size; i++) {
        int cnt = 0;
        if (pw->pw[pw->lo - 1] == pw->letter) cnt++;
        if (pw->pw[pw->hi - 1] == pw->letter) cnt++;
        if (cnt == 1) total++;
        pw++;
    }
    return total;
}
