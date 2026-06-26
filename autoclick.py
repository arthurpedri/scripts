#!/usr/bin/env python3

import asyncio
from evdev import InputDevice, UInput, ecodes as e

# Change this to your mouse event path from `sudo libinput list-devices`
MOUSE_DEVICE = "/dev/input/event5"

# Button used to toggle autoclick.
# Common options:
# e.BTN_MIDDLE = middle mouse
# e.BTN_SIDE   = back thumb button
# e.BTN_EXTRA  = forward thumb button
TRIGGER_BUTTON = e.BTN_SIDE

# Autoclick speed
CLICKS_PER_SECOND = 20
CLICK_HOLD_SECONDS = 0.03

# True  = press trigger once to toggle on/off
# False = autoclick only while holding trigger
TOGGLE_MODE = True

# True = block the trigger button from reaching the game/app
# False = let the trigger button also do its normal action
GRAB_MOUSE = False


async def click_loop(state, ui):
    click_interval = 1 / CLICKS_PER_SECOND
    release_delay = max(0, click_interval - CLICK_HOLD_SECONDS)

    while True:
        if state["enabled"]:
            print("click", flush=True)
            ui.write(e.EV_KEY, e.BTN_LEFT, 1)
            ui.syn()
            await asyncio.sleep(CLICK_HOLD_SECONDS)

            ui.write(e.EV_KEY, e.BTN_LEFT, 0)
            ui.syn()
            await asyncio.sleep(release_delay)
        else:
            await asyncio.sleep(0.02)


async def watch_mouse(state):
    mouse = InputDevice(MOUSE_DEVICE)

    if GRAB_MOUSE:
        mouse.grab()

    print(f"Listening on {MOUSE_DEVICE}")
    print("Autoclick starts OFF.")

    async for event in mouse.async_read_loop():
        if event.type == e.EV_KEY and event.code == TRIGGER_BUTTON:
            if TOGGLE_MODE:
                if event.value == 1:  # button pressed
                    state["enabled"] = not state["enabled"]
                    print("autoclick:", "ON" if state["enabled"] else "OFF")
            else:
                if event.value == 1:  # pressed
                    state["enabled"] = True
                    print("autoclick: ON")
                elif event.value == 0:  # released
                    state["enabled"] = False
                    print("autoclick: OFF")


async def main():
    state = {"enabled": False}
    capabilities = {
        e.EV_KEY: [e.BTN_LEFT],
        e.EV_REL: [e.REL_X, e.REL_Y],
    }

    with UInput(capabilities, name="python-autoclicker") as ui:
        await asyncio.gather(
            watch_mouse(state),
            click_loop(state, ui),
        )


if __name__ == "__main__":
    asyncio.run(main())
