#!/usr/bin/env python
from resource_management.libraries.functions.version import format_hdp_stack_version, compare_versions
from resource_management import *

# server configurations
config = Script.get_config()

kdc_realm = config['configurations']['krb5-config']['kdc.realm']
kdc_domain = config['configurations']['krb5-config']['kdc.domain']
kdc_admin = config['configurations']['krb5-config']['kdc.admin']
kdc_adminpassword = config['configurations']['krb5-config']['kdc.adminpassword']
kdb_password = config['configurations']['krb5-config']['kdb.password']

#kdc_host = config['configurations']['krb5-config']['kdc.host']
#detect hostname user selected for KDC
clusterHostInfo = config['clusterHostInfo']
kdc_host = str(clusterHostInfo['krb5_master_hosts'][0])