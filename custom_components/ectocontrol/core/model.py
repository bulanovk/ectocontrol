"""" API Pojo """
import numbers
import re
from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class EctoControlAPIDevice:
    # pylint: disable=too-many-instance-attributes
    """Ectocontrol devices Rest API Pojo"""

    id: numbers
    system_object_id: str
    type: str
    name: str
    state: str = None
    value: str = None
    signal_level: str = 0
    system_firmware_version: str = None
    connection: bool = True
    update_time: datetime = datetime.now()

    def __str__(self):
        return f'{self.id}-{self.name}'

    def __post_init__(self):
        if self.name is not None:
            self.name = re.sub('"(.*)"$', '\\1', self.name)

    def update(self, data: dict[str, Any]):
        """ Update Pojo by Map """
        for key, value in data.items():
            setattr(self, key, value)
        if self.name is not None:
            self.name = re.sub('"(.*)"$', '\\1', self.name)
            self.update_time=datetime.now()


@dataclass
class EctoControlAPIDevices:
    """Ectocontrol devices Rest API Pojo"""
    devices: dict[str, EctoControlAPIDevice]

    def __init__(self, devices):
        self.devices = {}
        if devices is not None:
            for device in devices:
                self.devices[device.get("id")] = EctoControlAPIDevice(**device)

    def __str__(self):
        return f"{self.devices}"
