import os
wdir = '/var/www/'
def get_apps():
    folders = [item for item in os.listdir(wdir) if os.path.isdir(wdir+item) and os.path.exists(wdir+item+"/docker-compose.yml") ]
    return folders
def start(app):
    os.chdir('/var/www/{0}'.format(app))
    os.system('docker-compose up -d --force-recreate')
def main():
    apps = get_apps()
    total = len(apps)
    print("Total {0} apps.".format(total))
    n = 1
    for app in apps:
        print("Starting the {0}/{1} app: {2}.".format(n,total,app))
        start(app)
        n = n + 1
    os.chdir(wdir)
    print("Restart nginx...")
    os.system('nginx -s reload')
    print("Done")
main()
