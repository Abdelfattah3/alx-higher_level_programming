#include "lists.h"
/**
* check_cycle - checks if the list has cycle
* @list: the list to be checked
* Return: 1 if true 0 if false
*/
int check_cycle(listint_t *list)
{
	listint_t *c;
	listint_t *a;

	if (!list)
	{
		return (0);
	}
	c = list;
	a = list;
	while (a && a->next)
	{
		c = c->next;
		a = a->next->next;
		if (a == c)
		{
			return (1);
		}
	}
	return (0);
}
