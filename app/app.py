from flask import Flask, render_template, request, redirect
from github import Github
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def trigger_workflow():
    if request.method == 'POST':
        # Obtén tu token personal de GitHub (debe tener permisos de repo)
        github_token = os.getenv("GITHUB_TOKEN")
        g = Github(github_token)

        repo_name = "tu_usuario/tu_repositorio"
        repo = g.get_repo(repo_name)

        # Crea una nueva rama basada en main
        main_branch = repo.get_branch("main")
        new_branch_name = "trigger-workflow"
        try:
            repo.create_git_ref(ref=f"refs/heads/{new_branch_name}", sha=main_branch.commit.sha)
        except Exception as e:
            print("Branch exists:", e)

        # Realiza un pequeño cambio en el archivo para generar el commit
        contents = repo.get_contents("trigger.txt", ref=new_branch_name)
        repo.update_file(contents.path, "Trigger workflow", "Trigger", contents.sha, branch=new_branch_name)

        # Abre automáticamente el pull request
        repo.create_pull(
            title="Trigger Ansible Workflow",
            body="Auto-generated PR to trigger Ansible Workflow",
            head=new_branch_name,
            base="main"
        )

        return redirect("/")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
