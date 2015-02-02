#!/usr/bin/env python
from resource_management.libraries.functions.version import format_hdp_stack_version, compare_versions
from resource_management import *

# server configurations
config = Script.get_config()

kdc_host = config['configurations']['krb5-config']['kdc.host']
kdc_realm = config['configurations']['krb5-config']['kdc.realm']
kdc_domain = config['configurations']['krb5-config']['kdc.domain']
kdc_admin = config['configurations']['krb5-config']['kdc.admin']
kdc_adminpassword = config['configurations']['krb5-config']['kdc.adminpassword']
kdb_password = config['configurations']['krb5-config']['kdb.password']



   <property>
    <name>kdc.host</name>
    <value>sandbox.hortonworks.com</value>
    <description>Host name where KDC resides e.g. sandbox.hortonworks.com</description>
  </property> 