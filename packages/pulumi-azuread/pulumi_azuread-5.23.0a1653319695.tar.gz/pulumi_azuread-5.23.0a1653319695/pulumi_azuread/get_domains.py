# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetDomainsResult',
    'AwaitableGetDomainsResult',
    'get_domains',
    'get_domains_output',
]

@pulumi.output_type
class GetDomainsResult:
    """
    A collection of values returned by getDomains.
    """
    def __init__(__self__, admin_managed=None, domains=None, id=None, include_unverified=None, only_default=None, only_initial=None, only_root=None, supports_services=None):
        if admin_managed and not isinstance(admin_managed, bool):
            raise TypeError("Expected argument 'admin_managed' to be a bool")
        pulumi.set(__self__, "admin_managed", admin_managed)
        if domains and not isinstance(domains, list):
            raise TypeError("Expected argument 'domains' to be a list")
        pulumi.set(__self__, "domains", domains)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if include_unverified and not isinstance(include_unverified, bool):
            raise TypeError("Expected argument 'include_unverified' to be a bool")
        pulumi.set(__self__, "include_unverified", include_unverified)
        if only_default and not isinstance(only_default, bool):
            raise TypeError("Expected argument 'only_default' to be a bool")
        pulumi.set(__self__, "only_default", only_default)
        if only_initial and not isinstance(only_initial, bool):
            raise TypeError("Expected argument 'only_initial' to be a bool")
        pulumi.set(__self__, "only_initial", only_initial)
        if only_root and not isinstance(only_root, bool):
            raise TypeError("Expected argument 'only_root' to be a bool")
        pulumi.set(__self__, "only_root", only_root)
        if supports_services and not isinstance(supports_services, list):
            raise TypeError("Expected argument 'supports_services' to be a list")
        pulumi.set(__self__, "supports_services", supports_services)

    @property
    @pulumi.getter(name="adminManaged")
    def admin_managed(self) -> Optional[bool]:
        """
        Whether the DNS for the domain is managed by Microsoft 365.
        """
        return pulumi.get(self, "admin_managed")

    @property
    @pulumi.getter
    def domains(self) -> Sequence['outputs.GetDomainsDomainResult']:
        """
        A list of tenant domains. Each `domain` object provides the attributes documented below.
        """
        return pulumi.get(self, "domains")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="includeUnverified")
    def include_unverified(self) -> Optional[bool]:
        return pulumi.get(self, "include_unverified")

    @property
    @pulumi.getter(name="onlyDefault")
    def only_default(self) -> Optional[bool]:
        return pulumi.get(self, "only_default")

    @property
    @pulumi.getter(name="onlyInitial")
    def only_initial(self) -> Optional[bool]:
        return pulumi.get(self, "only_initial")

    @property
    @pulumi.getter(name="onlyRoot")
    def only_root(self) -> Optional[bool]:
        return pulumi.get(self, "only_root")

    @property
    @pulumi.getter(name="supportsServices")
    def supports_services(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "supports_services")


class AwaitableGetDomainsResult(GetDomainsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainsResult(
            admin_managed=self.admin_managed,
            domains=self.domains,
            id=self.id,
            include_unverified=self.include_unverified,
            only_default=self.only_default,
            only_initial=self.only_initial,
            only_root=self.only_root,
            supports_services=self.supports_services)


def get_domains(admin_managed: Optional[bool] = None,
                include_unverified: Optional[bool] = None,
                only_default: Optional[bool] = None,
                only_initial: Optional[bool] = None,
                only_root: Optional[bool] = None,
                supports_services: Optional[Sequence[str]] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainsResult:
    """
    Use this data source to access information about existing Domains within Azure Active Directory.

    ## API Permissions

    The following API permissions are required in order to use this data source.

    When authenticated with a service principal, this data source requires one of the following application roles: `Domain.Read.All` or `Directory.Read.All`

    When authenticated with a user principal, this data source does not require any additional roles.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azuread as azuread

    aad_domains = azuread.get_domains()
    pulumi.export("domainNames", [__item.domain_name for __item in [aad_domains.domains]])
    ```


    :param bool admin_managed: Set to `true` to only return domains whose DNS is managed by Microsoft 365. Defaults to `false`.
    :param bool include_unverified: Set to `true` if unverified Azure AD domains should be included. Defaults to `false`.
    :param bool only_default: Set to `true` to only return the default domain.
    :param bool only_initial: Set to `true` to only return the initial domain, which is your primary Azure Active Directory tenant domain. Defaults to `false`.
    :param bool only_root: Set to `true` to only return verified root domains. Excludes subdomains and unverified domains.
    :param Sequence[str] supports_services: A list of supported services that must be supported by a domain. Possible values include `Email`, `Sharepoint`, `EmailInternalRelayOnly`, `OfficeCommunicationsOnline`, `SharePointDefaultDomain`, `FullRedelegation`, `SharePointPublic`, `OrgIdAuthentication`, `Yammer` and `Intune`.
    """
    __args__ = dict()
    __args__['adminManaged'] = admin_managed
    __args__['includeUnverified'] = include_unverified
    __args__['onlyDefault'] = only_default
    __args__['onlyInitial'] = only_initial
    __args__['onlyRoot'] = only_root
    __args__['supportsServices'] = supports_services
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azuread:index/getDomains:getDomains', __args__, opts=opts, typ=GetDomainsResult).value

    return AwaitableGetDomainsResult(
        admin_managed=__ret__.admin_managed,
        domains=__ret__.domains,
        id=__ret__.id,
        include_unverified=__ret__.include_unverified,
        only_default=__ret__.only_default,
        only_initial=__ret__.only_initial,
        only_root=__ret__.only_root,
        supports_services=__ret__.supports_services)


@_utilities.lift_output_func(get_domains)
def get_domains_output(admin_managed: Optional[pulumi.Input[Optional[bool]]] = None,
                       include_unverified: Optional[pulumi.Input[Optional[bool]]] = None,
                       only_default: Optional[pulumi.Input[Optional[bool]]] = None,
                       only_initial: Optional[pulumi.Input[Optional[bool]]] = None,
                       only_root: Optional[pulumi.Input[Optional[bool]]] = None,
                       supports_services: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainsResult]:
    """
    Use this data source to access information about existing Domains within Azure Active Directory.

    ## API Permissions

    The following API permissions are required in order to use this data source.

    When authenticated with a service principal, this data source requires one of the following application roles: `Domain.Read.All` or `Directory.Read.All`

    When authenticated with a user principal, this data source does not require any additional roles.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azuread as azuread

    aad_domains = azuread.get_domains()
    pulumi.export("domainNames", [__item.domain_name for __item in [aad_domains.domains]])
    ```


    :param bool admin_managed: Set to `true` to only return domains whose DNS is managed by Microsoft 365. Defaults to `false`.
    :param bool include_unverified: Set to `true` if unverified Azure AD domains should be included. Defaults to `false`.
    :param bool only_default: Set to `true` to only return the default domain.
    :param bool only_initial: Set to `true` to only return the initial domain, which is your primary Azure Active Directory tenant domain. Defaults to `false`.
    :param bool only_root: Set to `true` to only return verified root domains. Excludes subdomains and unverified domains.
    :param Sequence[str] supports_services: A list of supported services that must be supported by a domain. Possible values include `Email`, `Sharepoint`, `EmailInternalRelayOnly`, `OfficeCommunicationsOnline`, `SharePointDefaultDomain`, `FullRedelegation`, `SharePointPublic`, `OrgIdAuthentication`, `Yammer` and `Intune`.
    """
    ...
