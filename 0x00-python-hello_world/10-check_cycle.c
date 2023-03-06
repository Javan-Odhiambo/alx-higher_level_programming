#include "lists.h"

/**
 * check_cycle - checks for a cycle in a linked list.
 * @list:pointer to the first element of the linked list.
 * Return: 0 if no cycle is found and 1 if a cycle is found else -1.
*/

int check_cycle(listint_t *list)
{
	listint_t *hare = list;
	listint_t *tortoise = list;

	if (list == NULL)
		return (0);


	while(hare && hare->next)
	{	
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
