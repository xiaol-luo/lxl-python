1.解压Python-3.7.6.tar.xz到某个目录(假设是 "E:/code/Python-3.7.6"),此目录后统称python_code_dir.
2.build python debug版本：cd ${python_code_dir}/PCBuild/ && build.bat -d
3.改CmakeList.txt第五行，：SET(python_code_dir "E:/code/Python-3.7.6")
4.用Cmake工具创建VS工程
5.添加.\scripts\scripts.pyproj到工程
6.拷贝${python_code_dir}/PCBuild/win32/python37_d.*到工作目录
7.