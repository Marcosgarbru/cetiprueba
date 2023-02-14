from github import Github
import os

def run(file_path, repo_name, github_token):
    # Autenticación con el token de acceso
    g = Github(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)

    # Obtener el repositorio
    repo = g.get_user().get_repo(cetiprueba)

    # Leer el contenido del archivo
    with open(file_path, 'r') as file:
        content = file.read()

    # Crear el archivo en el repositorio
    try:
        repo.create_file(file_path, "Commit message", content)
        print(f"El archivo {file_path} ha sido creado en el repositorio {repo_name}.")
    except Exception as e:
        print(f"Ha ocurrido un error al crear el archivo en el repositorio: {str(e)}")
