// depending on distros, the exact path or Python version may vary.
#include </usr/include/python2.7/Python.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    PyObject *pName, *pModule, *pDict, *pFunc;
    PyObject *pArgs, *pValue;

    Py_Initialize();

    PySys_SetPath("/home/galo/python-modules");  // path to the module to import
    pName = PyString_FromString(argv[1]);

    pModule = PyImport_Import(pName);
    if (pModule != NULL) {
        PyObject *pythonArgument;
        pythonArgument = PyTuple_New(1);
        pValue = PyString_FromString(argv[3]);

        if (pValue == NULL) {
            return 1;
        }
        PyTuple_SetItem(pythonArgument, 0, pValue);
        pFunc = PyObject_GetAttrString(pModule, argv[2]);
        if (pFunc && PyCallable_Check(pFunc)) {
            pValue = PyObject_CallObject(pFunc, pythonArgument);
            if (pValue != NULL) {
                printf("Value returuend from the function %s", PyString_AsString(pValue));
            } else {
                PyErr_Print();
            }
        } else {
            if (PyErr_Occurred())
                PyErr_Print();
            fprintf(stderr, "Cannot find function \"%s\"\n", argv[2]);
        }
    }
    else {
        PyErr_Print();
        fprintf(stderr, "Failed to load \"%s\"\n", argv[1]);
        return 1;
    }
}
