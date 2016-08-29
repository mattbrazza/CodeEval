#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HASHSIZE 7

typedef struct _node_t_ {
	int index;
	char* key;
	char* value;
	struct _node_t_ *next;
} node_t;

typedef struct _hashtable_t_ {
	int size;
	node_t ** table;
} hashtable_t;


int hash_func(char* str) {
	return (strlen(str)%HASHSIZE);
}

node_t * create_node(char* key, char* val) {
	node_t * ans = (node_t*)malloc(sizeof(node_t));
	ans->index = hash_func(key);
	ans->key = key;
	ans->value = val;
	ans->next = NULL;
	return ans;
}

void print_node(node_t * node) {
	printf("%s-%s\n",node->key,node->value);
	return;
}

void print_hash(hashtable_t * ht) {
	int i, len=ht->size;
	printf("The %d entries (in order):\n",len);
	for (i=0; i<len; i++) {
		if (ht->table[i] != 0) { print_node(ht->table[i]); }
	}
	printf("\n");
	return;
}

int choosing(hashtable_t *, int);

int main(int argc, char* argv[]) {
	int size = (argc > 1) ? atoi(argv[1]) : HASHSIZE;
	hashtable_t * hashtable = (hashtable_t*)malloc(sizeof(hashtable));
	hashtable->size = size;
	hashtable->table = calloc(size, sizeof(node_t *));
	choosing(hashtable, 99);

return 0;
}

int choosing(hashtable_t * hashtable, int choice) {
	char key[16], value[16];
	int index;	
	node_t * node;

	while (choice > 0) {
	printf("Would you like to:\n");
	printf("Insert(1) - Delete(2) - Print Table(3) - Quit(0)\n");
	scanf("%d",&choice);
	switch (choice) {
	case 1:
		printf("Please enter key and value:\n");
		scanf("%s %s",key,value);
		node = create_node(key, value);
		hashtable->table[node->index] = node;
		break;
	case 2:
		printf("Please enter key to be removed:\n");
		scanf("%s",key);
		index = hash_func(key);
		if (hashtable->table[index] != 0) {
			print_node(hashtable->table[index]);
			hashtable->table[index] = 0;
		} else {
			printf("Nothing found\n");
		}
		break;
	case 3: print_hash(hashtable); break;
	case 0: free(hashtable); return 0; break;
	default: printf("Invalid choice...\n"); break;
	}
	printf("\n----------------------\n");
	}
	return 0;
}
