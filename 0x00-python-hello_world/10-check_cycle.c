#include "lists.h"
/**
 * check_cycle - checks if a singly list has a cycle
 * @list: The list to be checked
 *
 * Return: 0 if there is no cycle, and 1 if there is.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr = list;
	listint_t *fast_ptr = list;

	if (list == NULL)
	{
		return (0);
	}
	while (slow_ptr && fast_ptr && fast_ptr->next)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;

	if (slow_ptr == fast_ptr)
		return (1);
	}
	return (0);
}
