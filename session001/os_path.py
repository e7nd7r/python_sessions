import sys
import os
import time

# Sys library

print(sys.version)

# Os library
print(os.listdir())
print(os.getcwd())
# os.mkdir("test")

print(os.getcwd())

assert os.path.exists("./canis") == True
assert os.path.isfile("./canis") == False
assert os.path.isfile("./canis/lupus.json") == True
assert os.path.abspath("./canis").find("/canis") != -1
assert os.path.basename('./canis/latrans.json') == "latrans.json"
assert os.path.commonpath(["/canis/a", "/canis/a", "/canis/a/c"]) == "/canis/a"
assert os.path.dirname("/canis/a/latrans.json") == "/canis/a"
assert os.path.lexists("./canis") == True
assert os.path.expanduser("~").find("/home")
assert ".config" in os.listdir((os.path.expanduser('~')))

os.environ["HOME"] = "/home/test" 
assert os.path.expandvars('$HOME') == "/home/test"

atime = os.path.getatime('./canis/lupus.json')
readable_atime = time.ctime(atime)

print("", readable_atime)

assert os.path.getsize('./canis/lupus.json') >= 0
# print(os.path.isjunction('/canis')) added 3.12

assert os.path.islink('./canis') == False
assert os.path.ismount('./canis') == False

