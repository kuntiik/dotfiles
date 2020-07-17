syntax on

call plug#begin('~/.config/nvim/bundle')
Plug 'lifepillar/vim-solarized8'
Plug 'iCyMind/NeoSolarized'
Plug 'preservim/nerdcommenter'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
call plug#end()

set background=dark
colorscheme NeoSolarized
"colorscheme solarized8
set termguicolors

set number
set relativenumber

set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set smartcase
set incsearch

set updatetime=500

set splitright
set splitbelow

set mouse=a
set cursorline


let mapleader = ","
let maplocalleader = "`"

set clipboard+=unnamedplus

nnoremap <leader>ev :vsplit $MYVIMRC<cr>
nnoremap <leader>sv :source $MYVIMRC<cr>

set undodir=~/.config/nvim/undo-dir
set undofile

source $HOME/.config/nvim/plug-config/coc.vim
