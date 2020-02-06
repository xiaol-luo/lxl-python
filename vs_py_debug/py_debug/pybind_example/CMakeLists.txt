CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

SET(project_name pybind_example)
PROJECT(${project_name})

INCLUDE_DIRECTORIES(${PROJECT_SOURCE_DIR})


SET(all_files 
	"pybind_example.cpp"
)


LINK_LIBRARIES(python37_d)
ADD_LIBRARY(${project_name} SHARED ${all_files})






