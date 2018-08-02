#!/opt/comcast/interpreters/python-3.3.2/bin/python3.3

import natprov_ntp


#checking NTP and comparing it to the OS clock. If this is out of sync. The function will auto fix
natprov_ntp.test()
