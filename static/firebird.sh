vim -c 'map <Enter> :w <Bar> !nohup python firebird.py >> /tmp/res.txt <CR><CR>' firebird.sql
#watch -n 1 cat /tmp/res.txt
