import sys
import os
import pkg_resources
import logbook
import datetime

from quantumcore.storages import AttributeMapper
from quantumcore.resources import CSSResourceManager, css_from_pkg_stream
from quantumcore.resources import JSResourceManager, js_from_pkg_stream
from framework.utils import get_static_urlparser


JS = [
    js_from_pkg_stream(__name__, 'static/js/jquery-1.4.4.min.js', name="", merge=False, prio=1,),
]

CSS = [
    css_from_pkg_stream(__name__, 'static/css/screen.css', merge=True, prio=1, auto_reload=True),
]

def setup(**kw):
    """initialize the setup"""
    settings = AttributeMapper()
    settings['css'] = CSSResourceManager(CSS, prefix_url="/css", auto_reload=True)
    settings['js'] = JSResourceManager(JS, prefix_url="/js", auto_reload=True)
    settings['staticapp'] = get_static_urlparser(pkg_resources.resource_filename(__name__, 'static'))
    
    settings['log'] = logbook.Logger("frontend")
    settings.update(kw)
    return settings






