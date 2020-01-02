from http.server import BaseHTTPRequestHandler, HTTPServer
import sys

sys.path.insert(0, '/home/admin1/PycharmProjects/FundooApp/')
from view.profile import Profile, ListingPages


class Profile(BaseHTTPRequestHandler):
    def do_GET(self):
        p = Profile
        p.read_pic(self)
        l = ListingPages
        l.isArchieve(self)

    def do_PUT(self):
        p = Profile
        p.update_pic(self)
        l = ListingPages
        l.isArchieve(self)
        l.isTrash(self)

    def do_DELETE(self):
        p = Profile
        p.delete_pic(self)

    def do_POST(self):
        p = Profile
        p.create_pic(self)
        l = ListingPages
        l.isPinned(self)


def run(server_class=HTTPServer, handler_class=Profile, addr="localhost", port=8080):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    print(f"httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run(HTTPServer, Profile, "localhost", 8080)
