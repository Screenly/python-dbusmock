'''resolved mock template
'''

# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 3 of the License, or (at your option) any
# later version.  See http://www.gnu.org/copyleft/lgpl.html for the full text
# of the license.

__author__ = 'Renat Galimov'
__copyright__ = '''
(c) 2021 Red Hat
(c) 2017 - 2022 Martin Pitt <martin@piware.de>
'''

from gi.repository import GLib
import dbus

from dbusmock import MOCK_IFACE, mockobject

BUS_PREFIX = 'org.freedesktop.resolve1'
PATH_PREFIX = '/org/freedesktop/resolve1'


BUS_NAME = BUS_PREFIX
MAIN_OBJ = PATH_PREFIX
MAIN_IFACE = BUS_PREFIX + '.Manager'
SYSTEM_BUS = True


def load(mock, _parameters):
    mock.AddProperties(
        MAIN_IFACE,
        dbus.Dictionary(
            {'CacheStatistics': (6, 295, 108),
             'CurrentDNSServer': (0, 0, []),
             'DNS': [(3, 2, [192, 168, 1, 1])],
             'DNSOverTLS': 'no',
             'DNSSEC': 'no',
             'DNSSECNegativeTrustAnchors': [
                 '17.172.in-addr.arpa',
                 '18.172.in-addr.arpa',
                 '16.172.in-addr.arpa',
                 'test',
                 '21.172.in-addr.arpa',
                 '28.172.in-addr.arpa',
                 'lan',
                 'intranet',
                 'private',
                 '30.172.in-addr.arpa',
                 '168.192.in-addr.arpa',
                 '29.172.in-addr.arpa',
                 '10.in-addr.arpa',
                 '20.172.in-addr.arpa',
                 '27.172.in-addr.arpa',
                 '23.172.in-addr.arpa',
                 'local',
                 '19.172.in-addr.arpa',
                 'corp',
                 '24.172.in-addr.arpa',
                 '31.172.in-addr.arpa',
                 '26.172.in-addr.arpa',
                 'internal',
                 'd.f.ip6.arpa',
                 '22.172.in-addr.arpa',
                 'home',
                 '25.172.in-addr.arpa'],
             'DNSSECStatistics': (0, 0, 0, 0),
             'DNSSECSupported': 0,
             'DNSStubListener': 'yes',
             'Domains': [(3, '.', 1)],
             'FallbackDNS': [],
             'LLMNR': 'no',
             'LLMNRHostname': 'srly-xwy9j0s41vdi1s3',
             'MulticastDNS': 'no',
             'TransactionStatistics': (0, 1248)}
            , signature='sv'))


@dbus.service.method(MAIN_IFACE, in_signature="isit", out_signature="a(iaay)st")
def ResolveHostame(self, ifindex, name, family, flags):
    return (
        dbus.Array(
            [
                dbus.Struct(
                    (
                        dbus.Int32(3),
                        dbus.Int32(2),
                        dbus.Array(
                            [
                                dbus.Byte(216),
                                dbus.Byte(239),
                                dbus.Byte(38),
                                dbus.Byte(120),
                            ],
                            signature=dbus.Signature("y"),
                        ),
                    ),
                    signature=None,
                )
            ],
            signature=dbus.Signature("(iiay)"),
        ),
        dbus.String(name),
        dbus.UInt64(1),
    )
