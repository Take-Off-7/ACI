from acitoolkit.acitoolkit import *
from pprint import pprint

# See capabilities
# print(dir())

url = 'https://sandboxapicdc.cisco.com'
user = 'admin'
pw = '!v3G@!4@Y'

# Create the session object
session = Session(url, user, pw)

# Login to the session
session.login()

# Get tenants
tenants = Tenant.get(session)
for tenant in tenants:
    print(tenant.name)
    print(tenant.descr)
    print('*' * 30)
    print(' ')

# Create a new Tenant
new_tenant = Tenant("TakeOff_Landlord")

# Create the application profile and the EPG
anp = AppProfile('TakeOff_app', new_tenant)
epg = EPG('TakeOff_epg', anp)

# Create the L3 namespace
context = Context('TakeOff_VRF', new_tenant)
bridge_domain = BridgeDomain('TakeOff_bd', new_tenant)

# Associate the BD with the L3 Namespace
bridge_domain.add_context(context)
epg.add_bd(bridge_domain)

##### Tenant Creation is Completed #####
print(new_tenant.get_url())
pprint(new_tenant.get_json())

# response = session.push_to_apic(
#     new_tenant.get_url(),
#     data=new_tenant.get_json()
# )
# pprint(response)

tenants = Tenant.get(session)
for tenant in tenants:
    if tenant.name == 'TakeOff_Landlord':
        print(tenant.name)

# To delete tenant
new_tenant.mark_as_deleted()
session.push_to_apic(
    new_tenant.get_url(),
    data=new_tenant.get_json()
)

