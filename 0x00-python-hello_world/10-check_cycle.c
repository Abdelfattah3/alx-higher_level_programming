#include "lists.h"
/**
* check_cycle - checks if the list has cycle
* @list: the list to be checked
* Return: 1 if true 0 if false
*/
int check_cycle(listint_t *list)
{
	listint_t *c;
	int i;

	c = list->next;
	i = list->n;
	if (!list)
	{
		return (0);
	}
	while (c)
	{
		if (c && c->n == i)
		{
			return (1);
		}
		c = c->next;
	}
	return (0);
}
