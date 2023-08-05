# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ServicePrincipalClaimsMappingPolicyAssignmentArgs', 'ServicePrincipalClaimsMappingPolicyAssignment']

@pulumi.input_type
class ServicePrincipalClaimsMappingPolicyAssignmentArgs:
    def __init__(__self__, *,
                 claims_mapping_policy_id: pulumi.Input[str],
                 service_principal_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a ServicePrincipalClaimsMappingPolicyAssignment resource.
        :param pulumi.Input[str] claims_mapping_policy_id: The ID of the claims mapping policy to assign.
        :param pulumi.Input[str] service_principal_id: The object ID of the service principal for the policy assignment.
        """
        pulumi.set(__self__, "claims_mapping_policy_id", claims_mapping_policy_id)
        pulumi.set(__self__, "service_principal_id", service_principal_id)

    @property
    @pulumi.getter(name="claimsMappingPolicyId")
    def claims_mapping_policy_id(self) -> pulumi.Input[str]:
        """
        The ID of the claims mapping policy to assign.
        """
        return pulumi.get(self, "claims_mapping_policy_id")

    @claims_mapping_policy_id.setter
    def claims_mapping_policy_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "claims_mapping_policy_id", value)

    @property
    @pulumi.getter(name="servicePrincipalId")
    def service_principal_id(self) -> pulumi.Input[str]:
        """
        The object ID of the service principal for the policy assignment.
        """
        return pulumi.get(self, "service_principal_id")

    @service_principal_id.setter
    def service_principal_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_principal_id", value)


@pulumi.input_type
class _ServicePrincipalClaimsMappingPolicyAssignmentState:
    def __init__(__self__, *,
                 claims_mapping_policy_id: Optional[pulumi.Input[str]] = None,
                 service_principal_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ServicePrincipalClaimsMappingPolicyAssignment resources.
        :param pulumi.Input[str] claims_mapping_policy_id: The ID of the claims mapping policy to assign.
        :param pulumi.Input[str] service_principal_id: The object ID of the service principal for the policy assignment.
        """
        if claims_mapping_policy_id is not None:
            pulumi.set(__self__, "claims_mapping_policy_id", claims_mapping_policy_id)
        if service_principal_id is not None:
            pulumi.set(__self__, "service_principal_id", service_principal_id)

    @property
    @pulumi.getter(name="claimsMappingPolicyId")
    def claims_mapping_policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the claims mapping policy to assign.
        """
        return pulumi.get(self, "claims_mapping_policy_id")

    @claims_mapping_policy_id.setter
    def claims_mapping_policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "claims_mapping_policy_id", value)

    @property
    @pulumi.getter(name="servicePrincipalId")
    def service_principal_id(self) -> Optional[pulumi.Input[str]]:
        """
        The object ID of the service principal for the policy assignment.
        """
        return pulumi.get(self, "service_principal_id")

    @service_principal_id.setter
    def service_principal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_principal_id", value)


class ServicePrincipalClaimsMappingPolicyAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 claims_mapping_policy_id: Optional[pulumi.Input[str]] = None,
                 service_principal_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Claims Mapping Policy Assignment within Azure Active Directory.

        ## API Permissions

        The following API permissions are required in order to use this resource.

        When authenticated with a service principal, this resource requires the following application roles: `Policy.ReadWrite.ApplicationConfiguration`

        When authenticated with a user principal, this resource requires one of the following directory roles: `Application Administrator` or `Global Administrator`

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuread as azuread

        app = azuread.ServicePrincipalClaimsMappingPolicyAssignment("app",
            claims_mapping_policy_id=azuread_claims_mapping_policy["my_policy"]["id"],
            service_principal_id=azuread_service_principal["my_principal"]["id"])
        ```

        ## Import

        Claims Mapping Policy can be imported using the `id`, in the form `service-principal-uuid/claimsMappingPolicy/claims-mapping-policy-uuid`, e.g

        ```sh
         $ pulumi import azuread:index/servicePrincipalClaimsMappingPolicyAssignment:ServicePrincipalClaimsMappingPolicyAssignment app 00000000-0000-0000-0000-000000000000/claimsMappingPolicy/11111111-0000-0000-0000-000000000000
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] claims_mapping_policy_id: The ID of the claims mapping policy to assign.
        :param pulumi.Input[str] service_principal_id: The object ID of the service principal for the policy assignment.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServicePrincipalClaimsMappingPolicyAssignmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Claims Mapping Policy Assignment within Azure Active Directory.

        ## API Permissions

        The following API permissions are required in order to use this resource.

        When authenticated with a service principal, this resource requires the following application roles: `Policy.ReadWrite.ApplicationConfiguration`

        When authenticated with a user principal, this resource requires one of the following directory roles: `Application Administrator` or `Global Administrator`

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azuread as azuread

        app = azuread.ServicePrincipalClaimsMappingPolicyAssignment("app",
            claims_mapping_policy_id=azuread_claims_mapping_policy["my_policy"]["id"],
            service_principal_id=azuread_service_principal["my_principal"]["id"])
        ```

        ## Import

        Claims Mapping Policy can be imported using the `id`, in the form `service-principal-uuid/claimsMappingPolicy/claims-mapping-policy-uuid`, e.g

        ```sh
         $ pulumi import azuread:index/servicePrincipalClaimsMappingPolicyAssignment:ServicePrincipalClaimsMappingPolicyAssignment app 00000000-0000-0000-0000-000000000000/claimsMappingPolicy/11111111-0000-0000-0000-000000000000
        ```

        :param str resource_name: The name of the resource.
        :param ServicePrincipalClaimsMappingPolicyAssignmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServicePrincipalClaimsMappingPolicyAssignmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 claims_mapping_policy_id: Optional[pulumi.Input[str]] = None,
                 service_principal_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = ServicePrincipalClaimsMappingPolicyAssignmentArgs.__new__(ServicePrincipalClaimsMappingPolicyAssignmentArgs)

            if claims_mapping_policy_id is None and not opts.urn:
                raise TypeError("Missing required property 'claims_mapping_policy_id'")
            __props__.__dict__["claims_mapping_policy_id"] = claims_mapping_policy_id
            if service_principal_id is None and not opts.urn:
                raise TypeError("Missing required property 'service_principal_id'")
            __props__.__dict__["service_principal_id"] = service_principal_id
        super(ServicePrincipalClaimsMappingPolicyAssignment, __self__).__init__(
            'azuread:index/servicePrincipalClaimsMappingPolicyAssignment:ServicePrincipalClaimsMappingPolicyAssignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            claims_mapping_policy_id: Optional[pulumi.Input[str]] = None,
            service_principal_id: Optional[pulumi.Input[str]] = None) -> 'ServicePrincipalClaimsMappingPolicyAssignment':
        """
        Get an existing ServicePrincipalClaimsMappingPolicyAssignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] claims_mapping_policy_id: The ID of the claims mapping policy to assign.
        :param pulumi.Input[str] service_principal_id: The object ID of the service principal for the policy assignment.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServicePrincipalClaimsMappingPolicyAssignmentState.__new__(_ServicePrincipalClaimsMappingPolicyAssignmentState)

        __props__.__dict__["claims_mapping_policy_id"] = claims_mapping_policy_id
        __props__.__dict__["service_principal_id"] = service_principal_id
        return ServicePrincipalClaimsMappingPolicyAssignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="claimsMappingPolicyId")
    def claims_mapping_policy_id(self) -> pulumi.Output[str]:
        """
        The ID of the claims mapping policy to assign.
        """
        return pulumi.get(self, "claims_mapping_policy_id")

    @property
    @pulumi.getter(name="servicePrincipalId")
    def service_principal_id(self) -> pulumi.Output[str]:
        """
        The object ID of the service principal for the policy assignment.
        """
        return pulumi.get(self, "service_principal_id")

