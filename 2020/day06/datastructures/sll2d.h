#ifndef LL2D_H
#define LL2D_H

typedef struct _StringEntry {
    char *string;
    struct _StringEntry *next;
} StringEntry;

typedef struct _ListEntry {
    StringEntry *stringList;
    struct _ListEntry *next;
} ListEntry;

typedef struct _StringLinkedList {
    ListEntry *head;
} StringLinkedList;

StringLinkedList *StringLinkedListComp();

ListEntry *sllNewListEntry(StringLinkedList *sll);

void sllNewStringEntry(ListEntry *le, char *string);

void sllShow(StringLinkedList *sll);

#endif
