import os
import sys
from hashlib import md5

from pyftpdlib.authorizers import DummyAuthorizer, AuthenticationFailed
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


class DummyMD5Authorizer(DummyAuthorizer):

    def validate_authentication(self, username, password, handler):
        if sys.version_info >= (3, 0):
            password = password.encode('latin1')
        hash = md5(password).hexdigest()
        try:
            if self.user_table[username]['pwd'] != hash:
                raise KeyError
        except KeyError:
            raise AuthenticationFailed


def ftp_server(username:str, passwd:str, port:int):
    # get a hash digest from a clear-text password
    hash = md5(passwd.encode('latin1')).hexdigest()
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyMD5Authorizer()

    # Define a new user having full r/w permissions and a read-only
    # anonymous user
    authorizer.add_user(username, hash, os.getcwd(), perm='elradfmwMT')
    authorizer.add_anonymous(os.getcwd())

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "Here you go."

    # Specify a masquerade address and the range of ports to use for
    # passive connections.  Decomment in case you're behind a NAT.
    #handler.masquerade_address = '151.25.42.11'
    #handler.passive_ports = range(60000, 65535)

    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = ('0.0.0.0', port)
    server = FTPServer(address, handler)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # start ftp server
    server.serve_forever()


def main():
    print("""
    "username, password and port" can be ignored, then default settings is:
    [*] username: user
    [*] password: 123456
    [*] port: 21
    Also, you can type what you want via follow steps!
          """)
    username = input('Input username:')
    password = input('Input password:')
    port = input('Input port:')

    if not username:
        username = 'user'
    if not password:
        password = '123456'
    if not port:
        port = 21

    ftp_server(username, password, port)

if __name__ == '__main__':
    main()