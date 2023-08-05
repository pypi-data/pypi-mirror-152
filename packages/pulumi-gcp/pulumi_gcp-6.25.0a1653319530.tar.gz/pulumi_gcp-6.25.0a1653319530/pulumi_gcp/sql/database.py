# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DatabaseArgs', 'Database']

@pulumi.input_type
class DatabaseArgs:
    def __init__(__self__, *,
                 instance: pulumi.Input[str],
                 charset: Optional[pulumi.Input[str]] = None,
                 collation: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Database resource.
        :param pulumi.Input[str] instance: The name of the Cloud SQL instance. This does not include the project
               ID.
        :param pulumi.Input[str] charset: The charset value. See MySQL's
               [Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
               and Postgres' [Character Set Support](https://www.postgresql.org/docs/9.6/static/multibyte.html)
               for more details and supported values. Postgres databases only support
               a value of `UTF8` at creation time.
        :param pulumi.Input[str] collation: The collation value. See MySQL's
               [Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
               and Postgres' [Collation Support](https://www.postgresql.org/docs/9.6/static/collation.html)
               for more details and supported values. Postgres databases only support
               a value of `en_US.UTF8` at creation time.
        :param pulumi.Input[str] name: The name of the database in the Cloud SQL instance.
               This does not include the project ID or instance name.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        pulumi.set(__self__, "instance", instance)
        if charset is not None:
            pulumi.set(__self__, "charset", charset)
        if collation is not None:
            pulumi.set(__self__, "collation", collation)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def instance(self) -> pulumi.Input[str]:
        """
        The name of the Cloud SQL instance. This does not include the project
        ID.
        """
        return pulumi.get(self, "instance")

    @instance.setter
    def instance(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance", value)

    @property
    @pulumi.getter
    def charset(self) -> Optional[pulumi.Input[str]]:
        """
        The charset value. See MySQL's
        [Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
        and Postgres' [Character Set Support](https://www.postgresql.org/docs/9.6/static/multibyte.html)
        for more details and supported values. Postgres databases only support
        a value of `UTF8` at creation time.
        """
        return pulumi.get(self, "charset")

    @charset.setter
    def charset(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "charset", value)

    @property
    @pulumi.getter
    def collation(self) -> Optional[pulumi.Input[str]]:
        """
        The collation value. See MySQL's
        [Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
        and Postgres' [Collation Support](https://www.postgresql.org/docs/9.6/static/collation.html)
        for more details and supported values. Postgres databases only support
        a value of `en_US.UTF8` at creation time.
        """
        return pulumi.get(self, "collation")

    @collation.setter
    def collation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "collation", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the database in the Cloud SQL instance.
        This does not include the project ID or instance name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _DatabaseState:
    def __init__(__self__, *,
                 charset: Optional[pulumi.Input[str]] = None,
                 collation: Optional[pulumi.Input[str]] = None,
                 instance: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Database resources.
        :param pulumi.Input[str] charset: The charset value. See MySQL's
               [Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
               and Postgres' [Character Set Support](https://www.postgresql.org/docs/9.6/static/multibyte.html)
               for more details and supported values. Postgres databases only support
               a value of `UTF8` at creation time.
        :param pulumi.Input[str] collation: The collation value. See MySQL's
               [Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
               and Postgres' [Collation Support](https://www.postgresql.org/docs/9.6/static/collation.html)
               for more details and supported values. Postgres databases only support
               a value of `en_US.UTF8` at creation time.
        :param pulumi.Input[str] instance: The name of the Cloud SQL instance. This does not include the project
               ID.
        :param pulumi.Input[str] name: The name of the database in the Cloud SQL instance.
               This does not include the project ID or instance name.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        """
        if charset is not None:
            pulumi.set(__self__, "charset", charset)
        if collation is not None:
            pulumi.set(__self__, "collation", collation)
        if instance is not None:
            pulumi.set(__self__, "instance", instance)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if self_link is not None:
            pulumi.set(__self__, "self_link", self_link)

    @property
    @pulumi.getter
    def charset(self) -> Optional[pulumi.Input[str]]:
        """
        The charset value. See MySQL's
        [Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
        and Postgres' [Character Set Support](https://www.postgresql.org/docs/9.6/static/multibyte.html)
        for more details and supported values. Postgres databases only support
        a value of `UTF8` at creation time.
        """
        return pulumi.get(self, "charset")

    @charset.setter
    def charset(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "charset", value)

    @property
    @pulumi.getter
    def collation(self) -> Optional[pulumi.Input[str]]:
        """
        The collation value. See MySQL's
        [Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
        and Postgres' [Collation Support](https://www.postgresql.org/docs/9.6/static/collation.html)
        for more details and supported values. Postgres databases only support
        a value of `en_US.UTF8` at creation time.
        """
        return pulumi.get(self, "collation")

    @collation.setter
    def collation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "collation", value)

    @property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Cloud SQL instance. This does not include the project
        ID.
        """
        return pulumi.get(self, "instance")

    @instance.setter
    def instance(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the database in the Cloud SQL instance.
        This does not include the project ID or instance name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[str]]:
        """
        The URI of the created resource.
        """
        return pulumi.get(self, "self_link")

    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "self_link", value)


class Database(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 charset: Optional[pulumi.Input[str]] = None,
                 collation: Optional[pulumi.Input[str]] = None,
                 instance: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a SQL database inside the Cloud SQL instance, hosted in
        Google's cloud.

        ## Example Usage
        ### Sql Database Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        # See versions at https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance#database_version
        instance = gcp.sql.DatabaseInstance("instance",
            region="us-central1",
            database_version="MYSQL_8_0",
            settings=gcp.sql.DatabaseInstanceSettingsArgs(
                tier="db-f1-micro",
            ),
            deletion_protection=True)
        database = gcp.sql.Database("database", instance=instance.name)
        ```

        ## Import

        Database can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:sql/database:Database default projects/{{project}}/instances/{{instance}}/databases/{{name}}
        ```

        ```sh
         $ pulumi import gcp:sql/database:Database default instances/{{instance}}/databases/{{name}}
        ```

        ```sh
         $ pulumi import gcp:sql/database:Database default {{project}}/{{instance}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:sql/database:Database default {{instance}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:sql/database:Database default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] charset: The charset value. See MySQL's
               [Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
               and Postgres' [Character Set Support](https://www.postgresql.org/docs/9.6/static/multibyte.html)
               for more details and supported values. Postgres databases only support
               a value of `UTF8` at creation time.
        :param pulumi.Input[str] collation: The collation value. See MySQL's
               [Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
               and Postgres' [Collation Support](https://www.postgresql.org/docs/9.6/static/collation.html)
               for more details and supported values. Postgres databases only support
               a value of `en_US.UTF8` at creation time.
        :param pulumi.Input[str] instance: The name of the Cloud SQL instance. This does not include the project
               ID.
        :param pulumi.Input[str] name: The name of the database in the Cloud SQL instance.
               This does not include the project ID or instance name.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatabaseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a SQL database inside the Cloud SQL instance, hosted in
        Google's cloud.

        ## Example Usage
        ### Sql Database Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        # See versions at https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance#database_version
        instance = gcp.sql.DatabaseInstance("instance",
            region="us-central1",
            database_version="MYSQL_8_0",
            settings=gcp.sql.DatabaseInstanceSettingsArgs(
                tier="db-f1-micro",
            ),
            deletion_protection=True)
        database = gcp.sql.Database("database", instance=instance.name)
        ```

        ## Import

        Database can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:sql/database:Database default projects/{{project}}/instances/{{instance}}/databases/{{name}}
        ```

        ```sh
         $ pulumi import gcp:sql/database:Database default instances/{{instance}}/databases/{{name}}
        ```

        ```sh
         $ pulumi import gcp:sql/database:Database default {{project}}/{{instance}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:sql/database:Database default {{instance}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:sql/database:Database default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param DatabaseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatabaseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 charset: Optional[pulumi.Input[str]] = None,
                 collation: Optional[pulumi.Input[str]] = None,
                 instance: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
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
            __props__ = DatabaseArgs.__new__(DatabaseArgs)

            __props__.__dict__["charset"] = charset
            __props__.__dict__["collation"] = collation
            if instance is None and not opts.urn:
                raise TypeError("Missing required property 'instance'")
            __props__.__dict__["instance"] = instance
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["self_link"] = None
        super(Database, __self__).__init__(
            'gcp:sql/database:Database',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            charset: Optional[pulumi.Input[str]] = None,
            collation: Optional[pulumi.Input[str]] = None,
            instance: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None) -> 'Database':
        """
        Get an existing Database resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] charset: The charset value. See MySQL's
               [Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
               and Postgres' [Character Set Support](https://www.postgresql.org/docs/9.6/static/multibyte.html)
               for more details and supported values. Postgres databases only support
               a value of `UTF8` at creation time.
        :param pulumi.Input[str] collation: The collation value. See MySQL's
               [Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
               and Postgres' [Collation Support](https://www.postgresql.org/docs/9.6/static/collation.html)
               for more details and supported values. Postgres databases only support
               a value of `en_US.UTF8` at creation time.
        :param pulumi.Input[str] instance: The name of the Cloud SQL instance. This does not include the project
               ID.
        :param pulumi.Input[str] name: The name of the database in the Cloud SQL instance.
               This does not include the project ID or instance name.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DatabaseState.__new__(_DatabaseState)

        __props__.__dict__["charset"] = charset
        __props__.__dict__["collation"] = collation
        __props__.__dict__["instance"] = instance
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["self_link"] = self_link
        return Database(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def charset(self) -> pulumi.Output[str]:
        """
        The charset value. See MySQL's
        [Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
        and Postgres' [Character Set Support](https://www.postgresql.org/docs/9.6/static/multibyte.html)
        for more details and supported values. Postgres databases only support
        a value of `UTF8` at creation time.
        """
        return pulumi.get(self, "charset")

    @property
    @pulumi.getter
    def collation(self) -> pulumi.Output[str]:
        """
        The collation value. See MySQL's
        [Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
        and Postgres' [Collation Support](https://www.postgresql.org/docs/9.6/static/collation.html)
        for more details and supported values. Postgres databases only support
        a value of `en_US.UTF8` at creation time.
        """
        return pulumi.get(self, "collation")

    @property
    @pulumi.getter
    def instance(self) -> pulumi.Output[str]:
        """
        The name of the Cloud SQL instance. This does not include the project
        ID.
        """
        return pulumi.get(self, "instance")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the database in the Cloud SQL instance.
        This does not include the project ID or instance name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The URI of the created resource.
        """
        return pulumi.get(self, "self_link")

