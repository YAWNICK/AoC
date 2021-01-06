#include "hashmap.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

HashMap *HashMapComp() {
    HashMap *hm = (HashMap*) malloc(sizeof(HashMap));
    hm->filled = 0;
    hm->size = HASHMAPSIZE;
    for (int i = 0; i < HASHMAPSIZE; i++) {
        hm->entries[i] = NULL;
    }
    return hm;
}

int hash(char *key) {
    int total = 0;
    while (*key != '\0') {
        total += *key;
        key++;
    }
    return total % HASHMAPSIZE;
}

int put(HashMap *map, char *key, char *val) {
    int h = hash(key);
    int shift = 0;
    Entry *e = map->entries[h];
    while (e != NULL) {
        if (!strcmp(e->key, key)) {
            free(e->val);
            char *newval = (char*) malloc(strlen(val));
            strcpy(newval, val);
            e->val = newval;
            return 0;
        }
        shift++;
        if (shift == HASHMAPSIZE) {
            printf("Hashmap full");
            exit(1);
        }
        e = map->entries[(h + shift) % HASHMAPSIZE];
    }
    e = (Entry*) malloc(sizeof(Entry));
    char *k = (char*) malloc(strlen(key));
    char *v = (char*) malloc(strlen(val));
    strcpy(k, key);
    strcpy(v, val);
    e->hash = h;
    e->key = k;
    e->val = v;
    map->entries[(h + shift) % HASHMAPSIZE] = e;
    map->filled += 1;
    return 0;
}

char *get(HashMap *map, char *key) {
    int h = hash(key);
    if (!strcmp(map->entries[h]->key, key)) {
        return map->entries[h]->val;
    } else {
        exit(1);
    }
}

void show(HashMap *map) {
    printf("HashMap is:\n{");
    for (int i = 0; i < HASHMAPSIZE; i++) {
        Entry *e = map->entries[i];
        if (e == NULL) {
            printf("(NULL)");
        } else {
            printf("(%d:%s:%s)", e->hash, e->key, e->val);
        }
    }
    printf("}\n");
    /*
    for (int i = 0; i < HASHMAPSIZE; i++) {
        Entry *e = map->entries[i];
        if (e == NULL) {
            printf("empty\n");
        } else {
            printf("%d %s %s\n", e->hash, e->key, e->val);
        }
    }*/
}
