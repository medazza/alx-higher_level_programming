#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if list cycle.
 * @list: linked list to check (pointer).
 *
 * Return: 1 if the list has a cycle, 0 otherwise.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_one = list, *fast_one = list;

	if (!list)
		return (0);
	while (slow_one && fast_one && fast_one->next)
	{
		slow_one = slow_one->next;
		fast_one = fast_one->next->next;
		if (slow_one == fast_one)
			return (1);
	}
	return (0);
}
