# Home Lab

## My Home Lab config :
My main hypervisor is proxmox , I have 2 major VM all of them install consul-client and node-exporter to get service discovery & monitoring use prometheus & consul
this action because logging in proxmox for VM is not very detail

Read more about Home Lab on virgool(persion): https://vrgl.ir/J46uS  
Read more about Monitoring on virgool(persion): https://vrgl.ir/W2egj  
Read more about Monitoring on medium(english): https://medium.com/@mr.salehi/prometheus-consul-3f3df009efaf

![Proxmox](images/proxmox.PNG)

<details><summary><b>Consul Server</b></summary>

![Consul server nodes](images/consul_node.PNG)
  
At its show I have 2 VM (rancher & ubentu) and pve is the proxmox server
  
![Consul server service](images/consul_service.PNG)
  
I have a lot of services and it increases 

</details>

<details><summary><b>Prometheus Server</b></summary>

![Prometheus server](images/Prometheus_targets.PNG)
  
all the node-exporter is up and working
