# http://www.equiclouds.com/
Build better Web apps with CBSE by PaaS! 

## Get Started

* Install requirements:

```bash
sudo su
cd /tmp
git clone https://github.com/equiclouds/equi-docker.git
rm -rf /usr/equi
mv /tmp/equi-docker /usr/equi
mkdir /usr/equi/tmp
python /usr/equi/script/setup.py
```

* Create an app whose web server and database server are both hosted in docker:

```bash
python /usr/equi/script/app_create.py -appid 1 -appname app1 -server_name www.yourdomain.com -password password
```

You can specify the appid, appname, server_name, and password your app by change the params in the last line of scripts above.

When excuted, visit http://www.yourdomian.com to view the app. Of couse, you should first resolved the domain name to ip of the server. Otherwise your can visit http://yourserverip:10010 by ip and port!

Your can see the port with command:

```bash
docker-compose ps -a
```

- You could create many apps in a server without conflict:

```bash
python /usr/equi/script/app_create.py -appid 2 -appname app2 -server_name www.yourdomain2.com -password password2
```

Have fun!
