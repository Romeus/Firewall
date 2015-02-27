from libmproxy.protocol.http import HTTPResponse
from netlib.odict import ODictCaseless

"""
Reject requests contained in whitelist.txt
"""

with open ("whitelist.txt", "r") as my_whitelist_file:
    whitelist = my_whitelist_file.readlines()
    whitelist = map(lambda s: s.rstrip('\n'), whitelist)
    print whitelist

with open ("access_denied_template.html", "r") as myfile:
    template=myfile.read()

def request(context, flow):

#    with open ("access_denied_template.html", "r") as myfile:
#        template=myfile.read()

    # pretty_host(hostheader=True) takes the Host: header of the request into account,
    # which is useful in transparent mode where we usually only have the IP otherwise.

    # Method 1: Answer with a locally generated response
    header = flow.request.pretty_host(hostheader=True)
    if not header in whitelist:
        resp = HTTPResponse(
            [1, 1], 200, "OK",
            ODictCaseless([["Content-Type", "text/html"]]),
            template.replace('$URL', flow.request.pretty_host(hostheader=True)))
        flow.reply(resp)
