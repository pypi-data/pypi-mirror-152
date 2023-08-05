
REM # install wxpython and tomopy from conda-forge

REM # use pip to install some known-safe-for-pip packages
%PREFIX%\Scripts\pip.exe install xraylarch wxmplot wxutils pyepics epicsapps psycopg2-binary pyfai

REM # make desktop icons
%PREFIX%\Scripts\larch.exe -m

echo '# Larch post install done!'
timeout /t 5
