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

__all__ = ['FunctionJavascriptUdaArgs', 'FunctionJavascriptUda']

@pulumi.input_type
class FunctionJavascriptUdaArgs:
    def __init__(__self__, *,
                 inputs: pulumi.Input[Sequence[pulumi.Input['FunctionJavascriptUdaInputArgs']]],
                 output: pulumi.Input['FunctionJavascriptUdaOutputArgs'],
                 script: pulumi.Input[str],
                 stream_analytics_job_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FunctionJavascriptUda resource.
        :param pulumi.Input[Sequence[pulumi.Input['FunctionJavascriptUdaInputArgs']]] inputs: One or more `input` blocks as defined below.
        :param pulumi.Input['FunctionJavascriptUdaOutputArgs'] output: An `output` block as defined below.
        :param pulumi.Input[str] script: The JavaScript of this UDA Function.
        :param pulumi.Input[str] stream_analytics_job_id: The resource ID of the Stream Analytics Job where this Function should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the JavaScript UDA Function. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "inputs", inputs)
        pulumi.set(__self__, "output", output)
        pulumi.set(__self__, "script", script)
        pulumi.set(__self__, "stream_analytics_job_id", stream_analytics_job_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def inputs(self) -> pulumi.Input[Sequence[pulumi.Input['FunctionJavascriptUdaInputArgs']]]:
        """
        One or more `input` blocks as defined below.
        """
        return pulumi.get(self, "inputs")

    @inputs.setter
    def inputs(self, value: pulumi.Input[Sequence[pulumi.Input['FunctionJavascriptUdaInputArgs']]]):
        pulumi.set(self, "inputs", value)

    @property
    @pulumi.getter
    def output(self) -> pulumi.Input['FunctionJavascriptUdaOutputArgs']:
        """
        An `output` block as defined below.
        """
        return pulumi.get(self, "output")

    @output.setter
    def output(self, value: pulumi.Input['FunctionJavascriptUdaOutputArgs']):
        pulumi.set(self, "output", value)

    @property
    @pulumi.getter
    def script(self) -> pulumi.Input[str]:
        """
        The JavaScript of this UDA Function.
        """
        return pulumi.get(self, "script")

    @script.setter
    def script(self, value: pulumi.Input[str]):
        pulumi.set(self, "script", value)

    @property
    @pulumi.getter(name="streamAnalyticsJobId")
    def stream_analytics_job_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the Stream Analytics Job where this Function should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "stream_analytics_job_id")

    @stream_analytics_job_id.setter
    def stream_analytics_job_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "stream_analytics_job_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the JavaScript UDA Function. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _FunctionJavascriptUdaState:
    def __init__(__self__, *,
                 inputs: Optional[pulumi.Input[Sequence[pulumi.Input['FunctionJavascriptUdaInputArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 output: Optional[pulumi.Input['FunctionJavascriptUdaOutputArgs']] = None,
                 script: Optional[pulumi.Input[str]] = None,
                 stream_analytics_job_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FunctionJavascriptUda resources.
        :param pulumi.Input[Sequence[pulumi.Input['FunctionJavascriptUdaInputArgs']]] inputs: One or more `input` blocks as defined below.
        :param pulumi.Input[str] name: The name of the JavaScript UDA Function. Changing this forces a new resource to be created.
        :param pulumi.Input['FunctionJavascriptUdaOutputArgs'] output: An `output` block as defined below.
        :param pulumi.Input[str] script: The JavaScript of this UDA Function.
        :param pulumi.Input[str] stream_analytics_job_id: The resource ID of the Stream Analytics Job where this Function should be created. Changing this forces a new resource to be created.
        """
        if inputs is not None:
            pulumi.set(__self__, "inputs", inputs)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if output is not None:
            pulumi.set(__self__, "output", output)
        if script is not None:
            pulumi.set(__self__, "script", script)
        if stream_analytics_job_id is not None:
            pulumi.set(__self__, "stream_analytics_job_id", stream_analytics_job_id)

    @property
    @pulumi.getter
    def inputs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FunctionJavascriptUdaInputArgs']]]]:
        """
        One or more `input` blocks as defined below.
        """
        return pulumi.get(self, "inputs")

    @inputs.setter
    def inputs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FunctionJavascriptUdaInputArgs']]]]):
        pulumi.set(self, "inputs", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the JavaScript UDA Function. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def output(self) -> Optional[pulumi.Input['FunctionJavascriptUdaOutputArgs']]:
        """
        An `output` block as defined below.
        """
        return pulumi.get(self, "output")

    @output.setter
    def output(self, value: Optional[pulumi.Input['FunctionJavascriptUdaOutputArgs']]):
        pulumi.set(self, "output", value)

    @property
    @pulumi.getter
    def script(self) -> Optional[pulumi.Input[str]]:
        """
        The JavaScript of this UDA Function.
        """
        return pulumi.get(self, "script")

    @script.setter
    def script(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "script", value)

    @property
    @pulumi.getter(name="streamAnalyticsJobId")
    def stream_analytics_job_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the Stream Analytics Job where this Function should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "stream_analytics_job_id")

    @stream_analytics_job_id.setter
    def stream_analytics_job_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stream_analytics_job_id", value)


class FunctionJavascriptUda(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 inputs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FunctionJavascriptUdaInputArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 output: Optional[pulumi.Input[pulumi.InputType['FunctionJavascriptUdaOutputArgs']]] = None,
                 script: Optional[pulumi.Input[str]] = None,
                 stream_analytics_job_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a JavaScript UDA Function within a Stream Analytics Streaming Job.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.get_resource_group(name="example-resources")
        example_job = azure.streamanalytics.get_job(name="example-job",
            resource_group_name=azurerm_resource_group["example"]["name"])
        example_function_javascript_uda = azure.streamanalytics.FunctionJavascriptUda("exampleFunctionJavascriptUda",
            stream_analytics_job_id=example_job.id,
            script=\"\"\"function main() {
            this.init = function () {
                this.state = 0;
            }

            this.accumulate = function (value, timestamp) {
                this.state += value;
            }

            this.computeResult = function () {
                return this.state;
            }
        }
        \"\"\",
            inputs=[azure.streamanalytics.FunctionJavascriptUdaInputArgs(
                type="bigint",
            )],
            output=azure.streamanalytics.FunctionJavascriptUdaOutputArgs(
                type="bigint",
            ))
        ```

        ## Import

        Stream Analytics JavaScript UDA Functions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:streamanalytics/functionJavascriptUda:FunctionJavascriptUda example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.StreamAnalytics/streamingjobs/job1/functions/func1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FunctionJavascriptUdaInputArgs']]]] inputs: One or more `input` blocks as defined below.
        :param pulumi.Input[str] name: The name of the JavaScript UDA Function. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['FunctionJavascriptUdaOutputArgs']] output: An `output` block as defined below.
        :param pulumi.Input[str] script: The JavaScript of this UDA Function.
        :param pulumi.Input[str] stream_analytics_job_id: The resource ID of the Stream Analytics Job where this Function should be created. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FunctionJavascriptUdaArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a JavaScript UDA Function within a Stream Analytics Streaming Job.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.get_resource_group(name="example-resources")
        example_job = azure.streamanalytics.get_job(name="example-job",
            resource_group_name=azurerm_resource_group["example"]["name"])
        example_function_javascript_uda = azure.streamanalytics.FunctionJavascriptUda("exampleFunctionJavascriptUda",
            stream_analytics_job_id=example_job.id,
            script=\"\"\"function main() {
            this.init = function () {
                this.state = 0;
            }

            this.accumulate = function (value, timestamp) {
                this.state += value;
            }

            this.computeResult = function () {
                return this.state;
            }
        }
        \"\"\",
            inputs=[azure.streamanalytics.FunctionJavascriptUdaInputArgs(
                type="bigint",
            )],
            output=azure.streamanalytics.FunctionJavascriptUdaOutputArgs(
                type="bigint",
            ))
        ```

        ## Import

        Stream Analytics JavaScript UDA Functions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:streamanalytics/functionJavascriptUda:FunctionJavascriptUda example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.StreamAnalytics/streamingjobs/job1/functions/func1
        ```

        :param str resource_name: The name of the resource.
        :param FunctionJavascriptUdaArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FunctionJavascriptUdaArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 inputs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FunctionJavascriptUdaInputArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 output: Optional[pulumi.Input[pulumi.InputType['FunctionJavascriptUdaOutputArgs']]] = None,
                 script: Optional[pulumi.Input[str]] = None,
                 stream_analytics_job_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = FunctionJavascriptUdaArgs.__new__(FunctionJavascriptUdaArgs)

            if inputs is None and not opts.urn:
                raise TypeError("Missing required property 'inputs'")
            __props__.__dict__["inputs"] = inputs
            __props__.__dict__["name"] = name
            if output is None and not opts.urn:
                raise TypeError("Missing required property 'output'")
            __props__.__dict__["output"] = output
            if script is None and not opts.urn:
                raise TypeError("Missing required property 'script'")
            __props__.__dict__["script"] = script
            if stream_analytics_job_id is None and not opts.urn:
                raise TypeError("Missing required property 'stream_analytics_job_id'")
            __props__.__dict__["stream_analytics_job_id"] = stream_analytics_job_id
        super(FunctionJavascriptUda, __self__).__init__(
            'azure:streamanalytics/functionJavascriptUda:FunctionJavascriptUda',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            inputs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FunctionJavascriptUdaInputArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            output: Optional[pulumi.Input[pulumi.InputType['FunctionJavascriptUdaOutputArgs']]] = None,
            script: Optional[pulumi.Input[str]] = None,
            stream_analytics_job_id: Optional[pulumi.Input[str]] = None) -> 'FunctionJavascriptUda':
        """
        Get an existing FunctionJavascriptUda resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FunctionJavascriptUdaInputArgs']]]] inputs: One or more `input` blocks as defined below.
        :param pulumi.Input[str] name: The name of the JavaScript UDA Function. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['FunctionJavascriptUdaOutputArgs']] output: An `output` block as defined below.
        :param pulumi.Input[str] script: The JavaScript of this UDA Function.
        :param pulumi.Input[str] stream_analytics_job_id: The resource ID of the Stream Analytics Job where this Function should be created. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FunctionJavascriptUdaState.__new__(_FunctionJavascriptUdaState)

        __props__.__dict__["inputs"] = inputs
        __props__.__dict__["name"] = name
        __props__.__dict__["output"] = output
        __props__.__dict__["script"] = script
        __props__.__dict__["stream_analytics_job_id"] = stream_analytics_job_id
        return FunctionJavascriptUda(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def inputs(self) -> pulumi.Output[Sequence['outputs.FunctionJavascriptUdaInput']]:
        """
        One or more `input` blocks as defined below.
        """
        return pulumi.get(self, "inputs")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the JavaScript UDA Function. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def output(self) -> pulumi.Output['outputs.FunctionJavascriptUdaOutput']:
        """
        An `output` block as defined below.
        """
        return pulumi.get(self, "output")

    @property
    @pulumi.getter
    def script(self) -> pulumi.Output[str]:
        """
        The JavaScript of this UDA Function.
        """
        return pulumi.get(self, "script")

    @property
    @pulumi.getter(name="streamAnalyticsJobId")
    def stream_analytics_job_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the Stream Analytics Job where this Function should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "stream_analytics_job_id")

