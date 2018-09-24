import os
eqdir = "/usr/equi"
os.chdir(eqdir)
def main():
    print("Install nginx.")
    os.system("apt-get install nginx")
    print("Build image for web server.")
    os.system("docker build -t web ./image/web")
    print("Build image for database server.")
    os.system("docker build -t db ./image/db")
    print("Setup completed successfully.")
main()
