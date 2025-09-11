from authenticateTOGemini import authenticate

def generateDockerFile(project_info):
    client = authenticate()

    prompt = f"Generate a docker file for this project please give me only the code:\n {project_info}"

    try:
        response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = prompt

    )

        return response.text
    except Exception as e:
        return f"An erro during the genration of docker file: {e} "