#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - returns python list infos
 * @p: PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyObject *item;
	PyListObject *list = (PyListObject *)p;
	int s, i, a;

	s = Py_SIZE(p);
	a = (*list).allocated;
	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", a);

	for (i = 0; i < s; i++)
	{
	item =  PyList_GetItem(p, i);
	printf("Element %d: %s\n", i, Py_TYPE(i)->tp_name);
	}
}
