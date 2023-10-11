#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p)
{
    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    PyBytesObject *byte_obj = (PyBytesObject *)p;

    printf("  size: %ld\n", PyBytes_GET_SIZE(byte_obj));
    printf("  trying string: %s\n", byte_obj->ob_sval);

    printf("  first %ld bytes:", PyBytes_GET_SIZE(byte_obj));

    for (long int i = 0; i < PyBytes_GET_SIZE(byte_obj); i++)
    {
        printf(" %02x", (unsigned char)byte_obj->ob_sval[i]);
    }

    printf("\n");
}

void print_python_list(PyObject *p)
{
    printf("[*] Python list info\n");
    long int size = ((PyVarObject *)(p))->ob_size;
    PyListObject *list = (PyListObject *)p;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (long int i = 0; i < size; i++)
    {
        PyObject *obj = list->ob_item[i];
        const char *type_name = Py_TYPE(obj)->tp_name;
        printf("Element %ld: %s\n", i, type_name);
        if (PyBytes_Check(obj))
            print_python_bytes(obj);
    }
}
