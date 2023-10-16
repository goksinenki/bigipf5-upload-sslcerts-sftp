# bigipf5-upload-sslcerts-sftp
A script to upload new ssl certificates to multiple F5 LTM Load Balancers and create SSL certificates on devices

Tested on Windows with PyCharm

Put the SSL files (.cert  .key RootCA.crt ) in the same directory with script

That script reads the F5 IP addresses from bigipf5ips.txt and connect the devices in the list one by one with SCP and upload the files to required directory.
Then you can execute the commands below on the devices to create a new certificate.

install /sys crypto cert SSLcertname from-local-file /config/ssl/ssl.crt/SSLcertname.crt
install /sys crypto key SSLcertname from-local-file /config/ssl/ssl.key/SSLcertname.key
install /sys crypto cert DigiCertRootG2 from-local-file /config/ssl/ssl.crt/DigiCertRootG2.crt


bigipf5ips.txt content example 

IP1
IP2

filenames.txt content example 

DigiCertRootG2.crt
sslfilename.crt
sslfilename.key

![image](https://github.com/goksinenki/bigipf5-upload-sslcerts-sftp/assets/917944/d98b03b5-09d0-4934-a23e-1eb48d853ca0)


You can contact me if you need



Bye 




