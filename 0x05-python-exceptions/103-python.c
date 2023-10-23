/*
 * File: 103-python.c
 * Author: AZZA Mohamed
 */
#include <stdio.h>
#include <stdlib.h>
#include <floatobject.h>
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_bytes - basic infos about bytes objects.
 * @p: PyObject object byte.
 */

void print_python_bytes(PyObject *p)
{
	unsigned char ind, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %d\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;
	printf("  first %ld bytes:", size);
	for (ind = 0; ind < size; ind++)
	{
		printf("%02hhx", bytes->ob_sval[ind]);
		if (ind == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Func that print info about py float
 * @p: a py object list object.
 */
void print_python_float(PyObject *p)
{
	double fd;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float"))
	{
		printf(" [ERROR] Invalid Float Object\n");
		return;
	}
	fd = ((PyFloatObject *)p)->ob_fval;
	printf(" value: %s\n",
			PyOS_double_to_string(fd, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}

/**
 * print_python_list - basic info about lists in python.
 * @p: a py object list object.
 */

void print_python_list(PyObject *p)
{
	int size, alloc, ind;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", list->alloc);

	for (ind = 0; ind < size; ind++)
	{
		type = list->ob_item[ind]->obj_type->tp_name;
		printf("Element %d: %s\n", ind, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[ind]);
                else if (strcmp(type, "float") == 0)
                        print_python_float(list->ob_item[ind]);
	}
}
