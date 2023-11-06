#include "lists.h"
/**
* is_palindrome - checks if the list is palindrome
* @head: the address of the head of the list
* Return: 1 if true 0 if false
*/
int is_palindrome(listint_t **head)
{
	if (!head || !*head)
	{
		return (1);
	}
	return (aux_palindrome(head, *head));
}
/**
* aux_palindrome - checks if the list is palindrome
* @head: the address of the head of the list
* @tail: the end of the list
* Return: 1 if true 0 if false
*/
int aux_palindrome(listint_t **head, listint_t *tail)
{
	if (tail == NULL)
	{
		return (1);
	}
	if (aux_palindrome(head, tail->next) && (*head)->n == tail->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
