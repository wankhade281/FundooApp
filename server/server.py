import sys

import jwt

sys.path.insert(0, '/home/admin1/PycharmProjects/FundooApp/')
from http.server import HTTPServer, BaseHTTPRequestHandler
from view.registration import FormDetails
from view.responce import Response


class Server(BaseHTTPRequestHandler):  # This class is used to perform operations related to http request
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, message):
        """This just generates an HTML document that includes `message`
        in the body."""
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")  # NOTE: must return a bytes object!

    def do_GET(self):
        self._set_headers()
        if self.path == '/register':
            with open('template/registration.html', 'r') as f:
                html_string_register = f.read()
                self.wfile.write(self._html(html_string_register))
        elif self.path == '/login':
            with open('template/login.html', 'r') as f:
                html_string_register = f.read()
                self.wfile.write(self._html(html_string_register))
        elif self.path == '/forget':
            with open('template/forget_password.html', 'r') as f:
                html_string_register = f.read()
                self.wfile.write(self._html(html_string_register))
        elif 'new' in self.path:
            from urllib.parse import urlparse, parse_qs
            query_comp = parse_qs(urlparse(self.path).query)
            token = query_comp["new"][0]
            with open('template/reset.html', 'r') as f:
                html_string_register = f.read()
                output = html_string_register.format(result=token)
                self.wfile.write(self._html(output))
        elif self.path == '/read':
            obj = FormDetails
            obj.read(self)
        else:
            with open('template/error.html', 'r') as f:
                html_string_register = f.read()
                self.wfile.write(self._html(html_string_register))

    def do_PUT(self):
        obj = FormDetails
        if self.path == '/update':
            obj.update(self)

    def do_DELETE(self):
        obj = FormDetails
        if self.path == "/delete":
            obj.delete(self)

    def do_POST(self):
        # do database operations with posted data
        obj = FormDetails
        if self.path == "/register":
            obj.register(self)
        elif self.path == "/login":
            obj.login(self)
        elif self.path == '/login/forget':
            obj.forget_password(self)
        # elif self.path == "/gettoken":
        #     obj.gettoken(self)
        elif self.path == '/create':
            obj.create(self)
        elif 'new' in self.path:
            from urllib.parse import urlparse, parse_qs
            query_comp = parse_qs(urlparse(self.path).query)
            token = query_comp["token"][0]
            token = jwt.decode(token, "secret", algorithm='HS256')
            obj.set_password(self, token['email'])
        else:
            responce_data = {'success': False, 'data': [], 'message': "Invalid URL"}
            Response(self).jsonResponse(status=404, data=responce_data)


def run(server_class=HTTPServer, handler_class=Server, addr="localhost", port=8080):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    print(f"httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run(HTTPServer, Server, "localhost", 8080)
