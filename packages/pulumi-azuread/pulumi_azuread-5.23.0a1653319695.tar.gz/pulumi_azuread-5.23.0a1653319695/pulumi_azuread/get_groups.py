# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetGroupsResult',
    'AwaitableGetGroupsResult',
    'get_groups',
    'get_groups_output',
]

@pulumi.output_type
class GetGroupsResult:
    """
    A collection of values returned by getGroups.
    """
    def __init__(__self__, display_name_prefix=None, display_names=None, id=None, ignore_missing=None, mail_enabled=None, object_ids=None, return_all=None, security_enabled=None):
        if display_name_prefix and not isinstance(display_name_prefix, str):
            raise TypeError("Expected argument 'display_name_prefix' to be a str")
        pulumi.set(__self__, "display_name_prefix", display_name_prefix)
        if display_names and not isinstance(display_names, list):
            raise TypeError("Expected argument 'display_names' to be a list")
        pulumi.set(__self__, "display_names", display_names)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ignore_missing and not isinstance(ignore_missing, bool):
            raise TypeError("Expected argument 'ignore_missing' to be a bool")
        pulumi.set(__self__, "ignore_missing", ignore_missing)
        if mail_enabled and not isinstance(mail_enabled, bool):
            raise TypeError("Expected argument 'mail_enabled' to be a bool")
        pulumi.set(__self__, "mail_enabled", mail_enabled)
        if object_ids and not isinstance(object_ids, list):
            raise TypeError("Expected argument 'object_ids' to be a list")
        pulumi.set(__self__, "object_ids", object_ids)
        if return_all and not isinstance(return_all, bool):
            raise TypeError("Expected argument 'return_all' to be a bool")
        pulumi.set(__self__, "return_all", return_all)
        if security_enabled and not isinstance(security_enabled, bool):
            raise TypeError("Expected argument 'security_enabled' to be a bool")
        pulumi.set(__self__, "security_enabled", security_enabled)

    @property
    @pulumi.getter(name="displayNamePrefix")
    def display_name_prefix(self) -> str:
        return pulumi.get(self, "display_name_prefix")

    @property
    @pulumi.getter(name="displayNames")
    def display_names(self) -> Sequence[str]:
        """
        The display names of the groups.
        """
        return pulumi.get(self, "display_names")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ignoreMissing")
    def ignore_missing(self) -> Optional[bool]:
        return pulumi.get(self, "ignore_missing")

    @property
    @pulumi.getter(name="mailEnabled")
    def mail_enabled(self) -> bool:
        return pulumi.get(self, "mail_enabled")

    @property
    @pulumi.getter(name="objectIds")
    def object_ids(self) -> Sequence[str]:
        """
        The object IDs of the groups.
        """
        return pulumi.get(self, "object_ids")

    @property
    @pulumi.getter(name="returnAll")
    def return_all(self) -> Optional[bool]:
        return pulumi.get(self, "return_all")

    @property
    @pulumi.getter(name="securityEnabled")
    def security_enabled(self) -> bool:
        return pulumi.get(self, "security_enabled")


class AwaitableGetGroupsResult(GetGroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGroupsResult(
            display_name_prefix=self.display_name_prefix,
            display_names=self.display_names,
            id=self.id,
            ignore_missing=self.ignore_missing,
            mail_enabled=self.mail_enabled,
            object_ids=self.object_ids,
            return_all=self.return_all,
            security_enabled=self.security_enabled)


def get_groups(display_name_prefix: Optional[str] = None,
               display_names: Optional[Sequence[str]] = None,
               ignore_missing: Optional[bool] = None,
               mail_enabled: Optional[bool] = None,
               object_ids: Optional[Sequence[str]] = None,
               return_all: Optional[bool] = None,
               security_enabled: Optional[bool] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGroupsResult:
    """
    Gets Object IDs or Display Names for multiple Azure Active Directory groups.

    ## API Permissions

    The following API permissions are required in order to use this data source.

    When authenticated with a service principal, this data source requires one of the following application roles: `Group.Read.All` or `Directory.Read.All`

    When authenticated with a user principal, this data source does not require any additional roles.

    ## Example Usage

    *Look up by group name*
    ```python
    import pulumi
    import pulumi_azuread as azuread

    example = azuread.get_groups(display_names=[
        "group-a",
        "group-b",
    ])
    ```

    *Look up by display name prefix*
    ```python
    import pulumi
    import pulumi_azuread as azuread

    sales = azuread.get_groups(display_name_prefix="sales-")
    ```

    *Look up all groups*
    ```python
    import pulumi
    import pulumi_azuread as azuread

    all = azuread.get_groups(return_all=True)
    ```

    *Look up all mail-enabled groups*
    ```python
    import pulumi
    import pulumi_azuread as azuread

    mail_enabled = azuread.get_groups(mail_enabled=True,
        return_all=True)
    ```

    *Look up all security-enabled groups that are not mail-enabled*
    ```python
    import pulumi
    import pulumi_azuread as azuread

    security_only = azuread.get_groups(mail_enabled=False,
        return_all=True,
        security_enabled=True)
    ```


    :param str display_name_prefix: A common display name prefix to match when returning groups.
    :param Sequence[str] display_names: The display names of the groups.
    :param bool ignore_missing: Ignore missing groups and return groups that were found. The data source will still fail if no groups are found. Cannot be specified with `return_all`. Defaults to `false`.
    :param bool mail_enabled: Whether the returned groups should be mail-enabled. By itself this does not exclude security-enabled groups. Setting this to `true` ensures all groups are mail-enabled, and setting to `false` ensures that all groups are _not_ mail-enabled. To ignore this filter, omit the property or set it to null. Cannot be specified together with `object_ids`.
    :param Sequence[str] object_ids: The object IDs of the groups.
    :param bool return_all: A flag to denote if all groups should be fetched and returned. Cannot be specified wth `ignore_missing`. Defaults to `false`.
    :param bool security_enabled: Whether the returned groups should be security-enabled. By itself this does not exclude mail-enabled groups. Setting this to `true` ensures all groups are security-enabled, and setting to `false` ensures that all groups are _not_ security-enabled. To ignore this filter, omit the property or set it to null. Cannot be specified together with `object_ids`.
    """
    __args__ = dict()
    __args__['displayNamePrefix'] = display_name_prefix
    __args__['displayNames'] = display_names
    __args__['ignoreMissing'] = ignore_missing
    __args__['mailEnabled'] = mail_enabled
    __args__['objectIds'] = object_ids
    __args__['returnAll'] = return_all
    __args__['securityEnabled'] = security_enabled
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azuread:index/getGroups:getGroups', __args__, opts=opts, typ=GetGroupsResult).value

    return AwaitableGetGroupsResult(
        display_name_prefix=__ret__.display_name_prefix,
        display_names=__ret__.display_names,
        id=__ret__.id,
        ignore_missing=__ret__.ignore_missing,
        mail_enabled=__ret__.mail_enabled,
        object_ids=__ret__.object_ids,
        return_all=__ret__.return_all,
        security_enabled=__ret__.security_enabled)


@_utilities.lift_output_func(get_groups)
def get_groups_output(display_name_prefix: Optional[pulumi.Input[Optional[str]]] = None,
                      display_names: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                      ignore_missing: Optional[pulumi.Input[Optional[bool]]] = None,
                      mail_enabled: Optional[pulumi.Input[Optional[bool]]] = None,
                      object_ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                      return_all: Optional[pulumi.Input[Optional[bool]]] = None,
                      security_enabled: Optional[pulumi.Input[Optional[bool]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGroupsResult]:
    """
    Gets Object IDs or Display Names for multiple Azure Active Directory groups.

    ## API Permissions

    The following API permissions are required in order to use this data source.

    When authenticated with a service principal, this data source requires one of the following application roles: `Group.Read.All` or `Directory.Read.All`

    When authenticated with a user principal, this data source does not require any additional roles.

    ## Example Usage

    *Look up by group name*
    ```python
    import pulumi
    import pulumi_azuread as azuread

    example = azuread.get_groups(display_names=[
        "group-a",
        "group-b",
    ])
    ```

    *Look up by display name prefix*
    ```python
    import pulumi
    import pulumi_azuread as azuread

    sales = azuread.get_groups(display_name_prefix="sales-")
    ```

    *Look up all groups*
    ```python
    import pulumi
    import pulumi_azuread as azuread

    all = azuread.get_groups(return_all=True)
    ```

    *Look up all mail-enabled groups*
    ```python
    import pulumi
    import pulumi_azuread as azuread

    mail_enabled = azuread.get_groups(mail_enabled=True,
        return_all=True)
    ```

    *Look up all security-enabled groups that are not mail-enabled*
    ```python
    import pulumi
    import pulumi_azuread as azuread

    security_only = azuread.get_groups(mail_enabled=False,
        return_all=True,
        security_enabled=True)
    ```


    :param str display_name_prefix: A common display name prefix to match when returning groups.
    :param Sequence[str] display_names: The display names of the groups.
    :param bool ignore_missing: Ignore missing groups and return groups that were found. The data source will still fail if no groups are found. Cannot be specified with `return_all`. Defaults to `false`.
    :param bool mail_enabled: Whether the returned groups should be mail-enabled. By itself this does not exclude security-enabled groups. Setting this to `true` ensures all groups are mail-enabled, and setting to `false` ensures that all groups are _not_ mail-enabled. To ignore this filter, omit the property or set it to null. Cannot be specified together with `object_ids`.
    :param Sequence[str] object_ids: The object IDs of the groups.
    :param bool return_all: A flag to denote if all groups should be fetched and returned. Cannot be specified wth `ignore_missing`. Defaults to `false`.
    :param bool security_enabled: Whether the returned groups should be security-enabled. By itself this does not exclude mail-enabled groups. Setting this to `true` ensures all groups are security-enabled, and setting to `false` ensures that all groups are _not_ security-enabled. To ignore this filter, omit the property or set it to null. Cannot be specified together with `object_ids`.
    """
    ...
