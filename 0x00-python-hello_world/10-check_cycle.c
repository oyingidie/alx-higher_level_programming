#include "lists.h"

/**
 * check_cycle - Checks singly linked list for cycle
 * @list: Linked list
 *
 * Return: 0 if there is no cycle, 1 if there is
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
