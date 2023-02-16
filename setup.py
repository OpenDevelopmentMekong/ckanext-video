#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-video
# Created by the Natural History Museum in London, UK

from setuptools import setup

version = '2.1.5'

setup(
    name = "ckanext-video",
    version = version,
    description = "A CKAN extension for embedding Youtube or Vimeo videos as views.",
    license = "GPL-3.0-or-later",
    author = "Natural History Museum",
    author_email = "data@nhm.ac.uk",
    keywords = ["CKAN", "data", "video"],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    entry_points ='''
        [ckan.plugins]
        video = ckanext.video.plugin:VideoPlugin
    '''
)