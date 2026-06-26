#!/usr/bin/env bash

if pgrep -f "$HOME/dev/scripts/autoclick.py" >/dev/null; then
    pkill -f "$HOME/dev/scripts/autoclick.py"
else
    pkexec "$HOME/dev/scripts/autoclick.py"
fi
