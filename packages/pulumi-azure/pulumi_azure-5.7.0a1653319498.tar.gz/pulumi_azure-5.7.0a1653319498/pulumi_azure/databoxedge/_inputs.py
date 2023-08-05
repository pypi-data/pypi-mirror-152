# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'DeviceDevicePropertyArgs',
    'OrderContactArgs',
    'OrderReturnTrackingArgs',
    'OrderShipmentAddressArgs',
    'OrderShipmentHistoryArgs',
    'OrderShipmentTrackingArgs',
    'OrderStatusArgs',
]

@pulumi.input_type
class DeviceDevicePropertyArgs:
    def __init__(__self__, *,
                 capacity: Optional[pulumi.Input[int]] = None,
                 configured_role_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 culture: Optional[pulumi.Input[str]] = None,
                 hcs_version: Optional[pulumi.Input[str]] = None,
                 model: Optional[pulumi.Input[str]] = None,
                 node_count: Optional[pulumi.Input[int]] = None,
                 serial_number: Optional[pulumi.Input[str]] = None,
                 software_version: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[int] capacity: The Data Box Edge/Gateway device local capacity in MB.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] configured_role_types: Type of compute roles configured.
        :param pulumi.Input[str] culture: The Data Box Edge/Gateway device culture.
        :param pulumi.Input[str] hcs_version: The device software version number of the device (e.g. 1.2.18105.6).
        :param pulumi.Input[str] model: The Data Box Edge/Gateway device model.
        :param pulumi.Input[int] node_count: The number of nodes in the cluster.
        :param pulumi.Input[str] serial_number: The Serial Number of Data Box Edge/Gateway device.
        :param pulumi.Input[str] software_version: The Data Box Edge/Gateway device software version.
        :param pulumi.Input[str] status: The status of the Data Box Edge/Gateway device.
        :param pulumi.Input[str] time_zone: The Data Box Edge/Gateway device timezone.
        :param pulumi.Input[str] type: The type of the Data Box Edge/Gateway device.
        """
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)
        if configured_role_types is not None:
            pulumi.set(__self__, "configured_role_types", configured_role_types)
        if culture is not None:
            pulumi.set(__self__, "culture", culture)
        if hcs_version is not None:
            pulumi.set(__self__, "hcs_version", hcs_version)
        if model is not None:
            pulumi.set(__self__, "model", model)
        if node_count is not None:
            pulumi.set(__self__, "node_count", node_count)
        if serial_number is not None:
            pulumi.set(__self__, "serial_number", serial_number)
        if software_version is not None:
            pulumi.set(__self__, "software_version", software_version)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if time_zone is not None:
            pulumi.set(__self__, "time_zone", time_zone)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[int]]:
        """
        The Data Box Edge/Gateway device local capacity in MB.
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "capacity", value)

    @property
    @pulumi.getter(name="configuredRoleTypes")
    def configured_role_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Type of compute roles configured.
        """
        return pulumi.get(self, "configured_role_types")

    @configured_role_types.setter
    def configured_role_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "configured_role_types", value)

    @property
    @pulumi.getter
    def culture(self) -> Optional[pulumi.Input[str]]:
        """
        The Data Box Edge/Gateway device culture.
        """
        return pulumi.get(self, "culture")

    @culture.setter
    def culture(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "culture", value)

    @property
    @pulumi.getter(name="hcsVersion")
    def hcs_version(self) -> Optional[pulumi.Input[str]]:
        """
        The device software version number of the device (e.g. 1.2.18105.6).
        """
        return pulumi.get(self, "hcs_version")

    @hcs_version.setter
    def hcs_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hcs_version", value)

    @property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[str]]:
        """
        The Data Box Edge/Gateway device model.
        """
        return pulumi.get(self, "model")

    @model.setter
    def model(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model", value)

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of nodes in the cluster.
        """
        return pulumi.get(self, "node_count")

    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "node_count", value)

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[pulumi.Input[str]]:
        """
        The Serial Number of Data Box Edge/Gateway device.
        """
        return pulumi.get(self, "serial_number")

    @serial_number.setter
    def serial_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "serial_number", value)

    @property
    @pulumi.getter(name="softwareVersion")
    def software_version(self) -> Optional[pulumi.Input[str]]:
        """
        The Data Box Edge/Gateway device software version.
        """
        return pulumi.get(self, "software_version")

    @software_version.setter
    def software_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "software_version", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the Data Box Edge/Gateway device.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[str]]:
        """
        The Data Box Edge/Gateway device timezone.
        """
        return pulumi.get(self, "time_zone")

    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_zone", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the Data Box Edge/Gateway device.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class OrderContactArgs:
    def __init__(__self__, *,
                 company_name: pulumi.Input[str],
                 emails: pulumi.Input[Sequence[pulumi.Input[str]]],
                 name: pulumi.Input[str],
                 phone_number: pulumi.Input[str]):
        """
        :param pulumi.Input[str] company_name: The name of the company. Changing this forces a new Databox Edge Order to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] emails: A list of email address to send order notification to. Changing this forces a new Databox Edge Order to be created.
        :param pulumi.Input[str] name: The contact person name. Changing this forces a new Databox Edge Order to be created.
        :param pulumi.Input[str] phone_number: The phone number. Changing this forces a new Databox Edge Order to be created.
        """
        pulumi.set(__self__, "company_name", company_name)
        pulumi.set(__self__, "emails", emails)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "phone_number", phone_number)

    @property
    @pulumi.getter(name="companyName")
    def company_name(self) -> pulumi.Input[str]:
        """
        The name of the company. Changing this forces a new Databox Edge Order to be created.
        """
        return pulumi.get(self, "company_name")

    @company_name.setter
    def company_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "company_name", value)

    @property
    @pulumi.getter
    def emails(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of email address to send order notification to. Changing this forces a new Databox Edge Order to be created.
        """
        return pulumi.get(self, "emails")

    @emails.setter
    def emails(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "emails", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The contact person name. Changing this forces a new Databox Edge Order to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[str]:
        """
        The phone number. Changing this forces a new Databox Edge Order to be created.
        """
        return pulumi.get(self, "phone_number")

    @phone_number.setter
    def phone_number(self, value: pulumi.Input[str]):
        pulumi.set(self, "phone_number", value)


@pulumi.input_type
class OrderReturnTrackingArgs:
    def __init__(__self__, *,
                 carrier_name: Optional[pulumi.Input[str]] = None,
                 serial_number: Optional[pulumi.Input[str]] = None,
                 tracking_id: Optional[pulumi.Input[str]] = None,
                 tracking_url: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] carrier_name: Name of the carrier used in the delivery.
        :param pulumi.Input[str] serial_number: Serial number of the device being tracked.
        :param pulumi.Input[str] tracking_id: The ID of the tracking.
        :param pulumi.Input[str] tracking_url: Tracking URL of the shipment.
        """
        if carrier_name is not None:
            pulumi.set(__self__, "carrier_name", carrier_name)
        if serial_number is not None:
            pulumi.set(__self__, "serial_number", serial_number)
        if tracking_id is not None:
            pulumi.set(__self__, "tracking_id", tracking_id)
        if tracking_url is not None:
            pulumi.set(__self__, "tracking_url", tracking_url)

    @property
    @pulumi.getter(name="carrierName")
    def carrier_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the carrier used in the delivery.
        """
        return pulumi.get(self, "carrier_name")

    @carrier_name.setter
    def carrier_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "carrier_name", value)

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[pulumi.Input[str]]:
        """
        Serial number of the device being tracked.
        """
        return pulumi.get(self, "serial_number")

    @serial_number.setter
    def serial_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "serial_number", value)

    @property
    @pulumi.getter(name="trackingId")
    def tracking_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the tracking.
        """
        return pulumi.get(self, "tracking_id")

    @tracking_id.setter
    def tracking_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tracking_id", value)

    @property
    @pulumi.getter(name="trackingUrl")
    def tracking_url(self) -> Optional[pulumi.Input[str]]:
        """
        Tracking URL of the shipment.
        """
        return pulumi.get(self, "tracking_url")

    @tracking_url.setter
    def tracking_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tracking_url", value)


@pulumi.input_type
class OrderShipmentAddressArgs:
    def __init__(__self__, *,
                 addresses: pulumi.Input[Sequence[pulumi.Input[str]]],
                 city: pulumi.Input[str],
                 country: pulumi.Input[str],
                 postal_code: pulumi.Input[str],
                 state: pulumi.Input[str]):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] addresses: The list of upto 3 lines for address information. Changing this forces a new Databox Edge Order to be created.
        :param pulumi.Input[str] city: The city name. Changing this forces a new Databox Edge Order to be created.
        :param pulumi.Input[str] country: The name of the country to ship the Databox Edge Device to. Valid values are "Algeria", "Argentina", "Australia", "Austria", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belgium", "Bermuda", "Bolivia", "Bosnia and Herzegovina", "Brazil", "Bulgaria", "Canada", "Cayman Islands", "Chile", "Colombia", "Costa Rica", "Croatia", "Cyprus", "Czechia", "CÃ´te D'ivoire", "Denmark", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Estonia", "Ethiopia", "Finland", "France", "Georgia", "Germany", "Ghana", "Greece", "Guatemala", "Honduras", "Hong Kong SAR", "Hungary", "Iceland", "India", "Indonesia", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kuwait", "Kyrgyzstan", "Latvia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macao SAR", "Malaysia", "Malta", "Mauritius", "Mexico", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Namibia", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Nigeria", "Norway", "Oman", "Pakistan", "Palestinian Authority", "Panama", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Puerto Rico", "Qatar", "Republic of Korea", "Romania", "Russia", "Rwanda", "Saint Kitts And Nevis", "Saudi Arabia", "Senegal", "Serbia", "Singapore", "Slovakia", "Slovenia", "South Africa", "Spain", "Sri Lanka", "Sweden", "Switzerland", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Trinidad And Tobago", "Tunisia", "Turkey", "Turkmenistan", "U.S. Virgin Islands", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Venezuela", "Vietnam", "Yemen", "Zambia" or "Zimbabwe". Changing this forces a new Databox Edge Order to be created.
        :param pulumi.Input[str] postal_code: The postal code. Changing this forces a new Databox Edge Order to be created.
        :param pulumi.Input[str] state: The name of the state to ship the Databox Edge Device to. Changing this forces a new Databox Edge Order to be created.
        """
        pulumi.set(__self__, "addresses", addresses)
        pulumi.set(__self__, "city", city)
        pulumi.set(__self__, "country", country)
        pulumi.set(__self__, "postal_code", postal_code)
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def addresses(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The list of upto 3 lines for address information. Changing this forces a new Databox Edge Order to be created.
        """
        return pulumi.get(self, "addresses")

    @addresses.setter
    def addresses(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "addresses", value)

    @property
    @pulumi.getter
    def city(self) -> pulumi.Input[str]:
        """
        The city name. Changing this forces a new Databox Edge Order to be created.
        """
        return pulumi.get(self, "city")

    @city.setter
    def city(self, value: pulumi.Input[str]):
        pulumi.set(self, "city", value)

    @property
    @pulumi.getter
    def country(self) -> pulumi.Input[str]:
        """
        The name of the country to ship the Databox Edge Device to. Valid values are "Algeria", "Argentina", "Australia", "Austria", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belgium", "Bermuda", "Bolivia", "Bosnia and Herzegovina", "Brazil", "Bulgaria", "Canada", "Cayman Islands", "Chile", "Colombia", "Costa Rica", "Croatia", "Cyprus", "Czechia", "CÃ´te D'ivoire", "Denmark", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Estonia", "Ethiopia", "Finland", "France", "Georgia", "Germany", "Ghana", "Greece", "Guatemala", "Honduras", "Hong Kong SAR", "Hungary", "Iceland", "India", "Indonesia", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kuwait", "Kyrgyzstan", "Latvia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macao SAR", "Malaysia", "Malta", "Mauritius", "Mexico", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Namibia", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Nigeria", "Norway", "Oman", "Pakistan", "Palestinian Authority", "Panama", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Puerto Rico", "Qatar", "Republic of Korea", "Romania", "Russia", "Rwanda", "Saint Kitts And Nevis", "Saudi Arabia", "Senegal", "Serbia", "Singapore", "Slovakia", "Slovenia", "South Africa", "Spain", "Sri Lanka", "Sweden", "Switzerland", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Trinidad And Tobago", "Tunisia", "Turkey", "Turkmenistan", "U.S. Virgin Islands", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Venezuela", "Vietnam", "Yemen", "Zambia" or "Zimbabwe". Changing this forces a new Databox Edge Order to be created.
        """
        return pulumi.get(self, "country")

    @country.setter
    def country(self, value: pulumi.Input[str]):
        pulumi.set(self, "country", value)

    @property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> pulumi.Input[str]:
        """
        The postal code. Changing this forces a new Databox Edge Order to be created.
        """
        return pulumi.get(self, "postal_code")

    @postal_code.setter
    def postal_code(self, value: pulumi.Input[str]):
        pulumi.set(self, "postal_code", value)

    @property
    @pulumi.getter
    def state(self) -> pulumi.Input[str]:
        """
        The name of the state to ship the Databox Edge Device to. Changing this forces a new Databox Edge Order to be created.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: pulumi.Input[str]):
        pulumi.set(self, "state", value)


@pulumi.input_type
class OrderShipmentHistoryArgs:
    def __init__(__self__, *,
                 additional_details: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 comments: Optional[pulumi.Input[str]] = None,
                 last_update: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_details: Dictionary to hold generic information which is not stored by the already existing properties.
        :param pulumi.Input[str] comments: Comments related to this status change.
        :param pulumi.Input[str] last_update: Time of status update.
        """
        if additional_details is not None:
            pulumi.set(__self__, "additional_details", additional_details)
        if comments is not None:
            pulumi.set(__self__, "comments", comments)
        if last_update is not None:
            pulumi.set(__self__, "last_update", last_update)

    @property
    @pulumi.getter(name="additionalDetails")
    def additional_details(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Dictionary to hold generic information which is not stored by the already existing properties.
        """
        return pulumi.get(self, "additional_details")

    @additional_details.setter
    def additional_details(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "additional_details", value)

    @property
    @pulumi.getter
    def comments(self) -> Optional[pulumi.Input[str]]:
        """
        Comments related to this status change.
        """
        return pulumi.get(self, "comments")

    @comments.setter
    def comments(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comments", value)

    @property
    @pulumi.getter(name="lastUpdate")
    def last_update(self) -> Optional[pulumi.Input[str]]:
        """
        Time of status update.
        """
        return pulumi.get(self, "last_update")

    @last_update.setter
    def last_update(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_update", value)


@pulumi.input_type
class OrderShipmentTrackingArgs:
    def __init__(__self__, *,
                 carrier_name: Optional[pulumi.Input[str]] = None,
                 serial_number: Optional[pulumi.Input[str]] = None,
                 tracking_id: Optional[pulumi.Input[str]] = None,
                 tracking_url: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] carrier_name: Name of the carrier used in the delivery.
        :param pulumi.Input[str] serial_number: Serial number of the device being tracked.
        :param pulumi.Input[str] tracking_id: The ID of the tracking.
        :param pulumi.Input[str] tracking_url: Tracking URL of the shipment.
        """
        if carrier_name is not None:
            pulumi.set(__self__, "carrier_name", carrier_name)
        if serial_number is not None:
            pulumi.set(__self__, "serial_number", serial_number)
        if tracking_id is not None:
            pulumi.set(__self__, "tracking_id", tracking_id)
        if tracking_url is not None:
            pulumi.set(__self__, "tracking_url", tracking_url)

    @property
    @pulumi.getter(name="carrierName")
    def carrier_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the carrier used in the delivery.
        """
        return pulumi.get(self, "carrier_name")

    @carrier_name.setter
    def carrier_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "carrier_name", value)

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[pulumi.Input[str]]:
        """
        Serial number of the device being tracked.
        """
        return pulumi.get(self, "serial_number")

    @serial_number.setter
    def serial_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "serial_number", value)

    @property
    @pulumi.getter(name="trackingId")
    def tracking_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the tracking.
        """
        return pulumi.get(self, "tracking_id")

    @tracking_id.setter
    def tracking_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tracking_id", value)

    @property
    @pulumi.getter(name="trackingUrl")
    def tracking_url(self) -> Optional[pulumi.Input[str]]:
        """
        Tracking URL of the shipment.
        """
        return pulumi.get(self, "tracking_url")

    @tracking_url.setter
    def tracking_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tracking_url", value)


@pulumi.input_type
class OrderStatusArgs:
    def __init__(__self__, *,
                 additional_details: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 comments: Optional[pulumi.Input[str]] = None,
                 info: Optional[pulumi.Input[str]] = None,
                 last_update: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_details: Dictionary to hold generic information which is not stored by the already existing properties.
        :param pulumi.Input[str] comments: Comments related to this status change.
        :param pulumi.Input[str] info: The current status of the order. Possible values include `Untracked`, `AwaitingFulfilment`, `AwaitingPreparation`, `AwaitingShipment`, `Shipped`, `Arriving`, `Delivered`, `ReplacementRequested`, `LostDevice`, `Declined`, `ReturnInitiated`, `AwaitingReturnShipment`, `ShippedBack` or `CollectedAtMicrosoft`.
        :param pulumi.Input[str] last_update: Time of status update.
        """
        if additional_details is not None:
            pulumi.set(__self__, "additional_details", additional_details)
        if comments is not None:
            pulumi.set(__self__, "comments", comments)
        if info is not None:
            pulumi.set(__self__, "info", info)
        if last_update is not None:
            pulumi.set(__self__, "last_update", last_update)

    @property
    @pulumi.getter(name="additionalDetails")
    def additional_details(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Dictionary to hold generic information which is not stored by the already existing properties.
        """
        return pulumi.get(self, "additional_details")

    @additional_details.setter
    def additional_details(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "additional_details", value)

    @property
    @pulumi.getter
    def comments(self) -> Optional[pulumi.Input[str]]:
        """
        Comments related to this status change.
        """
        return pulumi.get(self, "comments")

    @comments.setter
    def comments(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comments", value)

    @property
    @pulumi.getter
    def info(self) -> Optional[pulumi.Input[str]]:
        """
        The current status of the order. Possible values include `Untracked`, `AwaitingFulfilment`, `AwaitingPreparation`, `AwaitingShipment`, `Shipped`, `Arriving`, `Delivered`, `ReplacementRequested`, `LostDevice`, `Declined`, `ReturnInitiated`, `AwaitingReturnShipment`, `ShippedBack` or `CollectedAtMicrosoft`.
        """
        return pulumi.get(self, "info")

    @info.setter
    def info(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "info", value)

    @property
    @pulumi.getter(name="lastUpdate")
    def last_update(self) -> Optional[pulumi.Input[str]]:
        """
        Time of status update.
        """
        return pulumi.get(self, "last_update")

    @last_update.setter
    def last_update(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_update", value)


