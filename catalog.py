from terrascript import Terrascript
from terrascript import provider as provider
import terrascript.vsphere.r as r
import terrascript.vsphere.d as d


def get_counts():
    item_class = "data"
    item_type = "vsphere_resource_pool"




def catalog():
    ts = Terrascript()
    vsphere = ts.add(provider('vsphere',
                              user='administrator@vsphere.local',
                              password='Secret@123',
                              vsphere_server='acnvc1',
                              allow_unverified_ssl='true'))

    dc = ts.add(d.vsphere_datacenter(obj_name='vesxi'))
    rp = ts.add(d.vsphere_resource_pool(obj_name='resource_pool',  # hack :( can't get naming to work
                                        name='rp',
                                        datacenter_id=dc.id))
    rp2 = ts.add(d.vsphere_resource_pool(obj_name='resource_pool2',  # hack :( can't get naming to work
                                        name='rp2',
                                        datacenter_id=dc.id))


    item = "vsphere_resource_pool"
    rp_2 = ts.get(item_class="data",
                  item_type="vsphere_resource_pool",
                  item_name="resource_pool")
    print(rp_2)
    print("EOF")

    print("Getting counts")
    item_class = "data"
    item_type = "vsphere_resource_pool"


    keys = ts.catalog[item_class][item_type]
    num_keys = len(keys)
    print(keys)
    ts.dump()




    print("EOF")
    return ts


ts = catalog()
