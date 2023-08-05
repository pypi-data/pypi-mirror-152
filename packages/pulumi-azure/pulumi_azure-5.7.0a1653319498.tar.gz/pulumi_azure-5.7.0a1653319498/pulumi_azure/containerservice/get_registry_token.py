# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetRegistryTokenResult',
    'AwaitableGetRegistryTokenResult',
    'get_registry_token',
    'get_registry_token_output',
]

@pulumi.output_type
class GetRegistryTokenResult:
    """
    A collection of values returned by getRegistryToken.
    """
    def __init__(__self__, container_registry_name=None, enabled=None, id=None, name=None, resource_group_name=None, scope_map_id=None):
        if container_registry_name and not isinstance(container_registry_name, str):
            raise TypeError("Expected argument 'container_registry_name' to be a str")
        pulumi.set(__self__, "container_registry_name", container_registry_name)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if scope_map_id and not isinstance(scope_map_id, str):
            raise TypeError("Expected argument 'scope_map_id' to be a str")
        pulumi.set(__self__, "scope_map_id", scope_map_id)

    @property
    @pulumi.getter(name="containerRegistryName")
    def container_registry_name(self) -> str:
        return pulumi.get(self, "container_registry_name")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Whether this Token is enabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="scopeMapId")
    def scope_map_id(self) -> str:
        """
        The Scope Map ID used by the token.
        """
        return pulumi.get(self, "scope_map_id")


class AwaitableGetRegistryTokenResult(GetRegistryTokenResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegistryTokenResult(
            container_registry_name=self.container_registry_name,
            enabled=self.enabled,
            id=self.id,
            name=self.name,
            resource_group_name=self.resource_group_name,
            scope_map_id=self.scope_map_id)


def get_registry_token(container_registry_name: Optional[str] = None,
                       name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRegistryTokenResult:
    """
    Use this data source to access information about an existing Container Registry token.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.containerservice.get_registry_token(name="exampletoken",
        resource_group_name="example-resource-group",
        container_registry_name="example-registry")
    pulumi.export("scopeMapId", example.scope_map_id)
    ```


    :param str container_registry_name: The Name of the Container Registry where the token exists.
    :param str name: The name of the Container Registry token.
    :param str resource_group_name: The Name of the Resource Group where this Container Registry token exists.
    """
    __args__ = dict()
    __args__['containerRegistryName'] = container_registry_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:containerservice/getRegistryToken:getRegistryToken', __args__, opts=opts, typ=GetRegistryTokenResult).value

    return AwaitableGetRegistryTokenResult(
        container_registry_name=__ret__.container_registry_name,
        enabled=__ret__.enabled,
        id=__ret__.id,
        name=__ret__.name,
        resource_group_name=__ret__.resource_group_name,
        scope_map_id=__ret__.scope_map_id)


@_utilities.lift_output_func(get_registry_token)
def get_registry_token_output(container_registry_name: Optional[pulumi.Input[str]] = None,
                              name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRegistryTokenResult]:
    """
    Use this data source to access information about an existing Container Registry token.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.containerservice.get_registry_token(name="exampletoken",
        resource_group_name="example-resource-group",
        container_registry_name="example-registry")
    pulumi.export("scopeMapId", example.scope_map_id)
    ```


    :param str container_registry_name: The Name of the Container Registry where the token exists.
    :param str name: The name of the Container Registry token.
    :param str resource_group_name: The Name of the Resource Group where this Container Registry token exists.
    """
    ...
