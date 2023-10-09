#include <Python.h>

/**
 * print_python_list_info - Prints  info basic about the  Python lists.
 * @p: A Python Object list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, ind;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	for (ind = 0; ind < size; ind++)
	{
		printf("Element %d: ", ind);
		obj = PyList_GetItem(p, ind);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
