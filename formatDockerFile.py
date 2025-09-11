

def formatDockerFile_v1(content):
    begining_of_docker_file = "FROM"
    j = 0
    for i in range(len(content)):
        j =i+1
        if content[i] !="`":
            break
    
    while j < len(content):
        if content[j] =="F":
            i = 0
            while j<len(content) and i<len(begining_of_docker_file):
                if content[j] ==begining_of_docker_file[i]:
                    i+=1
                    j+=1

            if i>=len(begining_of_docker_file):
                break

        else:
            j+=1
    r = len(content)

    while r>=0:
        if content[r] =="`":
            r-=1
    return content[j:r+1]

def formatDockerFile_v2(content):
    if content.startswith("```"):
        first_newline = content.find("\n")
        if first_newline != -1:
            content = content[first_newline+1:]
        else:
            content = ""

    if content.endswith("```"):
        content = content[:-3]

    return content.strip()

