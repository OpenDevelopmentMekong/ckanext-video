#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-video
# Created by the Natural History Museum in London, UK

import logging
import re

from ckan.plugins import SingletonPlugin, implements, interfaces, toolkit
from ckanext.video.logic.validators import is_valid_video_url, is_valid_video_url_with_context
from ckanext.video.providers import video_provider_patterns

log = logging.getLogger(__name__)
ignore_empty = toolkit.get_validator('ignore_empty')
not_empty = toolkit.get_validator('not_empty')
is_positive_integer = toolkit.get_validator('is_positive_integer')


class VideoPlugin(SingletonPlugin):
    """
    Resource view for embedding videos (youtube/vimeo)
    """

    implements(interfaces.IConfigurer)
    implements(interfaces.IResourceView)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'theme/templates')
        toolkit.add_resource('theme/assets', 'ckanext-video')

    def info(self):
        return {
            'name': 'video',
            'title': toolkit._('Embedded Video'),
            'default_title': toolkit._('Video Preview'),
            'schema': {
                'video_url': [ignore_empty, str, is_valid_video_url_with_context]
            },
            'iframed': False,
            'icon': 'film',
        }

    def can_view(self, data_dict):
        video_url = data_dict['resource'].get('url')
        return is_valid_video_url(video_url)

    def view_template(self, context, data_dict):
        return 'embedded_video/video_view.html'

    def form_template(self, context, data_dict):
        return 'embedded_video/video_form.html'
    
    def setup_template_variables(self, context, data_dict):
        """
        Setup variables available to templates.

        :param context:
        :param data_dict:
        """
        video_url = data_dict['resource_view'].get('video_url') or data_dict[
            'resource'
        ].get('url')

        # Is this a youtube video?
        for key in video_provider_patterns:
            if not key.startswith('youtube'):
                continue
            match = re.search(
                video_provider_patterns[key], video_url, re.IGNORECASE
            )
            if match:
                video_url = 'https://www.youtube.com/embed/{embed_url}'.format(embed_url=match.group(1))
                break

        # TODO - More video provider types
        return {'defaults': {'width': 480, 'height': 390}, 'video_url': video_url}
