# Ectocontrol Integration

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]


**This component will set up the following platforms.**

| Platform        | Description                                                               |
| --------------- | ------------------------------------------------------------------------- |
| `binary_sensor` | Show something `True` or `False`.                                         |
| `sensor`        | Show info from Ectocontrol API. |
| `switch`        | Switch something `True` or `False`.                                       |


## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `ectocontrol`.
4. Download _all_ the files from the `custom_components/ectocontrol/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Ectocontrol"

## Configuration is done in the UI

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

## Credits

This project was generated from [@oncleben31](https://github.com/oncleben31)'s [Home Assistant Custom Component Cookiecutter](https://github.com/oncleben31/cookiecutter-homeassistant-custom-component) template.

Code template was mainly taken from [@Ludeeus](https://github.com/ludeeus)'s [integration_blueprint][integration_blueprint] template

---

[integration_blueprint]: https://github.com/custom-components/integration_blueprint
[commits-shield]: https://img.shields.io/github/commit-activity/y/bulanovk/ha_test_component.svg?style=for-the-badge
[commits]: https://github.com/bulanovk/ha_test_component/commits/main
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/bulanovk/ha_test_component.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40bulanovk-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/bulanovk/ha_test_component.svg?style=for-the-badge
[releases]: https://github.com/bulanovk/ha_test_component/releases
[user_profile]: https://github.com/bulanovk
