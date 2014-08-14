#! /usr/bin/env python3

import os

import hg_plugin_shared
from hg_plugin_shared import hg


dest = os.environ['PERU_FETCH_DEST']
cache_path = os.environ['PERU_PLUGIN_CACHE']
url = os.environ['PERU_MODULE_URL']
rev = os.environ.get('PERU_MODULE_REV') or 'default'

clone = hg_plugin_shared.clone_if_needed(url, cache_path, verbose=True)
if not hg_plugin_shared.already_has_rev(clone, rev):
    print('hg pull', url)
    hg('pull', hg_dir=clone)

# TODO: Should this handle subrepos?
hg('archive', '--type', 'files', '--rev', rev, dest, hg_dir=clone)
