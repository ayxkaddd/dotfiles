#!/bin/bash

ignore="firefox.instance$(pgrep firefox)"

get_song_art () {
  TMP_DIR="$HOME/.cache/eww"
  TMP_COVER_PATH=$TMP_DIR/cover.png
  TMP_TEMP_PATH=$TMP_DIR/temp.png

  if [[ ! -d $TMP_DIR ]]; then
    mkdir -p $TMP_DIR
  fi

  ART_FROM_SPOTIFY="$(playerctl -i $ignore -p %any,spotify metadata mpris:artUrl | sed -e 's/open.spotify.com/i.scdn.co/g')"
  ART_FROM_BROWSER="$(playerctl -i $ignore -p %any,mpd,chromium,brave metadata mpris:artUrl | sed -e 's/file:\/\///g')"

  if [[ $(playerctl -i $ignore -p spotify,%any,firefox,chromium,brave,mpd metadata mpris:artUrl) ]]; then
    curl -s "$ART_FROM_SPOTIFY" --output $TMP_TEMP_PATH
  elif [[ -n $ART_FROM_BROWSER ]]; then
    cp $ART_FROM_BROWSER $TMP_TEMP_PATH
  else
    cp $HOME/.config/hypr/assets/fallback.png $TMP_TEMP_PATH
  fi

  cp $TMP_TEMP_PATH $TMP_COVER_PATH
}

echo_song_art_url () {
  echo "$HOME/.cache/eww/cover.png"
}

if [[ $1 == "echo" ]]; then
  echo_song_art_url
fi

if [[ $1 == "get" ]]; then
  get_song_art
fi

