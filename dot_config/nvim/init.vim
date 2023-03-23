filetype plugin on

nnoremap <space> <Nop>
map <space> <leader>

set relativenumber
set cursorline
set mouse=a

set tabstop=4
set softtabstop=4
set shiftwidth=4

set splitright
set splitbelow

if has("unnamedplus")
    set clipboard=unnamedplus
else
    set clipboard=unnamed
endif

if !isdirectory($HOME."/.config/nvim/undo-dir")
    call mkdir($HOME."/.config/nvim/undo-dir", "p", 0700)
endif
set undodir=~/.config/nvim/undo-dir
set undofile

call plug#begin('~/.config/nvim/plugged')
Plug 'navarasu/onedark.nvim'
Plug 'nvim-lualine/lualine.nvim'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'preservim/nerdcommenter'
Plug 'kyazdani42/nvim-web-devicons'
call plug#end()

colorscheme OneDark
source ~/.config/nvim/coc.vim

lua << END
require('lualine').setup()
END

