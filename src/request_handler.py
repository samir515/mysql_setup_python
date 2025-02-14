from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs
import user_service

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    # Handle GET requests
    def do_GET(self):
        if self.path == "/users":
            self._set_headers()
            users = user_service.get_users()
            self.wfile.write(json.dumps(users).encode())

    # Handle POST requests (Create User)
    def do_POST(self):
        if self.path == "/users":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            user_data = json.loads(post_data)

            response = user_service.create_user(
                user_data["name"],
                user_data["email"],
                user_data["password"]
            )
            self._set_headers()
            self.wfile.write(json.dumps(response).encode())

    # Handle PUT requests (Update User)
    def do_PUT(self):
        parsed_url = urlparse(self.path)
        if parsed_url.path.startswith("/users/"):
            user_id = int(parsed_url.path.split("/")[-1])

            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            user_data = json.loads(post_data)

            response = user_service.update_user(user_id, user_data.get("name"), user_data.get("email"))
            self._set_headers()
            self.wfile.write(json.dumps(response).encode())

    # Handle DELETE requests (Deactivate User)
    def do_DELETE(self):
        parsed_url = urlparse(self.path)
        if parsed_url.path.startswith("/users/"):
            user_id = int(parsed_url.path.split("/")[-1])

            response = user_service.delete_user(user_id)
            self._set_headers()
            self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
