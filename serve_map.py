import http.server
import socketserver
import os
import webbrowser
from threading import Thread

os.chdir(r'd:\hack4delhi')

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        httpd.serve_forever()

# Start server in background
server_thread = Thread(target=start_server, daemon=True)
server_thread.start()

# Open browser
webbrowser.open(f'http://localhost:{PORT}/infrastructure_map.html')

# Keep server running
import time
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Server stopped")
