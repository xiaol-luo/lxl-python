#include <Python.h>
#include <string>

#include "Python.h"

#ifdef MS_WINDOWS
int wmain(int argc, wchar_t **argv)
{
	Py_SetPath(L""
#ifdef PY_MODULE_SEARCH_DIR
		PY_MODULE_SEARCH_DIR ";"
#endif // PY_MODULE_SEARCH_DIR

#ifdef CUSTOM_MODULE_SEARCH_DIR
		CUSTOM_MODULE_SEARCH_DIR ";"
#endif // CUSTOM_MODULE_SEARCH_DIR
	);

	int ret = Py_Main(argc, argv);
	return ret;
}
#else
int main(int argc, char **argv)
{
	Py_SetPath(L""
#ifdef PY_MODULE_SEARCH_DIR
		PY_MODULE_SEARCH_DIR ";"
#endif // PY_MODULE_SEARCH_DIR
	);
	return _Py_UnixMain(argc, argv);
}
#endif

/*

int main(int argc, char ** argv)
{


	Py_Main(argc, argv);
	Py_Initialize();

	PyRun_SimpleString("from time import time,ctime \n" 
		"print('Today is', ctime(time()) )");
	Py_Finalize();

	return 0;
}
*/