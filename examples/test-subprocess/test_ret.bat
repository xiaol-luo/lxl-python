
set input_val=%1
test_ret.py %input_val%
echo "errorlevel is %errorlevel%"
rem %errorlevel% is the exitcode of the last process

set return_code=%errorlevel%
echo "return_code is %return_code% " 
exit /b %return_code%
rem use exit /b exit_code to indicate the exit_code of this process