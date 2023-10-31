#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
* insert_node - inserts a node in a sorted list
* @head: dounle pointer to the head
* @number: the number to be added
* Return:  pointer to the added node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *pre;

	if (!head || !*head)
	{
		return (NULL);
	}
	new = malloc(sizeof(listint_t));
	if (!new)
	{
		free(new);
		return (NULL);
	}
	new->n = number;
	if ((*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	pre = *head;
	while (pre && pre->next)
	{
		if (pre->next->n > number)
		{
			new->next = pre->next;
			pre->next = new;
			return (new);
		}
		pre = pre->next;
	}
	if (number > pre->n)
	{
		return (add_nodeint_end(head, number));
	}
	return (NULL);
}
