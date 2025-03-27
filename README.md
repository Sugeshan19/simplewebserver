# EX01 Developing a Simple Webserver
## name: sugeshan
## reg.no: 212224040337
## Date:27.03.2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.


## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
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
```

## OUTPUT:

![alt text](<Screenshot 2025-03-27 111303.png>)

![alt text](<Screenshot 2025-03-27 111322.png>)


## RESULT:
The program for implementing simple webserver is executed successfully.
