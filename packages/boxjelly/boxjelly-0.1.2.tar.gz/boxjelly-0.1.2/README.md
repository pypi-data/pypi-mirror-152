# BoxJelly

**BoxJelly** is a tool for viewing and editing object tracks in video.

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org/downloads/)

![BoxJelly logo](boxjelly/assets/images/boxjelly_logo_128.png)

Author: Kevin Barnard, [kbarnard@mbari.org](mailto:kbarnard@mbari.org)

---

## Cthulhu Integration

This branch is for the [Cthulhu](https://github.com/mbari-media-management/cthulhu) integration. This integration is still in development. Currently, the integration has some limitations:

- Cthulhu does not report video framerate, so a default of 29.97 is assumed. This is configurable in the settings (Ctrl+,).
- Cthulhu must be running before you load a video/track file in BoxJelly.

## Install

### From PyPI

BoxJelly is available on PyPI as `boxjelly`. To install, run:

```bash
pip install boxjelly
```

### From source

This project is build with Poetry. To install from source, run (in the project root):

```bash
poetry install
```

## Run

Once BoxJelly is installed, you can run it from the command line:

```bash
boxjelly
```

---

Copyright &copy; 2021&ndash;2022 [Monterey Bay Aquarium Research Institute](https://www.mbari.org)
