#!/usr/bin/env python
import os
import sys

# Include . in python path
sys.path.append('.')
os.environ['DJANGO_SETTINGS_MODULE'] = 'nazs.settings'

# Activate virtual env
manage_path = os.path.dirname(os.path.realpath(__file__))
activate_this = os.path.join(manage_path, 'env/bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

from django.core import management

management.call_command('test',
                        '--with-coverage',
                        '--cover-inclusive',
                        '--cover-erase',
                        '--cover-package=nazs')