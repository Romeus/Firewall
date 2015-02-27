#!/usr/bin/env python
"""
Firewall based on whitelist rules
"""
import os
from libmproxy import flow, proxy
from libmproxy.proxy.server import ProxyServer


class Firewall(flow.FlowMaster):
    def run(self):
        try:
            flow.FlowMaster.run(self)
        except KeyboardInterrupt:
            self.shutdown()

    def handle_request(self, f):
        f = flow.FlowMaster.handle_request(self, f)
        if f:
            f.reply()
        return f

    def handle_response(self, f):
        f = flow.FlowMaster.handle_response(self, f)
        if f:
            f.reply()
        #print f
        return f


config = proxy.ProxyConfig(
    port=8080,
    cadir="~/.mitmproxy/"
)
state = flow.State()
server = ProxyServer(config)
m = Firewall(server, state)
m.load_script('whitelist.py')
m.run()
