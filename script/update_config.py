#coding=utf-8
import os
os.chdir('/usr/equi/script/')
apppath = "/var/www/"

def read_file(filepath):
    with open(filepath) as file:
        return file.read()

def write_file(filepath, content):
    with open(filepath,'w') as file:
        file.write(content)

template = read_file("Web.config")

def node_pattern(node_name):
    return '<{0}>.+</{0}>'.format(node_name)

def xml_element(xmlstr, node_name):
    pattern = node_pattern(node_name)
    return re.search(pattern, xmlstr, re.S ).group(0)

nodes = ['runtime', 'entityFramework', 'system.data']
import re
def update_file(filepath):
    output_xml = read_file(filepath)
    for node in nodes:
        src = xml_element(template, node)
        output_xml = re.sub( node_pattern(node), src, output_xml, 0, re.S )
    write_file(filepath, output_xml)

def is_equi_path(path):
    return os.path.exists(path+"/www/Web.config")
	
def main():
    print(apppath)
    paths = os.listdir(apppath)
    apps = [ apppath + path + "/www" for path in paths if is_equi_path(apppath+path)]
    print(apps)	
    ch = raw_input("Will update the Web.config of apps.(y/n)")
    if ch!='y': return
    for app in apps:
        filepath = app + "/" + "Web.config"
        print(filepath)
        update_file(filepath)
main()
