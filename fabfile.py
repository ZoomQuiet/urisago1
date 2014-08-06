# -*- coding: utf-8 -*-
from fabric.api import (local
    , run
    , env
    , cd
)

env.hosts = ['23.239.0.15']
env.port = 22
env.user = 'zoomq'
code_dir = '~/gae/urisago1'
gae_dir = '~/gae'

env.deploy_path = './'

def deploy():
    loc0pu()
    git2pl()
    gae4up()


def git2pl():
    with cd(code_dir):
        run('pwd')
        run('git pull')

def gae4up():
    with cd(gae_dir):
        run('pwd')
        run('/opt/sbin/gae4go/appcfg.py update urisago1/')

def loc0pu():
    local('cd {deploy_path} && '
            'git add --all . && '
            'git ci -am "upgraded in local. @MBP111216ZQ" && '
            #'git pu cafe gitcafe-page '
            'git pu && '
            'pwd '.format(**env)
          )

