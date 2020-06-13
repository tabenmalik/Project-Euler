#!/usr/bin/env python

import setuptools

setuptools.setup(name='project_euler',
                 version='0.0.0',
                 description='Solutions to project euler problems',
                 packages=setuptools.find_packages(),
                 scripts=['project_euler/scripts/euler']
                 )
      
