#include <Python.h>




/* Define C function */
 
unsigned long int c_factorial(unsigned long int n)
{
    if (n < 1)
        return 1;
    else
        return n * c_factorial(n - 1);
}



/* Link C function to *PyObject via PyBuildValue */

static PyObject* factorial(PyObject* self, PyObject* args)
{
    unsigned long int n;
 
    if (!PyArg_ParseTuple(args, "l", &n))
        return NULL;
 
    return Py_BuildValue("l", c_factorial(n));
}

static PyObject* version(PyObject* self)
{
    return Py_BuildValue("s", "BETA");
}
 
static PyMethodDef Methods[] = {
    {"factorial", factorial, METH_VARARGS, "C factorial function"},
    {"version", (PyCFunction)version, METH_NOARGS, "Returns the version."},
    {NULL, NULL, 0, NULL}
};
 
static struct PyModuleDef cfactorial = {
	PyModuleDef_HEAD_INIT,
	"cfactorial",
	"C Factorial Function",
	-1,
	Methods
};

PyMODINIT_FUNC PyInit_cfactorial(void)
{
    return PyModule_Create(&cfactorial);
}
