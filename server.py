import http.server
import socketserver
PORT = 3000
Handler = http.server.SimpleHTTPRequestHandler
def serve(port):
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("serving at port", f'http://localhost:{port}/')
        httpd.serve_forever()
if PORT:
    serve(PORT)
else:
    input = 'Enter Port #'
    serve(input)
