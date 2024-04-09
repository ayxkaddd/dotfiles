#!/bin/sh

lastwall=$(cat $HOME/.cache/swww/eDP-1)
img=$HOME/.cache/hyprland/hyprlock.png

prev_wall=$(cat $HOME/.cache/hyprland/.hyprlock_lw)

echo $lastwall > $HOME/.cache/hyprland/.hyprlock_lw

if [[ $lastwall == $prev_wall ]]; then
    hyprlock
else
    convert $lastwall -scale 10% -blur 0x3 -resize 1000% $img
    hyprlock
fi

exit