function fish_prompt
    set_color 708491
    echo -n "┌──["
    set_color dc5bbc
    echo -n "$(ip -4 addr | grep -v '127.0.0.1' | grep -v 'secondary' | grep -oP '(?<=inet\s)\d+(\.\d+){3}' | sed -z 's/\n/|/g;s/|\$/\n/' | rev | cut -c 2- | rev)"
    echo -n "|$USER"
    set_color 708491
    echo "]"
    set_color 708491
    echo -n "└──╼[]─"
    set_color 00d19f
    echo (pwd) '$' (set_color normal)
    end
