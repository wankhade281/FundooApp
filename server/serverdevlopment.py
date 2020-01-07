from http.server import BaseHTTPRequestHandler, HTTPServer

import sys

sys.path.insert(0, '/home/admin1/PycharmProjects/FundooApp/')
from view.profile import Profile, ListingPages


class ProfilePic(BaseHTTPRequestHandler):  # This class is used to perform operations related to http request

    def do_GET(self):
        p = Profile
        if self.path == '/profile/read':
            p.read_pic()
        # self.l.isArchieve(self)

    # def do_PUT(self):
    #     self.p.update_pic(self)
    #     self.l.isArchieve(self)
    #     self.l.isTrash(self)

    # def do_DELETE(self):
    #     self.p.delete_pic(self)

    # def do_POST(self):
    #     self.p.create_pic(self)
    #     self.l.isPinned(self)


def run(server_class=HTTPServer, handler_class=ProfilePic, addr="localhost", port=8080):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    print(f"httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run(HTTPServer, ProfilePic, "localhost", 8080)
