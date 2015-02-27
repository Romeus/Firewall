How to use firewall:

1. Install mitmproxy
   1.1. Install prerequisites as described here:

        http://mitmproxy.org/doc/install.html  

        For example for debian-based systems:
        $ sudo apt-get install build-essential python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev

   1.2. Install mitmproxy with python package manager:
     
        $ pip install mitmproxy  

2. Edit file 'whitelist.txt'. It contains list of domains  
   Note: That file must no contain any space before or after domain names.

3. Edit file 'access_denied_template.html'. It's name is self described. '$URL' is placeholder for domain name. 

4. Configure your web client's (e.g. your browser) proxy settings to firewall's bind address: 127.0.0.1:8080 

5. Run firewall from command line:
   $./firewall.py 

6. Test it!
