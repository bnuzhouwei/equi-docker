import os
eqdir = "/usr/equi"
os.chdir(eqdir)
def main():
    print("Install nginx and docker-compose.")
    os.system("apt-get install nginx docker-compose")
    print("Build image for web server.")
    os.system("docker build -t web ./image/web")
    print("Build image for database server.")
    os.system("docker build -t db ./image/db")
    print("Setup completed successfully.")
main()
