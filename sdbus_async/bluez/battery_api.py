# SPDX-License-Identifier: LGPL-2.1-or-later

# Copyright (C) 2022 igo95862

# This file is part of python-sdbus

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
from __future__ import annotations

from sdbus import DbusInterfaceCommonAsync, dbus_property_async


class BatteryInterfaceAsync(
    DbusInterfaceCommonAsync,
    interface_name='org.bluez.Battery1',
):

    @dbus_property_async(
        property_signature='y',
    )
    def percentage(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def source(self) -> str:
        raise NotImplementedError
