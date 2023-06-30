from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import yaml
import os
import random

settings = {
    "random-port":False,
    "random-port-range": [8000, 655635],
    "file-to-load": "test.htm"
}

if os.path.isfile("config.yml"):
    temp = yaml.safe_load(open("config.yml", "r")) # futurt proofing : staring
    for i in settings:
        if i in temp:
            settings[i] = temp[i]
        else:
            temp[i] = settings[i]
    f = open("config.yml", "w")
    yaml.dump(temp, f)
    f.close() # future proofing : ending
else:
    f = open("config.yml", "w")
    yaml.dump(settings, f)
    f.close()

if (not os.path.isfile("test.htm")) and settings["file-to-load"] == "test.htm":
    f = open("test.htm", "w")
    f.write("<html><body>Hey dummy!</body></html>")
    f.close()

port = 8000 if not settings["random-port"] else random.randint(settings["random-port-range"][0], settings["random-port-range"][1])

httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
webbrowser.open(f"http://localhost:{port}/{settings['file-to-load']}")
httpd.serve_forever()