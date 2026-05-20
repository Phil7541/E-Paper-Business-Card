# E-Paper Business Card

A custom-built e-paper business card designed to combine embedded systems, low-power display technology, and personal branding into a reusable standalone device.
The project explores compact hardware design, QR/NFC interaction, and rendering custom graphics for ultra-low-power e-paper displays using Python and Raspberry Pi hardware.

![Platform](https://img.shields.io/badge/platform-Raspberry%20Pi-darkgreen)
![Language](https://img.shields.io/badge/language-Python-blue)
![Hardware](https://img.shields.io/badge/hardware-E--Paper-yellow)
![Status](https://img.shields.io/badge/status-In%20Development-orange)

---

## Features

* Custom-rendered e-paper business card interface
* QR code integration for instant profile/contact access
* Planned NFC support for tap-to-share functionality
* Fully standalone embedded hardware design
* Python-based rendering pipeline using Pillow
* Optimised layout for low-resolution colour e-paper displays
* Modular asset loading for fonts, icons, and graphics
* Hardware abstraction separating rendering and display logic
* Logging system for easier debugging and testing

---

## Screenshots

| Render Preview | Hardware Test |
| -------------- | ------------- |
| image_here     | image_here    |

---

## Hardware Overview

Current hardware used during development:

* Raspberry Pi Raspberry Pi for rendering and display control
* 7.5" four-colour Waveshare e-paper display (used for prototyping)
* Planned migration to smaller dedicated e-paper display hardware
* NFC tag integration (planned)
* Custom 3D printed enclosure (in development)

---

## Tech Stack

* Python 3
* Pillow (PIL)
* Waveshare EPD drivers
* Raspberry Pi GPIO/SPI
* Fusion 360 (hardware enclosure design)
* Git + GitHub

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/e-paper-business-card.git
```

2. Navigate to the project directory:

```bash
cd e-paper-business-card
```

3. Create and activate a virtual environment:

```bash
python3 -m venv dashboard-env
source dashboard-env/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the renderer test:

```bash
python src/renderer.py
```

6. Run on compatible Raspberry Pi hardware:

```bash
python src/main.py
```

---

## Project Structure

```text
E-Paper-Business-Card/
├── assets/
│   ├── fonts/
│   ├── icons/
│   └── images/
├── images/
├── lib/
│   └── waveshare_epd/
├── logs/
├── src/
│   ├── main.py
│   └── renderer.py
└── README.md
```

---

## Design Goals

The project was designed around a few core ideas:

* Creating a memorable physical portfolio piece
* Exploring low-power embedded display technology
* Learning more about hardware/software integration
* Designing around the limitations of small e-paper displays
* Building a reusable rendering pipeline for future display projects

The intention is for the final hardware to feel closer to a polished standalone device than a simple prototype board with a screen attached.

---

## What I Learned

This project has involved a mixture of software, hardware, and physical design challenges, including:

* Rendering readable layouts on low-resolution e-paper displays
* Working with colour limitations and refresh behaviour
* Structuring rendering pipelines for embedded systems
* Managing assets and fonts dynamically in Python
* Using SPI-based display hardware with Raspberry Pi
* Designing around real-world hardware constraints such as ribbon cable routing and enclosure tolerances
* Iterating UI layouts specifically for e-paper readability

It also helped reinforce the importance of separating rendering logic from hardware control, making the project significantly easier to test and expand.

---

## Future Improvements

* Finalise dedicated compact hardware platform
* Add NFC tap-to-share support
* Add configuration-based card generation
* Create multiple card templates/themes
* Design and print final enclosure
* Add automated image optimisation for e-paper palettes
* Create desktop/web preview tooling

---

## License

This project is licensed under the MIT License.
