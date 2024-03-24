# Rumble Scope
Visualize controller rumble without a physical controller.

## Features:
- Emulates an Xbox 360 controller using vgamepad.
- Displays real-time progress bars for small and large motor rumble intensities.
- Button to press 'start' four times on the virtual controller. _may be needed for some programs to see the controller (click button then switch to the program inteded to recieve start buttons)_

## Requirements:
- Windows operating system
- Python 3.6 or newer
- [ViGEmBus driver](https://github.com/nefarius/ViGEmBus/releases/latest)
- vgamepad library (install with [pip install vgamepad])

## Usage:
1. Download and install [ViGEmBus](https://github.com/nefarius/ViGEmBus/releases/latest) driver. _this is the driver for the virtual controller._
2. Download [RumbleScope](https://github.com/ferocioustoast/RumbleScope/releases/latest).
3. Run rumble_scope.exe.
4. Connect the controller to the program you are testing.
5. Observe rumble values as they are triggered

## Examples:
Here is an example gif showing the application receiving rumble by connecting to [MultiFunPlayer](https://github.com/Yoooi0/MultiFunPlayer), using [Intiface](https://intiface.com/central/).

_note: the bar is not lined up perfectly with the graph in the video_

![example gif](https://raw.githubusercontent.com/ferocioustoast/RumbleScope/master/imgs/animation.gif)

Here is another example gif showing the application receiving rumble by connecting directly to [XToys](https://xtoys.app/).

![example gif 2](https://raw.githubusercontent.com/ferocioustoast/RumbleScope/master/imgs/animation2.gif)
