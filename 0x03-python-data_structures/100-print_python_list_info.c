#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int val = Py_Size(p);
	int x;
	Py_Object *obj = (Py_Object *)p;

	printf("[*] Size of the Python List = %li\n", val);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (x = 0; x < size; x++)
		printf("Element %i: %s\n", x, Py_TYPE(obj->ob_item[x])->tp_name);
}
