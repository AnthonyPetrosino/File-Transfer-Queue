
myhost = input("myhost > ").strip()
mypwd = input("mypwd > ").strip()
myuser = "sftpuser"

import paramiko
from datetime import datetime
myport = 22
# Setup transport object for SFTP connection
with paramiko.Transport((myhost, myport)) as transport:
    transport.connect(None,username=myuser, password=mypwd)
    # Create SFTP client
    with paramiko.SFTPClient.from_transport(transport) as sftp:
        # Put the file
        sftp.put('sftptasks.csv', f"/uploads/sftptasks{datetime.utcnow().strftime('%Y%m%d%H')}.csv")
        # List the files
        print("Remote contents: ", sftp.listdir("/uploads/"))
        # Get the file
        sftp.get(f"/uploads/sftptasks{datetime.utcnow().strftime('%Y%m%d%H')}.csv", "sftptasks.csv")
        # Delete the file
        # sftp.remove("/uploads/tutorial")
        # list the files again
        print("*" * 20)
        print("Final contents: ", sftp.listdir("/uploads/"))