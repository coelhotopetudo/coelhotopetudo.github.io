ssh -t -X $USER@10.32.128.172 "emacs -nw --eval \
'(progn (setq server-host \"10.32.128.172\" server-use-tcp t) (server-start))'"
