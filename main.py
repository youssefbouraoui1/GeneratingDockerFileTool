from generateDockerFile import generateDockerFile
from identifyingProjectType import detectProjectType
from formatDockerFile import formatDockerFile_v2
import os

def main():
    projectType = detectProjectType()

    if projectType=="maven":
        pom_path = "pom.xml"

        if not os.path.exists(pom_path):
            print("pom.xml not found in the current directory.")
            return
        with open(pom_path,"r",encoding="utf-8") as f:
            project_info = f.read()
        
        docker_file = generateDockerFile(project_info)
        docker_file = formatDockerFile_v2(docker_file)

        with open("Dockerfile", "w", encoding="utf-8") as f:
            f.write(docker_file)

    print("Dockerfile generated successfully!")

if __name__ == "__main__":
    main()