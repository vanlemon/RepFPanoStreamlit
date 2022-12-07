#! /bin/bash

read -p "Do you want to put the file? (y/n) " answer

cd $(dirname $0)
./push.sh

sftp lab724 << EOF
put -r /Users/limengfan/PycharmProjects/220925_RepFPanoStreamlit /home/lmf/Deploy
EOF
