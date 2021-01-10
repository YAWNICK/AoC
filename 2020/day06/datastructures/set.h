#ifndef SET_H
#define SET_H

typedef struct _Entry {
    char val;
    struct _Entry *next;
} Entry;

typedef struct _CharSet {
    Entry *head;
} CharSet;

CharSet *CharSetComp();

int setAdd(CharSet *set, char val);

int setRemove(CharSet *set, char val);

int setContains(CharSet *set, char val);

/*
 * stores the union of set and setToUnite in set
 * and leaves setToUnite the same
 */
int setUnite(CharSet *set, CharSet *setToUnite);

int setIntersect(CharSet *set, CharSet *setToIsect);

int setSize(CharSet *set);

void setShow(CharSet *set);

#endif
