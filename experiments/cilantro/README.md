# backups

```
for ((i=2;i<=20;i++)); do ssh-copy-id 10.10.1.$i; sleep 1 ; done
for ((i=2;i<=20;i++)); do echo 10.10.1.$i; done > ~/.pssh_hosts_files
  
parallel-ssh -i -h ~/.pssh_hosts_files date

parallel-ssh -h ~/.pssh_hosts_files -- sudo apt-get -y update

parallel-scp -r -i -h ~/.pssh_hosts_files peakler/ ~/
parallel-ssh -i -h ~/.pssh_hosts_files -- ~/peakler/scripts/install_k8s.sh
parallel-ssh -i -h ~/.pssh_hosts_files -- rm -rf peakler

crontab crontab.txt
crontab -r
```
