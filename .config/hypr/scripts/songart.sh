#!/bin/bash

ignore=$(playerctl -l | grep firefox.instance | head -n1)
parg="-i $ignore"

if [ -z "$ignore" ]; then
  parg=""
else
  echo 1>/dev/null 
fi

get_song_art () {
  TMP_DIR="$HOME/.cache/eww"
  TMP_COVER_PATH=$TMP_DIR/cover.png
  TMP_TEMP_PATH=$TMP_DIR/temp.png

  if [[ ! -d $TMP_DIR ]]; then
    mkdir -p $TMP_DIR
  fi

  ART_FROM_SPOTIFY="$(playerctl $parg -p %any,spotify metadata mpris:artUrl | sed -e 's/open.spotify.com/i.scdn.co/g')"
  #ART_FROM_BROWSER="$(playerctl $parg -p %any,mpd,chromium,brave metadata mpris:artUrl | sed -e 's/file:\/\///g')"

  if [[ $(playerctl $parg -p spotify,%any,firefox,chromium,brave,mpd metadata mpris:artUrl) ]]; then
    curl -s "$ART_FROM_SPOTIFY" --output $TMP_TEMP_PATH
  else
    cp $TMP_DIR/fallback.png $TMP_TEMP_PATH
  fi
  # elif [[ -n $ART_FROM_BROWSER ]]; then
  #   cp $ART_FROM_BROWSER $TMP_TEMP_PATH

  cp $TMP_TEMP_PATH $TMP_COVER_PATH
}

if [[ $1 == "echo" ]]; then
  echo "$HOME/.cache/eww/cover.png"
fi

if [[ $1 == "get" ]]; then
  get_song_art
fi
