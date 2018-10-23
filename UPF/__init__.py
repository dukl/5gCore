# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask

import v1

#CurrentPath = '~/5GCORE/UPF/__init__.py'

def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        v1.bp,
        url_prefix='/nupf/v1')
    return app

if __name__ == '__main__':
	#p = subprocess.Popen('sudo brctl addbr br0',shell=True,close_fds=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
	create_app().run(port=5012,debug=True)
