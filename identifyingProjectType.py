import os

def detectProjectType():

    mavenProject = "pom.xml"
    gradleProject = "build.gradle"
    gradleKotlinProject = "build.gradle.kts"
    
    entries = os.listdir('.')
    files = set()
    for entry in entries:
        if os.path.isfile(entry):
            files.add(entry)
    if mavenProject in files:
        return "maven"
    elif gradleProject in files:
        return "gradle"
    elif gradleKotlinProject in files:
        return "gradleKotlin"
    else:
        return "unkonwn"

print("hello")
