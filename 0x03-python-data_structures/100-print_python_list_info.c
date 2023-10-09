#include <Python.h>

/**
 * print_python_list_info - Prints  info basic about the  Python lists.
 * @p: A Python Object list.
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int ind;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (ind = 0; ind < size; ind++)
		printf("Element %ind: %s\n", ind, Py_TYPE(obj->ob_item[ind])->tp_name);
}
