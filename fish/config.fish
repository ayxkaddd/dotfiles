alias ls='lsd --group-directories-first'
alias ll='ls -hlA'
alias l='ls -l'
alias fishcfg='nvim $HOME/.config/fish/config.fish'
alias code='vscodium'
alias fdisks='df --total --block-size=G | grep dev/sd --color=never'
alias myps='watch ps o pid,ppid,stat,comm'
alias neofetch="/bin/neofetch --ascii $HOME/.config/neofetch/btw --ascii_colors 5 --colors 2 2 7 2 2 7"
alias ....="cd ../../../"
alias ...="cd ../../"
alias  ..="cd ../"
alias logouth="hyprclt dispatch exit"
alias encrypt="openssl enc -aes-256-cbc -in -out"
alias decrypt="openssl enc -d -aes-256-cbc -in -out"
alias muc="muc --file /home/ayx/.local/share/fish/fish_history.raw"
alias cls="clear"

fish_add_path $HOME/.spicetify $HOME/.local/bin $HOME/.local/scripts
