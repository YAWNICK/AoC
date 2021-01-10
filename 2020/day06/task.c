#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "datastructures/set.h"
#include "datastructures/sll2d.h"

#define MAXQS 26

int part1(StringLinkedList *groups);

int part2(StringLinkedList *groups);

int main() {
    FILE *fp;
    fp = fopen("input.txt", "r");
    if (fp == NULL) exit(EXIT_FAILURE);

    StringLinkedList *groups = StringLinkedListComp();  // 2d Linked List of Strings
    ListEntry *group = sllNewListEntry(groups);  // Linked List of Strings
    char line[MAXQS + 2];  // + 2 for '\n\0'
    while (fgets(line, MAXQS + 2, fp) != NULL) {
        if (*line == '\n') {
            group = sllNewListEntry(groups);  // create new group
            continue;
        }
        line[strlen(line) - 1] = '\0';
        sllNewStringEntry(group, line);  // add line to current group
    }

    printf("Part 1: %d\n", part1(groups));
    printf("Part 2: %d\n", part2(groups));

    return 0;
}

int part1(StringLinkedList *groups) {
    int total = 0;
    ListEntry *group = groups->head;
    while (group != NULL) {  // iterate over groups
        StringEntry *panswers = group->stringList;
        // there might be empty groups due to empty lines at the end of the
        // input file
        if (panswers == NULL) break;
        CharSet *groupQuestions = CharSetComp();  // counted Qs for this group
        while (panswers != NULL) {  // iterate over people
            CharSet *pQuestions = CharSetComp();  // Qs for current person
            char *panswer = panswers->string;
            while (*panswer != '\0') {  // iterate over current person's answers
                setAdd(pQuestions, *panswer);
                panswer++;
            }
            setUnite(groupQuestions, pQuestions);
            panswers = panswers->next;
        }
        total += setSize(groupQuestions);
        group = group->next;
    }
    return total;
}

int part2(StringLinkedList *groups) {
    int total = 0;
    ListEntry *group = groups->head;
    while (group != NULL) {  // iterate over groups
        StringEntry *panswers = group->stringList;
        // there might be empty groups due to empty lines at the end of the
        // input file
        if (panswers == NULL) break;
        CharSet *groupQuestions = CharSetComp();  // counted Qs for this group
        // fill groupQuestions with all possible questions
        for (char letter = 'a'; letter <= 'z'; letter++) {
            setAdd(groupQuestions, letter);
        }
        while (panswers != NULL) {  // iterate over people
            CharSet *pQuestions = CharSetComp();  // Qs for current person
            char *panswer = panswers->string;
            while (*panswer != '\0') {  // iterate over Qs for current person
                setAdd(pQuestions, *panswer);
                panswer++;
            }
            setIntersect(groupQuestions, pQuestions);
            panswers = panswers->next;
        }
        total += setSize(groupQuestions);
        group = group->next;
    }
    return total;
}
