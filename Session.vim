let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/Docker/dissocam_documentation
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd docker-compose.override.yml
$argadd docker-compose.yml
$argadd pythonScripts/api.py
$argadd pythonScripts/dissocam.py
$argadd pythonScripts/helper_functions.py
$argadd pythonScripts/__init__.py
$argadd pythonScripts/wsgi.py
$argadd docs/source/acronyms.rst
$argadd docs/source/codesdocumentation.rst
$argadd docs/source/index.rst
$argadd docs/source/introduction.rst
$argadd docs/source/references.rst
$argadd docs/source/versionhistory.rst
$argadd docs/source/conf.py
$argadd docs/source/\*.yml
edit docker-compose.override.yml
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 1 - ((0 * winheight(0) + 25) / 50)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
tabnext 1
badd +0 docker-compose.override.yml
badd +0 docker-compose.yml
badd +0 pythonScripts/api.py
badd +0 pythonScripts/dissocam.py
badd +0 pythonScripts/helper_functions.py
badd +0 pythonScripts/__init__.py
badd +0 pythonScripts/wsgi.py
badd +0 docs/source/acronyms.rst
badd +0 docs/source/codesdocumentation.rst
badd +0 docs/source/index.rst
badd +0 docs/source/introduction.rst
badd +0 docs/source/references.rst
badd +0 docs/source/versionhistory.rst
badd +0 docs/source/conf.py
badd +0 docs/source/\*.yml
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOFc
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
