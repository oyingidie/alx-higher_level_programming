#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts number into sorted singly linked list
 * @head: Pointer to the head of linked list
 * @number: Integer value to be inserted
 *
 * Return: Address of the new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new = NULL;
	listint_t *temp = NULL;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (current && current->n < number)
		{
			temp = current;
			current = current->next;
		}

		temp->next = new;
		new->next = current;
	}

	return (new);
}
