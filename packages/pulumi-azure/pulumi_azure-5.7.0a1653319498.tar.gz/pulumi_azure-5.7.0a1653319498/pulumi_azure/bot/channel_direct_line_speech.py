# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ChannelDirectLineSpeechArgs', 'ChannelDirectLineSpeech']

@pulumi.input_type
class ChannelDirectLineSpeechArgs:
    def __init__(__self__, *,
                 bot_name: pulumi.Input[str],
                 cognitive_service_access_key: pulumi.Input[str],
                 cognitive_service_location: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 custom_speech_model_id: Optional[pulumi.Input[str]] = None,
                 custom_voice_deployment_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ChannelDirectLineSpeech resource.
        :param pulumi.Input[str] bot_name: The name of the Bot Resource this channel will be associated with. Changing this forces a new resource to be created.
        :param pulumi.Input[str] cognitive_service_access_key: The access key to access the Cognitive Service.
        :param pulumi.Input[str] cognitive_service_location: Specifies the supported Azure location where the Cognitive Service resource exists.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the Direct Line Speech Channel should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] custom_speech_model_id: The custom speech model id for the Direct Line Speech Channel.
        :param pulumi.Input[str] custom_voice_deployment_id: The custom voice deployment id for the Direct Line Speech Channel.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "bot_name", bot_name)
        pulumi.set(__self__, "cognitive_service_access_key", cognitive_service_access_key)
        pulumi.set(__self__, "cognitive_service_location", cognitive_service_location)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if custom_speech_model_id is not None:
            pulumi.set(__self__, "custom_speech_model_id", custom_speech_model_id)
        if custom_voice_deployment_id is not None:
            pulumi.set(__self__, "custom_voice_deployment_id", custom_voice_deployment_id)
        if location is not None:
            pulumi.set(__self__, "location", location)

    @property
    @pulumi.getter(name="botName")
    def bot_name(self) -> pulumi.Input[str]:
        """
        The name of the Bot Resource this channel will be associated with. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "bot_name")

    @bot_name.setter
    def bot_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "bot_name", value)

    @property
    @pulumi.getter(name="cognitiveServiceAccessKey")
    def cognitive_service_access_key(self) -> pulumi.Input[str]:
        """
        The access key to access the Cognitive Service.
        """
        return pulumi.get(self, "cognitive_service_access_key")

    @cognitive_service_access_key.setter
    def cognitive_service_access_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "cognitive_service_access_key", value)

    @property
    @pulumi.getter(name="cognitiveServiceLocation")
    def cognitive_service_location(self) -> pulumi.Input[str]:
        """
        Specifies the supported Azure location where the Cognitive Service resource exists.
        """
        return pulumi.get(self, "cognitive_service_location")

    @cognitive_service_location.setter
    def cognitive_service_location(self, value: pulumi.Input[str]):
        pulumi.set(self, "cognitive_service_location", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group where the Direct Line Speech Channel should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="customSpeechModelId")
    def custom_speech_model_id(self) -> Optional[pulumi.Input[str]]:
        """
        The custom speech model id for the Direct Line Speech Channel.
        """
        return pulumi.get(self, "custom_speech_model_id")

    @custom_speech_model_id.setter
    def custom_speech_model_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_speech_model_id", value)

    @property
    @pulumi.getter(name="customVoiceDeploymentId")
    def custom_voice_deployment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The custom voice deployment id for the Direct Line Speech Channel.
        """
        return pulumi.get(self, "custom_voice_deployment_id")

    @custom_voice_deployment_id.setter
    def custom_voice_deployment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_voice_deployment_id", value)

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


@pulumi.input_type
class _ChannelDirectLineSpeechState:
    def __init__(__self__, *,
                 bot_name: Optional[pulumi.Input[str]] = None,
                 cognitive_service_access_key: Optional[pulumi.Input[str]] = None,
                 cognitive_service_location: Optional[pulumi.Input[str]] = None,
                 custom_speech_model_id: Optional[pulumi.Input[str]] = None,
                 custom_voice_deployment_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ChannelDirectLineSpeech resources.
        :param pulumi.Input[str] bot_name: The name of the Bot Resource this channel will be associated with. Changing this forces a new resource to be created.
        :param pulumi.Input[str] cognitive_service_access_key: The access key to access the Cognitive Service.
        :param pulumi.Input[str] cognitive_service_location: Specifies the supported Azure location where the Cognitive Service resource exists.
        :param pulumi.Input[str] custom_speech_model_id: The custom speech model id for the Direct Line Speech Channel.
        :param pulumi.Input[str] custom_voice_deployment_id: The custom voice deployment id for the Direct Line Speech Channel.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the Direct Line Speech Channel should be created. Changing this forces a new resource to be created.
        """
        if bot_name is not None:
            pulumi.set(__self__, "bot_name", bot_name)
        if cognitive_service_access_key is not None:
            pulumi.set(__self__, "cognitive_service_access_key", cognitive_service_access_key)
        if cognitive_service_location is not None:
            pulumi.set(__self__, "cognitive_service_location", cognitive_service_location)
        if custom_speech_model_id is not None:
            pulumi.set(__self__, "custom_speech_model_id", custom_speech_model_id)
        if custom_voice_deployment_id is not None:
            pulumi.set(__self__, "custom_voice_deployment_id", custom_voice_deployment_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)

    @property
    @pulumi.getter(name="botName")
    def bot_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Bot Resource this channel will be associated with. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "bot_name")

    @bot_name.setter
    def bot_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bot_name", value)

    @property
    @pulumi.getter(name="cognitiveServiceAccessKey")
    def cognitive_service_access_key(self) -> Optional[pulumi.Input[str]]:
        """
        The access key to access the Cognitive Service.
        """
        return pulumi.get(self, "cognitive_service_access_key")

    @cognitive_service_access_key.setter
    def cognitive_service_access_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cognitive_service_access_key", value)

    @property
    @pulumi.getter(name="cognitiveServiceLocation")
    def cognitive_service_location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the supported Azure location where the Cognitive Service resource exists.
        """
        return pulumi.get(self, "cognitive_service_location")

    @cognitive_service_location.setter
    def cognitive_service_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cognitive_service_location", value)

    @property
    @pulumi.getter(name="customSpeechModelId")
    def custom_speech_model_id(self) -> Optional[pulumi.Input[str]]:
        """
        The custom speech model id for the Direct Line Speech Channel.
        """
        return pulumi.get(self, "custom_speech_model_id")

    @custom_speech_model_id.setter
    def custom_speech_model_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_speech_model_id", value)

    @property
    @pulumi.getter(name="customVoiceDeploymentId")
    def custom_voice_deployment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The custom voice deployment id for the Direct Line Speech Channel.
        """
        return pulumi.get(self, "custom_voice_deployment_id")

    @custom_voice_deployment_id.setter
    def custom_voice_deployment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_voice_deployment_id", value)

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
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource group where the Direct Line Speech Channel should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)


class ChannelDirectLineSpeech(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bot_name: Optional[pulumi.Input[str]] = None,
                 cognitive_service_access_key: Optional[pulumi.Input[str]] = None,
                 cognitive_service_location: Optional[pulumi.Input[str]] = None,
                 custom_speech_model_id: Optional[pulumi.Input[str]] = None,
                 custom_voice_deployment_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Direct Line Speech integration for a Bot Channel

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        current = azure.core.get_client_config()
        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.cognitive.Account("exampleAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            kind="SpeechServices",
            sku_name="S0")
        example_channels_registration = azure.bot.ChannelsRegistration("exampleChannelsRegistration",
            location="global",
            resource_group_name=example_resource_group.name,
            sku="F0",
            microsoft_app_id=current.client_id)
        example_channel_direct_line_speech = azure.bot.ChannelDirectLineSpeech("exampleChannelDirectLineSpeech",
            bot_name=example_channels_registration.name,
            location=example_channels_registration.location,
            resource_group_name=example_resource_group.name,
            cognitive_service_location=example_account.location,
            cognitive_service_access_key=example_account.primary_access_key)
        ```

        ## Import

        Direct Line Speech Channels can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:bot/channelDirectLineSpeech:ChannelDirectLineSpeech example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.BotService/botServices/botService1/channels/DirectLineSpeechChannel
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bot_name: The name of the Bot Resource this channel will be associated with. Changing this forces a new resource to be created.
        :param pulumi.Input[str] cognitive_service_access_key: The access key to access the Cognitive Service.
        :param pulumi.Input[str] cognitive_service_location: Specifies the supported Azure location where the Cognitive Service resource exists.
        :param pulumi.Input[str] custom_speech_model_id: The custom speech model id for the Direct Line Speech Channel.
        :param pulumi.Input[str] custom_voice_deployment_id: The custom voice deployment id for the Direct Line Speech Channel.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the Direct Line Speech Channel should be created. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ChannelDirectLineSpeechArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Direct Line Speech integration for a Bot Channel

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        current = azure.core.get_client_config()
        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.cognitive.Account("exampleAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            kind="SpeechServices",
            sku_name="S0")
        example_channels_registration = azure.bot.ChannelsRegistration("exampleChannelsRegistration",
            location="global",
            resource_group_name=example_resource_group.name,
            sku="F0",
            microsoft_app_id=current.client_id)
        example_channel_direct_line_speech = azure.bot.ChannelDirectLineSpeech("exampleChannelDirectLineSpeech",
            bot_name=example_channels_registration.name,
            location=example_channels_registration.location,
            resource_group_name=example_resource_group.name,
            cognitive_service_location=example_account.location,
            cognitive_service_access_key=example_account.primary_access_key)
        ```

        ## Import

        Direct Line Speech Channels can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:bot/channelDirectLineSpeech:ChannelDirectLineSpeech example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.BotService/botServices/botService1/channels/DirectLineSpeechChannel
        ```

        :param str resource_name: The name of the resource.
        :param ChannelDirectLineSpeechArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ChannelDirectLineSpeechArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bot_name: Optional[pulumi.Input[str]] = None,
                 cognitive_service_access_key: Optional[pulumi.Input[str]] = None,
                 cognitive_service_location: Optional[pulumi.Input[str]] = None,
                 custom_speech_model_id: Optional[pulumi.Input[str]] = None,
                 custom_voice_deployment_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ChannelDirectLineSpeechArgs.__new__(ChannelDirectLineSpeechArgs)

            if bot_name is None and not opts.urn:
                raise TypeError("Missing required property 'bot_name'")
            __props__.__dict__["bot_name"] = bot_name
            if cognitive_service_access_key is None and not opts.urn:
                raise TypeError("Missing required property 'cognitive_service_access_key'")
            __props__.__dict__["cognitive_service_access_key"] = cognitive_service_access_key
            if cognitive_service_location is None and not opts.urn:
                raise TypeError("Missing required property 'cognitive_service_location'")
            __props__.__dict__["cognitive_service_location"] = cognitive_service_location
            __props__.__dict__["custom_speech_model_id"] = custom_speech_model_id
            __props__.__dict__["custom_voice_deployment_id"] = custom_voice_deployment_id
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
        super(ChannelDirectLineSpeech, __self__).__init__(
            'azure:bot/channelDirectLineSpeech:ChannelDirectLineSpeech',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bot_name: Optional[pulumi.Input[str]] = None,
            cognitive_service_access_key: Optional[pulumi.Input[str]] = None,
            cognitive_service_location: Optional[pulumi.Input[str]] = None,
            custom_speech_model_id: Optional[pulumi.Input[str]] = None,
            custom_voice_deployment_id: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None) -> 'ChannelDirectLineSpeech':
        """
        Get an existing ChannelDirectLineSpeech resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bot_name: The name of the Bot Resource this channel will be associated with. Changing this forces a new resource to be created.
        :param pulumi.Input[str] cognitive_service_access_key: The access key to access the Cognitive Service.
        :param pulumi.Input[str] cognitive_service_location: Specifies the supported Azure location where the Cognitive Service resource exists.
        :param pulumi.Input[str] custom_speech_model_id: The custom speech model id for the Direct Line Speech Channel.
        :param pulumi.Input[str] custom_voice_deployment_id: The custom voice deployment id for the Direct Line Speech Channel.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the Direct Line Speech Channel should be created. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ChannelDirectLineSpeechState.__new__(_ChannelDirectLineSpeechState)

        __props__.__dict__["bot_name"] = bot_name
        __props__.__dict__["cognitive_service_access_key"] = cognitive_service_access_key
        __props__.__dict__["cognitive_service_location"] = cognitive_service_location
        __props__.__dict__["custom_speech_model_id"] = custom_speech_model_id
        __props__.__dict__["custom_voice_deployment_id"] = custom_voice_deployment_id
        __props__.__dict__["location"] = location
        __props__.__dict__["resource_group_name"] = resource_group_name
        return ChannelDirectLineSpeech(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="botName")
    def bot_name(self) -> pulumi.Output[str]:
        """
        The name of the Bot Resource this channel will be associated with. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "bot_name")

    @property
    @pulumi.getter(name="cognitiveServiceAccessKey")
    def cognitive_service_access_key(self) -> pulumi.Output[str]:
        """
        The access key to access the Cognitive Service.
        """
        return pulumi.get(self, "cognitive_service_access_key")

    @property
    @pulumi.getter(name="cognitiveServiceLocation")
    def cognitive_service_location(self) -> pulumi.Output[str]:
        """
        Specifies the supported Azure location where the Cognitive Service resource exists.
        """
        return pulumi.get(self, "cognitive_service_location")

    @property
    @pulumi.getter(name="customSpeechModelId")
    def custom_speech_model_id(self) -> pulumi.Output[Optional[str]]:
        """
        The custom speech model id for the Direct Line Speech Channel.
        """
        return pulumi.get(self, "custom_speech_model_id")

    @property
    @pulumi.getter(name="customVoiceDeploymentId")
    def custom_voice_deployment_id(self) -> pulumi.Output[Optional[str]]:
        """
        The custom voice deployment id for the Direct Line Speech Channel.
        """
        return pulumi.get(self, "custom_voice_deployment_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group where the Direct Line Speech Channel should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

