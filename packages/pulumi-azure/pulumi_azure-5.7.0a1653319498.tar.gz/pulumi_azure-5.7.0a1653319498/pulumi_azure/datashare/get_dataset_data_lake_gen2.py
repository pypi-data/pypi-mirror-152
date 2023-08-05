# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetDatasetDataLakeGen2Result',
    'AwaitableGetDatasetDataLakeGen2Result',
    'get_dataset_data_lake_gen2',
    'get_dataset_data_lake_gen2_output',
]

@pulumi.output_type
class GetDatasetDataLakeGen2Result:
    """
    A collection of values returned by getDatasetDataLakeGen2.
    """
    def __init__(__self__, display_name=None, file_path=None, file_system_name=None, folder_path=None, id=None, name=None, share_id=None, storage_account_id=None):
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if file_path and not isinstance(file_path, str):
            raise TypeError("Expected argument 'file_path' to be a str")
        pulumi.set(__self__, "file_path", file_path)
        if file_system_name and not isinstance(file_system_name, str):
            raise TypeError("Expected argument 'file_system_name' to be a str")
        pulumi.set(__self__, "file_system_name", file_system_name)
        if folder_path and not isinstance(folder_path, str):
            raise TypeError("Expected argument 'folder_path' to be a str")
        pulumi.set(__self__, "folder_path", folder_path)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if share_id and not isinstance(share_id, str):
            raise TypeError("Expected argument 'share_id' to be a str")
        pulumi.set(__self__, "share_id", share_id)
        if storage_account_id and not isinstance(storage_account_id, str):
            raise TypeError("Expected argument 'storage_account_id' to be a str")
        pulumi.set(__self__, "storage_account_id", storage_account_id)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The name of the Data Share Dataset.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="filePath")
    def file_path(self) -> str:
        """
        The path of the file in the data lake file system to be shared with the receiver.
        """
        return pulumi.get(self, "file_path")

    @property
    @pulumi.getter(name="fileSystemName")
    def file_system_name(self) -> str:
        """
        The name of the data lake file system to be shared with the receiver.
        """
        return pulumi.get(self, "file_system_name")

    @property
    @pulumi.getter(name="folderPath")
    def folder_path(self) -> str:
        """
        The folder path in the data lake file system to be shared with the receiver.
        """
        return pulumi.get(self, "folder_path")

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
    @pulumi.getter(name="shareId")
    def share_id(self) -> str:
        return pulumi.get(self, "share_id")

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> str:
        """
        The resource ID of the storage account of the data lake file system to be shared with the receiver.
        """
        return pulumi.get(self, "storage_account_id")


class AwaitableGetDatasetDataLakeGen2Result(GetDatasetDataLakeGen2Result):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatasetDataLakeGen2Result(
            display_name=self.display_name,
            file_path=self.file_path,
            file_system_name=self.file_system_name,
            folder_path=self.folder_path,
            id=self.id,
            name=self.name,
            share_id=self.share_id,
            storage_account_id=self.storage_account_id)


def get_dataset_data_lake_gen2(name: Optional[str] = None,
                               share_id: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatasetDataLakeGen2Result:
    """
    Use this data source to access information about an existing Data Share Data Lake Gen2 Dataset.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.datashare.get_dataset_data_lake_gen2(name="example-dsdlg2ds",
        share_id="example-share-id")
    pulumi.export("id", example.id)
    ```


    :param str name: The name of this Data Share Data Lake Gen2 Dataset.
    :param str share_id: The resource ID of the Data Share where this Data Share Data Lake Gen2 Dataset should be created.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['shareId'] = share_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:datashare/getDatasetDataLakeGen2:getDatasetDataLakeGen2', __args__, opts=opts, typ=GetDatasetDataLakeGen2Result).value

    return AwaitableGetDatasetDataLakeGen2Result(
        display_name=__ret__.display_name,
        file_path=__ret__.file_path,
        file_system_name=__ret__.file_system_name,
        folder_path=__ret__.folder_path,
        id=__ret__.id,
        name=__ret__.name,
        share_id=__ret__.share_id,
        storage_account_id=__ret__.storage_account_id)


@_utilities.lift_output_func(get_dataset_data_lake_gen2)
def get_dataset_data_lake_gen2_output(name: Optional[pulumi.Input[str]] = None,
                                      share_id: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatasetDataLakeGen2Result]:
    """
    Use this data source to access information about an existing Data Share Data Lake Gen2 Dataset.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.datashare.get_dataset_data_lake_gen2(name="example-dsdlg2ds",
        share_id="example-share-id")
    pulumi.export("id", example.id)
    ```


    :param str name: The name of this Data Share Data Lake Gen2 Dataset.
    :param str share_id: The resource ID of the Data Share where this Data Share Data Lake Gen2 Dataset should be created.
    """
    ...
