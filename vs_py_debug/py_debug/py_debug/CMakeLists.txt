CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

SET(project_name py_debug)
PROJECT(${project_name})

INCLUDE_DIRECTORIES(${PROJECT_SOURCE_DIR})


SET(all_files 
	"main.cpp"
)


LINK_LIBRARIES(python37_d)

SET(python_module_search_dir ${python_code_dir}/Lib)
add_compile_options(-DPY_MODULE_SEARCH_DIR="${python_module_search_dir}") 

SET(custom_module_search_dir "E:/ws/py_debug/Debug")
add_compile_options(-DCUSTOM_MODULE_SEARCH_DIR="${custom_module_search_dir}") 

ADD_EXECUTABLE(${project_name} ${all_files})






