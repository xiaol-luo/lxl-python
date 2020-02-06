#include <Python.h>
#include <string>

#include "Python.h"
#include <pybind11/pybind11.h>

__declspec (dllexport) int add(int a, int b)
{ 
	int ret = a + b;
	return ret;
}

PYBIND11_MODULE(example, m) {
	m.doc() = "pybind11 example plugin"; // optional module docstring

	m.def("add", &add, "A function which adds two numbers");
}
