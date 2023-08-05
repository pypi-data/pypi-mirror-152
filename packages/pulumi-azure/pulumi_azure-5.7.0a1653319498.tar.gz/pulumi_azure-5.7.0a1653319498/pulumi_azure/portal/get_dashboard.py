# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetDashboardResult',
    'AwaitableGetDashboardResult',
    'get_dashboard',
    'get_dashboard_output',
]

@pulumi.output_type
class GetDashboardResult:
    """
    A collection of values returned by getDashboard.
    """
    def __init__(__self__, dashboard_properties=None, id=None, location=None, name=None, resource_group_name=None, tags=None):
        if dashboard_properties and not isinstance(dashboard_properties, str):
            raise TypeError("Expected argument 'dashboard_properties' to be a str")
        pulumi.set(__self__, "dashboard_properties", dashboard_properties)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="dashboardProperties")
    def dashboard_properties(self) -> str:
        """
        JSON data representing dashboard body.
        """
        return pulumi.get(self, "dashboard_properties")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The Azure Region where the shared Azure Portal dashboard exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags assigned to the shared Azure Portal dashboard.
        """
        return pulumi.get(self, "tags")


class AwaitableGetDashboardResult(GetDashboardResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDashboardResult(
            dashboard_properties=self.dashboard_properties,
            id=self.id,
            location=self.location,
            name=self.name,
            resource_group_name=self.resource_group_name,
            tags=self.tags)


def get_dashboard(dashboard_properties: Optional[str] = None,
                  name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDashboardResult:
    """
    Use this data source to access information about an existing shared dashboard in the Azure Portal. This is the data source of the `portal.Dashboard` resource.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.portal.get_dashboard(name="existing-dashboard",
        resource_group_name="dashboard-rg")
    pulumi.export("id", data["azurerm_dashboard"]["example"]["id"])
    ```


    :param str dashboard_properties: JSON data representing dashboard body.
    :param str name: Specifies the name of the shared Azure Portal Dashboard.
    :param str resource_group_name: Specifies the name of the resource group the shared Azure Portal Dashboard is located in.
    """
    __args__ = dict()
    __args__['dashboardProperties'] = dashboard_properties
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:portal/getDashboard:getDashboard', __args__, opts=opts, typ=GetDashboardResult).value

    return AwaitableGetDashboardResult(
        dashboard_properties=__ret__.dashboard_properties,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        resource_group_name=__ret__.resource_group_name,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_dashboard)
def get_dashboard_output(dashboard_properties: Optional[pulumi.Input[Optional[str]]] = None,
                         name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDashboardResult]:
    """
    Use this data source to access information about an existing shared dashboard in the Azure Portal. This is the data source of the `portal.Dashboard` resource.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.portal.get_dashboard(name="existing-dashboard",
        resource_group_name="dashboard-rg")
    pulumi.export("id", data["azurerm_dashboard"]["example"]["id"])
    ```


    :param str dashboard_properties: JSON data representing dashboard body.
    :param str name: Specifies the name of the shared Azure Portal Dashboard.
    :param str resource_group_name: Specifies the name of the resource group the shared Azure Portal Dashboard is located in.
    """
    ...
