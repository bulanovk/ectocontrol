"""Sensor platform for Ectocontrol."""
import logging
from datetime import date, datetime
from decimal import Decimal

from homeassistant.components.sensor import SensorDeviceClass, SensorEntity
from homeassistant.const import UnitOfTemperature
from homeassistant.helpers.typing import StateType

from . import EctocontrolDataUpdateCoordinator
from .const import DOMAIN
from .entity import EctocontrolEntity

_LOGGER: logging.Logger = logging.getLogger(__package__)


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator: EctocontrolDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]
    _LOGGER.debug("Got Device List  %s", coordinator.devices)
    devs = []
    for _, device in coordinator.devices.devices.items():
        if device.type == "Датчик температуры":
            devs.append(TemperatureEctoControlSensor(coordinator, entry, device))
    async_add_devices(devs)


class EctocontrolSensor(EctocontrolEntity, SensorEntity):
    """ectocontrol Sensor class."""

    @property
    def native_value(self) -> StateType | date | datetime | Decimal:
        """Return the value reported by the sensor."""
        coordinator: EctocontrolDataUpdateCoordinator = self.coordinator
        return coordinator.devices.devices.get(self.device.id).value


class TemperatureEctoControlSensor(EctocontrolSensor):  # pylint: disable=too-many-ancestors
    """ Ectocontrol Temperature Sensor Class"""
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
    _attr_id_postfix = "temperature"
