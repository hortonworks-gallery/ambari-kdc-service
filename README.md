#### An Ambari Stack for Kerberos KDC
Ambari stack for easily installing and managing KDC on HDP cluster

- Download HDP 2.2 sandbox VM image (Sandbox_HDP_2.2_VMware.ova) from [Hortonworks website](http://hortonworks.com/products/hortonworks-sandbox/)
- Import Sandbox_HDP_2.2_VMware.ova into VMWare and set the VM memory size to 8GB
- Now start the VM
- After it boots up, find the IP address of the VM and add an entry into your machines hosts file e.g.
```
192.168.191.241 sandbox.hortonworks.com sandbox    
```
- Connect to the VM via SSH (password hadoop) and start Ambari server
```
ssh root@sandbox.hortonworks.com
/root/start_ambari.sh
```

- To deploy the KDC stack, run below
```
cd /var/lib/ambari-server/resources/stacks/HDP/2.2/services
git clone https://github.com/abajwa-hw/kdc-stack.git    
sudo service ambari restart
```
- Then you can click on 'Add Service' from the 'Actions' dropdown menu in the bottom left of the Ambari dashboard:

On bottom left -> Actions -> Add service -> check KDC server -> Next -> Next -> Enter password -> Next -> Deploy
![Image](../master/screenshots/screenshot-vnc-config.png?raw=true)

- On successful deployment you will see the KDC service as part of Ambari stack and will be able to start/stop the service from here:
![Image](../master/screenshots/screenshot-vnc-stack.png?raw=true)

- When you've completed the install process, KDC server will appear in Ambari 
![Image](../master/screenshots/screenshot-freeipa-stack.png?raw=true)

- You can see the parameters you configured under 'Configs' tab
![Image](../master/screenshots/screenshot-freeipa-stack-config.png?raw=true)

- To remove the KDC service: 
  - Stop the service via Ambari
  - Delete the service
  
    ```
    curl -u admin:admin -i -H 'X-Requested-By: ambari' -X DELETE http://sandbox.hortonworks.com:8080/api/v1/clusters/Sandbox/services/KRB5
    ```
  - Remove artifacts 
  
    ```
    /var/lib/ambari-server/resources/stacks/HDP/2.2/services/openldap-stack/remove.sh
    ```


#### Run kadmin commands

- You now have Kerberos KDC running on your Hadoop cluster

```
# kadmin -p admin/admin -w hortonworks -r HORTONWORKS.COM -q "get_principal admin/admin"
Authenticating as principal admin/admin with password.
Principal: admin/admin@HORTONWORKS.COM
Expiration date: [never]
Last password change: Mon Feb 02 01:22:39 PST 2015
Password expiration date: [none]
Maximum ticket life: 1 day 00:00:00
Maximum renewable life: 0 days 00:00:00
Last modified: Mon Feb 02 01:22:39 PST 2015 (root/admin@HORTONWORKS.COM)
Last successful authentication: [never]
Last failed authentication: [never]
Failed password attempts: 0
Number of keys: 4
Key: vno 1, aes256-cts-hmac-sha1-96, no salt
Key: vno 1, aes128-cts-hmac-sha1-96, no salt
Key: vno 1, des3-cbc-sha1, no salt
Key: vno 1, arcfour-hmac, no salt
MKey: vno 1
Attributes:
Policy: [none]
``` 


