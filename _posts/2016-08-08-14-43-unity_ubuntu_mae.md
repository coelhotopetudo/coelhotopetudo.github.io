---
layout: post
title: 'Fazendo o unity voltar a funcionar para conta da minha mae'
---



Can someone affected by this please run

  gsettings get org.compiz.core:/org/compiz/profiles/unity/plugins/core/ active-plugins

  in a terminal and paste the output to this bug?

  Also please attach your ~/.xsession-errors file.

  Then try running

    gsettings reset org.compiz.core:/org/compiz/profiles/unity/plugins/core/ active-plugins

    and restarting/logging out and in to see if you get your session back.


fonte: https://bugs.launchpad.net/ubuntu/+source/compiz/+bug/1166765/comments/9




***************



Switch to tty1 using Ctrl+Alt+F1

Login to your user account

And export your Display with

export DISPLAY=:0

Add opengl to Compiz active plugins list

```
dconf write /org/compiz/profiles/unity/plugins/core/active-plugins "[`dconf read /org/compiz/profiles/unity/plugins/core/active-plugins | sed -r 's/(\[|\])//g'`, 'opengl']"
```

Or reset the key to default

```
dconf reset /org/compiz/profiles/unity/plugins/core/active-plugins
```

If it didn't work, come back and reset all Compiz settings to defaults

```
dconf reset -f /org/compiz/
```

Restart graphical display manager after one of the dconf command above

```
sudo service lightdm restart
```

Switch back to tty7 (X graphic display) Ctrl+Alt+F7

Try login again.


*********************

De alguma forma, tentando a maioria dos comandos possíveis, no ccsm, o Ubuntu está sem checkbox, cliquei no botão e apareceu para reabilitar, pediu para reabilitar uns dois e depois apareceu resolver conflitos e escolhi resolver atribuindo um valor alguma coisa

[editar o .dmrc para tentar o 2d, mas acho que não estava disponível no 14.04](http://askubuntu.com/questions/145359/how-can-i-make-unity-2d-the-default-session-at-start-up)

[tentei bastante desse, instalando o compizconfig-settings-manager (ccsm)](http://askubuntu.com/questions/17381/unity-doesnt-load-no-launcher-no-dash-appears/)

fiz pesquisa no google por unity no icons

pode ser pq minha mãe deve ter instalado coisa, vi q tinha um plugin do facebook no chrome

http://askubuntu.com/questions/61947/unity-shows-no-icons-or-launcher-i-get-only-the-wallpaper
http://askubuntu.com/questions/17381/unity-doesnt-load-no-launcher-no-dash-appears
unity no icons mae ubuntu
