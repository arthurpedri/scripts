#!/bin/bash

## PC uses alsamixer for muting yeti mic

# Define default source and sink
# pactl list sources short
SOURCE_NAME="alsa_input.usb-Yamaha_Corporation_ARIUS-00.iec958-stereo"

# pactl list sinks short
SINK_NAME="alsa_output.usb-Generic_Blue_Microphones_2101BAB0FPH8-00.analog-stereo"

# Under 40ms latency is too low
LATENCY=${2:-"40"}

# Check for the parameter
if [ "$1" == "load" ]; then
    # Load the loopback module with a latency parameter
    echo "Loopback module loading with source $SOURCE_NAME and sink $SINK_NAME. Latency: $LATENCY ms"
    pactl load-module module-loopback source=$SOURCE_NAME sink=$SINK_NAME latency_msec="$LATENCY"

elif [ "$1" == "unload" ]; then
    # Unload the loopback module
    MODULE_ID=$(pactl list modules short | awk '/module-loopback/ {print $1}')
    if [ -n "$MODULE_ID" ]; then
        pactl unload-module "$MODULE_ID"
        echo "Loopback module unloaded."
    else
        echo "No loopback module found to unload."
    fi

else
    echo "Usage: $0 {load|unload}"
fi
