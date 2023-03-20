filetype plugin on

set relativenumber

nnoremap <space> <Nop>
map <space> <leader>

if has("unnamedplus")
    set clipboard=unnamedplus
else
    set clipboard=unnamed
endif

call plug#begin()
Plug 'navarasu/onedark.nvim'
Plug 'nvim-lualine/lualine.nvim'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'preservim/nerdcommenter'
Plug 'kyazdani42/nvim-web-devicons'
call plug#end()

source ~/.config/nvim/coc.vim
