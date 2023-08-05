# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetMariaDbServerStorageProfileResult',
]

@pulumi.output_type
class GetMariaDbServerStorageProfileResult(dict):
    def __init__(__self__, *,
                 auto_grow: str,
                 backup_retention_days: int,
                 geo_redundant_backup: str,
                 storage_mb: int):
        """
        :param str auto_grow: Whether autogrow is enabled or disabled for the storage.
        :param int backup_retention_days: Backup retention days for the server.
        :param str geo_redundant_backup: Whether Geo-redundant is enabled or not for server backup.
        :param int storage_mb: The max storage allowed for a server.
        """
        pulumi.set(__self__, "auto_grow", auto_grow)
        pulumi.set(__self__, "backup_retention_days", backup_retention_days)
        pulumi.set(__self__, "geo_redundant_backup", geo_redundant_backup)
        pulumi.set(__self__, "storage_mb", storage_mb)

    @property
    @pulumi.getter(name="autoGrow")
    def auto_grow(self) -> str:
        """
        Whether autogrow is enabled or disabled for the storage.
        """
        return pulumi.get(self, "auto_grow")

    @property
    @pulumi.getter(name="backupRetentionDays")
    def backup_retention_days(self) -> int:
        """
        Backup retention days for the server.
        """
        return pulumi.get(self, "backup_retention_days")

    @property
    @pulumi.getter(name="geoRedundantBackup")
    def geo_redundant_backup(self) -> str:
        """
        Whether Geo-redundant is enabled or not for server backup.
        """
        return pulumi.get(self, "geo_redundant_backup")

    @property
    @pulumi.getter(name="storageMb")
    def storage_mb(self) -> int:
        """
        The max storage allowed for a server.
        """
        return pulumi.get(self, "storage_mb")


