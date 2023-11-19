from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body><form enctype="multipart/form-data" method="post"><input name="file" type="file"/><input type="submit"/></form></body></html>')

    def do_POST(self):
        content_type, pdict = cgi.parse_header(self.headers.get('content-type'))
        pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
        if content_type == 'multipart/form-data':
            fields = cgi.parse_multipart(self.rfile, pdict)
            file_data = fields.get('file')
            if file_data:
                # You can process or save the file_data here
                with open('uploaded_file', 'wb') as file:
                    file.write(file_data[0])
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"File uploaded successfully.")
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"No file was uploaded.")
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Unsupported Media Type.")

if __name__ == "__main__":
    port = 8000
    server = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    print(f"Server started on localhost:{port}")
    server.serve_forever()
