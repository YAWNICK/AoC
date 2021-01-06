#ifndef HASHMAP_H
#define HASHMAP_H

#define HASHMAPSIZE 8

typedef struct _Entry {
    int hash;
    char *key;
    char *val;
} Entry;

typedef struct _HashMap {
    int size;
    int filled;
    Entry *entries[HASHMAPSIZE];
} HashMap;

HashMap *HashMapComp();

int hash(char *key);

int put(HashMap *map, char *key, char *val);

char *get(HashMap *map, char *key);

void show(HashMap *map);

#endif
