
from terrascript import Terrascript
from terrascript import provider as provider
import terrascript.vsphere.r as r
import terrascript.vsphere.d as d


def test_catalog():
    terrascript = Terrascript()

    # Provider
    provider_in = terrascript.add(provider("vsphere",
                                           user="x",
                                           password="y",
                                           vsphere_server="z"))
    provider_out = terrascript.get("provider", "vsphere", "__DEFAULT__")

    # Data
    dc_in = terrascript.add(d.vsphere_datacenter("dc"))
    dc_out = terrascript.get("data", "vsphere_datacenter", "dc")

    # Resource
    cc_in = terrascript.add(r.vsphere_compute_cluster("cc",
                                                      name="cc_name",
                                                      datacenter_id=dc_in.id))
    cc_out = terrascript.get("resource", "vsphere_compute_cluster", "cc")


    print("Catalog: {}".format(terrascript.catalog))
    assert provider_in == provider_out
    assert dc_in == dc_out
    assert cc_in == cc_out