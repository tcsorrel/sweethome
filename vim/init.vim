if &compatible
  set nocompatible
endif
" Add the dein installation directory into runtimepath
set runtimepath+=~/.cache/dein/repos/github.com/Shougo/dein.vim

if dein#load_state('~/.cache/dein')
  call dein#begin('~/.cache/dein')

  call dein#add('~/.cache/dein/repos/github.com/Shougo/dein.vim')

  call dein#add('icymind/NeoSolarized')
  call dein#add('vim-airline/vim-airline')
  call dein#add('vim-airline/vim-airline-themes')
  call dein#add('tpope/vim-fugitive')
  call dein#add('scrooloose/nerdtree')
  call dein#add('dense-analysis/ale')
  call dein#add('rking/ag.vim')
  call dein#add('jremmen/vim-ripgrep')
" requires
" aptitude install silversearcher-ag (available since Ubuntu 14.04)
  call dein#add('kien/ctrlp.vim')
  call dein#add('mattn/emmet-vim')
  call dein#add('hynek/vim-python-pep8-indent')

  if !has('nvim')
    call dein#add('roxma/nvim-yarp')
    call dein#add('roxma/vim-hug-neovim-rpc')
  endif

call dein#end()
call dein#save_state()
endif

filetype plugin indent on
syntax enable

" If you want to install not installed plugins on startup.
if dein#check_install()
  call dein#install()
endif

" Airline setup
let g:airline_theme='base16_solarized'

" ALE setup
let g:ale_completion_enabled = 1
" requires 'pip install python-language-server flake8 pylint'
let g:ale_linters = {'python': ['pyls', 'flake8', 'pylint']}
" requires 'pip install black isort'
let g:ale_fixers = {'python': ['black', 'isort']}
let g:ale_fix_on_save = 1

" solarized 
syntax on
set background=dark
set termguicolors
colorscheme NeoSolarized

" General
set number
"set textwidth=80
"set cc=+1

" let tab always be 4 spaces
set shiftwidth=4
set softtabstop=4
set expandtab

" wildmenu
set wildmenu
set wildignore=*.o,*~,*.pyc

" check spelling (requiring aspell, hunspell or ispell to be installed)
"set spell

" search
set hlsearch

set mouse=""

" Salt state file syntax highlight
filetype on
au BufNewFile,BufRead *.sls set filetype=yaml

au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif

" NerdTree
" Force encoding for NerdTree directorie arrows
set encoding=utf-8

"load externalfiles
"execute 'source '. $HOME . '/vim/shortkeys.vim'
map <F2> <Esc>:NERDTreeToggle<CR>
map <F3> <Esc>:CtrlP<CR>
"Toggle for mouse copy/paste
map <F10> <Esc>:set nu textwidth=80 cc=1 nopaste<CR>
map <F12> <Esc>:set nonu textwidth=0 cc=0 paste<CR>

function! SourceIfExists(file)
  if filereadable(expand(a:file))
    exe 'source' a:file
  endif
endfunction

call SourceIfExists("./utils.vim")
