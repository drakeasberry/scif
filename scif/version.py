'''

Copyright (C) 2017 The Board of Trustees of the Leland Stanford Junior
University.
Copyright (C) 2017 Vanessa Sochat.

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

__version__ = "0.0.5"
AUTHOR = 'Vanessa Sochat'
AUTHOR_EMAIL = 'vsochat@stanford.edu'
NAME = 'scif'
PACKAGE_URL = "http://www.github.com/containers-ftw/scif-cli"
KEYWORDS = 'the scientific filesystem'
DESCRIPTION = "a filesystem organization for scientific software and metadata"
LICENSE = "LICENSE"

INSTALL_REQUIRES = (

    ('demjson', {'exact_version': "2.2.4"}),
    ('python-dateutil', {'exact_verison': "2.5.3"}),
    ('requests', {'exact_version': '2.18.4'}),
    ('requests-toolbelt', {'exact_version': '0.8.0'}),
    ('retrying', {'exact_version': '1.3.3'}),
    ('pygments', {'min_version': '2.1.3'})
)

# Submodule Requirements

INSTALL_REQUIRES_ALL = (INSTALL_REQUIRES)
