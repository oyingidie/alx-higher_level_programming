#include "lists.h"
#include <stdio.h>

int compare_lists(listint *head, listint_t *middle, int len);
void reverse(listint_t **head);

/**
 * is_palindrome - Checks if singly linked list is a palindrome
 * @head: Double pointer to the first node in the list
 *
 * Return: 0 (not palindrome) or 1 (palindrome)
 */
int is_palindrome(listint_t **head)
{
	int len, i;
	listint_t *tmp;
	listint_t *middle;

	if (head == NULL || *head == NULL)
		return (1);
	tmp = *head;
	middle = *head;

	for (len = 0; tmp != NULL; len++)
		tmp = tmp->next;
	len = len / 2;

	for (i = 1; i < len; i++)
		middle = middle->next;
	if (len % 2 != 0 && len != 1)
	{
		middle = middle->next;
		len = len - 1;
	}
	reverse(&middle);
	i = compare_lists(*head, middle, len);

	return (0);
}

/**
 * compare_lists - Compares two parts of a linked list
 * @head: Pointer to the head node
 * @middle: Pointer to node in the middle
 * @len: Length (number) of nodes
 *
 * Return: 1 if the same, 0 if not
 */
int compare_lists(listint *head, listint_t *middle, int len)
{
	int i;

	if (head == NULL || middle == NULL)
		return (1);
	for (i = 0; i < len; i++)
	{
		if (head->n != middle->n)
			return (0);
		head = head->next;
		middle = middle->next;
	}
	return (1);
}

/**
 * reverse - Reverses elements in a linked list
 * @head: Pointer to head in the list
 */
void reverse(listint_t **head)
{
	listint_t *current;
	listint_t *next;
	listint_t *prev;

	if (head == NULL || *head == NULL)
		return;

	prev = NULL;
	current = *head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
