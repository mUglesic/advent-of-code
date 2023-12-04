#include <stdio.h>
#include <stdlib.h>

struct List {
    struct ListElement  *first;
    struct ListElement  *last;
    int                 size;
};

struct ListElement {
    struct element      *el;
    struct ListElement  *next;
};

struct element {
    long    address;
    long    value;
};

// FUNCTION DECLARATIONS

// // GETTERS

struct ListElement *listGetByIndex(struct List *l, int index);

int listGetIndex(struct List *l, struct element *e);

// // PRINTING

void listPrintAll(struct List *l);

void listPrintFirst(struct List *l);

void listPrintLast(struct List *l);

void listPrintElement(struct ListElement *le);

// // CLEANING MEMORY

void listCleanListElement(struct ListElement *le);

///////////////////////////////////////////////

// UTIL FUNCTIONS

int listMatchElement(struct element *e1, struct element *e2);

long listGetElementValue(struct ListElement *le);

///////////////////////////////////////////////

struct ListElement *createListElement(struct element *e) {
    struct ListElement *le = malloc(sizeof(struct ListElement));
    le->el = e;
    le->next = NULL;
    return le;
}

struct List createList() {
    struct List list;
    struct ListElement *first = createListElement(NULL);
    list.first = first;
    list.last = first;
    list.size = 0;
    return list;
}

struct element *createElement(long address, long value) {
    struct element *e = malloc(sizeof(struct element));
    e->address = address;
    e->value = value;
    return e;
}

void listAdd(struct List *l, struct element *e) {
    struct ListElement *le = createListElement(e);

    if (l->size == 0) {
        l->first->next = le;
        l->last->next = le;
    }
    else {
        l->last = l->last->next;
        l->last->next = le;
    }

    l->size++;
}

void listRemove(struct List *l, int index) {
    if (index >= l->size || index < 0) {
        return;
    }

    struct ListElement *le = l->first;
    int i = 0;

    while (i != index) {
        le = le->next;
        i++;
    }

    struct ListElement *toDelete = le->next;

    if (l->size == 1) {
        l->first->next = NULL;
        // printf("%p %p\n", NULL, l->first->next);
        l->last = l->first;
    }
    else if (le == l->last) {
        printf("debug 4\n");
        struct ListElement *secondLast = listGetByIndex(l, l->size - 2);
        le->next = NULL;
        secondLast->next = le;
        l->last = secondLast;
    }
    else {
        le->next = le->next->next;
        if (toDelete == l->last) {
            l->last = le;
        }
    }

    l->size--;

    listCleanListElement(toDelete);

}

struct ListElement *listGetByIndex(struct List *l, int index) {
    // printf("Getting element at index: %d\n", index);

    if (index >= l->size || index < 0) {
        return NULL;
    }

    struct ListElement *le = l->first;
    int i = 0;

    while (i != index) {
        le = le->next;
        i++;
    }

    return le;
}

int listGetIndex(struct List *l, struct element *e) {

    struct ListElement *le = l->first;
    int index = 0;

    int found = 0;

    while (le->next) {
        if (listMatchElement(le->next->el, e)) {
            found = 1;
            break;
        }
        index++;
        le = le->next;
    }

    return found ? index : -1;
}

int listMatchElement(struct element *e1, struct element *e2) {
    return e1->address == e2->address;
}

long listGetElementValue(struct ListElement *le) {
	return le->next->el->value;
}

long listSumElements(struct List *l) {
	
	struct ListElement *le = l->first;
	
	long sum = 0;
	
	while (le->next) {
		sum += listGetElementValue(le);
		le = le->next;
	}
	
	return sum;
}

void listPrintAll(struct List *l) {

    struct ListElement *le = l->first;

    printf("List size: %d\n", l->size);

    if (l->size == 0) {
        printf("List is empty!\n");
    }

    // printf("%p\n", l->first->next);

    while (le->next) {
        listPrintElement(le);
        le = le->next;
    }

}

void listPrintFirst(struct List *l) {
    if (l->size == 0) {
        printf("List is empty\n");    
        return;
    }
    printf("First element: ");
    listPrintElement(l->first);
}

void listPrintLast(struct List *l) {
    if (l->size == 0) {
        printf("List is empty!\n");    
        return;
    }
    printf("Last element: ");
    listPrintElement(l->last);
}

void listPrintElement(struct ListElement *le) {
    printf("[Address: %ld, Value: %ld]\n", le->next->el->address, le->next->el->value);
}

void listCleanListElement(struct ListElement *le) {
    free(le->el);
    free(le);
}

// TESTING

// int main() {
    
//     struct List l = createList();

//     listPrintAll(&l);

//     listAdd(&l, createElement(2, 25));
//     listAdd(&l, createElement(14, 7));
//     listAdd(&l, createElement(29, 86));
//     listAdd(&l, createElement(18, 29));
//     listAdd(&l, createElement(15, 111));

//     listPrintAll(&l);
//     listPrintFirst(&l);
//     listPrintLast(&l);

//     listRemove(&l, 3);

//     listPrintAll(&l);
//     listPrintFirst(&l);
//     listPrintLast(&l);

//     listPrintElement(listGetByIndex(&l, 2));

//     printf("Index of element with address 2: %d\n", listGetIndex(&l, createElement(2, 89)));

//     return 0;
// }