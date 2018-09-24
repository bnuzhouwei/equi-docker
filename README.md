# [Equiclouds](http://www.equiclouds.com/)

## Features

Build better Web apps with CBSE by PaaS! 

A browser and a database tool can build the whole large web app:

* Automatic Management Interface
  * Automatically analyze data dictionaries, intelligently create data grids, rich custom configurations, dozens of form controls, comprehensive data validation, lightweight role workflows, powerful far wins Django admin backstage. Developers only focus on the Assembly and implementation of the components, without focusing on the development of the interface.
* Component-based Development
  * Component-based development provides a more organized reuse approach, the concept of "assembling rather than coding, integrating rather than implementing" provides data-driven business artifacts to dramatically improve the development speed and software quality of Web applications, dramatically lowering costs through the development platform online configuration, assembly and development of artifacts.
* Online Integrated Development Environment
  * Anytime, anywhere online coding, automatic preservation of historical version, intelligent dynamic compilation, detailed debug logs, lazy loading execution, code complement full code folding, grammar highlighting, full-screen mode, adaptive content size. You only need Web browsers and database management tools to build Web applications.

## GetStarted

* First, buy a virtual server with Ubuntu Server 14.04/16.04/18.04 LTS X64 from any of the following cloud computing providers:
  * [Microsoft Azure](https://azure.microsoft.com/), [Amazon AWS](https://aws.amazon.com/)
  * [阿里云](https://promotion.aliyun.com/ntms/yunparter/invite.html?userCode=jrx3bb1f), [腾讯云](https://cloud.tencent.com/redirect.php?redirect=1014&cps_key=3903997dfdf207961c180fc52fd875cf&from=console)
 
* Second, install requirements with following scripts:

```bash
sudo su
cd /tmp
git clone https://github.com/equiclouds/equi-docker.git
rm -rf /usr/equi
mv /tmp/equi-docker /usr/equi
mkdir /usr/equi/tmp
python /usr/equi/script/setup.py
```

* Third, Create an app whose web server and database server are both hosted in docker:

```bash
python /usr/equi/script/app_create.py -appid 1 -appname app1 -server_name www.yourdomain.com -password password
```

You can specify the appid, appname, server_name, and password your app by change the params in the last line of scripts above.

When excuted, visit http://www.yourdomian.com to view the app. Of couse, you should first resolved the domain name to ip of the server. Otherwise your can visit http://yourserverip:10010 by ip and port!

Your can see the web server port and database server port with command:

```bash
docker-compose ps -a
```

* Last, use database management tools, such as navicat and pgadmin, connect to the database server, and create tables and views.

Tips:

You could create many apps in a server without conflict:

```bash
python /usr/equi/script/app_create.py -appid 2 -appname app2 -server_name www.yourdomain2.com -password password2
```

Have fun!
