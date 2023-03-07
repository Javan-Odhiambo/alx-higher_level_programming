#include "lists.h"
#include <stdlib.h>

/**
* insert_node - inserts a node into an ordered singly linked list
* @head: Address of the head
* @number: Number to be inserted.
* Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode;
	listint_t *trav;
	listint_t *prev;

	if (head == NULL)
		return (NULL);

	newNode = (listint_t *) malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->n = number;

	if (*head == NULL)
	{
		*head = newNode;
		return (newNode);
	}

	trav = *head;
	prev = *head;
	while (trav->n < number)
	{
		prev = trav;
		trav = trav->next;
	}

	newNode->next = trav;
	prev->next = newNode;

	return (newNode);
}
