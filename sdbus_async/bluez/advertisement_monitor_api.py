# SPDX-License-Identifier: LGPL-2.1-or-later
# Copyright (C) 2022 Shin'ichiro Kawasaki

# This file is part of python-sdbus

# https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/doc/advertisement-monitor-api.txt

from __future__ import annotations

from typing import Any, Dict, List, Tuple

from sdbus import (
    DbusInterfaceCommonAsync,
    dbus_method_async,
    dbus_property_async,
)


class AdvertisementMonitorInterfaceAsync(
    DbusInterfaceCommonAsync,
    interface_name='org.bluez.AdvertisementMonitor1',
):

    @dbus_method_async()
    async def release(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async()
    async def activate(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='o',
    )
    async def device_found(
        self,
        device: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='o',
    )
    async def device_lost(
        self,
        device: str,
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def type(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='n',
        property_name='RSSILowThreshold'
    )
    def rssi_low_threshold(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='n',
        property_name='RSSIHighThreshold'
    )
    def rssi_high_threshold(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='q',
        property_name='RSSILowTimeout'
    )
    def rssi_low_timeout(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='q',
        property_name='RSSIHighTimeout'
    )
    def rssi_high_timeout(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='q',
        property_name='RSSISamplingPeriod'
    )
    def rssi_sampling_period(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a{sv}',
    )
    def patterns(self) -> Dict[str, Tuple[str, Any]]:
        raise NotImplementedError


class AdvertisementMonitorManagerInterfaceAsync(
    DbusInterfaceCommonAsync,
    interface_name='org.bluez.AdvertisementMonitorManager1',
):

    @dbus_method_async(
        input_signature='o',
    )
    async def register_monitor(
        self,
        application: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='o',
    )
    async def unregister_monitor(
        self,
        application: str,
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
    )
    def supported_monitor_types(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
    )
    def supported_features(self) -> List[str]:
        raise NotImplementedError


