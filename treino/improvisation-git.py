import subprocess
from time import sleep

def git_intial(msg, url):
    init = subprocess.call(["git init"], shell=True)
    print(init)

    sleep(2)

    add = subprocess.call(["git add ."], shell=True)
    print(add)

    commit = subprocess.call([f"git commit -m {msg}"], shell=True)
    print(commit)

    remote = subprocess.call([f"git remote add origin {url}"], shell=True)
    print(remote)

    push = subprocess.call([f"git push origin master"], shell=True)
    print(push)

# msg = str(input("Mensagem do Commit: "))
# url = str(input("URL do Repositório: "))

git_intial(msg, url)