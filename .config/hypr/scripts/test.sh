#!/bin/sh

lastwall=$(cat $HOME/.cache/swww/eDP-1)
img=/tmp/hyprlock.png

prev_wall=$(cat /tmp/.hyprlock_lw)

echo $lastwall > /tmp/.hyprlock_lw

if [[ $lastwall == $prev_wall ]]; then
    hyprlock
else
    convert $lastwall -scale 10% -blur 0x3 -resize 1000% $img
    hyprlock
fi
