import http.server
import socketserver
Handler = http.server.SimpleHTTPRequestHandler
def serve(port):
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"Serving at http://localhost:{port}/")
        httpd.serve_forever()
try:
    PORT = int(input("Enter port number (default 3000): ") or 3000)
except ValueError:
    print("Invalid input. Using default port 3000.")
    PORT = 3000
serve(PORT)