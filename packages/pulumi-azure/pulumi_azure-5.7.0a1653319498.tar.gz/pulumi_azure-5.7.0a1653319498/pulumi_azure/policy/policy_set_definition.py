# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['PolicySetDefinitionArgs', 'PolicySetDefinition']

@pulumi.input_type
class PolicySetDefinitionArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 policy_definition_references: pulumi.Input[Sequence[pulumi.Input['PolicySetDefinitionPolicyDefinitionReferenceArgs']]],
                 policy_type: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 management_group_id: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[str]] = None,
                 policy_definition_groups: Optional[pulumi.Input[Sequence[pulumi.Input['PolicySetDefinitionPolicyDefinitionGroupArgs']]]] = None):
        """
        The set of arguments for constructing a PolicySetDefinition resource.
        :param pulumi.Input[str] display_name: The display name of the policy set definition.
        :param pulumi.Input[Sequence[pulumi.Input['PolicySetDefinitionPolicyDefinitionReferenceArgs']]] policy_definition_references: One or more `policy_definition_reference` blocks as defined below.
        :param pulumi.Input[str] policy_type: The policy set type. Possible values are `BuiltIn` or `Custom`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] description: The description of the policy set definition.
        :param pulumi.Input[str] management_group_id: The name of the Management Group where this policy set definition should be defined. Changing this forces a new resource to be created.
        :param pulumi.Input[str] metadata: The metadata for the policy set definition. This is a JSON object representing additional metadata that should be stored with the policy definition.
        :param pulumi.Input[str] name: The name of the policy set definition. Changing this forces a new resource to be created.
        :param pulumi.Input[str] parameters: Parameters for the policy set definition. This field is a JSON object that allows you to parameterize your policy definition.
        :param pulumi.Input[Sequence[pulumi.Input['PolicySetDefinitionPolicyDefinitionGroupArgs']]] policy_definition_groups: One or more `policy_definition_group` blocks as defined below.
        """
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "policy_definition_references", policy_definition_references)
        pulumi.set(__self__, "policy_type", policy_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if management_group_id is not None:
            pulumi.set(__self__, "management_group_id", management_group_id)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if policy_definition_groups is not None:
            pulumi.set(__self__, "policy_definition_groups", policy_definition_groups)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The display name of the policy set definition.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="policyDefinitionReferences")
    def policy_definition_references(self) -> pulumi.Input[Sequence[pulumi.Input['PolicySetDefinitionPolicyDefinitionReferenceArgs']]]:
        """
        One or more `policy_definition_reference` blocks as defined below.
        """
        return pulumi.get(self, "policy_definition_references")

    @policy_definition_references.setter
    def policy_definition_references(self, value: pulumi.Input[Sequence[pulumi.Input['PolicySetDefinitionPolicyDefinitionReferenceArgs']]]):
        pulumi.set(self, "policy_definition_references", value)

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Input[str]:
        """
        The policy set type. Possible values are `BuiltIn` or `Custom`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "policy_type")

    @policy_type.setter
    def policy_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the policy set definition.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="managementGroupId")
    def management_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Management Group where this policy set definition should be defined. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "management_group_id")

    @management_group_id.setter
    def management_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "management_group_id", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[str]]:
        """
        The metadata for the policy set definition. This is a JSON object representing additional metadata that should be stored with the policy definition.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy set definition. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[str]]:
        """
        Parameters for the policy set definition. This field is a JSON object that allows you to parameterize your policy definition.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="policyDefinitionGroups")
    def policy_definition_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PolicySetDefinitionPolicyDefinitionGroupArgs']]]]:
        """
        One or more `policy_definition_group` blocks as defined below.
        """
        return pulumi.get(self, "policy_definition_groups")

    @policy_definition_groups.setter
    def policy_definition_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PolicySetDefinitionPolicyDefinitionGroupArgs']]]]):
        pulumi.set(self, "policy_definition_groups", value)


@pulumi.input_type
class _PolicySetDefinitionState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 management_group_id: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[str]] = None,
                 policy_definition_groups: Optional[pulumi.Input[Sequence[pulumi.Input['PolicySetDefinitionPolicyDefinitionGroupArgs']]]] = None,
                 policy_definition_references: Optional[pulumi.Input[Sequence[pulumi.Input['PolicySetDefinitionPolicyDefinitionReferenceArgs']]]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering PolicySetDefinition resources.
        :param pulumi.Input[str] description: The description of the policy set definition.
        :param pulumi.Input[str] display_name: The display name of the policy set definition.
        :param pulumi.Input[str] management_group_id: The name of the Management Group where this policy set definition should be defined. Changing this forces a new resource to be created.
        :param pulumi.Input[str] metadata: The metadata for the policy set definition. This is a JSON object representing additional metadata that should be stored with the policy definition.
        :param pulumi.Input[str] name: The name of the policy set definition. Changing this forces a new resource to be created.
        :param pulumi.Input[str] parameters: Parameters for the policy set definition. This field is a JSON object that allows you to parameterize your policy definition.
        :param pulumi.Input[Sequence[pulumi.Input['PolicySetDefinitionPolicyDefinitionGroupArgs']]] policy_definition_groups: One or more `policy_definition_group` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input['PolicySetDefinitionPolicyDefinitionReferenceArgs']]] policy_definition_references: One or more `policy_definition_reference` blocks as defined below.
        :param pulumi.Input[str] policy_type: The policy set type. Possible values are `BuiltIn` or `Custom`. Changing this forces a new resource to be created.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if management_group_id is not None:
            pulumi.set(__self__, "management_group_id", management_group_id)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if policy_definition_groups is not None:
            pulumi.set(__self__, "policy_definition_groups", policy_definition_groups)
        if policy_definition_references is not None:
            pulumi.set(__self__, "policy_definition_references", policy_definition_references)
        if policy_type is not None:
            pulumi.set(__self__, "policy_type", policy_type)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the policy set definition.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the policy set definition.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="managementGroupId")
    def management_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Management Group where this policy set definition should be defined. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "management_group_id")

    @management_group_id.setter
    def management_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "management_group_id", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[str]]:
        """
        The metadata for the policy set definition. This is a JSON object representing additional metadata that should be stored with the policy definition.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy set definition. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[str]]:
        """
        Parameters for the policy set definition. This field is a JSON object that allows you to parameterize your policy definition.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="policyDefinitionGroups")
    def policy_definition_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PolicySetDefinitionPolicyDefinitionGroupArgs']]]]:
        """
        One or more `policy_definition_group` blocks as defined below.
        """
        return pulumi.get(self, "policy_definition_groups")

    @policy_definition_groups.setter
    def policy_definition_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PolicySetDefinitionPolicyDefinitionGroupArgs']]]]):
        pulumi.set(self, "policy_definition_groups", value)

    @property
    @pulumi.getter(name="policyDefinitionReferences")
    def policy_definition_references(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PolicySetDefinitionPolicyDefinitionReferenceArgs']]]]:
        """
        One or more `policy_definition_reference` blocks as defined below.
        """
        return pulumi.get(self, "policy_definition_references")

    @policy_definition_references.setter
    def policy_definition_references(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PolicySetDefinitionPolicyDefinitionReferenceArgs']]]]):
        pulumi.set(self, "policy_definition_references", value)

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[str]]:
        """
        The policy set type. Possible values are `BuiltIn` or `Custom`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "policy_type")

    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_type", value)


class PolicySetDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 management_group_id: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[str]] = None,
                 policy_definition_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicySetDefinitionPolicyDefinitionGroupArgs']]]]] = None,
                 policy_definition_references: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicySetDefinitionPolicyDefinitionReferenceArgs']]]]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a policy set definition.

        > **NOTE:**  Policy set definitions (also known as policy initiatives) do not take effect until they are assigned to a scope using a Policy Set Assignment.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.policy.PolicySetDefinition("example",
            display_name="Test Policy Set",
            parameters=\"\"\"    {
                "allowedLocations": {
                    "type": "Array",
                    "metadata": {
                        "description": "The list of allowed locations for resources.",
                        "displayName": "Allowed locations",
                        "strongType": "location"
                    }
                }
            }

        \"\"\",
            policy_definition_references=[azure.policy.PolicySetDefinitionPolicyDefinitionReferenceArgs(
                parameter_values=\"\"\"    {
              "listOfAllowedLocations": {"value": "[parameters('allowedLocations')]"}
            }
            
        \"\"\",
                policy_definition_id="/providers/Microsoft.Authorization/policyDefinitions/e765b5de-1225-4ba3-bd56-1ac6695af988",
            )],
            policy_type="Custom")
        ```

        ## Import

        Policy Set Definitions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:policy/policySetDefinition:PolicySetDefinition example /subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Authorization/policySetDefinitions/testPolicySet
        ```

         or

        ```sh
         $ pulumi import azure:policy/policySetDefinition:PolicySetDefinition example /providers/Microsoft.Management/managementGroups/my-mgmt-group-id/providers/Microsoft.Authorization/policySetDefinitions/testPolicySet
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the policy set definition.
        :param pulumi.Input[str] display_name: The display name of the policy set definition.
        :param pulumi.Input[str] management_group_id: The name of the Management Group where this policy set definition should be defined. Changing this forces a new resource to be created.
        :param pulumi.Input[str] metadata: The metadata for the policy set definition. This is a JSON object representing additional metadata that should be stored with the policy definition.
        :param pulumi.Input[str] name: The name of the policy set definition. Changing this forces a new resource to be created.
        :param pulumi.Input[str] parameters: Parameters for the policy set definition. This field is a JSON object that allows you to parameterize your policy definition.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicySetDefinitionPolicyDefinitionGroupArgs']]]] policy_definition_groups: One or more `policy_definition_group` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicySetDefinitionPolicyDefinitionReferenceArgs']]]] policy_definition_references: One or more `policy_definition_reference` blocks as defined below.
        :param pulumi.Input[str] policy_type: The policy set type. Possible values are `BuiltIn` or `Custom`. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PolicySetDefinitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a policy set definition.

        > **NOTE:**  Policy set definitions (also known as policy initiatives) do not take effect until they are assigned to a scope using a Policy Set Assignment.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.policy.PolicySetDefinition("example",
            display_name="Test Policy Set",
            parameters=\"\"\"    {
                "allowedLocations": {
                    "type": "Array",
                    "metadata": {
                        "description": "The list of allowed locations for resources.",
                        "displayName": "Allowed locations",
                        "strongType": "location"
                    }
                }
            }

        \"\"\",
            policy_definition_references=[azure.policy.PolicySetDefinitionPolicyDefinitionReferenceArgs(
                parameter_values=\"\"\"    {
              "listOfAllowedLocations": {"value": "[parameters('allowedLocations')]"}
            }
            
        \"\"\",
                policy_definition_id="/providers/Microsoft.Authorization/policyDefinitions/e765b5de-1225-4ba3-bd56-1ac6695af988",
            )],
            policy_type="Custom")
        ```

        ## Import

        Policy Set Definitions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:policy/policySetDefinition:PolicySetDefinition example /subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Authorization/policySetDefinitions/testPolicySet
        ```

         or

        ```sh
         $ pulumi import azure:policy/policySetDefinition:PolicySetDefinition example /providers/Microsoft.Management/managementGroups/my-mgmt-group-id/providers/Microsoft.Authorization/policySetDefinitions/testPolicySet
        ```

        :param str resource_name: The name of the resource.
        :param PolicySetDefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PolicySetDefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 management_group_id: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[str]] = None,
                 policy_definition_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicySetDefinitionPolicyDefinitionGroupArgs']]]]] = None,
                 policy_definition_references: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicySetDefinitionPolicyDefinitionReferenceArgs']]]]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PolicySetDefinitionArgs.__new__(PolicySetDefinitionArgs)

            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["management_group_id"] = management_group_id
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["name"] = name
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["policy_definition_groups"] = policy_definition_groups
            if policy_definition_references is None and not opts.urn:
                raise TypeError("Missing required property 'policy_definition_references'")
            __props__.__dict__["policy_definition_references"] = policy_definition_references
            if policy_type is None and not opts.urn:
                raise TypeError("Missing required property 'policy_type'")
            __props__.__dict__["policy_type"] = policy_type
        super(PolicySetDefinition, __self__).__init__(
            'azure:policy/policySetDefinition:PolicySetDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            management_group_id: Optional[pulumi.Input[str]] = None,
            metadata: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parameters: Optional[pulumi.Input[str]] = None,
            policy_definition_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicySetDefinitionPolicyDefinitionGroupArgs']]]]] = None,
            policy_definition_references: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicySetDefinitionPolicyDefinitionReferenceArgs']]]]] = None,
            policy_type: Optional[pulumi.Input[str]] = None) -> 'PolicySetDefinition':
        """
        Get an existing PolicySetDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the policy set definition.
        :param pulumi.Input[str] display_name: The display name of the policy set definition.
        :param pulumi.Input[str] management_group_id: The name of the Management Group where this policy set definition should be defined. Changing this forces a new resource to be created.
        :param pulumi.Input[str] metadata: The metadata for the policy set definition. This is a JSON object representing additional metadata that should be stored with the policy definition.
        :param pulumi.Input[str] name: The name of the policy set definition. Changing this forces a new resource to be created.
        :param pulumi.Input[str] parameters: Parameters for the policy set definition. This field is a JSON object that allows you to parameterize your policy definition.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicySetDefinitionPolicyDefinitionGroupArgs']]]] policy_definition_groups: One or more `policy_definition_group` blocks as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicySetDefinitionPolicyDefinitionReferenceArgs']]]] policy_definition_references: One or more `policy_definition_reference` blocks as defined below.
        :param pulumi.Input[str] policy_type: The policy set type. Possible values are `BuiltIn` or `Custom`. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PolicySetDefinitionState.__new__(_PolicySetDefinitionState)

        __props__.__dict__["description"] = description
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["management_group_id"] = management_group_id
        __props__.__dict__["metadata"] = metadata
        __props__.__dict__["name"] = name
        __props__.__dict__["parameters"] = parameters
        __props__.__dict__["policy_definition_groups"] = policy_definition_groups
        __props__.__dict__["policy_definition_references"] = policy_definition_references
        __props__.__dict__["policy_type"] = policy_type
        return PolicySetDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the policy set definition.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The display name of the policy set definition.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="managementGroupId")
    def management_group_id(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the Management Group where this policy set definition should be defined. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "management_group_id")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[str]:
        """
        The metadata for the policy set definition. This is a JSON object representing additional metadata that should be stored with the policy definition.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the policy set definition. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[str]]:
        """
        Parameters for the policy set definition. This field is a JSON object that allows you to parameterize your policy definition.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="policyDefinitionGroups")
    def policy_definition_groups(self) -> pulumi.Output[Optional[Sequence['outputs.PolicySetDefinitionPolicyDefinitionGroup']]]:
        """
        One or more `policy_definition_group` blocks as defined below.
        """
        return pulumi.get(self, "policy_definition_groups")

    @property
    @pulumi.getter(name="policyDefinitionReferences")
    def policy_definition_references(self) -> pulumi.Output[Sequence['outputs.PolicySetDefinitionPolicyDefinitionReference']]:
        """
        One or more `policy_definition_reference` blocks as defined below.
        """
        return pulumi.get(self, "policy_definition_references")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Output[str]:
        """
        The policy set type. Possible values are `BuiltIn` or `Custom`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "policy_type")

