#include "lists.h"
/**
 * check_cycle - checks if the linked has a cycle
 * @list: linked list head pointer
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = NULL, *fast = NULL;
	size_t counter = 0, safety_counter = 0;

	if (!list)
		return (0);

	slow = list;
	fast = list->next;

	while (fast && fast->next && slow)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next;
	}

	return (0);
}
