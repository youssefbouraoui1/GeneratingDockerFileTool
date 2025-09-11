import os

def detectProjectType():

    springBootFileName = "pom.xml"
    entries = os.listdir('.')
    files = set()
    for entry in entries:
        if os.path.isfile(entry):
            files.add(entry)
    if springBootFileName in files:
        return "spring"
    else:
        return "unkonwn"

print("hello")
