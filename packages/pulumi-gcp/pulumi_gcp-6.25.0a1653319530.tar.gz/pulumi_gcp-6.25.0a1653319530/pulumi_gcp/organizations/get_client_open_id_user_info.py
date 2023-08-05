# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetClientOpenIdUserInfoResult',
    'AwaitableGetClientOpenIdUserInfoResult',
    'get_client_open_id_user_info',
]

@pulumi.output_type
class GetClientOpenIdUserInfoResult:
    """
    A collection of values returned by getClientOpenIdUserInfo.
    """
    def __init__(__self__, email=None, id=None):
        if email and not isinstance(email, str):
            raise TypeError("Expected argument 'email' to be a str")
        pulumi.set(__self__, "email", email)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        The email of the account used by the provider to authenticate with GCP.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetClientOpenIdUserInfoResult(GetClientOpenIdUserInfoResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClientOpenIdUserInfoResult(
            email=self.email,
            id=self.id)


def get_client_open_id_user_info(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClientOpenIdUserInfoResult:
    """
    Get OpenID userinfo about the credentials used with the Google provider,
    specifically the email.

    This datasource enables you to export the email of the account you've
    authenticated the provider with; this can be used alongside
    `data.google_client_config`'s `access_token` to perform OpenID Connect
    authentication with GKE and configure an RBAC role for the email used.

    > This resource will only work as expected if the provider is configured to
    use the `https://www.googleapis.com/auth/userinfo.email` scope! You will
    receive an error otherwise. The provider uses this scope by default.

    ## Example Usage
    ### Exporting An Email

    ```python
    import pulumi
    import pulumi_gcp as gcp

    me = gcp.organizations.get_client_open_id_user_info()
    pulumi.export("my-email", me.email)
    ```
    """
    __args__ = dict()
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('gcp:organizations/getClientOpenIdUserInfo:getClientOpenIdUserInfo', __args__, opts=opts, typ=GetClientOpenIdUserInfoResult).value

    return AwaitableGetClientOpenIdUserInfoResult(
        email=__ret__.email,
        id=__ret__.id)
