import vgamepad as vg
import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.title("Rumble Scope")

small_motor_label = tk.Label(
    root,
    text="Small Motor"
).grid(row=1, column=1)

small_motor_bar = ttk.Progressbar(
    root,
    orient='vertical',
    mode='determinate',
    length=400,
    maximum=255
)
small_motor_bar.grid(row=2, column=1)

large_motor_label = tk.Label(
    root,
    text="Large Motor"
).grid(row=1, column=3)

large_motor_bar = ttk.Progressbar(
    root,
    orient='vertical',
    mode='determinate',
    length=400,
    maximum=255
)
large_motor_bar.grid(row=2, column=3)

press_button_button = tk.Button(
    root,
    text="Press 'start' button x4",
    command=lambda: spam_buttons()
).grid(row=2, column=0)


def spam_buttons():
    # Press the start button on the controller a few times
    for i in range(4):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        gamepad.update()
        time.sleep(0.5)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        gamepad.update()
        time.sleep(0.5)


def rumble(client, target, large_motor, small_motor, led_number, user_data):
    """
    Callback function triggered at each received state change
    :param small_motor: integer in [0, 255]
    """
    small_motor_bar["value"] = small_motor
    large_motor_bar["value"] = large_motor


if __name__ == '__main__':
    gamepad = vg.VX360Gamepad()
    gamepad.register_notification(callback_function=rumble)

    root.mainloop()
