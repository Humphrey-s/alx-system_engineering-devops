#!/usr/bin/python3
from fabric.api import env, run, local
env.hosts = ["ubuntu@18.207.112.206", "ubuntu@54.89.195.83"]

def do_net():
    """install net tools"""
    run("sudo apt install net-tools -y")
    run("sudo git clone https://github.com/Humphrey-s/AirBnB_clone_v2.git")
