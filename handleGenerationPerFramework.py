import os

def handleDjango():
    if os.path.exists("requirements.txt"):
        with open("requirements.txt", "r", encoding="utf-8") as f:
            project_info = f.read()
    elif os.path.exists("pyproject.toml"):
        with open("pyproject.toml", "r", encoding="utf-8") as f:
            project_info = f.read()
    else:
        project_info = "Django project without requirements.txt or pyproject.toml"
    

    return project_info

def findDependeciesByImportsForDjango():
    return
def findDependeciesByVenvForDjango():
    return