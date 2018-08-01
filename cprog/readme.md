C Programming



combine both functions 

hwclock.c = sysclock.c

systime = OS time 

Combine sysclock.c and systime. Then compare the two


Get seconds
min * 60(minutes in a hour)


total seconds for 24 hour format 
time * 3600




formula .. need to compare the time then minutes . 


hour check if hour is not equal to 

for min 
check if one is greater than. 

http://www.programmingnotes.org/?p=2062
https://en.cppreference.com
https://www.boost.org/
https://www.tutorialspoint.com/cplusplus/cpp_date_time.htm

https://isocpp.org/

https://akrzemi1.wordpress.com/2018/07/07/functions-in-std/



=====

requirements 

pip3 install ntplib
pip3 install dateutil
pip3 install six 
if the install for dateutil fails . Use the upgrade option 
Collecting dateutil
Could not find a version that satisfies the requirement dateutil (from versions: )
No matching distribution found for dateutil

pip3 install python-dateutil --upgrade

Verify the version 
pip3 freeze | grep dateutil ?




Lab
export LD_LIBRARY_PATH=/opt/rh/rh-python35/root/usr/lib64
export PATH=$PATH:/opt/rh/rh-python35/root/usr/bin



package notes 
zip -r clock time.sh clock_lib/* demo_prod.py

modified line 8 clock_lib/dateutil/relativedelta.py
to from clock_lib.six import integer_types
