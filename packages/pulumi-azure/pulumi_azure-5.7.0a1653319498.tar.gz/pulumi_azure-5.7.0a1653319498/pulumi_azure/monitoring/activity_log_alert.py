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

__all__ = ['ActivityLogAlertArgs', 'ActivityLogAlert']

@pulumi.input_type
class ActivityLogAlertArgs:
    def __init__(__self__, *,
                 criteria: pulumi.Input['ActivityLogAlertCriteriaArgs'],
                 resource_group_name: pulumi.Input[str],
                 scopes: pulumi.Input[Sequence[pulumi.Input[str]]],
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input['ActivityLogAlertActionArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ActivityLogAlert resource.
        :param pulumi.Input['ActivityLogAlertCriteriaArgs'] criteria: A `criteria` block as defined below.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the activity log alert instance.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: The Scope at which the Activity Log should be applied, for example a the Resource ID of a Subscription or a Resource (such as a Storage Account).
        :param pulumi.Input[Sequence[pulumi.Input['ActivityLogAlertActionArgs']]] actions: One or more `action` blocks as defined below.
        :param pulumi.Input[str] description: The description of this activity log alert.
        :param pulumi.Input[bool] enabled: Should this Activity Log Alert be enabled? Defaults to `true`.
        :param pulumi.Input[str] name: The name of the activity log alert. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        pulumi.set(__self__, "criteria", criteria)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "scopes", scopes)
        if actions is not None:
            pulumi.set(__self__, "actions", actions)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def criteria(self) -> pulumi.Input['ActivityLogAlertCriteriaArgs']:
        """
        A `criteria` block as defined below.
        """
        return pulumi.get(self, "criteria")

    @criteria.setter
    def criteria(self, value: pulumi.Input['ActivityLogAlertCriteriaArgs']):
        pulumi.set(self, "criteria", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group in which to create the activity log alert instance.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The Scope at which the Activity Log should be applied, for example a the Resource ID of a Subscription or a Resource (such as a Storage Account).
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter
    def actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ActivityLogAlertActionArgs']]]]:
        """
        One or more `action` blocks as defined below.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ActivityLogAlertActionArgs']]]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of this activity log alert.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Should this Activity Log Alert be enabled? Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the activity log alert. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _ActivityLogAlertState:
    def __init__(__self__, *,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input['ActivityLogAlertActionArgs']]]] = None,
                 criteria: Optional[pulumi.Input['ActivityLogAlertCriteriaArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering ActivityLogAlert resources.
        :param pulumi.Input[Sequence[pulumi.Input['ActivityLogAlertActionArgs']]] actions: One or more `action` blocks as defined below.
        :param pulumi.Input['ActivityLogAlertCriteriaArgs'] criteria: A `criteria` block as defined below.
        :param pulumi.Input[str] description: The description of this activity log alert.
        :param pulumi.Input[bool] enabled: Should this Activity Log Alert be enabled? Defaults to `true`.
        :param pulumi.Input[str] name: The name of the activity log alert. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the activity log alert instance.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: The Scope at which the Activity Log should be applied, for example a the Resource ID of a Subscription or a Resource (such as a Storage Account).
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        if actions is not None:
            pulumi.set(__self__, "actions", actions)
        if criteria is not None:
            pulumi.set(__self__, "criteria", criteria)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if scopes is not None:
            pulumi.set(__self__, "scopes", scopes)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ActivityLogAlertActionArgs']]]]:
        """
        One or more `action` blocks as defined below.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ActivityLogAlertActionArgs']]]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def criteria(self) -> Optional[pulumi.Input['ActivityLogAlertCriteriaArgs']]:
        """
        A `criteria` block as defined below.
        """
        return pulumi.get(self, "criteria")

    @criteria.setter
    def criteria(self, value: Optional[pulumi.Input['ActivityLogAlertCriteriaArgs']]):
        pulumi.set(self, "criteria", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of this activity log alert.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Should this Activity Log Alert be enabled? Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the activity log alert. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource group in which to create the activity log alert instance.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The Scope at which the Activity Log should be applied, for example a the Resource ID of a Subscription or a Resource (such as a Storage Account).
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class ActivityLogAlert(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ActivityLogAlertActionArgs']]]]] = None,
                 criteria: Optional[pulumi.Input[pulumi.InputType['ActivityLogAlertCriteriaArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages an Activity Log Alert within Azure Monitor.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example", location="West Europe")
        main_action_group = azure.monitoring.ActionGroup("mainActionGroup",
            resource_group_name=example.name,
            short_name="p0action",
            webhook_receivers=[azure.monitoring.ActionGroupWebhookReceiverArgs(
                name="callmyapi",
                service_uri="http://example.com/alert",
            )])
        to_monitor = azure.storage.Account("toMonitor",
            resource_group_name=example.name,
            location=example.location,
            account_tier="Standard",
            account_replication_type="GRS")
        main_activity_log_alert = azure.monitoring.ActivityLogAlert("mainActivityLogAlert",
            resource_group_name=example.name,
            scopes=[example.id],
            description="This alert will monitor a specific storage account updates.",
            criteria=azure.monitoring.ActivityLogAlertCriteriaArgs(
                resource_id=to_monitor.id,
                operation_name="Microsoft.Storage/storageAccounts/write",
                category="Recommendation",
            ),
            actions=[azure.monitoring.ActivityLogAlertActionArgs(
                action_group_id=main_action_group.id,
                webhook_properties={
                    "from": "source",
                },
            )])
        ```

        ## Import

        Activity log alerts can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:monitoring/activityLogAlert:ActivityLogAlert example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Insights/activityLogAlerts/myalertname
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ActivityLogAlertActionArgs']]]] actions: One or more `action` blocks as defined below.
        :param pulumi.Input[pulumi.InputType['ActivityLogAlertCriteriaArgs']] criteria: A `criteria` block as defined below.
        :param pulumi.Input[str] description: The description of this activity log alert.
        :param pulumi.Input[bool] enabled: Should this Activity Log Alert be enabled? Defaults to `true`.
        :param pulumi.Input[str] name: The name of the activity log alert. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the activity log alert instance.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: The Scope at which the Activity Log should be applied, for example a the Resource ID of a Subscription or a Resource (such as a Storage Account).
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ActivityLogAlertArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an Activity Log Alert within Azure Monitor.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example", location="West Europe")
        main_action_group = azure.monitoring.ActionGroup("mainActionGroup",
            resource_group_name=example.name,
            short_name="p0action",
            webhook_receivers=[azure.monitoring.ActionGroupWebhookReceiverArgs(
                name="callmyapi",
                service_uri="http://example.com/alert",
            )])
        to_monitor = azure.storage.Account("toMonitor",
            resource_group_name=example.name,
            location=example.location,
            account_tier="Standard",
            account_replication_type="GRS")
        main_activity_log_alert = azure.monitoring.ActivityLogAlert("mainActivityLogAlert",
            resource_group_name=example.name,
            scopes=[example.id],
            description="This alert will monitor a specific storage account updates.",
            criteria=azure.monitoring.ActivityLogAlertCriteriaArgs(
                resource_id=to_monitor.id,
                operation_name="Microsoft.Storage/storageAccounts/write",
                category="Recommendation",
            ),
            actions=[azure.monitoring.ActivityLogAlertActionArgs(
                action_group_id=main_action_group.id,
                webhook_properties={
                    "from": "source",
                },
            )])
        ```

        ## Import

        Activity log alerts can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:monitoring/activityLogAlert:ActivityLogAlert example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Insights/activityLogAlerts/myalertname
        ```

        :param str resource_name: The name of the resource.
        :param ActivityLogAlertArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ActivityLogAlertArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ActivityLogAlertActionArgs']]]]] = None,
                 criteria: Optional[pulumi.Input[pulumi.InputType['ActivityLogAlertCriteriaArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = ActivityLogAlertArgs.__new__(ActivityLogAlertArgs)

            __props__.__dict__["actions"] = actions
            if criteria is None and not opts.urn:
                raise TypeError("Missing required property 'criteria'")
            __props__.__dict__["criteria"] = criteria
            __props__.__dict__["description"] = description
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if scopes is None and not opts.urn:
                raise TypeError("Missing required property 'scopes'")
            __props__.__dict__["scopes"] = scopes
            __props__.__dict__["tags"] = tags
        super(ActivityLogAlert, __self__).__init__(
            'azure:monitoring/activityLogAlert:ActivityLogAlert',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ActivityLogAlertActionArgs']]]]] = None,
            criteria: Optional[pulumi.Input[pulumi.InputType['ActivityLogAlertCriteriaArgs']]] = None,
            description: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'ActivityLogAlert':
        """
        Get an existing ActivityLogAlert resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ActivityLogAlertActionArgs']]]] actions: One or more `action` blocks as defined below.
        :param pulumi.Input[pulumi.InputType['ActivityLogAlertCriteriaArgs']] criteria: A `criteria` block as defined below.
        :param pulumi.Input[str] description: The description of this activity log alert.
        :param pulumi.Input[bool] enabled: Should this Activity Log Alert be enabled? Defaults to `true`.
        :param pulumi.Input[str] name: The name of the activity log alert. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the activity log alert instance.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: The Scope at which the Activity Log should be applied, for example a the Resource ID of a Subscription or a Resource (such as a Storage Account).
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ActivityLogAlertState.__new__(_ActivityLogAlertState)

        __props__.__dict__["actions"] = actions
        __props__.__dict__["criteria"] = criteria
        __props__.__dict__["description"] = description
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["scopes"] = scopes
        __props__.__dict__["tags"] = tags
        return ActivityLogAlert(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Optional[Sequence['outputs.ActivityLogAlertAction']]]:
        """
        One or more `action` blocks as defined below.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def criteria(self) -> pulumi.Output['outputs.ActivityLogAlertCriteria']:
        """
        A `criteria` block as defined below.
        """
        return pulumi.get(self, "criteria")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of this activity log alert.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Should this Activity Log Alert be enabled? Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the activity log alert. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the activity log alert instance.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Sequence[str]]:
        """
        The Scope at which the Activity Log should be applied, for example a the Resource ID of a Subscription or a Resource (such as a Storage Account).
        """
        return pulumi.get(self, "scopes")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

