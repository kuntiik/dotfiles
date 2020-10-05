syntax on

call plug#begin('~/.config/nvim/plugged')
Plug 'lifepillar/vim-solarized8'
Plug 'iCyMind/NeoSolarized'
Plug 'preservim/nerdcommenter'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'mboughaba/i3config.vim'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'dhruvasagar/vim-table-mode'
Plug 'lervag/vimtex'
Plug 'liuchengxu/vim-which-key'
Plug 'mhinz/vim-startify'
Plug 'kshenoy/vim-signature'
Plug 'tpope/vim-surround'
Plug 'puremourning/vimspector'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
"Plug 'honza/vim-snippets'

Plug 'francoiscabrol/ranger.vim'
Plug 'rbgrouleff/bclose.vim'
call plug#end()

set background=dark
colorscheme NeoSolarized
"colorscheme solarized8
set termguicolors
let g:airline_powerline_fonts=1
let g:airline_theme='solarized'
set showtabline=2

set number
set relativenumber

set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set smartcase
set incsearch
set scrolloff=5

set updatetime=500

set splitright
set splitbelow

set mouse=a
set cursorline


let mapleader = " "
let maplocalleader = "`"
nnoremap <Space> <Nop>

"move between buffers
nnoremap <silent> <TAB> :bnext<CR>
nnoremap <silent> <S-TAB> :bprevious<CR>


set clipboard+=unnamedplus

nnoremap <leader>ev :vsplit $MYVIMRC<cr>
nnoremap <leader>sv :source $MYVIMRC<cr>

set undodir=~/.config/nvim/undo-dir
set undofile

source $HOME/.config/nvim/plug-config/coc.vim
source $HOME/.config/nvim/plug-config/snippets.vim
source $HOME/.config/nvim/plug-config/vimspector.vim

aug i3config_ft_detection
  au!
  au BufNewFile,BufRead ~/.config/i3/config set filetype=i3config
aug end

"TODO modify for tex only
nnoremap j gj
nnoremap k gk

" Get text in files with Rg
command! -bang -nargs=* Rg
  \ call fzf#vim#grep(
  \   'rg --column --line-number --no-heading --color=always --smart-case '.shellescape(<q-args>), 1,
  \   fzf#vim#with_preview(), <bang>0)
