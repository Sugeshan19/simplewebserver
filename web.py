from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<head>
    <title>saveetha engineering collage</title>
    
</head>
<body >
    <style>
        table,th,td{    
        border : 2px solid yellow;
        }
        body{
            background-color: black;
            color: white;
        }
    </style>
<center>
   <table>
    <tr>
        <th>APPLICATION LAYER</th>
        <TH>TRANSPORT LAYER</TH>
        <TH>INTERNET LAYER</TH>
        <TH>NETWORK ACCESS LAYER</TH>
    </tr>
    <tr>
        <td>HTTP <br> FTP<br> DNS<br> TELNET <br></td>
        <td>TCP<br>
            UDP</td>
        <TD>IPv4<br>IPv6</TD>
        <td>ETHERNET</td>
    </tr>
   </table>
</center>
</body>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()