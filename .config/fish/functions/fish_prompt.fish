function fish_prompt
    set_color e4b9b5 
    set mdpwd (string replace --all -- "$HOME" "~" $PWD)
    echo -n (set_color normal)"[ "(set_color D27D9F)"$USER"(set_color E6A4A2)"@"(set_color E78F8E)"gh0st "(set_color normal)" ]"
    set_color E6A4A2 
    echo "" $mdpwd""'#' (set_color normal)
end
