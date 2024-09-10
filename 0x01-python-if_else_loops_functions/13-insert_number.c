#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a node into a sorted singly linked list
 * @head: start node
 * @number: new node number
 * Return: updated list
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL, *itr = NULL, *tmp = NULL;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	itr = *head;

	while (itr && itr->next->n < number)
		itr = itr->next;

	if (!itr)
		return (NULL);

	tmp = itr->next;
	itr->next = new_node;
	new_node->next = tmp;

	return (*head);
}
