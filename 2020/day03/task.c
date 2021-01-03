#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXHEIGHT 10000
#define MAXWIDTH 100

int treecnt(char biome[][MAXWIDTH], int height, int width, int r, int d);

int part1(char biome[][MAXWIDTH], int height, int width);

int part2(char biome[][MAXWIDTH], int height, int width);

int main() {
    FILE *fp;

    fp = fopen("input.txt", "r");
    if (fp == NULL) exit(EXIT_FAILURE);

    char biome[MAXHEIGHT][MAXWIDTH];
    int height = 0;
    int width = 0;
    while (fscanf(fp, "%s", biome[height]) != EOF) height++;
    fclose(fp);
    width = strlen(biome[0]);
    
    printf("Part 1: %d\n", part1(biome, height, width));
    printf("Part 2: %d\n", part2(biome, height, width));
    return 0;
}

int treecnt(char biome[][MAXWIDTH], int height, int width, int r, int d) {
    int total = 0;
    int x = 0;
    int y = 0;
    while (x < height) {
        if (biome[x][y] == '#') total++;
        x += d;
        y = (y + r) % width;
    }
    return total;
}

int part1(char biome[][MAXWIDTH], int height, int width) {
    return treecnt(biome, height, width, 3, 1);
}

int part2(char biome[][MAXWIDTH], int height, int width) {
    int total = 1;
    int dirs[5][2] = {{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}};
    for (int i = 0; i < 5; i++) {
        total *= treecnt(biome, height, width, dirs[i][0], dirs[i][1]);
    }
    return total;
}
