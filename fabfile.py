# -*- coding: utf-8 -*-
from fabric.api import (local
    , run
    , env
    , cd
)

env.hosts = ['23.239.0.15']
env.port = 22
env.user = 'zoomq'
code_dir = '~/gae'

env.deploy_path = './'

def deploy():
    git4pu()
    gae2sora()

def gae2sora():
    with cd(code_dir):
        run('pwd')
        run('git pull')
        run('/opt/sbin/gae4go/appcfg.py update urisago1/')

def git4pu():
    local('cd {deploy_path} && '
            'git add --all . && '
            'git ci -am "upgraded in local. @MBP111216ZQ" && '
            #'git pu cafe gitcafe-page '
            'git pu && '
            'pwd '.format(**env)
          )

