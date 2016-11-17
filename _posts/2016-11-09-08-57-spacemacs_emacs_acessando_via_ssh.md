---
layout: post
title: 'Acessando o spacemacs ou emacs via ssh'
--- 

ssh -t -X <login>@10.32.128.172 "emacs -nw --eval \
'(progn (setq server-host \"10.32.128.172\" server-use-tcp t) (server-start))'"

Fonte: http://stackoverflow.com/questions/12546722/using-emacs-server-and-emacsclient-on-other-machines-as-other-users
