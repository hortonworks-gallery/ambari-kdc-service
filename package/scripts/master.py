import sys, os, pwd, signal, time
from resource_management import *
from subprocess import call

class Master(Script):
  def install(self, env):
    # Install packages listed in metainfo.xml
    self.install_packages(env)
    self.configure(env)
    import params

    Execute('sed -i "s/EXAMPLE.COM/'+params.kdc_realm+'/g" /var/lib/ambari-server/resources/scripts/krb5.conf')
    Execute('sed -i "s/kerberos.example.com/'+params.kdc_host+'/g" /var/lib/ambari-server/resources/scripts/krb5.conf')
    Execute('sed -i "s/example.com/'+params.kdc_domain+'/g" /var/lib/ambari-server/resources/scripts/krb5.conf')

    Execute('/bin/cp -f /var/lib/ambari-server/resources/scripts/krb5.conf /etc')

    Execute('echo "'+params.kdb_password+'" > passwd.txt')
    Execute('echo "'+params.kdb_password+'" >> passwd.txt')
    Execute('echo >> passwd.txt')
    Execute('kdb5_util create -s < passwd.txt')
    Execute('rm passwd.txt')

    Execute('/etc/rc.d/init.d/krb5kdc start')
    Execute('/etc/rc.d/init.d/kadmin start')

    Execute('chkconfig krb5kdc on')
    Execute('chkconfig kadmin on')

    Execute('echo "'+params.kdc_adminpassword+'" > passwd.txt')
    Execute('echo "'+params.kdc_adminpassword+'" >> passwd.txt')
    Execute('echo >> passwd.txt')
    Execute('kadmin.local -q "addprinc '+params.kdc_admin+'" < passwd.txt')
    Execute('rm passwd.txt')

    Execute('echo "*/admin@HORTONWORKS.COM *" > /var/kerberos/krb5kdc/kadm5.acl')

    #Execute('/etc/rc.d/init.d/krb5kdc restart')
    #Execute('/etc/rc.d/init.d/kadmin restart')


  def configure(self, env):
    import params
    env.set_params(params)

  def stop(self, env):
    import params
    Execute('service krb5kdc stop')
    Execute('service kadmin stop')
          
  def start(self, env):
    import params
    Execute('service krb5kdc start')
    Execute('service kadmin start')
	

  def status(self, env):
    import params
    Execute('service krb5kdc status')

    
if __name__ == "__main__":
  Master().execute()
