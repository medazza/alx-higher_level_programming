#include "lists.h"

/**
 * is_palindrome - Checks if singly linked_list is a palindrome.
 * @head: head of the linked_list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         Or if the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palindorme(head, *head));
}

/**
 * aux_palindrome - know how if is it palin.
 * @top: list head
 * @bot: end of list
 * Return: 0 or 1
 */

int aux_palindrome(listint_t **top, listint_t *bot)
{
	if (bot == NULL)
		return (1);
	if (aux_palindrome(top, bot->next) && (*top)->n == bot->n)
	{
		*top = (*top)->next;
		return (1);
	}
	return (0);
}
