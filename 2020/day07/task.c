#include <stdio.h>
#include <stdlib.h>


typedef struct _Bag {
    char[30] name;
    int num_of_parents;
    (_Bag*)[100] parents;
} Bag;

int main() {
    FILE *fp;
    fp = fopen("input.txt", "r");
    if (fp == NULL) exit(EXIT_FAILURE);


}
