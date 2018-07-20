
from terrascript import Terrascript
from terrascript import provider as provider
import terrascript.vsphere.r as r
import terrascript.vsphere.d as d


def test_catalog():
    terrascript = Terrascript()

    # Provider
    provider_in = terrascript.add(provider("vsphere",user="x",password="y",vsphere_server="z"))
    provider_out = terrascript.get("provider", "vsphere", "__DEFAULT__")
    assert provider_in == provider_out

    # Data
    dc_in = terrascript.add(d.vsphere_datacenter("dc"))
    dc_out = terrascript.get("data", "vsphere_datacenter", "dc")
    dc_in2 = terrascript.add(d.vsphere_datacenter("dc2"))
    dc_out2 = terrascript.get("data", "vsphere_datacenter", "dc2")
    assert dc_in == dc_out
    assert dc_in2 == dc_out2

    # Resource
    cc_in = terrascript.add(r.vsphere_compute_cluster("cc",name="cc_name",datacenter_id=dc_in.id))
    cc_out = terrascript.get("resource", "vsphere_compute_cluster", "cc")
    assert cc_in == cc_out

    # ... get all resources and data sources by type.
    get_by_type = terrascript.get(None, "vsphere_datacenter", None)
    assert isinstance(get_by_type["data"]["dc"], d.vsphere_datacenter)
    assert isinstance(get_by_type["data"]["dc2"], d.vsphere_datacenter)