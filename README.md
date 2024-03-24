# Rumble Scope
Visualize controller rumble without a physical controller.

## Features:
- Emulates an Xbox 360 controller using vgamepad.
- Displays real-time progress bars for small and large motor rumble intensities.
- Button to press 'start' four times on the virtual controller. _Some programs may need to see input from the controller. (Click the button, then switch to the program intended to receive start buttons.)_

## Requirements:
- Windows 10/11 (x86, amd64 and ARM64) operating system
- [ViGEmBus driver](https://github.com/nefarius/ViGEmBus/releases/latest) _This is the driver for the virtual controller._

## Usage:
1. Download and install the [ViGEmBus](https://github.com/nefarius/ViGEmBus/releases/latest) driver.
2. Download [RumbleScope](https://github.com/ferocioustoast/RumbleScope/releases/latest).
3. Run rumble_scope.exe.
4. Connect the controller to the program you are testing.
5. Observe rumble values as they are triggered. _Sometimes the program sending rumble needs to be the active window._

## Examples:
Here is an example gif showing the application receiving rumble by connecting to [MultiFunPlayer](https://github.com/Yoooi0/MultiFunPlayer), using [Intiface](https://intiface.com/central/).

_Note: The bar is not lined up perfectly with the graph in the video_

![example gif](https://raw.githubusercontent.com/ferocioustoast/RumbleScope/master/imgs/animation.gif)

Here is another example gif showing the application receiving rumble by connecting directly to [XToys](https://xtoys.app/).

![example gif 2](https://raw.githubusercontent.com/ferocioustoast/RumbleScope/master/imgs/animation2.gif)

Here is an example gif showing the application pressing 'start' and receiving rumble directly from ELDEN RING.

![example gif 3](https://raw.githubusercontent.com/ferocioustoast/RumbleScope/master/imgs/animation3.gif)
