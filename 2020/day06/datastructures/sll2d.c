#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "sll2d.h"

StringLinkedList *StringLinkedListComp() {
    StringLinkedList *sll = (StringLinkedList*) malloc(sizeof(StringLinkedList));
    sll->head = NULL;
    return sll;
}

ListEntry *sllNewListEntry(StringLinkedList *sll) {
    ListEntry *newle = (ListEntry*) malloc(sizeof(ListEntry));
    newle->stringList = NULL;
    newle->next = NULL;
    ListEntry *le = sll->head;
    if (le == NULL) {
        sll->head = newle;
        return newle;
    }
    while (le->next != NULL) le = le->next;
    le->next = newle;
    return newle;
}

void sllNewStringEntry(ListEntry *le, char *string) {
    StringEntry *newse = (StringEntry*) malloc(sizeof(StringEntry));
    newse->string = (char*) malloc(sizeof(char) * (strlen(string) + 1));
    strcpy(newse->string, string);
    newse->next = NULL;
    StringEntry *se = le->stringList;
    if (se == NULL) {
        le->stringList = newse;
        return;
    }
    while (se->next != NULL) se = se->next;
    se->next = newse;
    return;
}

void sllShow(StringLinkedList *sll) {
    ListEntry *le = sll->head;
    while (le != NULL) {
        printf("{");
        StringEntry *se = le->stringList;
        while (se != NULL) {
            printf("%s, ", se->string);
            se = se->next;
        }
        printf("}, ");
        le = le->next;
    }
    printf("\n");
}
