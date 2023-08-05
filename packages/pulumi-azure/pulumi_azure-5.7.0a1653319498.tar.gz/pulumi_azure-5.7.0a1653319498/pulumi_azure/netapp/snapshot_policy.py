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

__all__ = ['SnapshotPolicyArgs', 'SnapshotPolicy']

@pulumi.input_type
class SnapshotPolicyArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 enabled: pulumi.Input[bool],
                 resource_group_name: pulumi.Input[str],
                 daily_schedule: Optional[pulumi.Input['SnapshotPolicyDailyScheduleArgs']] = None,
                 hourly_schedule: Optional[pulumi.Input['SnapshotPolicyHourlyScheduleArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 monthly_schedule: Optional[pulumi.Input['SnapshotPolicyMonthlyScheduleArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 weekly_schedule: Optional[pulumi.Input['SnapshotPolicyWeeklyScheduleArgs']] = None):
        """
        The set of arguments for constructing a SnapshotPolicy resource.
        :param pulumi.Input[str] account_name: The name of the NetApp Account in which the NetApp Snapshot Policy should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] enabled: Defines that the NetApp Snapshot Policy is enabled or not.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the NetApp Snapshot Policy should be created. Changing this forces a new resource to be created.
        :param pulumi.Input['SnapshotPolicyDailyScheduleArgs'] daily_schedule: Sets a daily snapshot schedule. See details in below `daily_schedule` block.
        :param pulumi.Input['SnapshotPolicyHourlyScheduleArgs'] hourly_schedule: Sets an hourly snapshot schedule. See details in below `hourly_schedule` block.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input['SnapshotPolicyMonthlyScheduleArgs'] monthly_schedule: Sets a monthly snapshot schedule. See details in below `monthly_schedule` block.
        :param pulumi.Input[str] name: The name of the NetApp Snapshot Policy. Changing this forces a new resource to be created.
        :param pulumi.Input['SnapshotPolicyWeeklyScheduleArgs'] weekly_schedule: Sets a weekly snapshot schedule. See details in below `weekly_schedule` block.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if daily_schedule is not None:
            pulumi.set(__self__, "daily_schedule", daily_schedule)
        if hourly_schedule is not None:
            pulumi.set(__self__, "hourly_schedule", hourly_schedule)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if monthly_schedule is not None:
            pulumi.set(__self__, "monthly_schedule", monthly_schedule)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if weekly_schedule is not None:
            pulumi.set(__self__, "weekly_schedule", weekly_schedule)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the NetApp Account in which the NetApp Snapshot Policy should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Defines that the NetApp Snapshot Policy is enabled or not.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group where the NetApp Snapshot Policy should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="dailySchedule")
    def daily_schedule(self) -> Optional[pulumi.Input['SnapshotPolicyDailyScheduleArgs']]:
        """
        Sets a daily snapshot schedule. See details in below `daily_schedule` block.
        """
        return pulumi.get(self, "daily_schedule")

    @daily_schedule.setter
    def daily_schedule(self, value: Optional[pulumi.Input['SnapshotPolicyDailyScheduleArgs']]):
        pulumi.set(self, "daily_schedule", value)

    @property
    @pulumi.getter(name="hourlySchedule")
    def hourly_schedule(self) -> Optional[pulumi.Input['SnapshotPolicyHourlyScheduleArgs']]:
        """
        Sets an hourly snapshot schedule. See details in below `hourly_schedule` block.
        """
        return pulumi.get(self, "hourly_schedule")

    @hourly_schedule.setter
    def hourly_schedule(self, value: Optional[pulumi.Input['SnapshotPolicyHourlyScheduleArgs']]):
        pulumi.set(self, "hourly_schedule", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="monthlySchedule")
    def monthly_schedule(self) -> Optional[pulumi.Input['SnapshotPolicyMonthlyScheduleArgs']]:
        """
        Sets a monthly snapshot schedule. See details in below `monthly_schedule` block.
        """
        return pulumi.get(self, "monthly_schedule")

    @monthly_schedule.setter
    def monthly_schedule(self, value: Optional[pulumi.Input['SnapshotPolicyMonthlyScheduleArgs']]):
        pulumi.set(self, "monthly_schedule", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the NetApp Snapshot Policy. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="weeklySchedule")
    def weekly_schedule(self) -> Optional[pulumi.Input['SnapshotPolicyWeeklyScheduleArgs']]:
        """
        Sets a weekly snapshot schedule. See details in below `weekly_schedule` block.
        """
        return pulumi.get(self, "weekly_schedule")

    @weekly_schedule.setter
    def weekly_schedule(self, value: Optional[pulumi.Input['SnapshotPolicyWeeklyScheduleArgs']]):
        pulumi.set(self, "weekly_schedule", value)


@pulumi.input_type
class _SnapshotPolicyState:
    def __init__(__self__, *,
                 account_name: Optional[pulumi.Input[str]] = None,
                 daily_schedule: Optional[pulumi.Input['SnapshotPolicyDailyScheduleArgs']] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 hourly_schedule: Optional[pulumi.Input['SnapshotPolicyHourlyScheduleArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 monthly_schedule: Optional[pulumi.Input['SnapshotPolicyMonthlyScheduleArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 weekly_schedule: Optional[pulumi.Input['SnapshotPolicyWeeklyScheduleArgs']] = None):
        """
        Input properties used for looking up and filtering SnapshotPolicy resources.
        :param pulumi.Input[str] account_name: The name of the NetApp Account in which the NetApp Snapshot Policy should be created. Changing this forces a new resource to be created.
        :param pulumi.Input['SnapshotPolicyDailyScheduleArgs'] daily_schedule: Sets a daily snapshot schedule. See details in below `daily_schedule` block.
        :param pulumi.Input[bool] enabled: Defines that the NetApp Snapshot Policy is enabled or not.
        :param pulumi.Input['SnapshotPolicyHourlyScheduleArgs'] hourly_schedule: Sets an hourly snapshot schedule. See details in below `hourly_schedule` block.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input['SnapshotPolicyMonthlyScheduleArgs'] monthly_schedule: Sets a monthly snapshot schedule. See details in below `monthly_schedule` block.
        :param pulumi.Input[str] name: The name of the NetApp Snapshot Policy. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the NetApp Snapshot Policy should be created. Changing this forces a new resource to be created.
        :param pulumi.Input['SnapshotPolicyWeeklyScheduleArgs'] weekly_schedule: Sets a weekly snapshot schedule. See details in below `weekly_schedule` block.
        """
        if account_name is not None:
            pulumi.set(__self__, "account_name", account_name)
        if daily_schedule is not None:
            pulumi.set(__self__, "daily_schedule", daily_schedule)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if hourly_schedule is not None:
            pulumi.set(__self__, "hourly_schedule", hourly_schedule)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if monthly_schedule is not None:
            pulumi.set(__self__, "monthly_schedule", monthly_schedule)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if weekly_schedule is not None:
            pulumi.set(__self__, "weekly_schedule", weekly_schedule)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the NetApp Account in which the NetApp Snapshot Policy should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="dailySchedule")
    def daily_schedule(self) -> Optional[pulumi.Input['SnapshotPolicyDailyScheduleArgs']]:
        """
        Sets a daily snapshot schedule. See details in below `daily_schedule` block.
        """
        return pulumi.get(self, "daily_schedule")

    @daily_schedule.setter
    def daily_schedule(self, value: Optional[pulumi.Input['SnapshotPolicyDailyScheduleArgs']]):
        pulumi.set(self, "daily_schedule", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Defines that the NetApp Snapshot Policy is enabled or not.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="hourlySchedule")
    def hourly_schedule(self) -> Optional[pulumi.Input['SnapshotPolicyHourlyScheduleArgs']]:
        """
        Sets an hourly snapshot schedule. See details in below `hourly_schedule` block.
        """
        return pulumi.get(self, "hourly_schedule")

    @hourly_schedule.setter
    def hourly_schedule(self, value: Optional[pulumi.Input['SnapshotPolicyHourlyScheduleArgs']]):
        pulumi.set(self, "hourly_schedule", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="monthlySchedule")
    def monthly_schedule(self) -> Optional[pulumi.Input['SnapshotPolicyMonthlyScheduleArgs']]:
        """
        Sets a monthly snapshot schedule. See details in below `monthly_schedule` block.
        """
        return pulumi.get(self, "monthly_schedule")

    @monthly_schedule.setter
    def monthly_schedule(self, value: Optional[pulumi.Input['SnapshotPolicyMonthlyScheduleArgs']]):
        pulumi.set(self, "monthly_schedule", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the NetApp Snapshot Policy. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource group where the NetApp Snapshot Policy should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="weeklySchedule")
    def weekly_schedule(self) -> Optional[pulumi.Input['SnapshotPolicyWeeklyScheduleArgs']]:
        """
        Sets a weekly snapshot schedule. See details in below `weekly_schedule` block.
        """
        return pulumi.get(self, "weekly_schedule")

    @weekly_schedule.setter
    def weekly_schedule(self, value: Optional[pulumi.Input['SnapshotPolicyWeeklyScheduleArgs']]):
        pulumi.set(self, "weekly_schedule", value)


class SnapshotPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 daily_schedule: Optional[pulumi.Input[pulumi.InputType['SnapshotPolicyDailyScheduleArgs']]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 hourly_schedule: Optional[pulumi.Input[pulumi.InputType['SnapshotPolicyHourlyScheduleArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 monthly_schedule: Optional[pulumi.Input[pulumi.InputType['SnapshotPolicyMonthlyScheduleArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 weekly_schedule: Optional[pulumi.Input[pulumi.InputType['SnapshotPolicyWeeklyScheduleArgs']]] = None,
                 __props__=None):
        """
        Manages a NetApp Snapshot Policy.

        ## NetApp Snapshot Policy Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="East US")
        example_account = azure.netapp.Account("exampleAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_snapshot_policy = azure.netapp.SnapshotPolicy("exampleSnapshotPolicy",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            account_name=example_account.name,
            enabled=True,
            hourly_schedule=azure.netapp.SnapshotPolicyHourlyScheduleArgs(
                snapshots_to_keep=4,
                minute=15,
            ),
            daily_schedule=azure.netapp.SnapshotPolicyDailyScheduleArgs(
                snapshots_to_keep=2,
                hour=20,
                minute=15,
            ),
            weekly_schedule=azure.netapp.SnapshotPolicyWeeklyScheduleArgs(
                snapshots_to_keep=1,
                days_of_weeks=[
                    "Monday",
                    "Friday",
                ],
                hour=23,
                minute=0,
            ),
            monthly_schedule=azure.netapp.SnapshotPolicyMonthlyScheduleArgs(
                snapshots_to_keep=1,
                days_of_months=[
                    1,
                    15,
                    20,
                    30,
                ],
                hour=5,
                minute=45,
            ))
        ```

        ## Import

        NetApp Snapshot Policy can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:netapp/snapshotPolicy:SnapshotPolicy example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.NetApp/netAppAccounts/account1/snapshotPolicies/snapshotpolicy1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the NetApp Account in which the NetApp Snapshot Policy should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['SnapshotPolicyDailyScheduleArgs']] daily_schedule: Sets a daily snapshot schedule. See details in below `daily_schedule` block.
        :param pulumi.Input[bool] enabled: Defines that the NetApp Snapshot Policy is enabled or not.
        :param pulumi.Input[pulumi.InputType['SnapshotPolicyHourlyScheduleArgs']] hourly_schedule: Sets an hourly snapshot schedule. See details in below `hourly_schedule` block.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['SnapshotPolicyMonthlyScheduleArgs']] monthly_schedule: Sets a monthly snapshot schedule. See details in below `monthly_schedule` block.
        :param pulumi.Input[str] name: The name of the NetApp Snapshot Policy. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the NetApp Snapshot Policy should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['SnapshotPolicyWeeklyScheduleArgs']] weekly_schedule: Sets a weekly snapshot schedule. See details in below `weekly_schedule` block.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SnapshotPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a NetApp Snapshot Policy.

        ## NetApp Snapshot Policy Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="East US")
        example_account = azure.netapp.Account("exampleAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_snapshot_policy = azure.netapp.SnapshotPolicy("exampleSnapshotPolicy",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            account_name=example_account.name,
            enabled=True,
            hourly_schedule=azure.netapp.SnapshotPolicyHourlyScheduleArgs(
                snapshots_to_keep=4,
                minute=15,
            ),
            daily_schedule=azure.netapp.SnapshotPolicyDailyScheduleArgs(
                snapshots_to_keep=2,
                hour=20,
                minute=15,
            ),
            weekly_schedule=azure.netapp.SnapshotPolicyWeeklyScheduleArgs(
                snapshots_to_keep=1,
                days_of_weeks=[
                    "Monday",
                    "Friday",
                ],
                hour=23,
                minute=0,
            ),
            monthly_schedule=azure.netapp.SnapshotPolicyMonthlyScheduleArgs(
                snapshots_to_keep=1,
                days_of_months=[
                    1,
                    15,
                    20,
                    30,
                ],
                hour=5,
                minute=45,
            ))
        ```

        ## Import

        NetApp Snapshot Policy can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:netapp/snapshotPolicy:SnapshotPolicy example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.NetApp/netAppAccounts/account1/snapshotPolicies/snapshotpolicy1
        ```

        :param str resource_name: The name of the resource.
        :param SnapshotPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SnapshotPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 daily_schedule: Optional[pulumi.Input[pulumi.InputType['SnapshotPolicyDailyScheduleArgs']]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 hourly_schedule: Optional[pulumi.Input[pulumi.InputType['SnapshotPolicyHourlyScheduleArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 monthly_schedule: Optional[pulumi.Input[pulumi.InputType['SnapshotPolicyMonthlyScheduleArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 weekly_schedule: Optional[pulumi.Input[pulumi.InputType['SnapshotPolicyWeeklyScheduleArgs']]] = None,
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
            __props__ = SnapshotPolicyArgs.__new__(SnapshotPolicyArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["daily_schedule"] = daily_schedule
            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["hourly_schedule"] = hourly_schedule
            __props__.__dict__["location"] = location
            __props__.__dict__["monthly_schedule"] = monthly_schedule
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["weekly_schedule"] = weekly_schedule
        super(SnapshotPolicy, __self__).__init__(
            'azure:netapp/snapshotPolicy:SnapshotPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_name: Optional[pulumi.Input[str]] = None,
            daily_schedule: Optional[pulumi.Input[pulumi.InputType['SnapshotPolicyDailyScheduleArgs']]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            hourly_schedule: Optional[pulumi.Input[pulumi.InputType['SnapshotPolicyHourlyScheduleArgs']]] = None,
            location: Optional[pulumi.Input[str]] = None,
            monthly_schedule: Optional[pulumi.Input[pulumi.InputType['SnapshotPolicyMonthlyScheduleArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            weekly_schedule: Optional[pulumi.Input[pulumi.InputType['SnapshotPolicyWeeklyScheduleArgs']]] = None) -> 'SnapshotPolicy':
        """
        Get an existing SnapshotPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the NetApp Account in which the NetApp Snapshot Policy should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['SnapshotPolicyDailyScheduleArgs']] daily_schedule: Sets a daily snapshot schedule. See details in below `daily_schedule` block.
        :param pulumi.Input[bool] enabled: Defines that the NetApp Snapshot Policy is enabled or not.
        :param pulumi.Input[pulumi.InputType['SnapshotPolicyHourlyScheduleArgs']] hourly_schedule: Sets an hourly snapshot schedule. See details in below `hourly_schedule` block.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['SnapshotPolicyMonthlyScheduleArgs']] monthly_schedule: Sets a monthly snapshot schedule. See details in below `monthly_schedule` block.
        :param pulumi.Input[str] name: The name of the NetApp Snapshot Policy. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the NetApp Snapshot Policy should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['SnapshotPolicyWeeklyScheduleArgs']] weekly_schedule: Sets a weekly snapshot schedule. See details in below `weekly_schedule` block.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SnapshotPolicyState.__new__(_SnapshotPolicyState)

        __props__.__dict__["account_name"] = account_name
        __props__.__dict__["daily_schedule"] = daily_schedule
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["hourly_schedule"] = hourly_schedule
        __props__.__dict__["location"] = location
        __props__.__dict__["monthly_schedule"] = monthly_schedule
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["tags"] = tags
        __props__.__dict__["weekly_schedule"] = weekly_schedule
        return SnapshotPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Output[str]:
        """
        The name of the NetApp Account in which the NetApp Snapshot Policy should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter(name="dailySchedule")
    def daily_schedule(self) -> pulumi.Output['outputs.SnapshotPolicyDailySchedule']:
        """
        Sets a daily snapshot schedule. See details in below `daily_schedule` block.
        """
        return pulumi.get(self, "daily_schedule")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        Defines that the NetApp Snapshot Policy is enabled or not.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="hourlySchedule")
    def hourly_schedule(self) -> pulumi.Output['outputs.SnapshotPolicyHourlySchedule']:
        """
        Sets an hourly snapshot schedule. See details in below `hourly_schedule` block.
        """
        return pulumi.get(self, "hourly_schedule")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="monthlySchedule")
    def monthly_schedule(self) -> pulumi.Output['outputs.SnapshotPolicyMonthlySchedule']:
        """
        Sets a monthly snapshot schedule. See details in below `monthly_schedule` block.
        """
        return pulumi.get(self, "monthly_schedule")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the NetApp Snapshot Policy. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group where the NetApp Snapshot Policy should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="weeklySchedule")
    def weekly_schedule(self) -> pulumi.Output['outputs.SnapshotPolicyWeeklySchedule']:
        """
        Sets a weekly snapshot schedule. See details in below `weekly_schedule` block.
        """
        return pulumi.get(self, "weekly_schedule")

