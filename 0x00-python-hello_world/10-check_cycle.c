#include "lists.h"
/**
 * check_cycle - checks if the linked has a cycle
 * @list: linked list head pointer
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp = list, *safety_node = NULL;
	size_t counter = 0, safety_counter = 0;

	while (tmp)
	{
		tmp = tmp->next;
		counter++;
		safety_node = list;
		safety_counter = 0;

		while (safety_counter < counter)
		{
			if (safety_node == tmp)
				return (1);
			safety_node = safety_node->next;
			safety_counter++;
		}
	}

	return (0);
}
