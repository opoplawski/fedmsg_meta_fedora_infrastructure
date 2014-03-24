# This file is part of fedmsg.
# Copyright (C) 2014 Red Hat, Inc.
#
# fedmsg is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# fedmsg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with fedmsg; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Authors:  Ralph Bean <rbean@redhat.com>
#
""" Tests for ftpsync messages """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from common import add_doc


class TestFTPSyncFedora(Base):
    """ These messages are published when new updates (fresh out of the "mash"
    process) are synced out to the mirror master.

    Here's an example for the fedora 20 stable repos:
    """
    expected_title = "bodhi.updates.fedora.sync"
    expected_subti = "New Fedora 20 updates content synced out " + \
        "(28493 new bytes, 0 files deleted)"
    expected_link = \
        "https://download.fedoraproject.org/pub/fedora/linux/updates/20/"
    expected_objects = set(['fedora/updates/20'])

    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.bodhi.updates.fedora.sync",
        "msg": {
            "bytes": "28493",
            "deleted": "0",
            "repo": "updates",
            "release": "20",
        },
    }


class TestFTPSyncEPELTesting(Base):
    """ These messages are published when new updates (fresh out of the "mash"
    process) are synced out to the mirror master.

    Here's an example for the epel 6 testing repos:
    """
    expected_title = "bodhi.updates.epel.sync"
    expected_subti = "New EPEL 6 epel-testing content synced out " + \
        "(28493 new bytes, 0 files deleted)"
    expected_link = \
        "https://download.fedoraproject.org/pub/epel/testing/6/"
    expected_objects = set(['epel/epel-testing/6'])

    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.bodhi.updates.epel.sync",
        "msg": {
            "bytes": "28493",
            "deleted": "0",
            "repo": "epel-testing",
            "release": "6",
        },
    }


add_doc(locals())