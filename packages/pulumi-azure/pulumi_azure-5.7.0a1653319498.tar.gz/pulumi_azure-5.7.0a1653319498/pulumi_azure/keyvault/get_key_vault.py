# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetKeyVaultResult',
    'AwaitableGetKeyVaultResult',
    'get_key_vault',
    'get_key_vault_output',
]

@pulumi.output_type
class GetKeyVaultResult:
    """
    A collection of values returned by getKeyVault.
    """
    def __init__(__self__, access_policies=None, enable_rbac_authorization=None, enabled_for_deployment=None, enabled_for_disk_encryption=None, enabled_for_template_deployment=None, id=None, location=None, name=None, network_acls=None, purge_protection_enabled=None, resource_group_name=None, sku_name=None, tags=None, tenant_id=None, vault_uri=None):
        if access_policies and not isinstance(access_policies, list):
            raise TypeError("Expected argument 'access_policies' to be a list")
        pulumi.set(__self__, "access_policies", access_policies)
        if enable_rbac_authorization and not isinstance(enable_rbac_authorization, bool):
            raise TypeError("Expected argument 'enable_rbac_authorization' to be a bool")
        pulumi.set(__self__, "enable_rbac_authorization", enable_rbac_authorization)
        if enabled_for_deployment and not isinstance(enabled_for_deployment, bool):
            raise TypeError("Expected argument 'enabled_for_deployment' to be a bool")
        pulumi.set(__self__, "enabled_for_deployment", enabled_for_deployment)
        if enabled_for_disk_encryption and not isinstance(enabled_for_disk_encryption, bool):
            raise TypeError("Expected argument 'enabled_for_disk_encryption' to be a bool")
        pulumi.set(__self__, "enabled_for_disk_encryption", enabled_for_disk_encryption)
        if enabled_for_template_deployment and not isinstance(enabled_for_template_deployment, bool):
            raise TypeError("Expected argument 'enabled_for_template_deployment' to be a bool")
        pulumi.set(__self__, "enabled_for_template_deployment", enabled_for_template_deployment)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_acls and not isinstance(network_acls, list):
            raise TypeError("Expected argument 'network_acls' to be a list")
        pulumi.set(__self__, "network_acls", network_acls)
        if purge_protection_enabled and not isinstance(purge_protection_enabled, bool):
            raise TypeError("Expected argument 'purge_protection_enabled' to be a bool")
        pulumi.set(__self__, "purge_protection_enabled", purge_protection_enabled)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if sku_name and not isinstance(sku_name, str):
            raise TypeError("Expected argument 'sku_name' to be a str")
        pulumi.set(__self__, "sku_name", sku_name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if vault_uri and not isinstance(vault_uri, str):
            raise TypeError("Expected argument 'vault_uri' to be a str")
        pulumi.set(__self__, "vault_uri", vault_uri)

    @property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> Sequence['outputs.GetKeyVaultAccessPolicyResult']:
        """
        One or more `access_policy` blocks as defined below.
        """
        return pulumi.get(self, "access_policies")

    @property
    @pulumi.getter(name="enableRbacAuthorization")
    def enable_rbac_authorization(self) -> bool:
        """
        Is Role Based Access Control (RBAC) for authorization of data actions enabled on this Key Vault?
        """
        return pulumi.get(self, "enable_rbac_authorization")

    @property
    @pulumi.getter(name="enabledForDeployment")
    def enabled_for_deployment(self) -> bool:
        """
        Can Azure Virtual Machines retrieve certificates stored as secrets from the Key Vault?
        """
        return pulumi.get(self, "enabled_for_deployment")

    @property
    @pulumi.getter(name="enabledForDiskEncryption")
    def enabled_for_disk_encryption(self) -> bool:
        """
        Can Azure Disk Encryption retrieve secrets from the Key Vault?
        """
        return pulumi.get(self, "enabled_for_disk_encryption")

    @property
    @pulumi.getter(name="enabledForTemplateDeployment")
    def enabled_for_template_deployment(self) -> bool:
        """
        Can Azure Resource Manager retrieve secrets from the Key Vault?
        """
        return pulumi.get(self, "enabled_for_template_deployment")

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
        The Azure Region in which the Key Vault exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkAcls")
    def network_acls(self) -> Sequence['outputs.GetKeyVaultNetworkAclResult']:
        return pulumi.get(self, "network_acls")

    @property
    @pulumi.getter(name="purgeProtectionEnabled")
    def purge_protection_enabled(self) -> bool:
        """
        Is purge protection enabled on this Key Vault?
        """
        return pulumi.get(self, "purge_protection_enabled")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="skuName")
    def sku_name(self) -> str:
        """
        The Name of the SKU used for this Key Vault.
        """
        return pulumi.get(self, "sku_name")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags assigned to the Key Vault.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The Azure Active Directory Tenant ID used to authenticate requests for this Key Vault.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="vaultUri")
    def vault_uri(self) -> str:
        """
        The URI of the vault for performing operations on keys and secrets.
        """
        return pulumi.get(self, "vault_uri")


class AwaitableGetKeyVaultResult(GetKeyVaultResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKeyVaultResult(
            access_policies=self.access_policies,
            enable_rbac_authorization=self.enable_rbac_authorization,
            enabled_for_deployment=self.enabled_for_deployment,
            enabled_for_disk_encryption=self.enabled_for_disk_encryption,
            enabled_for_template_deployment=self.enabled_for_template_deployment,
            id=self.id,
            location=self.location,
            name=self.name,
            network_acls=self.network_acls,
            purge_protection_enabled=self.purge_protection_enabled,
            resource_group_name=self.resource_group_name,
            sku_name=self.sku_name,
            tags=self.tags,
            tenant_id=self.tenant_id,
            vault_uri=self.vault_uri)


def get_key_vault(name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKeyVaultResult:
    """
    Use this data source to access information about an existing Key Vault.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.keyvault.get_key_vault(name="mykeyvault",
        resource_group_name="some-resource-group")
    pulumi.export("vaultUri", example.vault_uri)
    ```


    :param str name: Specifies the name of the Key Vault.
    :param str resource_group_name: The name of the Resource Group in which the Key Vault exists.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:keyvault/getKeyVault:getKeyVault', __args__, opts=opts, typ=GetKeyVaultResult).value

    return AwaitableGetKeyVaultResult(
        access_policies=__ret__.access_policies,
        enable_rbac_authorization=__ret__.enable_rbac_authorization,
        enabled_for_deployment=__ret__.enabled_for_deployment,
        enabled_for_disk_encryption=__ret__.enabled_for_disk_encryption,
        enabled_for_template_deployment=__ret__.enabled_for_template_deployment,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        network_acls=__ret__.network_acls,
        purge_protection_enabled=__ret__.purge_protection_enabled,
        resource_group_name=__ret__.resource_group_name,
        sku_name=__ret__.sku_name,
        tags=__ret__.tags,
        tenant_id=__ret__.tenant_id,
        vault_uri=__ret__.vault_uri)


@_utilities.lift_output_func(get_key_vault)
def get_key_vault_output(name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKeyVaultResult]:
    """
    Use this data source to access information about an existing Key Vault.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.keyvault.get_key_vault(name="mykeyvault",
        resource_group_name="some-resource-group")
    pulumi.export("vaultUri", example.vault_uri)
    ```


    :param str name: Specifies the name of the Key Vault.
    :param str resource_group_name: The name of the Resource Group in which the Key Vault exists.
    """
    ...
