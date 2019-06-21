# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from .service_type_delta_health_policy_py3 import ServiceTypeDeltaHealthPolicy
    from .application_delta_health_policy_py3 import ApplicationDeltaHealthPolicy
    from .service_type_health_policy_py3 import ServiceTypeHealthPolicy
    from .application_health_policy_py3 import ApplicationHealthPolicy
    from .available_operation_display_py3 import AvailableOperationDisplay
    from .azure_active_directory_py3 import AzureActiveDirectory
    from .certificate_description_py3 import CertificateDescription
    from .client_certificate_common_name_py3 import ClientCertificateCommonName
    from .client_certificate_thumbprint_py3 import ClientCertificateThumbprint
    from .cluster_version_details_py3 import ClusterVersionDetails
    from .server_certificate_common_name_py3 import ServerCertificateCommonName
    from .server_certificate_common_names_py3 import ServerCertificateCommonNames
    from .diagnostics_storage_account_config_py3 import DiagnosticsStorageAccountConfig
    from .settings_parameter_description_py3 import SettingsParameterDescription
    from .settings_section_description_py3 import SettingsSectionDescription
    from .endpoint_range_description_py3 import EndpointRangeDescription
    from .node_type_description_py3 import NodeTypeDescription
    from .cluster_health_policy_py3 import ClusterHealthPolicy
    from .cluster_upgrade_delta_health_policy_py3 import ClusterUpgradeDeltaHealthPolicy
    from .cluster_upgrade_policy_py3 import ClusterUpgradePolicy
    from .cluster_py3 import Cluster
    from .cluster_code_versions_result_py3 import ClusterCodeVersionsResult
    from .cluster_code_versions_list_result_py3 import ClusterCodeVersionsListResult
    from .cluster_list_result_py3 import ClusterListResult
    from .cluster_update_parameters_py3 import ClusterUpdateParameters
    from .operation_result_py3 import OperationResult
    from .resource_py3 import Resource
    from .error_model_error_py3 import ErrorModelError
    from .error_model_py3 import ErrorModel, ErrorModelException
    from .application_metric_description_py3 import ApplicationMetricDescription
    from .application_resource_py3 import ApplicationResource
    from .application_resource_list_py3 import ApplicationResourceList
    from .arm_rolling_upgrade_monitoring_policy_py3 import ArmRollingUpgradeMonitoringPolicy
    from .arm_service_type_health_policy_py3 import ArmServiceTypeHealthPolicy
    from .arm_application_health_policy_py3 import ArmApplicationHealthPolicy
    from .application_upgrade_policy_py3 import ApplicationUpgradePolicy
    from .application_resource_update_py3 import ApplicationResourceUpdate
    from .application_type_resource_py3 import ApplicationTypeResource
    from .application_type_resource_list_py3 import ApplicationTypeResourceList
    from .application_type_version_resource_py3 import ApplicationTypeVersionResource
    from .application_type_version_resource_list_py3 import ApplicationTypeVersionResourceList
    from .service_correlation_description_py3 import ServiceCorrelationDescription
    from .named_partition_scheme_description_py3 import NamedPartitionSchemeDescription
    from .partition_scheme_description_py3 import PartitionSchemeDescription
    from .proxy_resource_py3 import ProxyResource
    from .service_load_metric_description_py3 import ServiceLoadMetricDescription
    from .service_placement_policy_description_py3 import ServicePlacementPolicyDescription
    from .service_resource_properties_py3 import ServiceResourceProperties
    from .service_resource_py3 import ServiceResource
    from .service_resource_list_py3 import ServiceResourceList
    from .service_resource_properties_base_py3 import ServiceResourcePropertiesBase
    from .service_resource_update_properties_py3 import ServiceResourceUpdateProperties
    from .service_resource_update_py3 import ServiceResourceUpdate
    from .singleton_partition_scheme_description_py3 import SingletonPartitionSchemeDescription
    from .stateful_service_properties_py3 import StatefulServiceProperties
    from .stateful_service_update_properties_py3 import StatefulServiceUpdateProperties
    from .stateless_service_properties_py3 import StatelessServiceProperties
    from .stateless_service_update_properties_py3 import StatelessServiceUpdateProperties
    from .uniform_int64_range_partition_scheme_description_py3 import UniformInt64RangePartitionSchemeDescription
except (SyntaxError, ImportError):
    from .service_type_delta_health_policy import ServiceTypeDeltaHealthPolicy
    from .application_delta_health_policy import ApplicationDeltaHealthPolicy
    from .service_type_health_policy import ServiceTypeHealthPolicy
    from .application_health_policy import ApplicationHealthPolicy
    from .available_operation_display import AvailableOperationDisplay
    from .azure_active_directory import AzureActiveDirectory
    from .certificate_description import CertificateDescription
    from .client_certificate_common_name import ClientCertificateCommonName
    from .client_certificate_thumbprint import ClientCertificateThumbprint
    from .cluster_version_details import ClusterVersionDetails
    from .server_certificate_common_name import ServerCertificateCommonName
    from .server_certificate_common_names import ServerCertificateCommonNames
    from .diagnostics_storage_account_config import DiagnosticsStorageAccountConfig
    from .settings_parameter_description import SettingsParameterDescription
    from .settings_section_description import SettingsSectionDescription
    from .endpoint_range_description import EndpointRangeDescription
    from .node_type_description import NodeTypeDescription
    from .cluster_health_policy import ClusterHealthPolicy
    from .cluster_upgrade_delta_health_policy import ClusterUpgradeDeltaHealthPolicy
    from .cluster_upgrade_policy import ClusterUpgradePolicy
    from .cluster import Cluster
    from .cluster_code_versions_result import ClusterCodeVersionsResult
    from .cluster_code_versions_list_result import ClusterCodeVersionsListResult
    from .cluster_list_result import ClusterListResult
    from .cluster_update_parameters import ClusterUpdateParameters
    from .operation_result import OperationResult
    from .resource import Resource
    from .error_model_error import ErrorModelError
    from .error_model import ErrorModel, ErrorModelException
    from .application_metric_description import ApplicationMetricDescription
    from .application_resource import ApplicationResource
    from .application_resource_list import ApplicationResourceList
    from .arm_rolling_upgrade_monitoring_policy import ArmRollingUpgradeMonitoringPolicy
    from .arm_service_type_health_policy import ArmServiceTypeHealthPolicy
    from .arm_application_health_policy import ArmApplicationHealthPolicy
    from .application_upgrade_policy import ApplicationUpgradePolicy
    from .application_resource_update import ApplicationResourceUpdate
    from .application_type_resource import ApplicationTypeResource
    from .application_type_resource_list import ApplicationTypeResourceList
    from .application_type_version_resource import ApplicationTypeVersionResource
    from .application_type_version_resource_list import ApplicationTypeVersionResourceList
    from .service_correlation_description import ServiceCorrelationDescription
    from .named_partition_scheme_description import NamedPartitionSchemeDescription
    from .partition_scheme_description import PartitionSchemeDescription
    from .proxy_resource import ProxyResource
    from .service_load_metric_description import ServiceLoadMetricDescription
    from .service_placement_policy_description import ServicePlacementPolicyDescription
    from .service_resource_properties import ServiceResourceProperties
    from .service_resource import ServiceResource
    from .service_resource_list import ServiceResourceList
    from .service_resource_properties_base import ServiceResourcePropertiesBase
    from .service_resource_update_properties import ServiceResourceUpdateProperties
    from .service_resource_update import ServiceResourceUpdate
    from .singleton_partition_scheme_description import SingletonPartitionSchemeDescription
    from .stateful_service_properties import StatefulServiceProperties
    from .stateful_service_update_properties import StatefulServiceUpdateProperties
    from .stateless_service_properties import StatelessServiceProperties
    from .stateless_service_update_properties import StatelessServiceUpdateProperties
    from .uniform_int64_range_partition_scheme_description import UniformInt64RangePartitionSchemeDescription
from .operation_result_paged import OperationResultPaged
from .service_fabric_management_client_enums import (
    ProvisioningState,
    ArmUpgradeFailureAction,
    ServiceCorrelationScheme,
    MoveCost,
    PartitionScheme,
    ServiceKind,
    ServiceLoadMetricWeight,
    ServicePlacementPolicyType,
    ArmServicePackageActivationMode,
)

__all__ = [
    'ServiceTypeDeltaHealthPolicy',
    'ApplicationDeltaHealthPolicy',
    'ServiceTypeHealthPolicy',
    'ApplicationHealthPolicy',
    'AvailableOperationDisplay',
    'AzureActiveDirectory',
    'CertificateDescription',
    'ClientCertificateCommonName',
    'ClientCertificateThumbprint',
    'ClusterVersionDetails',
    'ServerCertificateCommonName',
    'ServerCertificateCommonNames',
    'DiagnosticsStorageAccountConfig',
    'SettingsParameterDescription',
    'SettingsSectionDescription',
    'EndpointRangeDescription',
    'NodeTypeDescription',
    'ClusterHealthPolicy',
    'ClusterUpgradeDeltaHealthPolicy',
    'ClusterUpgradePolicy',
    'Cluster',
    'ClusterCodeVersionsResult',
    'ClusterCodeVersionsListResult',
    'ClusterListResult',
    'ClusterUpdateParameters',
    'OperationResult',
    'Resource',
    'ErrorModelError',
    'ErrorModel', 'ErrorModelException',
    'ApplicationMetricDescription',
    'ApplicationResource',
    'ApplicationResourceList',
    'ArmRollingUpgradeMonitoringPolicy',
    'ArmServiceTypeHealthPolicy',
    'ArmApplicationHealthPolicy',
    'ApplicationUpgradePolicy',
    'ApplicationResourceUpdate',
    'ApplicationTypeResource',
    'ApplicationTypeResourceList',
    'ApplicationTypeVersionResource',
    'ApplicationTypeVersionResourceList',
    'ServiceCorrelationDescription',
    'NamedPartitionSchemeDescription',
    'PartitionSchemeDescription',
    'ProxyResource',
    'ServiceLoadMetricDescription',
    'ServicePlacementPolicyDescription',
    'ServiceResourceProperties',
    'ServiceResource',
    'ServiceResourceList',
    'ServiceResourcePropertiesBase',
    'ServiceResourceUpdateProperties',
    'ServiceResourceUpdate',
    'SingletonPartitionSchemeDescription',
    'StatefulServiceProperties',
    'StatefulServiceUpdateProperties',
    'StatelessServiceProperties',
    'StatelessServiceUpdateProperties',
    'UniformInt64RangePartitionSchemeDescription',
    'OperationResultPaged',
    'ProvisioningState',
    'ArmUpgradeFailureAction',
    'ServiceCorrelationScheme',
    'MoveCost',
    'PartitionScheme',
    'ServiceKind',
    'ServiceLoadMetricWeight',
    'ServicePlacementPolicyType',
    'ArmServicePackageActivationMode',
]