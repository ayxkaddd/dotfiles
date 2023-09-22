vim.g.mapleader = " "

local keymap = vim.keymap -- haz las cosas facil..

-- General Keymaps

-- window management
keymap.set("n", "<leader>sv", "<C-w>v") -- split window vertically
keymap.set("n", "<leader>sh", "<C-w>s") -- split window horizontally
keymap.set("n", "<leader>se", "<C-w>=") -- make split windows equal width & height
keymap.set("n", "<leader>sx", ":close<CR>") -- close current split window

keymap.set("n", "<leader>o", ":tabnew<CR>") -- open new tab
keymap.set("n", "<leader>x", ":tabclose<CR>") -- close current tab
keymap.set("n", "<leader>n", ":tabn<CR>") --  go to next tab
keymap.set("n", "<leader>p", ":tabp<CR>") --  go to previous tab
keymap.set("n", "<leader>C", ":Telescope find_files<CR>", { noremap = true, silent = true })

-- nvim-tree
keymap.set("n", "<leader>t", ":NvimTreeToggle<CR>") -- toggle file explorer

keymap.set("n", "E", "$", { noremap = true} )
