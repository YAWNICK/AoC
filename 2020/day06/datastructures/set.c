#include <stdlib.h>
#include <stdio.h>
#include "set.h"

CharSet *CharSetComp() {
   CharSet *set = (CharSet*) malloc(sizeof(CharSet));
   set->head = NULL;
   return set;
}

int setAdd(CharSet *set, char val) {
    Entry *e = set->head;
    Entry *last = e;
    while (e != NULL) {
        if (e->val == val) return -1;
        if (e->next == NULL) last = e;
        e = e->next;
    }
    Entry *new = (Entry*) malloc(sizeof(Entry));
    new->val = val;
    new->next = NULL;
    if (last != NULL) {
        last->next = new;
    } else {
        set->head = new;
    }
    return 0;
}

int setRemove(CharSet *set, char val) {
    Entry *e = set->head;
    if (e == NULL) return -1;
    Entry *last = NULL;
    while (e->val != val && e->next != NULL) {
        last = e;
        e = e->next;
    }
    if (e->next == NULL && e->val != val) return -1;
    //here i need to remove e
    if (last != NULL) {
        last->next = e->next;
    } else {
        set->head = e->next;
    }
    free(e);
    return 0;
}

int setContains(CharSet *set, char val) {
    Entry *e = set->head;
    while (e != NULL) {
        if (e->val == val) return 1;
        e = e->next;
    }
    return 0;
}

int setUnite(CharSet *set, CharSet *setToUnite) {
    // this function could be optimized
    Entry *uEntry = setToUnite->head;
    while (uEntry != NULL) {
        setAdd(set, uEntry->val);
        uEntry = uEntry->next;
    }
    return 0;
}

int setIntersect(CharSet *set, CharSet *setToIsect) {
    Entry *eTest = set->head;
    while (eTest != NULL) {
        char val = eTest->val;
        eTest = eTest->next;
        if (!setContains(setToIsect, val)) {
            setRemove(set, val);
        }
    }
    return 0;
}

int setSize(CharSet *set) {
    Entry *e = set->head;
    int size = 0;
    while (e != NULL) {
        size++;
        e = e->next;
    }
    return size;
}

void setShow(CharSet *set) {
    Entry *e = set->head;
    while (e != NULL) {
        printf("%c", e->val);
        e = e->next;
    }
    printf("\n");
}
