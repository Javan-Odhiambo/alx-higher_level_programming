#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

#define IS_PALINDROME 1
#define NOT_PALINDROME 0
/**
 * is_palindrome - checks if a single linked list is a palindrome.
 * @head: Address of the head.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t **pointers;
	size_t arr_size = 1;
	listint_t *trav;
	int counter = 0;
	int middle = 0;

	if (head == NULL || *head == NULL)
		return (IS_PALINDROME);

	pointers = (listint_t **) malloc(sizeof(listint_t) * arr_size);
	if (pointers == NULL)
	{
		printf("Error allocating memory\n");
		exit(1);
	}

	trav = *head;
	while (trav)
	{
		pointers[counter] = trav;
		counter++;
		arr_size++;
		pointers = (listint_t **) realloc(pointers, sizeof(listint_t) * arr_size);
		trav = trav->next;
	}
	pointers[counter] = NULL;

	middle = counter / 2;

	for (int i = 0; i <= middle; i++)
	{
		if (pointers[i]->n != pointers[counter - i - 1]->n)
			return (NOT_PALINDROME);
	}
	free(pointers);
	return (IS_PALINDROME);
}
