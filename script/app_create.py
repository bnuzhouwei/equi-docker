import os
import sys
eqdir = '/usr/equi/'
def get_args(argv):
    if len(argv) % 2 == 0: return
    args = {}
    for i in range(0,len(argv)/2):
        args[argv[i*2+1][1:]] = argv[i*2+2]
    return args
def v_args(args):
    for key in ['appid','appname','server_name','password']:
        if key not in args:
            print('{0} is needed!'.format(key))
            return False
    return True
def copy_app(appname):
    print('Coping template to tmp/{0}'.format(appname))
    os.chdir(eqdir)
    os.system('cp -rf tmpl tmp/{0}'.format(appname))
def sed_app(appid, appname, server_name, password):
    print('Setting server_name, port and password!')
    webport = 10000 + appid * 10 if appid else 80
    dbport = 20000 + appid * 10 if appid else 5432
    os.chdir(eqdir+'tmp/{0}'.format(appname))
    os.system("sed -i 's/@password/{0}/g' www/Web.config".format(password))
    os.system("sed -i 's/@server_name/{0}/g' site.nginx".format(server_name))
    os.system("sed -i 's/@webport/{0}/g' site.nginx".format(webport))
    os.system("sed -i 's/@webport/{0}/g' docker-compose.yml".format(webport))
    os.system("sed -i 's/@dbport/{0}/g' docker-compose.yml".format(dbport))
    os.system("sed -i 's/@appid/{0}/g' docker-compose.yml".format(appid))
def set_dbpasswd(appname, password):
    wdir = eqdir+'tmp/{0}/'.format(appname)
    os.chdir(wdir)
    datadir = wdir + 'data'
    print("Create temp database container...")
    cmd = 'docker run -d -v {0}:/var/lib/postgresql/data --name {1} db'.format(datadir,appname)
    os.system(cmd)
    print("Waiting for temp database container up.")
    os.system('sleep 10')
    print("Restoring Database...")
    cmd = "docker exec -i {0} psql -U postgres -q postgres<{1}".format(appname, eqdir+"dbbak/pgsql.bak")
    os.system(cmd)
    print("Setting password...")
    cmd = '''docker exec {0} psql -U postgres -c "alter user postgres with password '{1}';update dd.dd_user set password=md5('{1}') where username='equiclouds';"'''.format(appname, password)
    os.system(cmd)
    print("Remove temp database container...")
    os.system('docker stop {0}'.format(appname))
    os.system('docker rm {0}'.format(appname))
def start_app(appname):
    srcdir = eqdir+'tmp/{0}/'.format(appname)
    destdir = '/var/www/'
    os.system('mv {0} {1}'.format(srcdir, destdir))
    os.chdir(destdir+appname)
    print("Start {0}.".format(appname))
    os.system('docker-compose up -d --force-recreate')
    os.system('mv site.nginx /etc/nginx/sites-enabled/{0}'.format(appname))
    os.system('nginx -s reload')
def main():
    args = get_args(sys.argv)
    if not args : 
        print('Please give some args: appid, appname server_name, and password.')
        return
    if not v_args(args): return
    appid, appname, server_name, password = int(args['appid']), args['appname'], args['server_name'], args['password']
    if appname in os.listdir('/var/www/'):
        print('The app is exites!')
        return
    copy_app(appname)
    sed_app(appid, appname, server_name, password)
    set_dbpasswd(appname,password)
    start_app(appname)
    print("Done")
main() 
