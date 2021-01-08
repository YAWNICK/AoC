#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "hashmap.h"

#define MAXPPS 10000

#define NUM_FIELDS 7
char *fields[] = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};

int arrstr(char *arr[], int size, char *string);

int validate_field(char *key, char *val);

int part1(HashMap *pps[], int size);

int part2(HashMap *pps[], int size);

int main() {
    
    FILE *fp;
    fp = fopen("input.txt", "r");
    if (fp == NULL) exit(EXIT_FAILURE);

    HashMap *pps[MAXPPS];
    int numpps = 0;  // number of passports
    HashMap *hm = HashMapComp();  // temp hm to collect each pp and store it in pps
    char line[500];
    while (fgets(line, 500, fp) != NULL) {
        // input.txt must end with an empts line, or else the last passport
        // will not be inserted into pps by the following if statement
        if (*line == '\n') {  // end of a passport
            pps[numpps] = hm;
            numpps++;
            hm = HashMapComp();
        }
        char *lineptr = line;  // ptr to traverse line
        char key[10];
        char val[20];
        int t = 0;  // lineptr increment
        while (sscanf(lineptr, "%[^:]:%s%n", key, val, &t) == 2) {
            put(hm, key, val);
            lineptr += t + 1;  // + 1 because or the space after each field
        }
    }
    
    printf("Part 1: %d\n", part1(pps, numpps));
    printf("Part 2: %d\n", part2(pps, numpps));

    return 0;
}

int part1(HashMap *pps[], int size) {
    int valid_pps = 0;
    for (int i_pp = 0; i_pp < size; i_pp++) {
        HashMap *pp = pps[i_pp];
        int valid_fields = 0;  // this bitvector stores which fields are present
        for (int i_f = 0; i_f < pp->size; i_f++) {
            if (pp->entries[i_f] == NULL) continue;
            int i_arr;
            if ((i_arr = arrstr(fields, NUM_FIELDS, pp->entries[i_f]->key)) != -1) {
                valid_fields |= (1 << i_arr);
            }
        }
        if (valid_fields == (1 << NUM_FIELDS) - 1) valid_pps++;
    }
    return valid_pps;
}

/*
 * arr: array of strings
 * size: size of array
 * string: string to search for
 *
 * returns: index of string in array on success, -1 on fail
 */
int arrstr(char *arr[], int size, char *string) {
    for (int i = 0; i < size; i++) {
        if (!strcmp(arr[i], string)) return i;
    }
    return -1;
}

#define NUM_ECLS 7
char *ecls[] = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"};

int part2(HashMap *pps[], int size) {
    int valid_pps = 0;
    for (int i_pp = 0; i_pp < size; i_pp++) {
        HashMap *pp = pps[i_pp];
        int valid_fields = 0;  // this bitvector stores which fields are valid
        for (int i_f = 0; i_f < pp->size; i_f++) {
            if (pp->entries[i_f] == NULL) continue;
            char *key = pp->entries[i_f]->key;
            char *val = pp->entries[i_f]->val;
            int i_arr = arrstr(fields, NUM_FIELDS, key);
            if (i_arr == -1) continue;
            if (!validate_field(key, val)) {
                valid_fields |= (1 << i_arr);
            }
        }
        if (valid_fields == (1 << NUM_FIELDS) - 1) valid_pps++;
    }
    return valid_pps;
}

int validate_field(char *key, char *val) {
    int vnum;
    char *vnumend;
    vnum = (int) strtol(val, &vnumend, 10);

    if (!strcmp(key, "byr")) {
        if (1920 <= vnum && vnum <= 2002 && *vnumend == 0) return 0;
    } else if (!strcmp(key, "iyr")) {
        if (2010 <= vnum && vnum <= 2020 && *vnumend == 0) return 0;
    } else if (!strcmp(key, "eyr")) {
        if (2020 <= vnum && vnum <= 2030 && *vnumend == 0) return 0;
    } else if (!strcmp(key, "hgt")) {
        if (150 <= vnum && vnum <= 193 && !strcmp(vnumend, "cm")) return 0;
        if (59 <= vnum && vnum <= 76 && !strcmp(vnumend, "in")) return 0;
    } else if (!strcmp(key, "hcl")) {
        if (*val != '#') return -1;
        for (int i = 1; i < 7; i++) {
            if ((val[i] < '0' || val[i] > '9') && (val[i] < 'a' || val[i] > 'f')) {
                return -1;
            }
        }
        if (val[7] != '\0') return -1;
        return 0;
    } else if (!strcmp(key, "ecl")) {
        if (arrstr(ecls, NUM_ECLS, val) != -1) return 0;
    } else if (!strcmp(key, "pid")) {
        if ((int) (vnumend - val) == 9 && *vnumend == 0) return 0;
    }
    return -1;
}
