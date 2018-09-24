import os
eqdir = "/usr/equi"
os.chdir(eqdir)
def main():
    print("Install nginx and docker-compose.")
    os.system("apt-get install -y nginx docker-compose")
    print("Build image for web server.")
    os.system("docker build -t web {0}/image/web".format(eqdir))
    print("Build image for database server.")
    os.system("docker build -t db {0}/image/db".format(eqdir))
    print("Setup completed successfully.")
main()
