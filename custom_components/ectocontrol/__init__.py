"""Ectocontrol Integration Platform"""
import asyncio
import logging
from datetime import timedelta
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.helpers.update_coordinator import UpdateFailed

from .api import EctocontrolApiClient
from .const import *
from .const import DOMAIN
from .const import PLATFORMS
from .const import STARTUP_MESSAGE
from .core.model import EctoControlAPIDevices

SCAN_INTERVAL = timedelta(seconds=30)

_LOGGER: logging.Logger = logging.getLogger(__package__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up this integration using UI."""
    if hass.data.get(DOMAIN) is None:
        hass.data.setdefault(DOMAIN, {})
        _LOGGER.info(STARTUP_MESSAGE)
    public_token = entry.data.get(CONF_PUBLIC_TOKEN)

    session = async_get_clientsession(hass)
    client = EctocontrolApiClient(public_token, session)

    coordinator = EctocontrolDataUpdateCoordinator(hass, client=client)
    await coordinator.async_config_entry_first_refresh()

    if not coordinator.last_update_success:
        _LOGGER.error("Failed to Perform Data update")
        raise ConfigEntryNotReady

    hass.data[DOMAIN][entry.entry_id] = coordinator
    _LOGGER.debug("INIT PLATFORMS")
    for platform in PLATFORMS:
        if entry.options.get(platform, True):
            coordinator.platforms.append(platform)
            hass.async_add_job(hass.config_entries.async_forward_entry_setup(entry, platform))

    entry.add_update_listener(async_reload_entry)
    return True


class EctocontrolDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Class to manage fetching data from the API."""

    def __init__(self, hass: HomeAssistant,
                 client: EctocontrolApiClient, ) -> None:
        """Initialize."""
        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=SCAN_INTERVAL)
        self.api = client
        self.platforms = []
        self.devices = EctoControlAPIDevices(None)

    async def update_devices(self):
        """"Update Device List """
        devices = await self.api.async_get_devices()
        self.devices = devices

    async def _async_update_data(self) -> dict[str, Any]:
        """Update data via library."""
        try:
            _LOGGER.debug("Going to refresh Coordinator Data. Devices %s", self.devices)
            return await self.api.async_get_data(self.devices)
        except Exception as exception:
            raise UpdateFailed() from exception

    async def async_config_entry_first_refresh(self) -> None:
        """Refresh data for the first time when a config entry is setup."""
        _LOGGER.debug("Start First refresh")
        self.devices = await self.api.async_get_devices()
        self.data = await self.async_refresh()
        await super().async_config_entry_first_refresh()


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Handle removal of an entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    unloaded = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, platform)
                for platform in PLATFORMS
                if platform in coordinator.platforms
            ]
        )
    )
    if unloaded:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unloaded


async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload config entry."""
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)
