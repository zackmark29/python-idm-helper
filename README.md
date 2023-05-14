# Python IDM Helper
**Python IDM Helper** will let you send any link inside python directly to IDM.

You can use this to automate your tool if you want better download speed with IDM.

---
## **EXAMPLE USAGE**:
```python
from pathlib import Path

from idm import IDMHelper

url = 'https://www.internetdownloadmanager.com/idman401.exe'
output_folder = Path.cwd()
output_filename = 'idman.exe'
flag = 3
idm = IDMHelper()
idm.send_link_to_idm(url, str(output_folder), output_filename, flag)
```
---

## PARAMETERS

- ``bstrUrl`` - Url to download
- ``bstrReferer`` - Referer
- `bstrCookies` - cookies
- `bstrData` - PostData (if using POST method)
- `bstrUser` - UserName (if server requires authentication)
- `bstrPassword` - Password
- `bstrLocalPath` - LocalPath (where to save a file on your computer)
- `bstrLocalFileName` - LocalFileName (file name to save with)
- `lFlags` - Flags, can be zero or a combination of the following values:  
  - `1` - do not show any confirmations dialogs;  
  - `2` - add to queue only, do not start downloading.
- `reserved1` - can be used to set a specific user-agent header with the following way:
    reserved1.vt = VT_BSTR;  
    reserved1.bstrVal = pbstrUA;  
    if you don’t need to specify a user agent, then `reserved1.vt` should be set to **`VT_EMPTY`**;
- `reserved2` - not used, you should set reserved2.vt to `*VT_EMPTY*`;
---
API REFERENCES:
- http://www.internetdownloadmanager.com/support/idm_api.html
- https://stackoverflow.com/a/22618308/14951175
---