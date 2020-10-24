#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
#use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.install_dependencies")

name = "ngab"
default_task = "publish"

coverage_break_build = False
coverage_threshold_warn = 0

@init
def set_properties(project):
    project.depends_on_requirements("requirement.txt")
