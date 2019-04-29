# 

import os
import sys
import platform
import subprocess
from threading import Thread

# import src


txt = """
<VirtualHost {{ServerName}}:80>
    DocumentRoot \"{{DocumentRoot}}\"
    ServerName {{ServerName}}
    ErrorLog \"/usr/local/var/log/httpd/{{ServerName}}-error_log\"
    CustomLog \"/usr/local/var/log/httpd/{{ServerName}}-access_log\" combined
    <Directory \"{{DocumentRoot}}\">
        Require all granted
    </Directory>
</VirtualHost>
"""


def writeVHost():
    f = open("demofile2.txt", "a")
    f.write(txt)
    f.close()
    pass


def main():
    # Thread(target = serve).start()
    Thread(target = writeVHost).start()
    print(os)
    print(platform.system())
    os.system('apachectl -V | grep SERVER_CONFIG_FILE')
    pass


if __name__ == '__main__':
    main()
    # print('This program is being run by itself')
    # print(parameter)
    # print(app)
    # doit('fuck')
else:
    main()
    print('I am being imported from another module')

# https://stackoverflow.com/questions/22492162/understanding-the-main-method-of-python
