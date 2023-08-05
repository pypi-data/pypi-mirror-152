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

__all__ = ['AccessApprovalSettingsArgs', 'AccessApprovalSettings']

@pulumi.input_type
class AccessApprovalSettingsArgs:
    def __init__(__self__, *,
                 enrolled_services: pulumi.Input[Sequence[pulumi.Input['AccessApprovalSettingsEnrolledServiceArgs']]],
                 folder_id: pulumi.Input[str],
                 active_key_version: Optional[pulumi.Input[str]] = None,
                 notification_emails: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AccessApprovalSettings resource.
        :param pulumi.Input[Sequence[pulumi.Input['AccessApprovalSettingsEnrolledServiceArgs']]] enrolled_services: A list of Google Cloud Services for which the given resource has Access Approval enrolled.
               Access requests for the resource given by name against any of these services contained here will be required
               to have explicit approval. Enrollment can only be done on an all or nothing basis.
               A maximum of 10 enrolled services will be enforced, to be expanded as the set of supported services is expanded.
               Structure is documented below.
        :param pulumi.Input[str] folder_id: ID of the folder of the access approval settings.
        :param pulumi.Input[str] active_key_version: The asymmetric crypto key version to use for signing approval requests.
               Empty active_key_version indicates that a Google-managed key should be used for signing.
               This property will be ignored if set by an ancestor of the resource, and new non-empty values may not be set.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] notification_emails: A list of email addresses to which notifications relating to approval requests should be sent.
               Notifications relating to a resource will be sent to all emails in the settings of ancestor
               resources of that resource. A maximum of 50 email addresses are allowed.
        """
        pulumi.set(__self__, "enrolled_services", enrolled_services)
        pulumi.set(__self__, "folder_id", folder_id)
        if active_key_version is not None:
            pulumi.set(__self__, "active_key_version", active_key_version)
        if notification_emails is not None:
            pulumi.set(__self__, "notification_emails", notification_emails)

    @property
    @pulumi.getter(name="enrolledServices")
    def enrolled_services(self) -> pulumi.Input[Sequence[pulumi.Input['AccessApprovalSettingsEnrolledServiceArgs']]]:
        """
        A list of Google Cloud Services for which the given resource has Access Approval enrolled.
        Access requests for the resource given by name against any of these services contained here will be required
        to have explicit approval. Enrollment can only be done on an all or nothing basis.
        A maximum of 10 enrolled services will be enforced, to be expanded as the set of supported services is expanded.
        Structure is documented below.
        """
        return pulumi.get(self, "enrolled_services")

    @enrolled_services.setter
    def enrolled_services(self, value: pulumi.Input[Sequence[pulumi.Input['AccessApprovalSettingsEnrolledServiceArgs']]]):
        pulumi.set(self, "enrolled_services", value)

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> pulumi.Input[str]:
        """
        ID of the folder of the access approval settings.
        """
        return pulumi.get(self, "folder_id")

    @folder_id.setter
    def folder_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "folder_id", value)

    @property
    @pulumi.getter(name="activeKeyVersion")
    def active_key_version(self) -> Optional[pulumi.Input[str]]:
        """
        The asymmetric crypto key version to use for signing approval requests.
        Empty active_key_version indicates that a Google-managed key should be used for signing.
        This property will be ignored if set by an ancestor of the resource, and new non-empty values may not be set.
        """
        return pulumi.get(self, "active_key_version")

    @active_key_version.setter
    def active_key_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "active_key_version", value)

    @property
    @pulumi.getter(name="notificationEmails")
    def notification_emails(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of email addresses to which notifications relating to approval requests should be sent.
        Notifications relating to a resource will be sent to all emails in the settings of ancestor
        resources of that resource. A maximum of 50 email addresses are allowed.
        """
        return pulumi.get(self, "notification_emails")

    @notification_emails.setter
    def notification_emails(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "notification_emails", value)


@pulumi.input_type
class _AccessApprovalSettingsState:
    def __init__(__self__, *,
                 active_key_version: Optional[pulumi.Input[str]] = None,
                 ancestor_has_active_key_version: Optional[pulumi.Input[bool]] = None,
                 enrolled_ancestor: Optional[pulumi.Input[bool]] = None,
                 enrolled_services: Optional[pulumi.Input[Sequence[pulumi.Input['AccessApprovalSettingsEnrolledServiceArgs']]]] = None,
                 folder_id: Optional[pulumi.Input[str]] = None,
                 invalid_key_version: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_emails: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering AccessApprovalSettings resources.
        :param pulumi.Input[str] active_key_version: The asymmetric crypto key version to use for signing approval requests.
               Empty active_key_version indicates that a Google-managed key should be used for signing.
               This property will be ignored if set by an ancestor of the resource, and new non-empty values may not be set.
        :param pulumi.Input[bool] ancestor_has_active_key_version: If the field is true, that indicates that an ancestor of this Folder has set active_key_version.
        :param pulumi.Input[bool] enrolled_ancestor: If the field is true, that indicates that at least one service is enrolled for Access Approval in one or more ancestors
               of the Folder.
        :param pulumi.Input[Sequence[pulumi.Input['AccessApprovalSettingsEnrolledServiceArgs']]] enrolled_services: A list of Google Cloud Services for which the given resource has Access Approval enrolled.
               Access requests for the resource given by name against any of these services contained here will be required
               to have explicit approval. Enrollment can only be done on an all or nothing basis.
               A maximum of 10 enrolled services will be enforced, to be expanded as the set of supported services is expanded.
               Structure is documented below.
        :param pulumi.Input[str] folder_id: ID of the folder of the access approval settings.
        :param pulumi.Input[bool] invalid_key_version: If the field is true, that indicates that there is some configuration issue with the active_key_version configured on
               this Folder (e.g. it doesn't exist or the Access Approval service account doesn't have the correct permissions on it,
               etc.) This key version is not necessarily the effective key version at this level, as key versions are inherited
               top-down.
        :param pulumi.Input[str] name: The resource name of the settings. Format is "folders/{folder_id}/accessApprovalSettings"
        :param pulumi.Input[Sequence[pulumi.Input[str]]] notification_emails: A list of email addresses to which notifications relating to approval requests should be sent.
               Notifications relating to a resource will be sent to all emails in the settings of ancestor
               resources of that resource. A maximum of 50 email addresses are allowed.
        """
        if active_key_version is not None:
            pulumi.set(__self__, "active_key_version", active_key_version)
        if ancestor_has_active_key_version is not None:
            pulumi.set(__self__, "ancestor_has_active_key_version", ancestor_has_active_key_version)
        if enrolled_ancestor is not None:
            pulumi.set(__self__, "enrolled_ancestor", enrolled_ancestor)
        if enrolled_services is not None:
            pulumi.set(__self__, "enrolled_services", enrolled_services)
        if folder_id is not None:
            pulumi.set(__self__, "folder_id", folder_id)
        if invalid_key_version is not None:
            pulumi.set(__self__, "invalid_key_version", invalid_key_version)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notification_emails is not None:
            pulumi.set(__self__, "notification_emails", notification_emails)

    @property
    @pulumi.getter(name="activeKeyVersion")
    def active_key_version(self) -> Optional[pulumi.Input[str]]:
        """
        The asymmetric crypto key version to use for signing approval requests.
        Empty active_key_version indicates that a Google-managed key should be used for signing.
        This property will be ignored if set by an ancestor of the resource, and new non-empty values may not be set.
        """
        return pulumi.get(self, "active_key_version")

    @active_key_version.setter
    def active_key_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "active_key_version", value)

    @property
    @pulumi.getter(name="ancestorHasActiveKeyVersion")
    def ancestor_has_active_key_version(self) -> Optional[pulumi.Input[bool]]:
        """
        If the field is true, that indicates that an ancestor of this Folder has set active_key_version.
        """
        return pulumi.get(self, "ancestor_has_active_key_version")

    @ancestor_has_active_key_version.setter
    def ancestor_has_active_key_version(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ancestor_has_active_key_version", value)

    @property
    @pulumi.getter(name="enrolledAncestor")
    def enrolled_ancestor(self) -> Optional[pulumi.Input[bool]]:
        """
        If the field is true, that indicates that at least one service is enrolled for Access Approval in one or more ancestors
        of the Folder.
        """
        return pulumi.get(self, "enrolled_ancestor")

    @enrolled_ancestor.setter
    def enrolled_ancestor(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enrolled_ancestor", value)

    @property
    @pulumi.getter(name="enrolledServices")
    def enrolled_services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AccessApprovalSettingsEnrolledServiceArgs']]]]:
        """
        A list of Google Cloud Services for which the given resource has Access Approval enrolled.
        Access requests for the resource given by name against any of these services contained here will be required
        to have explicit approval. Enrollment can only be done on an all or nothing basis.
        A maximum of 10 enrolled services will be enforced, to be expanded as the set of supported services is expanded.
        Structure is documented below.
        """
        return pulumi.get(self, "enrolled_services")

    @enrolled_services.setter
    def enrolled_services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AccessApprovalSettingsEnrolledServiceArgs']]]]):
        pulumi.set(self, "enrolled_services", value)

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the folder of the access approval settings.
        """
        return pulumi.get(self, "folder_id")

    @folder_id.setter
    def folder_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder_id", value)

    @property
    @pulumi.getter(name="invalidKeyVersion")
    def invalid_key_version(self) -> Optional[pulumi.Input[bool]]:
        """
        If the field is true, that indicates that there is some configuration issue with the active_key_version configured on
        this Folder (e.g. it doesn't exist or the Access Approval service account doesn't have the correct permissions on it,
        etc.) This key version is not necessarily the effective key version at this level, as key versions are inherited
        top-down.
        """
        return pulumi.get(self, "invalid_key_version")

    @invalid_key_version.setter
    def invalid_key_version(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "invalid_key_version", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the settings. Format is "folders/{folder_id}/accessApprovalSettings"
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="notificationEmails")
    def notification_emails(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of email addresses to which notifications relating to approval requests should be sent.
        Notifications relating to a resource will be sent to all emails in the settings of ancestor
        resources of that resource. A maximum of 50 email addresses are allowed.
        """
        return pulumi.get(self, "notification_emails")

    @notification_emails.setter
    def notification_emails(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "notification_emails", value)


class AccessApprovalSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active_key_version: Optional[pulumi.Input[str]] = None,
                 enrolled_services: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessApprovalSettingsEnrolledServiceArgs']]]]] = None,
                 folder_id: Optional[pulumi.Input[str]] = None,
                 notification_emails: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Access Approval enables you to require your explicit approval whenever Google support and engineering need to access your customer content.

        To get more information about FolderSettings, see:

        * [API documentation](https://cloud.google.com/access-approval/docs/reference/rest/v1/folders)

        ## Example Usage
        ### Folder Access Approval Full

        ```python
        import pulumi
        import pulumi_gcp as gcp

        my_folder = gcp.organizations.Folder("myFolder",
            display_name="my-folder",
            parent="organizations/123456789")
        folder_access_approval = gcp.folder.AccessApprovalSettings("folderAccessApproval",
            folder_id=my_folder.folder_id,
            notification_emails=[
                "testuser@example.com",
                "example.user@example.com",
            ],
            enrolled_services=[gcp.folder.AccessApprovalSettingsEnrolledServiceArgs(
                cloud_product="all",
            )])
        ```
        ### Folder Access Approval Active Key Version

        ```python
        import pulumi
        import pulumi_gcp as gcp

        my_folder = gcp.organizations.Folder("myFolder",
            display_name="my-folder",
            parent="organizations/123456789")
        my_project = gcp.organizations.Project("myProject",
            project_id="your-project-id",
            folder_id=my_folder.name)
        key_ring = gcp.kms.KeyRing("keyRing",
            location="global",
            project=my_project.project_id)
        crypto_key = gcp.kms.CryptoKey("cryptoKey",
            key_ring=key_ring.id,
            purpose="ASYMMETRIC_SIGN",
            version_template=gcp.kms.CryptoKeyVersionTemplateArgs(
                algorithm="EC_SIGN_P384_SHA384",
            ))
        service_account = gcp.accessapproval.get_folder_service_account_output(folder_id=my_folder.folder_id)
        iam = gcp.kms.CryptoKeyIAMMember("iam",
            crypto_key_id=crypto_key.id,
            role="roles/cloudkms.signerVerifier",
            member=service_account.apply(lambda service_account: f"serviceAccount:{service_account.account_email}"))
        crypto_key_version = gcp.kms.get_kms_crypto_key_version_output(crypto_key=crypto_key.id)
        folder_access_approval = gcp.folder.AccessApprovalSettings("folderAccessApproval",
            folder_id=my_folder.folder_id,
            active_key_version=crypto_key_version.name,
            enrolled_services=[gcp.folder.AccessApprovalSettingsEnrolledServiceArgs(
                cloud_product="all",
            )],
            opts=pulumi.ResourceOptions(depends_on=[iam]))
        ```

        ## Import

        FolderSettings can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:folder/accessApprovalSettings:AccessApprovalSettings default folders/{{folder_id}}/accessApprovalSettings
        ```

        ```sh
         $ pulumi import gcp:folder/accessApprovalSettings:AccessApprovalSettings default {{folder_id}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] active_key_version: The asymmetric crypto key version to use for signing approval requests.
               Empty active_key_version indicates that a Google-managed key should be used for signing.
               This property will be ignored if set by an ancestor of the resource, and new non-empty values may not be set.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessApprovalSettingsEnrolledServiceArgs']]]] enrolled_services: A list of Google Cloud Services for which the given resource has Access Approval enrolled.
               Access requests for the resource given by name against any of these services contained here will be required
               to have explicit approval. Enrollment can only be done on an all or nothing basis.
               A maximum of 10 enrolled services will be enforced, to be expanded as the set of supported services is expanded.
               Structure is documented below.
        :param pulumi.Input[str] folder_id: ID of the folder of the access approval settings.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] notification_emails: A list of email addresses to which notifications relating to approval requests should be sent.
               Notifications relating to a resource will be sent to all emails in the settings of ancestor
               resources of that resource. A maximum of 50 email addresses are allowed.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessApprovalSettingsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Access Approval enables you to require your explicit approval whenever Google support and engineering need to access your customer content.

        To get more information about FolderSettings, see:

        * [API documentation](https://cloud.google.com/access-approval/docs/reference/rest/v1/folders)

        ## Example Usage
        ### Folder Access Approval Full

        ```python
        import pulumi
        import pulumi_gcp as gcp

        my_folder = gcp.organizations.Folder("myFolder",
            display_name="my-folder",
            parent="organizations/123456789")
        folder_access_approval = gcp.folder.AccessApprovalSettings("folderAccessApproval",
            folder_id=my_folder.folder_id,
            notification_emails=[
                "testuser@example.com",
                "example.user@example.com",
            ],
            enrolled_services=[gcp.folder.AccessApprovalSettingsEnrolledServiceArgs(
                cloud_product="all",
            )])
        ```
        ### Folder Access Approval Active Key Version

        ```python
        import pulumi
        import pulumi_gcp as gcp

        my_folder = gcp.organizations.Folder("myFolder",
            display_name="my-folder",
            parent="organizations/123456789")
        my_project = gcp.organizations.Project("myProject",
            project_id="your-project-id",
            folder_id=my_folder.name)
        key_ring = gcp.kms.KeyRing("keyRing",
            location="global",
            project=my_project.project_id)
        crypto_key = gcp.kms.CryptoKey("cryptoKey",
            key_ring=key_ring.id,
            purpose="ASYMMETRIC_SIGN",
            version_template=gcp.kms.CryptoKeyVersionTemplateArgs(
                algorithm="EC_SIGN_P384_SHA384",
            ))
        service_account = gcp.accessapproval.get_folder_service_account_output(folder_id=my_folder.folder_id)
        iam = gcp.kms.CryptoKeyIAMMember("iam",
            crypto_key_id=crypto_key.id,
            role="roles/cloudkms.signerVerifier",
            member=service_account.apply(lambda service_account: f"serviceAccount:{service_account.account_email}"))
        crypto_key_version = gcp.kms.get_kms_crypto_key_version_output(crypto_key=crypto_key.id)
        folder_access_approval = gcp.folder.AccessApprovalSettings("folderAccessApproval",
            folder_id=my_folder.folder_id,
            active_key_version=crypto_key_version.name,
            enrolled_services=[gcp.folder.AccessApprovalSettingsEnrolledServiceArgs(
                cloud_product="all",
            )],
            opts=pulumi.ResourceOptions(depends_on=[iam]))
        ```

        ## Import

        FolderSettings can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:folder/accessApprovalSettings:AccessApprovalSettings default folders/{{folder_id}}/accessApprovalSettings
        ```

        ```sh
         $ pulumi import gcp:folder/accessApprovalSettings:AccessApprovalSettings default {{folder_id}}
        ```

        :param str resource_name: The name of the resource.
        :param AccessApprovalSettingsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessApprovalSettingsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active_key_version: Optional[pulumi.Input[str]] = None,
                 enrolled_services: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessApprovalSettingsEnrolledServiceArgs']]]]] = None,
                 folder_id: Optional[pulumi.Input[str]] = None,
                 notification_emails: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = AccessApprovalSettingsArgs.__new__(AccessApprovalSettingsArgs)

            __props__.__dict__["active_key_version"] = active_key_version
            if enrolled_services is None and not opts.urn:
                raise TypeError("Missing required property 'enrolled_services'")
            __props__.__dict__["enrolled_services"] = enrolled_services
            if folder_id is None and not opts.urn:
                raise TypeError("Missing required property 'folder_id'")
            __props__.__dict__["folder_id"] = folder_id
            __props__.__dict__["notification_emails"] = notification_emails
            __props__.__dict__["ancestor_has_active_key_version"] = None
            __props__.__dict__["enrolled_ancestor"] = None
            __props__.__dict__["invalid_key_version"] = None
            __props__.__dict__["name"] = None
        super(AccessApprovalSettings, __self__).__init__(
            'gcp:folder/accessApprovalSettings:AccessApprovalSettings',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            active_key_version: Optional[pulumi.Input[str]] = None,
            ancestor_has_active_key_version: Optional[pulumi.Input[bool]] = None,
            enrolled_ancestor: Optional[pulumi.Input[bool]] = None,
            enrolled_services: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessApprovalSettingsEnrolledServiceArgs']]]]] = None,
            folder_id: Optional[pulumi.Input[str]] = None,
            invalid_key_version: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            notification_emails: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'AccessApprovalSettings':
        """
        Get an existing AccessApprovalSettings resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] active_key_version: The asymmetric crypto key version to use for signing approval requests.
               Empty active_key_version indicates that a Google-managed key should be used for signing.
               This property will be ignored if set by an ancestor of the resource, and new non-empty values may not be set.
        :param pulumi.Input[bool] ancestor_has_active_key_version: If the field is true, that indicates that an ancestor of this Folder has set active_key_version.
        :param pulumi.Input[bool] enrolled_ancestor: If the field is true, that indicates that at least one service is enrolled for Access Approval in one or more ancestors
               of the Folder.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessApprovalSettingsEnrolledServiceArgs']]]] enrolled_services: A list of Google Cloud Services for which the given resource has Access Approval enrolled.
               Access requests for the resource given by name against any of these services contained here will be required
               to have explicit approval. Enrollment can only be done on an all or nothing basis.
               A maximum of 10 enrolled services will be enforced, to be expanded as the set of supported services is expanded.
               Structure is documented below.
        :param pulumi.Input[str] folder_id: ID of the folder of the access approval settings.
        :param pulumi.Input[bool] invalid_key_version: If the field is true, that indicates that there is some configuration issue with the active_key_version configured on
               this Folder (e.g. it doesn't exist or the Access Approval service account doesn't have the correct permissions on it,
               etc.) This key version is not necessarily the effective key version at this level, as key versions are inherited
               top-down.
        :param pulumi.Input[str] name: The resource name of the settings. Format is "folders/{folder_id}/accessApprovalSettings"
        :param pulumi.Input[Sequence[pulumi.Input[str]]] notification_emails: A list of email addresses to which notifications relating to approval requests should be sent.
               Notifications relating to a resource will be sent to all emails in the settings of ancestor
               resources of that resource. A maximum of 50 email addresses are allowed.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccessApprovalSettingsState.__new__(_AccessApprovalSettingsState)

        __props__.__dict__["active_key_version"] = active_key_version
        __props__.__dict__["ancestor_has_active_key_version"] = ancestor_has_active_key_version
        __props__.__dict__["enrolled_ancestor"] = enrolled_ancestor
        __props__.__dict__["enrolled_services"] = enrolled_services
        __props__.__dict__["folder_id"] = folder_id
        __props__.__dict__["invalid_key_version"] = invalid_key_version
        __props__.__dict__["name"] = name
        __props__.__dict__["notification_emails"] = notification_emails
        return AccessApprovalSettings(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="activeKeyVersion")
    def active_key_version(self) -> pulumi.Output[Optional[str]]:
        """
        The asymmetric crypto key version to use for signing approval requests.
        Empty active_key_version indicates that a Google-managed key should be used for signing.
        This property will be ignored if set by an ancestor of the resource, and new non-empty values may not be set.
        """
        return pulumi.get(self, "active_key_version")

    @property
    @pulumi.getter(name="ancestorHasActiveKeyVersion")
    def ancestor_has_active_key_version(self) -> pulumi.Output[bool]:
        """
        If the field is true, that indicates that an ancestor of this Folder has set active_key_version.
        """
        return pulumi.get(self, "ancestor_has_active_key_version")

    @property
    @pulumi.getter(name="enrolledAncestor")
    def enrolled_ancestor(self) -> pulumi.Output[bool]:
        """
        If the field is true, that indicates that at least one service is enrolled for Access Approval in one or more ancestors
        of the Folder.
        """
        return pulumi.get(self, "enrolled_ancestor")

    @property
    @pulumi.getter(name="enrolledServices")
    def enrolled_services(self) -> pulumi.Output[Sequence['outputs.AccessApprovalSettingsEnrolledService']]:
        """
        A list of Google Cloud Services for which the given resource has Access Approval enrolled.
        Access requests for the resource given by name against any of these services contained here will be required
        to have explicit approval. Enrollment can only be done on an all or nothing basis.
        A maximum of 10 enrolled services will be enforced, to be expanded as the set of supported services is expanded.
        Structure is documented below.
        """
        return pulumi.get(self, "enrolled_services")

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> pulumi.Output[str]:
        """
        ID of the folder of the access approval settings.
        """
        return pulumi.get(self, "folder_id")

    @property
    @pulumi.getter(name="invalidKeyVersion")
    def invalid_key_version(self) -> pulumi.Output[bool]:
        """
        If the field is true, that indicates that there is some configuration issue with the active_key_version configured on
        this Folder (e.g. it doesn't exist or the Access Approval service account doesn't have the correct permissions on it,
        etc.) This key version is not necessarily the effective key version at this level, as key versions are inherited
        top-down.
        """
        return pulumi.get(self, "invalid_key_version")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the settings. Format is "folders/{folder_id}/accessApprovalSettings"
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationEmails")
    def notification_emails(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of email addresses to which notifications relating to approval requests should be sent.
        Notifications relating to a resource will be sent to all emails in the settings of ancestor
        resources of that resource. A maximum of 50 email addresses are allowed.
        """
        return pulumi.get(self, "notification_emails")

