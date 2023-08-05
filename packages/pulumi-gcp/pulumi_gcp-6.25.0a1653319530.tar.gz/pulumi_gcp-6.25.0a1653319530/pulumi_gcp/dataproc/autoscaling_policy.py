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

__all__ = ['AutoscalingPolicyArgs', 'AutoscalingPolicy']

@pulumi.input_type
class AutoscalingPolicyArgs:
    def __init__(__self__, *,
                 policy_id: pulumi.Input[str],
                 basic_algorithm: Optional[pulumi.Input['AutoscalingPolicyBasicAlgorithmArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 secondary_worker_config: Optional[pulumi.Input['AutoscalingPolicySecondaryWorkerConfigArgs']] = None,
                 worker_config: Optional[pulumi.Input['AutoscalingPolicyWorkerConfigArgs']] = None):
        """
        The set of arguments for constructing a AutoscalingPolicy resource.
        :param pulumi.Input[str] policy_id: The policy id. The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_),
               and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between
               3 and 50 characters.
        :param pulumi.Input['AutoscalingPolicyBasicAlgorithmArgs'] basic_algorithm: Basic algorithm for autoscaling.
               Structure is documented below.
        :param pulumi.Input[str] location: The  location where the autoscaling policy should reside.
               The default value is `global`.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input['AutoscalingPolicySecondaryWorkerConfigArgs'] secondary_worker_config: Describes how the autoscaler will operate for secondary workers.
               Structure is documented below.
        :param pulumi.Input['AutoscalingPolicyWorkerConfigArgs'] worker_config: Describes how the autoscaler will operate for primary workers.
               Structure is documented below.
        """
        pulumi.set(__self__, "policy_id", policy_id)
        if basic_algorithm is not None:
            pulumi.set(__self__, "basic_algorithm", basic_algorithm)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if secondary_worker_config is not None:
            pulumi.set(__self__, "secondary_worker_config", secondary_worker_config)
        if worker_config is not None:
            pulumi.set(__self__, "worker_config", worker_config)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Input[str]:
        """
        The policy id. The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_),
        and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between
        3 and 50 characters.
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_id", value)

    @property
    @pulumi.getter(name="basicAlgorithm")
    def basic_algorithm(self) -> Optional[pulumi.Input['AutoscalingPolicyBasicAlgorithmArgs']]:
        """
        Basic algorithm for autoscaling.
        Structure is documented below.
        """
        return pulumi.get(self, "basic_algorithm")

    @basic_algorithm.setter
    def basic_algorithm(self, value: Optional[pulumi.Input['AutoscalingPolicyBasicAlgorithmArgs']]):
        pulumi.set(self, "basic_algorithm", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The  location where the autoscaling policy should reside.
        The default value is `global`.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

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
    @pulumi.getter(name="secondaryWorkerConfig")
    def secondary_worker_config(self) -> Optional[pulumi.Input['AutoscalingPolicySecondaryWorkerConfigArgs']]:
        """
        Describes how the autoscaler will operate for secondary workers.
        Structure is documented below.
        """
        return pulumi.get(self, "secondary_worker_config")

    @secondary_worker_config.setter
    def secondary_worker_config(self, value: Optional[pulumi.Input['AutoscalingPolicySecondaryWorkerConfigArgs']]):
        pulumi.set(self, "secondary_worker_config", value)

    @property
    @pulumi.getter(name="workerConfig")
    def worker_config(self) -> Optional[pulumi.Input['AutoscalingPolicyWorkerConfigArgs']]:
        """
        Describes how the autoscaler will operate for primary workers.
        Structure is documented below.
        """
        return pulumi.get(self, "worker_config")

    @worker_config.setter
    def worker_config(self, value: Optional[pulumi.Input['AutoscalingPolicyWorkerConfigArgs']]):
        pulumi.set(self, "worker_config", value)


@pulumi.input_type
class _AutoscalingPolicyState:
    def __init__(__self__, *,
                 basic_algorithm: Optional[pulumi.Input['AutoscalingPolicyBasicAlgorithmArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 secondary_worker_config: Optional[pulumi.Input['AutoscalingPolicySecondaryWorkerConfigArgs']] = None,
                 worker_config: Optional[pulumi.Input['AutoscalingPolicyWorkerConfigArgs']] = None):
        """
        Input properties used for looking up and filtering AutoscalingPolicy resources.
        :param pulumi.Input['AutoscalingPolicyBasicAlgorithmArgs'] basic_algorithm: Basic algorithm for autoscaling.
               Structure is documented below.
        :param pulumi.Input[str] location: The  location where the autoscaling policy should reside.
               The default value is `global`.
        :param pulumi.Input[str] name: The "resource name" of the autoscaling policy.
        :param pulumi.Input[str] policy_id: The policy id. The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_),
               and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between
               3 and 50 characters.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input['AutoscalingPolicySecondaryWorkerConfigArgs'] secondary_worker_config: Describes how the autoscaler will operate for secondary workers.
               Structure is documented below.
        :param pulumi.Input['AutoscalingPolicyWorkerConfigArgs'] worker_config: Describes how the autoscaler will operate for primary workers.
               Structure is documented below.
        """
        if basic_algorithm is not None:
            pulumi.set(__self__, "basic_algorithm", basic_algorithm)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if policy_id is not None:
            pulumi.set(__self__, "policy_id", policy_id)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if secondary_worker_config is not None:
            pulumi.set(__self__, "secondary_worker_config", secondary_worker_config)
        if worker_config is not None:
            pulumi.set(__self__, "worker_config", worker_config)

    @property
    @pulumi.getter(name="basicAlgorithm")
    def basic_algorithm(self) -> Optional[pulumi.Input['AutoscalingPolicyBasicAlgorithmArgs']]:
        """
        Basic algorithm for autoscaling.
        Structure is documented below.
        """
        return pulumi.get(self, "basic_algorithm")

    @basic_algorithm.setter
    def basic_algorithm(self, value: Optional[pulumi.Input['AutoscalingPolicyBasicAlgorithmArgs']]):
        pulumi.set(self, "basic_algorithm", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The  location where the autoscaling policy should reside.
        The default value is `global`.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The "resource name" of the autoscaling policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        The policy id. The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_),
        and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between
        3 and 50 characters.
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_id", value)

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
    @pulumi.getter(name="secondaryWorkerConfig")
    def secondary_worker_config(self) -> Optional[pulumi.Input['AutoscalingPolicySecondaryWorkerConfigArgs']]:
        """
        Describes how the autoscaler will operate for secondary workers.
        Structure is documented below.
        """
        return pulumi.get(self, "secondary_worker_config")

    @secondary_worker_config.setter
    def secondary_worker_config(self, value: Optional[pulumi.Input['AutoscalingPolicySecondaryWorkerConfigArgs']]):
        pulumi.set(self, "secondary_worker_config", value)

    @property
    @pulumi.getter(name="workerConfig")
    def worker_config(self) -> Optional[pulumi.Input['AutoscalingPolicyWorkerConfigArgs']]:
        """
        Describes how the autoscaler will operate for primary workers.
        Structure is documented below.
        """
        return pulumi.get(self, "worker_config")

    @worker_config.setter
    def worker_config(self, value: Optional[pulumi.Input['AutoscalingPolicyWorkerConfigArgs']]):
        pulumi.set(self, "worker_config", value)


class AutoscalingPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 basic_algorithm: Optional[pulumi.Input[pulumi.InputType['AutoscalingPolicyBasicAlgorithmArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 secondary_worker_config: Optional[pulumi.Input[pulumi.InputType['AutoscalingPolicySecondaryWorkerConfigArgs']]] = None,
                 worker_config: Optional[pulumi.Input[pulumi.InputType['AutoscalingPolicyWorkerConfigArgs']]] = None,
                 __props__=None):
        """
        Describes an autoscaling policy for Dataproc cluster autoscaler.

        ## Example Usage
        ### Dataproc Autoscaling Policy

        ```python
        import pulumi
        import pulumi_gcp as gcp

        asp = gcp.dataproc.AutoscalingPolicy("asp",
            policy_id="dataproc-policy",
            location="us-central1",
            worker_config=gcp.dataproc.AutoscalingPolicyWorkerConfigArgs(
                max_instances=3,
            ),
            basic_algorithm=gcp.dataproc.AutoscalingPolicyBasicAlgorithmArgs(
                yarn_config=gcp.dataproc.AutoscalingPolicyBasicAlgorithmYarnConfigArgs(
                    graceful_decommission_timeout="30s",
                    scale_up_factor=0.5,
                    scale_down_factor=0.5,
                ),
            ))
        basic = gcp.dataproc.Cluster("basic",
            region="us-central1",
            cluster_config=gcp.dataproc.ClusterClusterConfigArgs(
                autoscaling_config=gcp.dataproc.ClusterClusterConfigAutoscalingConfigArgs(
                    policy_uri=asp.name,
                ),
            ))
        ```

        ## Import

        AutoscalingPolicy can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:dataproc/autoscalingPolicy:AutoscalingPolicy default projects/{{project}}/locations/{{location}}/autoscalingPolicies/{{policy_id}}
        ```

        ```sh
         $ pulumi import gcp:dataproc/autoscalingPolicy:AutoscalingPolicy default {{project}}/{{location}}/{{policy_id}}
        ```

        ```sh
         $ pulumi import gcp:dataproc/autoscalingPolicy:AutoscalingPolicy default {{location}}/{{policy_id}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AutoscalingPolicyBasicAlgorithmArgs']] basic_algorithm: Basic algorithm for autoscaling.
               Structure is documented below.
        :param pulumi.Input[str] location: The  location where the autoscaling policy should reside.
               The default value is `global`.
        :param pulumi.Input[str] policy_id: The policy id. The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_),
               and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between
               3 and 50 characters.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['AutoscalingPolicySecondaryWorkerConfigArgs']] secondary_worker_config: Describes how the autoscaler will operate for secondary workers.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['AutoscalingPolicyWorkerConfigArgs']] worker_config: Describes how the autoscaler will operate for primary workers.
               Structure is documented below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AutoscalingPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Describes an autoscaling policy for Dataproc cluster autoscaler.

        ## Example Usage
        ### Dataproc Autoscaling Policy

        ```python
        import pulumi
        import pulumi_gcp as gcp

        asp = gcp.dataproc.AutoscalingPolicy("asp",
            policy_id="dataproc-policy",
            location="us-central1",
            worker_config=gcp.dataproc.AutoscalingPolicyWorkerConfigArgs(
                max_instances=3,
            ),
            basic_algorithm=gcp.dataproc.AutoscalingPolicyBasicAlgorithmArgs(
                yarn_config=gcp.dataproc.AutoscalingPolicyBasicAlgorithmYarnConfigArgs(
                    graceful_decommission_timeout="30s",
                    scale_up_factor=0.5,
                    scale_down_factor=0.5,
                ),
            ))
        basic = gcp.dataproc.Cluster("basic",
            region="us-central1",
            cluster_config=gcp.dataproc.ClusterClusterConfigArgs(
                autoscaling_config=gcp.dataproc.ClusterClusterConfigAutoscalingConfigArgs(
                    policy_uri=asp.name,
                ),
            ))
        ```

        ## Import

        AutoscalingPolicy can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:dataproc/autoscalingPolicy:AutoscalingPolicy default projects/{{project}}/locations/{{location}}/autoscalingPolicies/{{policy_id}}
        ```

        ```sh
         $ pulumi import gcp:dataproc/autoscalingPolicy:AutoscalingPolicy default {{project}}/{{location}}/{{policy_id}}
        ```

        ```sh
         $ pulumi import gcp:dataproc/autoscalingPolicy:AutoscalingPolicy default {{location}}/{{policy_id}}
        ```

        :param str resource_name: The name of the resource.
        :param AutoscalingPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AutoscalingPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 basic_algorithm: Optional[pulumi.Input[pulumi.InputType['AutoscalingPolicyBasicAlgorithmArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 secondary_worker_config: Optional[pulumi.Input[pulumi.InputType['AutoscalingPolicySecondaryWorkerConfigArgs']]] = None,
                 worker_config: Optional[pulumi.Input[pulumi.InputType['AutoscalingPolicyWorkerConfigArgs']]] = None,
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
            __props__ = AutoscalingPolicyArgs.__new__(AutoscalingPolicyArgs)

            __props__.__dict__["basic_algorithm"] = basic_algorithm
            __props__.__dict__["location"] = location
            if policy_id is None and not opts.urn:
                raise TypeError("Missing required property 'policy_id'")
            __props__.__dict__["policy_id"] = policy_id
            __props__.__dict__["project"] = project
            __props__.__dict__["secondary_worker_config"] = secondary_worker_config
            __props__.__dict__["worker_config"] = worker_config
            __props__.__dict__["name"] = None
        super(AutoscalingPolicy, __self__).__init__(
            'gcp:dataproc/autoscalingPolicy:AutoscalingPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            basic_algorithm: Optional[pulumi.Input[pulumi.InputType['AutoscalingPolicyBasicAlgorithmArgs']]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            policy_id: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            secondary_worker_config: Optional[pulumi.Input[pulumi.InputType['AutoscalingPolicySecondaryWorkerConfigArgs']]] = None,
            worker_config: Optional[pulumi.Input[pulumi.InputType['AutoscalingPolicyWorkerConfigArgs']]] = None) -> 'AutoscalingPolicy':
        """
        Get an existing AutoscalingPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AutoscalingPolicyBasicAlgorithmArgs']] basic_algorithm: Basic algorithm for autoscaling.
               Structure is documented below.
        :param pulumi.Input[str] location: The  location where the autoscaling policy should reside.
               The default value is `global`.
        :param pulumi.Input[str] name: The "resource name" of the autoscaling policy.
        :param pulumi.Input[str] policy_id: The policy id. The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_),
               and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between
               3 and 50 characters.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[pulumi.InputType['AutoscalingPolicySecondaryWorkerConfigArgs']] secondary_worker_config: Describes how the autoscaler will operate for secondary workers.
               Structure is documented below.
        :param pulumi.Input[pulumi.InputType['AutoscalingPolicyWorkerConfigArgs']] worker_config: Describes how the autoscaler will operate for primary workers.
               Structure is documented below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AutoscalingPolicyState.__new__(_AutoscalingPolicyState)

        __props__.__dict__["basic_algorithm"] = basic_algorithm
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["policy_id"] = policy_id
        __props__.__dict__["project"] = project
        __props__.__dict__["secondary_worker_config"] = secondary_worker_config
        __props__.__dict__["worker_config"] = worker_config
        return AutoscalingPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="basicAlgorithm")
    def basic_algorithm(self) -> pulumi.Output[Optional['outputs.AutoscalingPolicyBasicAlgorithm']]:
        """
        Basic algorithm for autoscaling.
        Structure is documented below.
        """
        return pulumi.get(self, "basic_algorithm")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The  location where the autoscaling policy should reside.
        The default value is `global`.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The "resource name" of the autoscaling policy.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[str]:
        """
        The policy id. The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_),
        and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between
        3 and 50 characters.
        """
        return pulumi.get(self, "policy_id")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="secondaryWorkerConfig")
    def secondary_worker_config(self) -> pulumi.Output[Optional['outputs.AutoscalingPolicySecondaryWorkerConfig']]:
        """
        Describes how the autoscaler will operate for secondary workers.
        Structure is documented below.
        """
        return pulumi.get(self, "secondary_worker_config")

    @property
    @pulumi.getter(name="workerConfig")
    def worker_config(self) -> pulumi.Output[Optional['outputs.AutoscalingPolicyWorkerConfig']]:
        """
        Describes how the autoscaler will operate for primary workers.
        Structure is documented below.
        """
        return pulumi.get(self, "worker_config")

