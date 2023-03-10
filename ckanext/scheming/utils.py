import logging

from pylons import config

from ckan import model
import ckan.plugins.toolkit as toolkit

_ = toolkit._

log = logging.getLogger(__name__)


def field_labels():
    '''
    Returns a dict with the user friendly translatable field labels that
    can be used in the frontend.
    '''

    return {
        'info_identification': _('Identification'),
        'info_provenance': _('Provenance information'),
        'info_spatial': _('Spatial information'),
        'info_responsible': _('Responsible party'),
    }


# Continuar traduccion