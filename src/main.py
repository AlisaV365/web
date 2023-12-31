from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 3000


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        with open('./contacts.html', "r", encoding="utf-8") as file:
            html_content = file.read()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(html_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
