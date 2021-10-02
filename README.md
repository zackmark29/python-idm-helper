# python-idm-helper
Use IDM Api in python.

# EXAMPLE
```python

import os
url = 'http://www.internetdownloadmanager.com/idman401.exe'
output_folder = os.getcwd()
output_filename = 'idman.exe'
user_agent = None
flag = 3 #see above the flag information
IDMHelper(url, output_folder, output_filename, flag, user_agent=user_agent).send_to_IDM()

```
API REFERENCE: http://www.internetdownloadmanager.com/support/idm_api.html
https://stackoverflow.com/a/22618308/14951175

Ps. I just made this idm helper for my python tools. Because my download speed is so slow when using built in downloader or aria2c. 
Hope this will be helpful to you also :)
