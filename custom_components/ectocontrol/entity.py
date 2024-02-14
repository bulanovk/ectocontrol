"""EctocontrolEntity class"""
from typing import Optional, Any

from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import EctocontrolDataUpdateCoordinator
from .const import ATTRIBUTION
from .const import DOMAIN
from .const import NAME
from .const import VERSION
from .core.model import EctoControlAPIDevice


class EctocontrolEntity(CoordinatorEntity):
    """ Ectocontrol entity base class"""
    device: EctoControlAPIDevice
    _attr_id_postfix: Optional[str] = None
    coordinator: EctocontrolDataUpdateCoordinator

    def __init__(self, coordinator, config_entry, device: EctoControlAPIDevice):
        super().__init__(coordinator)
        self.config_entry = config_entry
        self.device = device
        self._attr_name = self.device.name
        self._attr_unique_id = f"ec_{self.device.system_object_id}_{self.device.id}"
        if self._attr_id_postfix is not None:
            self._attr_unique_id = f"{self._attr_unique_id}_{self._attr_id_postfix}"
        self.entity_id = f"sensor.{self._attr_unique_id}"

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return the state attributes of the device."""
        coord_device: EctoControlAPIDevice = self.coordinator.devices.devices.get(self.device.id)
        return {
            "connection": coord_device.connection,
            "lastUpdate": coord_device.update_time,
        }

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.device.system_object_id)},
            "name": f"{NAME}-{self.device.system_object_id}",
            "model": VERSION,
            "manufacturer": "Ectostroy",
        }

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return {
            "attribution": ATTRIBUTION,
            "id": str(self.coordinator.data.get("id")),
            "integration": DOMAIN,
        }
