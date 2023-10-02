#include "lists.h"
#include <stdlib.h>
/**
 *check_cycle-checks the presence of cycle
 *@list: pointer to listint_t
 *Return: 0 if there is no cycle, else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *nocyc, *cyc;

	if (!list || !(*list).next)
	return (0);

	cyc = list;
	nocyc = (*list).next;

	while (nocyc && (*nocyc).next && cyc && (*cyc).next)
	{
		if (nocyc == cyc)
			return (1);
		nocyc = nocyc->next->next;
		if (!nocyc)
			break;
		cyc = (*cyc).next;
	}
	return (0);
}
