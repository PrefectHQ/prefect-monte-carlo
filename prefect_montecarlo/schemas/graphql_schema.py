import sgqlc.types
import sgqlc.types.datetime
import sgqlc.types.relay


graphql_schema = sgqlc.types.Schema()


# Unexport Node/PageInfo, let schema re-declare them
graphql_schema -= sgqlc.types.relay.Node
graphql_schema -= sgqlc.types.relay.PageInfo



########################################################################
# Scalars and Enumerations
########################################################################
class AccessKeyIndexEnum(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('account', 'user')


class AccountNotificationDigestSettingsModelDigestType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('ANOMALIES_DIGEST', 'MISCONF_DIGEST')


class AccountNotificationSettingsModelNotificationScheduleType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('BACKUP_OR_FAILURE', 'DIGEST', 'REALTIME')


class AccountNotificationSettingsModelType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('ALATION', 'EMAIL', 'MATTERMOST', 'MSTEAMS', 'OPSGENIE', 'PAGERDUTY', 'SLACK', 'SLACK_V2', 'WEBHOOK')


class AggregationFunction(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('AVG', 'MAX', 'MIN')


class BiContainerModelType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('LOOKER', 'POWER_BI', 'TABLEAU')


Boolean = sgqlc.types.Boolean

class ComparisonType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('ABSOLUTE_VOLUME', 'CHANGE', 'DYNAMIC_THRESHOLD', 'FRESHNESS', 'GROWTH_VOLUME', 'THRESHOLD')


class ConnectionModelType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('ATHENA', 'BIGQUERY', 'DATABRICKS_DELTA', 'DATABRICKS_METASTORE', 'DBT_CLOUD', 'GLUE', 'HIVE', 'HIVE_MYSQL', 'HIVE_S3', 'LOOKER', 'LOOKER_GIT', 'LOOKER_GIT_CLONE', 'LOOKER_GIT_SSH', 'POWER_BI', 'PRESTO', 'PRESTO_S3', 'REDSHIFT', 'S3', 'S3_AIRFLOW_LOG_EVENTS', 'S3_METADATA_EVENTS', 'S3_QL_EVENTS', 'SNOWFLAKE', 'SPARK', 'TABLEAU')


class CustomRuleComparisonOperator(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('EQ', 'GT', 'GTE', 'LT', 'LTE', 'NEQ')


class CustomRuleModelQueryResultType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('SINGLE_NUMERIC',)


class CustomRuleModelRuleType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('CUSTOM_SQL', 'FRESHNESS', 'TABLE_METRIC', 'VOLUME')


class DataCollectorEventTypes(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('s3_airflow_log_events', 's3_metadata_events', 's3_ql_events')


class DataCollectorScheduleModelDeleteReason(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('NONE', 'NO_COLLECTOR')


class DataCollectorScheduleModelScheduleType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('DYNAMIC', 'FIXED', 'LOOSE', 'MANUAL')


Date = sgqlc.types.datetime.Date

DateTime = sgqlc.types.datetime.DateTime

class DbtProjectModelSource(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('CLI', 'DBT_CLOUD')


class DbtProjectSource(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('CLI', 'DBT_CLOUD')


class DetectorStatus(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('ACTIVE', 'INACTIVE', 'TRAINING')


class EventModelEventState(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('FALSE_POSITIVE', 'MUTED', 'NOTIFIED', 'NO_ACTION_REQUIRED', 'OPEN', 'RESOLVED', 'STALE', 'SYSTEM_RESOLVED', 'TIMELINE', 'USER_RESOLVED')


class EventModelEventType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('COMMENT', 'CUSTOM_RULE_ANOM', 'DBT_MODEL_ERROR', 'DBT_TEST_FAILURE', 'DELETE_TABLE', 'DIST_ANOM', 'FRESH_ANOM', 'INCIDENT_OWNER_UPDATE', 'INCIDENT_SEVERITY_UPDATE', 'INCIDENT_SLACK_THREAD', 'INCIDENT_STATUS_UPDATE', 'JSON_SCHEMA_CHANGE', 'METRIC_ANOM', 'QUERY_RUNTIME_ANOM', 'SCHEMA_CHANGE', 'SIZE_ANOM', 'SIZE_DIFF', 'UNCHANGED_SIZE_ANOM')


class EventMutingRuleModelRuleType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('REGEX_RULE',)


class FacetType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('TAGS', 'TAG_NAMES', 'TAG_VALUES')


class FieldType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('BOOLEAN', 'DATE', 'NUMERIC', 'TEXT', 'TIME', 'UNKNOWN')


Float = sgqlc.types.Float

ID = sgqlc.types.ID

class ImportanceScoreOperator(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('EQ', 'GT', 'GTE', 'LT', 'LTE', 'RANGE')


class IncidentGroupBy(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('STATUS', 'TYPE')


class IncidentModelFeedback(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('EXPECTED', 'FALSE_POSITIVE', 'FALSE_POSITIVE_6', 'FIXED', 'HELPFUL', 'INVESTIGATING', 'NOT_HELPFUL', 'NO_ACTION_NEEDED')


class IncidentModelIncidentType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('ANOMALIES', 'CUSTOM_RULE_ANOMALIES', 'DBT_ERRORS', 'DELETED_TABLES', 'METRIC_ANOMALIES', 'PERFORMANCE_ANOMALIES', 'PSEUDO_INTEGRATION_TEST', 'SCHEMA_CHANGES')


class IncidentReactionReason(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('DetectorTooSensitive', 'DontCareAboutThisTable', 'SeenThisTooManyTimes')


class IncidentReactionType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('Helpful', 'NotHelpful')


class IncidentSubType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('abnormal_size_change', 'data_added', 'data_removed', 'dbt_model_error', 'dbt_test_failure', 'dimension_anomaly', 'field_metrics_anomaly', 'fields_added', 'fields_changed', 'fields_removed', 'freshness_anomaly', 'freshness_sli_rule_breach', 'sql_rule_breach', 'unchanged_size', 'volume_anomaly', 'volume_sli_rule_breach')


Int = sgqlc.types.Int

class IntegrationKeyScope(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('CircuitBreaker', 'DatabricksMetadata', 'Spark')


class InvitationType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('Discovery', 'Observability')


class JSONString(sgqlc.types.Scalar):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema


class JobExecutionStatus(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('FAILED', 'IN_PROGRESS', 'SUCCESS', 'TIMEOUT')


class LookbackRange(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('ONE_DAY', 'ONE_HOUR', 'SEVEN_DAY', 'TWELVE_HOUR')


class MetricMonitorSelectExpressionModelDataType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('BOOLEAN', 'DATETIME', 'NUMERIC', 'STRING')


class MetricMonitoringModelType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('CATEGORIES', 'HOURLY_STATS', 'JSON_SCHEMA', 'STATS')


class MonitorAggTimeInterval(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('DAY', 'HOUR')


class MonitorStatusType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('ERROR', 'IN_PROGRESS', 'IN_TRAINING', 'MISCONFIGURED', 'NO_STATUS', 'PAUSED', 'SNOOZED', 'SUCCESS')


class ObjectPropertyModelPropertySourceType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('COLLECTION', 'DASHBOARD', 'DBT', 'LINEAGE_API', 'TAGS_COLLECTION')


class Permission(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('CatalogAccess', 'CatalogEdit', 'DashboardAccess', 'DashboardEdit', 'GraphqlMutate', 'GraphqlQuery', 'IncidentsAccess', 'IncidentsEdit', 'IncidentsUpdateStatus', 'MonitorsAccess', 'MonitorsAggregates', 'MonitorsEdit', 'PipelinesAccess', 'PipelinesEdit', 'ProductsAccess', 'ProductsDiscoveryAccess', 'ProductsObservabilityAccess', 'SettingsAccess', 'SettingsApiAccess', 'SettingsDomainsAccess', 'SettingsDomainsEdit', 'SettingsDomainsList', 'SettingsDomainsViewDetail', 'SettingsEdit', 'SettingsIntegrationsAccess', 'SettingsIntegrationsEdit', 'SettingsNotificationsAccess', 'SettingsUsersAccess', 'SettingsUsersEdit', 'SettingsUsersEditSso', 'SettingsUsersManageOwners')


class PermissionEffect(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('Allow', 'Deny')


class PowerBIAuthModeEnum(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('MASTER_USER', 'SERVICE_PRINCIPAL')


class QueryResultType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('SINGLE_NUMERIC',)


class RcaJobType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('METRIC_CORRELATION', 'SIZE_DIFF_CORRELATION', 'SQL_RULE_CUSTOM_SAMPLING', 'SQL_RULE_PROFILING')


class RcaJobsModelJobType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('METRIC_CORRELATION', 'SIZE_DIFF_CORRELATION', 'SQL_RULE_CUSTOM_SAMPLING', 'SQL_RULE_PROFILING')


class RcaJobsModelStatus(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('CANCELED', 'EMPTY', 'FAILED', 'FOUND')


class RcaStatus(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('CANCELED', 'EMPTY', 'FAILED', 'FOUND')


class RelationshipType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('EXPERT', 'OWNER')


class ScheduleType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('DYNAMIC', 'FIXED', 'LOOSE', 'MANUAL')


class SensitivityLevels(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('HIGH', 'LOW', 'MEDIUM')


class SlackAppType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('DISCOVER', 'OBSERVE')


class SlackCredentialsV2ModelSlackAppType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('DISCOVER', 'OBSERVE')


class SlackEngagementEventType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('CHANNEL_COMMENT', 'REACTION_ADDED', 'REACTION_REMOVED', 'THREAD_REPLY')


class SqlJobCheckpointStatus(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('EXECUTING_COMPLETE', 'EXECUTING_START', 'HAS_ERROR', 'PROCESSING_COMPLETE', 'PROCESSING_START', 'REGISTERED')


String = sgqlc.types.String

class TableAnomalyModelReason(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('CUSTOM_RULE', 'DIST', 'FRESHNESS', 'METRIC', 'QUERY_RUNTIME', 'SIZE', 'SIZE_DIFF', 'UNCHANGED_SIZE')


class TableFieldToBiModelBiType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('TABLEAU_WORKBOOK',)


class ThresholdModifierType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('METRIC', 'PERCENTAGE')


class ThresholdStatus(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('ACTIVE', 'INACTIVE')


class ThresholdType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('SIZE_DIFF', 'UNCHANGED_SIZE')


class UUID(sgqlc.types.Scalar):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema


class UnifiedUserAssignmentModelRelationshipType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('EXPERT', 'OWNER')


class Upload(sgqlc.types.Scalar):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema


class UserDefinedMonitorModelMonitorType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('CATEGORIES', 'CUSTOM_SQL', 'FRESHNESS', 'HOURLY_STATS', 'JSON_SCHEMA', 'STATS', 'TABLE_METRIC', 'VOLUME')


class UserDefinedMonitorModelScheduleType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('DYNAMIC', 'FIXED', 'LOOSE', 'MANUAL')


class UserDefinedMonitorModelUdmType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('MONITOR', 'RULE')


class UserDefinedMonitors(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('CATEGORIES', 'CUSTOM_SQL', 'FRESHNESS', 'JSON_SCHEMA', 'STATS', 'TABLE_METRIC', 'VOLUME')


class UserInviteModelInviteType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('DISCOVERY', 'OBSERVABILITY')


class UserInviteModelState(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('ACCEPTED', 'INVALIDATED', 'SENT')


class UserModelState(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('CHECK_BACK', 'CONNECT_DW', 'DASHBOARD', 'INSTALL_DC', 'INTEGRATIONS', 'SET_ACCOUNT_NAME', 'SIGNED_UP')


class WarehouseModelConnectionType(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('BIGQUERY', 'DATA_LAKE', 'REDSHIFT', 'SNOWFLAKE')


class WarehouseTableModelStatus(sgqlc.types.Enum):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __choices__ = ('G', 'R', 'Y')



########################################################################
# Input Objects
########################################################################
class ConnectionTestOptions(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('dc_id', 'skip_validation', 'skip_permission_tests', 'test_options')
    dc_id = sgqlc.types.Field(UUID, graphql_name='dcId')
    skip_validation = sgqlc.types.Field(Boolean, graphql_name='skipValidation')
    skip_permission_tests = sgqlc.types.Field(Boolean, graphql_name='skipPermissionTests')
    test_options = sgqlc.types.Field('ValidatorTestOptions', graphql_name='testOptions')


class CreatedByFilters(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('created_by', 'is_template_managed', 'namespace', 'rule_name')
    created_by = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='createdBy')
    is_template_managed = sgqlc.types.Field(Boolean, graphql_name='isTemplateManaged')
    namespace = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='namespace')
    rule_name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='ruleName')


class CustomRuleComparisonInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('comparison_type', 'full_table_id', 'full_table_ids', 'mcon', 'field', 'metric', 'operator', 'threshold', 'baseline_agg_function', 'baseline_interval_minutes', 'is_threshold_relative', 'threshold_lookback_minutes', 'threshold_ref', 'min_buffer', 'max_buffer', 'number_of_agg_periods')
    comparison_type = sgqlc.types.Field(ComparisonType, graphql_name='comparisonType')
    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')
    full_table_ids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='fullTableIds')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    field = sgqlc.types.Field(String, graphql_name='field')
    metric = sgqlc.types.Field(String, graphql_name='metric')
    operator = sgqlc.types.Field(sgqlc.types.non_null(CustomRuleComparisonOperator), graphql_name='operator')
    threshold = sgqlc.types.Field(Float, graphql_name='threshold')
    baseline_agg_function = sgqlc.types.Field(AggregationFunction, graphql_name='baselineAggFunction')
    baseline_interval_minutes = sgqlc.types.Field(Int, graphql_name='baselineIntervalMinutes')
    is_threshold_relative = sgqlc.types.Field(Boolean, graphql_name='isThresholdRelative')
    threshold_lookback_minutes = sgqlc.types.Field(Int, graphql_name='thresholdLookbackMinutes')
    threshold_ref = sgqlc.types.Field(String, graphql_name='thresholdRef')
    min_buffer = sgqlc.types.Field('ThresholdModifierInput', graphql_name='minBuffer')
    max_buffer = sgqlc.types.Field('ThresholdModifierInput', graphql_name='maxBuffer')
    number_of_agg_periods = sgqlc.types.Field(Int, graphql_name='numberOfAggPeriods')


class ImportanceScoreTableStatsRule(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('operator', 'value', 'value_min', 'value_max')
    operator = sgqlc.types.Field(sgqlc.types.non_null(ImportanceScoreOperator), graphql_name='operator')
    value = sgqlc.types.Field(Float, graphql_name='value')
    value_min = sgqlc.types.Field(Float, graphql_name='valueMin')
    value_max = sgqlc.types.Field(Float, graphql_name='valueMax')


class IncidentReactionInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('type', 'reasons', 'notes')
    type = sgqlc.types.Field(sgqlc.types.non_null(IncidentReactionType), graphql_name='type')
    reasons = sgqlc.types.Field(sgqlc.types.list_of(IncidentReactionReason), graphql_name='reasons')
    notes = sgqlc.types.Field(String, graphql_name='notes')


class InputObjectProperty(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('mcon_id', 'property_name', 'property_value', 'property_source_type')
    mcon_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mconId')
    property_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='propertyName')
    property_value = sgqlc.types.Field(String, graphql_name='propertyValue')
    property_source_type = sgqlc.types.Field(String, graphql_name='propertySourceType')


class InviteUsersInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('emails', 'client_mutation_id')
    emails = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='emails')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class IsImportantTableStatsRule(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='value')


class MetricDimensionFilter(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'value', 'value_str')
    key = sgqlc.types.Field(String, graphql_name='key')
    value = sgqlc.types.Field(Float, graphql_name='value')
    value_str = sgqlc.types.Field(String, graphql_name='valueStr')


class MonitorConfigurationInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('mcon', 'time_fields')
    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')
    time_fields = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('TimestampResult')), graphql_name='timeFields')


class MonitorSelectExpressionInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('expression', 'data_type')
    expression = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='expression')
    data_type = sgqlc.types.Field(String, graphql_name='dataType')


class NodeInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('object_type', 'object_id', 'resource_id', 'resource_name')
    object_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='objectType')
    object_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='objectId')
    resource_id = sgqlc.types.Field(UUID, graphql_name='resourceId')
    resource_name = sgqlc.types.Field(String, graphql_name='resourceName')


class NotificationDigestSettings(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('start_time', 'interval_minutes', 'digest_type')
    start_time = sgqlc.types.Field(DateTime, graphql_name='startTime')
    interval_minutes = sgqlc.types.Field(Int, graphql_name='intervalMinutes')
    digest_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='digestType')


class NotificationExtra(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('slack_is_private', 'webhook_shared_secret', 'webhook_encrypted_secret', 'priority', 'url', 'username', 'password', 'dc_proxy')
    slack_is_private = sgqlc.types.Field(Boolean, graphql_name='slackIsPrivate')
    webhook_shared_secret = sgqlc.types.Field(String, graphql_name='webhookSharedSecret')
    webhook_encrypted_secret = sgqlc.types.Field(String, graphql_name='webhookEncryptedSecret')
    priority = sgqlc.types.Field(String, graphql_name='priority')
    url = sgqlc.types.Field(String, graphql_name='url')
    username = sgqlc.types.Field(String, graphql_name='username')
    password = sgqlc.types.Field(String, graphql_name='password')
    dc_proxy = sgqlc.types.Field(Boolean, graphql_name='dcProxy')


class NotificationRoutingRules(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('project_names', 'dataset_ids', 'full_table_ids', 'rule_ids', 'domain_ids', 'tag_keys', 'tag_key_values', 'table_stats_rules', 'monitor_labels', 'exclude_project_names', 'exclude_dataset_ids', 'exclude_full_table_ids', 'exclude_tag_keys', 'exclude_tag_key_values', 'table_regex')
    project_names = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='projectNames')
    dataset_ids = sgqlc.types.Field(sgqlc.types.list_of(UUID), graphql_name='datasetIds')
    full_table_ids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='fullTableIds')
    rule_ids = sgqlc.types.Field(sgqlc.types.list_of(UUID), graphql_name='ruleIds')
    domain_ids = sgqlc.types.Field(sgqlc.types.list_of(UUID), graphql_name='domainIds')
    tag_keys = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagKeys')
    tag_key_values = sgqlc.types.Field(sgqlc.types.list_of('NotificationTagPairs'), graphql_name='tagKeyValues')
    table_stats_rules = sgqlc.types.Field('TableStatsRules', graphql_name='tableStatsRules')
    monitor_labels = sgqlc.types.Field(sgqlc.types.list_of(UUID), graphql_name='monitorLabels')
    exclude_project_names = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='excludeProjectNames')
    exclude_dataset_ids = sgqlc.types.Field(sgqlc.types.list_of(UUID), graphql_name='excludeDatasetIds')
    exclude_full_table_ids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='excludeFullTableIds')
    exclude_tag_keys = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='excludeTagKeys')
    exclude_tag_key_values = sgqlc.types.Field(sgqlc.types.list_of('NotificationTagPairs'), graphql_name='excludeTagKeyValues')
    table_regex = sgqlc.types.Field(String, graphql_name='tableRegex')


class NotificationTagPairs(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(String, graphql_name='name')
    value = sgqlc.types.Field(String, graphql_name='value')


class ObjectPropertyInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('property_name', 'property_value')
    property_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='propertyName')
    property_value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='propertyValue')


class QueryAfterKeyInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('user', 'date', 'query_hash')
    user = sgqlc.types.Field(String, graphql_name='user')
    date = sgqlc.types.Field(String, graphql_name='date')
    query_hash = sgqlc.types.Field(String, graphql_name='queryHash')


class ScheduleConfigInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('schedule_type', 'interval_minutes', 'interval_crontab', 'start_time', 'min_interval_minutes')
    schedule_type = sgqlc.types.Field(sgqlc.types.non_null(ScheduleType), graphql_name='scheduleType')
    interval_minutes = sgqlc.types.Field(Int, graphql_name='intervalMinutes')
    interval_crontab = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='intervalCrontab')
    start_time = sgqlc.types.Field(DateTime, graphql_name='startTime')
    min_interval_minutes = sgqlc.types.Field(Int, graphql_name='minIntervalMinutes')


class SensitivityInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('min_delay', 'level')
    min_delay = sgqlc.types.Field(Int, graphql_name='minDelay')
    level = sgqlc.types.Field(SensitivityLevels, graphql_name='level')


class SetIncidentFeedbackInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('incident_id', 'feedback', 'client_mutation_id')
    incident_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='incidentId')
    feedback = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='feedback')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class SparkBinaryInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('database', 'host', 'port', 'username', 'password')
    database = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='database')
    host = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='host')
    port = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='port')
    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')


class SparkDatabricksInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('databricks_workspace_url', 'databricks_workspace_id', 'databricks_cluster_id', 'databricks_token')
    databricks_workspace_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='databricksWorkspaceUrl')
    databricks_workspace_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='databricksWorkspaceId')
    databricks_cluster_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='databricksClusterId')
    databricks_token = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='databricksToken')


class SparkHttpInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('url', 'username', 'password')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')


class SslInputOptions(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('ca', 'cert', 'key', 'mechanism', 'skip_verification')
    ca = sgqlc.types.Field(String, graphql_name='ca')
    cert = sgqlc.types.Field(String, graphql_name='cert')
    key = sgqlc.types.Field(String, graphql_name='key')
    mechanism = sgqlc.types.Field(String, graphql_name='mechanism')
    skip_verification = sgqlc.types.Field(Boolean, graphql_name='skipVerification')


class TableStatsRules(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('importance_score', 'is_important')
    importance_score = sgqlc.types.Field(ImportanceScoreTableStatsRule, graphql_name='importanceScore')
    is_important = sgqlc.types.Field(IsImportantTableStatsRule, graphql_name='isImportant')


class TagKeyValuePairInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(String, graphql_name='name')
    value = sgqlc.types.Field(String, graphql_name='value')


class TagPair(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class ThresholdModifierInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('modifier_type', 'value')
    modifier_type = sgqlc.types.Field(sgqlc.types.non_null(ThresholdModifierType), graphql_name='modifierType')
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')


class TimestampResult(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('field_name', 'timestamp')
    field_name = sgqlc.types.Field(String, graphql_name='fieldName')
    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')


class ToggleDatasetInputItem(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('dw_id', 'ds_id')
    dw_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='dwId')
    ds_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='dsId')


class ToggleMuteDatasetInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('dw_id', 'ds_id', 'mute', 'client_mutation_id')
    dw_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='dwId')
    ds_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='dsId')
    mute = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='mute')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class ToggleMuteDatasetsInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('datasets', 'mute', 'client_mutation_id')
    datasets = sgqlc.types.Field(sgqlc.types.list_of(ToggleDatasetInputItem), graphql_name='datasets')
    mute = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='mute')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class ToggleMuteTableInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('mcon', 'full_table_id', 'dw_id', 'mute', 'client_mutation_id')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')
    dw_id = sgqlc.types.Field(UUID, graphql_name='dwId')
    mute = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='mute')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class ToggleMuteTablesInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('tables', 'mute', 'client_mutation_id')
    tables = sgqlc.types.Field(sgqlc.types.list_of('ToggleTableInputItem'), graphql_name='tables')
    mute = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='mute')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class ToggleMuteWithRegexInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('dw_id', 'rule_regex', 'mute', 'client_mutation_id')
    dw_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='dwId')
    rule_regex = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ruleRegex')
    mute = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='mute')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class ToggleTableInputItem(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('mcon', 'full_table_id', 'dw_id')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')
    dw_id = sgqlc.types.Field(UUID, graphql_name='dwId')


class TrackTableInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('mcon', 'full_table_id', 'dw_id', 'track', 'client_mutation_id')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')
    dw_id = sgqlc.types.Field(UUID, graphql_name='dwId')
    track = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='track')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateUserStateInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('state', 'client_mutation_id')
    state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='state')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UserAfterKeyInput(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('user', 'source')
    user = sgqlc.types.Field(String, graphql_name='user')
    source = sgqlc.types.Field(String, graphql_name='source')


class UserAfterKeyInput2(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('user',)
    user = sgqlc.types.Field(String, graphql_name='user')


class ValidatorTestOptions(sgqlc.types.Input):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('validate_select', 'validate_info_access', 'validate_table_metadata', 'validate_syslog')
    validate_select = sgqlc.types.Field(Boolean, graphql_name='validateSelect')
    validate_info_access = sgqlc.types.Field(Boolean, graphql_name='validateInfoAccess')
    validate_table_metadata = sgqlc.types.Field(Boolean, graphql_name='validateTableMetadata')
    validate_syslog = sgqlc.types.Field(Boolean, graphql_name='validateSyslog')



########################################################################
# Output Objects and Interfaces
########################################################################
class AccessToken(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id', 'token')
    id = sgqlc.types.Field(String, graphql_name='id')
    token = sgqlc.types.Field(String, graphql_name='token')


class Account(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id', 'uuid', 'name', 'created_on', 'config', 'allow_non_sso_login', 'data_share', 'notification_settings', 'data_collectors', 'users', 'user_invites', 'warehouses', 'bi', 'connections', 'tableau_accounts', 'slack_credentials', 'slack_msg_details', 'resources', 'account_domains', 'slack_credentials_v2', 'identity_provider', 'active_collection_regions', 'internal_notifications')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    name = sgqlc.types.Field(String, graphql_name='name')
    created_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdOn')
    config = sgqlc.types.Field(JSONString, graphql_name='config')
    allow_non_sso_login = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='allowNonSsoLogin')
    data_share = sgqlc.types.Field(JSONString, graphql_name='dataShare')
    notification_settings = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AccountNotificationSetting'))), graphql_name='notificationSettings')
    data_collectors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DataCollector'))), graphql_name='dataCollectors')
    users = sgqlc.types.Field(sgqlc.types.non_null('UserConnection'), graphql_name='users', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('email', sgqlc.types.Arg(String, graphql_name='email', default=None)),
        ('first_name', sgqlc.types.Arg(String, graphql_name='firstName', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='lastName', default=None)),
        ('role', sgqlc.types.Arg(String, graphql_name='role', default=None)),
))
    )
    user_invites = sgqlc.types.Field(sgqlc.types.non_null('UserInviteConnection'), graphql_name='userInvites', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('state', sgqlc.types.Arg(String, graphql_name='state', default=None)),
))
    )
    warehouses = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Warehouse'))), graphql_name='warehouses')
    bi = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('BiContainer'))), graphql_name='bi')
    connections = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Connection'))), graphql_name='connections')
    tableau_accounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TableauAccount'))), graphql_name='tableauAccounts')
    slack_credentials = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SlackCredentials'))), graphql_name='slackCredentials')
    slack_msg_details = sgqlc.types.Field(sgqlc.types.non_null('SlackMessageDetailsConnection'), graphql_name='slackMsgDetails', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    resources = sgqlc.types.Field(sgqlc.types.non_null('ResourceConnection'), graphql_name='resources', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    account_domains = sgqlc.types.Field(sgqlc.types.non_null('DomainRestrictionConnection'), graphql_name='accountDomains', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    slack_credentials_v2 = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SlackCredentialsV2'))), graphql_name='slackCredentialsV2')
    identity_provider = sgqlc.types.Field('SamlIdentityProvider', graphql_name='identityProvider')
    active_collection_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='activeCollectionRegions')
    internal_notifications = sgqlc.types.Field(sgqlc.types.list_of('InternalNotifications'), graphql_name='internalNotifications')


class AccountNotificationDigestSettings(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id', 'interval_minutes', 'start_time', 'prev_execution_time', 'next_execution_time', 'created_time', 'uuid', 'digest_type', 'digest_settings')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    interval_minutes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='intervalMinutes')
    start_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startTime')
    prev_execution_time = sgqlc.types.Field(DateTime, graphql_name='prevExecutionTime')
    next_execution_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='nextExecutionTime')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    digest_type = sgqlc.types.Field(sgqlc.types.non_null(AccountNotificationDigestSettingsModelDigestType), graphql_name='digestType')
    digest_settings = sgqlc.types.Field('AccountNotificationSetting', graphql_name='digestSettings')


class AccountNotificationRoutingRules(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id', 'uuid', 'table_rules', 'tag_rules', 'sql_rules', 'table_stats_rules', 'domain_rules', 'monitor_labels', 'table_id_rules', 'routing_rules')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    table_rules = sgqlc.types.Field(String, graphql_name='tableRules')
    tag_rules = sgqlc.types.Field(JSONString, graphql_name='tagRules')
    sql_rules = sgqlc.types.Field(sgqlc.types.list_of(UUID), graphql_name='sqlRules')
    table_stats_rules = sgqlc.types.Field(JSONString, graphql_name='tableStatsRules')
    domain_rules = sgqlc.types.Field(sgqlc.types.list_of(UUID), graphql_name='domainRules')
    monitor_labels = sgqlc.types.Field(sgqlc.types.list_of(UUID), graphql_name='monitorLabels')
    table_id_rules = sgqlc.types.Field(JSONString, graphql_name='tableIdRules')
    routing_rules = sgqlc.types.Field('AccountNotificationSetting', graphql_name='routingRules')


class AccountNotificationSetting(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id', 'uuid', 'created_by', 'last_updated_by', 'type', 'recipient', 'recipients', 'anomaly_types', 'incident_sub_types', 'extra', 'routing_rules', 'custom_message', 'notification_schedule_type', 'digest_settings', 'specification_rule', 'slack_msg_details', 'recipient_display_name', 'recipients_display_names')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    created_by = sgqlc.types.Field('User', graphql_name='createdBy')
    last_updated_by = sgqlc.types.Field('User', graphql_name='lastUpdatedBy')
    type = sgqlc.types.Field(sgqlc.types.non_null(AccountNotificationSettingsModelType), graphql_name='type')
    recipient = sgqlc.types.Field(String, graphql_name='recipient')
    recipients = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='recipients')
    anomaly_types = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='anomalyTypes')
    incident_sub_types = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='incidentSubTypes')
    extra = sgqlc.types.Field(JSONString, graphql_name='extra')
    routing_rules = sgqlc.types.Field(AccountNotificationRoutingRules, graphql_name='routingRules')
    custom_message = sgqlc.types.Field(String, graphql_name='customMessage')
    notification_schedule_type = sgqlc.types.Field(sgqlc.types.non_null(AccountNotificationSettingsModelNotificationScheduleType), graphql_name='notificationScheduleType')
    digest_settings = sgqlc.types.Field(AccountNotificationDigestSettings, graphql_name='digestSettings')
    specification_rule = sgqlc.types.Field(String, graphql_name='specificationRule')
    slack_msg_details = sgqlc.types.Field(sgqlc.types.non_null('SlackMessageDetailsConnection'), graphql_name='slackMsgDetails', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    recipient_display_name = sgqlc.types.Field(String, graphql_name='recipientDisplayName')
    recipients_display_names = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='recipientsDisplayNames')


class AddBiConnectionMutation(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('connection',)
    connection = sgqlc.types.Field('Connection', graphql_name='connection')


class AddConnectionMutation(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('connection',)
    connection = sgqlc.types.Field('Connection', graphql_name='connection')


class AddDatabricksConnectionMutation(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('connection',)
    connection = sgqlc.types.Field('Connection', graphql_name='connection')


class AddTableauAccountMutation(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('tableau_account',)
    tableau_account = sgqlc.types.Field('TableauAccount', graphql_name='tableauAccount')


class AirflowTaskInstanceConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('AirflowTaskInstanceEdge')), graphql_name='edges')


class AirflowTaskInstanceEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('AirflowTaskInstance', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class AirflowTaskLog(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('messages', 'total_messages', '_id')
    messages = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='messages')
    total_messages = sgqlc.types.Field(Int, graphql_name='totalMessages')
    _id = sgqlc.types.Field(String, graphql_name='_id')


class AuthorRef(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name', 'username', 'email')
    name = sgqlc.types.Field(String, graphql_name='name')
    username = sgqlc.types.Field(String, graphql_name='username')
    email = sgqlc.types.Field(String, graphql_name='email')


class AuthorizationGroupOutput(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name', 'roles', 'version', 'is_managed', 'label', 'description', 'users', 'domain_restrictions')
    name = sgqlc.types.Field(String, graphql_name='name')
    roles = sgqlc.types.Field(sgqlc.types.list_of('RoleOutput'), graphql_name='roles')
    version = sgqlc.types.Field(String, graphql_name='version')
    is_managed = sgqlc.types.Field(Boolean, graphql_name='isManaged')
    label = sgqlc.types.Field(String, graphql_name='label')
    description = sgqlc.types.Field(String, graphql_name='description')
    users = sgqlc.types.Field(sgqlc.types.list_of('AuthUser'), graphql_name='users')
    domain_restrictions = sgqlc.types.Field(sgqlc.types.list_of('DomainRestriction'), graphql_name='domainRestrictions')


class BiContainer(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id', 'account', 'uuid', 'data_collector', 'type', 'connections')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    data_collector = sgqlc.types.Field('DataCollector', graphql_name='dataCollector')
    type = sgqlc.types.Field(sgqlc.types.non_null(BiContainerModelType), graphql_name='type')
    connections = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Connection'))), graphql_name='connections')


class BiLineage(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('workbook_id', 'friendly_name', 'content_url', 'owner_id', 'project_id', 'project_name', 'created', 'updated', 'total_views', 'workbook_creators', 'view_id', 'category', 'mcon', 'name', 'display_name')
    workbook_id = sgqlc.types.Field(String, graphql_name='workbookId')
    friendly_name = sgqlc.types.Field(String, graphql_name='friendlyName')
    content_url = sgqlc.types.Field(String, graphql_name='contentUrl')
    owner_id = sgqlc.types.Field(String, graphql_name='ownerId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    project_name = sgqlc.types.Field(String, graphql_name='projectName')
    created = sgqlc.types.Field(DateTime, graphql_name='created')
    updated = sgqlc.types.Field(DateTime, graphql_name='updated')
    total_views = sgqlc.types.Field(Int, graphql_name='totalViews')
    workbook_creators = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='workbookCreators')
    view_id = sgqlc.types.Field(String, graphql_name='viewId')
    category = sgqlc.types.Field(String, graphql_name='category')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    name = sgqlc.types.Field(String, graphql_name='name')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')


class BiMetadata(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('owner', 'site', 'uri', 'sheets', 'embedded_datasources', 'upstream_data_quality_warnings', 'view_path', 'workbook_id', 'workbook_name', 'view_id', 'dashboards', 'model_name', 'source_file', 'view_name', 'connection_name', 'lookml_model_id', 'explore_id', 'explore_name', 'query', 'is_deleted', 'user_id', 'hidden', 'deleted_at', 'last_accessed_at', 'last_viewed_at', 'description', 'favorite_count', 'view_count', 'preferred_viewer', 'readonly', 'refresh_interval', 'load_configuration', 'edit_uri', 'look_ids', 'looker_dashboard_tiles', 'model_id', 'dashboard', 'chart_title', 'user_emails', 'reason', 'is_manual', 'aggregation', 'date_range', 'workspace', 'created_by', 'modified_at', 'modified_by', 'report_type', 'tiles', 'project_name', 'creation_time', 'created_at')
    owner = sgqlc.types.Field('OwnerRef', graphql_name='owner')
    site = sgqlc.types.Field('SiteRef', graphql_name='site')
    uri = sgqlc.types.Field(String, graphql_name='uri')
    sheets = sgqlc.types.Field(sgqlc.types.list_of('SheetDashboardRef'), graphql_name='sheets')
    embedded_datasources = sgqlc.types.Field(sgqlc.types.list_of('NameRef'), graphql_name='embeddedDatasources')
    upstream_data_quality_warnings = sgqlc.types.Field(sgqlc.types.list_of('DataQualityWarningsRef'), graphql_name='upstreamDataQualityWarnings')
    view_path = sgqlc.types.Field(String, graphql_name='viewPath')
    workbook_id = sgqlc.types.Field(String, graphql_name='workbookId')
    workbook_name = sgqlc.types.Field(String, graphql_name='workbookName')
    view_id = sgqlc.types.Field(String, graphql_name='viewId')
    dashboards = sgqlc.types.Field(sgqlc.types.list_of('SheetDashboardRef'), graphql_name='dashboards')
    model_name = sgqlc.types.Field(String, graphql_name='modelName')
    source_file = sgqlc.types.Field(String, graphql_name='sourceFile')
    view_name = sgqlc.types.Field(String, graphql_name='viewName')
    connection_name = sgqlc.types.Field(String, graphql_name='connectionName')
    lookml_model_id = sgqlc.types.Field(String, graphql_name='lookmlModelId')
    explore_id = sgqlc.types.Field(String, graphql_name='exploreId')
    explore_name = sgqlc.types.Field(String, graphql_name='exploreName')
    query = sgqlc.types.Field('QueryRef', graphql_name='query')
    is_deleted = sgqlc.types.Field(Boolean, graphql_name='isDeleted')
    user_id = sgqlc.types.Field(String, graphql_name='userId')
    hidden = sgqlc.types.Field(String, graphql_name='hidden')
    deleted_at = sgqlc.types.Field(String, graphql_name='deletedAt')
    last_accessed_at = sgqlc.types.Field(String, graphql_name='lastAccessedAt')
    last_viewed_at = sgqlc.types.Field(String, graphql_name='lastViewedAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    favorite_count = sgqlc.types.Field(Int, graphql_name='favoriteCount')
    view_count = sgqlc.types.Field(Int, graphql_name='viewCount')
    preferred_viewer = sgqlc.types.Field(String, graphql_name='preferredViewer')
    readonly = sgqlc.types.Field(Boolean, graphql_name='readonly')
    refresh_interval = sgqlc.types.Field(String, graphql_name='refreshInterval')
    load_configuration = sgqlc.types.Field(String, graphql_name='loadConfiguration')
    edit_uri = sgqlc.types.Field(String, graphql_name='editUri')
    look_ids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lookIds')
    looker_dashboard_tiles = sgqlc.types.Field(sgqlc.types.list_of('LookerDashboardTileRef'), graphql_name='lookerDashboardTiles')
    model_id = sgqlc.types.Field(String, graphql_name='modelId')
    dashboard = sgqlc.types.Field('SheetDashboardRef', graphql_name='dashboard')
    chart_title = sgqlc.types.Field(String, graphql_name='chartTitle')
    user_emails = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='userEmails')
    reason = sgqlc.types.Field(String, graphql_name='reason')
    is_manual = sgqlc.types.Field(String, graphql_name='isManual')
    aggregation = sgqlc.types.Field(String, graphql_name='aggregation')
    date_range = sgqlc.types.Field(String, graphql_name='dateRange')
    workspace = sgqlc.types.Field('PowerBIWorkSpaceRef', graphql_name='workspace')
    created_by = sgqlc.types.Field(String, graphql_name='createdBy')
    modified_at = sgqlc.types.Field(String, graphql_name='modifiedAt')
    modified_by = sgqlc.types.Field(String, graphql_name='modifiedBy')
    report_type = sgqlc.types.Field(String, graphql_name='reportType')
    tiles = sgqlc.types.Field(sgqlc.types.list_of('PowerBIDashboardTileRef'), graphql_name='tiles')
    project_name = sgqlc.types.Field(String, graphql_name='projectName')
    creation_time = sgqlc.types.Field(String, graphql_name='creationTime')
    created_at = sgqlc.types.Field(String, graphql_name='createdAt')


class BigQueryProject(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('full_project_id', 'friendly_name')
    full_project_id = sgqlc.types.Field(String, graphql_name='fullProjectId')
    friendly_name = sgqlc.types.Field(String, graphql_name='friendlyName')


class BlastRadiusCount(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('query_count', 'user_count')
    query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='queryCount')
    user_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='userCount')


class BlastRadiusUserQuery(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('date', 'tables', 'query_hash', 'query_count')
    date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='date')
    tables = sgqlc.types.Field(sgqlc.types.list_of('TableInfo'), graphql_name='tables')
    query_hash = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='queryHash')
    query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='queryCount')


class BulkCreateOrUpdateObjectProperties(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('object_properties',)
    object_properties = sgqlc.types.Field(sgqlc.types.list_of('ObjectProperty'), graphql_name='objectProperties')


class CatalogObjectMetadataConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('CatalogObjectMetadataEdge')), graphql_name='edges')


class CatalogObjectMetadataEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('CatalogObjectMetadata', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class CategoryLabelRank(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('label', 'rank')
    label = sgqlc.types.Field(String, graphql_name='label')
    rank = sgqlc.types.Field(Float, graphql_name='rank')


class CircuitBreakerState(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('job_execution_uuid', 'account_uuid', 'resource_uuid', 'custom_rule_uuid', 'status', 'log')
    job_execution_uuid = sgqlc.types.Field(UUID, graphql_name='jobExecutionUuid')
    account_uuid = sgqlc.types.Field(UUID, graphql_name='accountUuid')
    resource_uuid = sgqlc.types.Field(UUID, graphql_name='resourceUuid')
    custom_rule_uuid = sgqlc.types.Field(UUID, graphql_name='customRuleUuid')
    status = sgqlc.types.Field(SqlJobCheckpointStatus, graphql_name='status')
    log = sgqlc.types.Field(JSONString, graphql_name='log')


class CleanupCollectorRecordInAccount(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class CollectionProperties(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('cross_account_external_id', 'customer_account_token', 'code_bucket', 'code_version', 'platform_aws_account_id', 'platform_region_details')
    cross_account_external_id = sgqlc.types.Field(String, graphql_name='crossAccountExternalId')
    customer_account_token = sgqlc.types.Field(String, graphql_name='customerAccountToken')
    code_bucket = sgqlc.types.Field(String, graphql_name='codeBucket')
    code_version = sgqlc.types.Field(String, graphql_name='codeVersion')
    platform_aws_account_id = sgqlc.types.Field(String, graphql_name='platformAwsAccountId')
    platform_region_details = sgqlc.types.Field('PlatformRegionProperties', graphql_name='platformRegionDetails')


class ColumnLineage(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('selected_column', 'lineage_sources')
    selected_column = sgqlc.types.Field(String, graphql_name='selectedColumn')
    lineage_sources = sgqlc.types.Field(sgqlc.types.list_of('LineageSources'), graphql_name='lineageSources')


class Connection(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id', 'uuid', 'type', 'account', 'warehouse', 'bi_container', 'job_types', 'credentials_s3_key', 'data', 'created_on', 'updated_on', 'connection_identifier', 'job_errors')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    type = sgqlc.types.Field(sgqlc.types.non_null(ConnectionModelType), graphql_name='type')
    account = sgqlc.types.Field(Account, graphql_name='account')
    warehouse = sgqlc.types.Field('Warehouse', graphql_name='warehouse')
    bi_container = sgqlc.types.Field(BiContainer, graphql_name='biContainer')
    job_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='jobTypes')
    credentials_s3_key = sgqlc.types.Field(String, graphql_name='credentialsS3Key')
    data = sgqlc.types.Field(JSONString, graphql_name='data')
    created_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdOn')
    updated_on = sgqlc.types.Field(DateTime, graphql_name='updatedOn')
    connection_identifier = sgqlc.types.Field('ConnectionIdentifier', graphql_name='connectionIdentifier')
    job_errors = sgqlc.types.Field(sgqlc.types.list_of('JobError'), graphql_name='jobErrors')


class ConnectionIdentifier(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'value')
    key = sgqlc.types.Field(String, graphql_name='key')
    value = sgqlc.types.Field(String, graphql_name='value')


class ConnectionValidation(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('type', 'message', 'data')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    message = sgqlc.types.Field(String, graphql_name='message')
    data = sgqlc.types.Field('ConnectionValidationData', graphql_name='data')


class ConnectionValidationData(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('database', 'table', 'error')
    database = sgqlc.types.Field(String, graphql_name='database')
    table = sgqlc.types.Field(String, graphql_name='table')
    error = sgqlc.types.Field(String, graphql_name='error')


class CreateAccessToken(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('access_token',)
    access_token = sgqlc.types.Field(AccessToken, graphql_name='accessToken')


class CreateCollectorRecord(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('dc',)
    dc = sgqlc.types.Field('DataCollector', graphql_name='dc')


class CreateCustomMetricRule(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')


class CreateCustomRule(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')


class CreateCustomUser(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('custom_user',)
    custom_user = sgqlc.types.Field('CustomUser', graphql_name='customUser')


class CreateDatabricksNotebookJob(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('databricks',)
    databricks = sgqlc.types.Field('DatabricksJobResponse', graphql_name='databricks')


class CreateDatabricksSecret(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class CreateDbtProject(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('dbt_project',)
    dbt_project = sgqlc.types.Field('DbtProject', graphql_name='dbtProject')


class CreateIntegrationKey(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key',)
    key = sgqlc.types.Field('IntegrationKey', graphql_name='key')


class CreateOrUpdateAuthorizationGroup(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('authorization_group',)
    authorization_group = sgqlc.types.Field(AuthorizationGroupOutput, graphql_name='authorizationGroup')


class CreateOrUpdateCatalogObjectMetadata(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('catalog_object_metadata',)
    catalog_object_metadata = sgqlc.types.Field('CatalogObjectMetadata', graphql_name='catalogObjectMetadata')


class CreateOrUpdateCustomMetricRule(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')


class CreateOrUpdateCustomRule(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')


class CreateOrUpdateDoc(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('doc',)
    doc = sgqlc.types.Field('Doc', graphql_name='doc')


class CreateOrUpdateDomain(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('domain',)
    domain = sgqlc.types.Field('DomainOutput', graphql_name='domain')


class CreateOrUpdateFreshnessCustomRule(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')


class CreateOrUpdateIncidentComment(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('comment_event',)
    comment_event = sgqlc.types.Field('Event', graphql_name='commentEvent')


class CreateOrUpdateLineageEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('edge',)
    edge = sgqlc.types.Field('LineageEdge', graphql_name='edge')


class CreateOrUpdateLineageNode(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node',)
    node = sgqlc.types.Field('LineageNode', graphql_name='node')


class CreateOrUpdateLineageNodeBlockPattern(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('pattern',)
    pattern = sgqlc.types.Field('LineageNodeBlockPattern', graphql_name='pattern')


class CreateOrUpdateMonitor(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('monitor',)
    monitor = sgqlc.types.Field('MetricMonitoring', graphql_name='monitor')


class CreateOrUpdateMonteCarloConfigTemplate(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('response',)
    response = sgqlc.types.Field('MonteCarloConfigTemplateUpdateResponse', graphql_name='response')


class CreateOrUpdateNotificationSetting(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('notification_setting',)
    notification_setting = sgqlc.types.Field(AccountNotificationSetting, graphql_name='notificationSetting')


class CreateOrUpdateObjectProperty(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('object_property',)
    object_property = sgqlc.types.Field('ObjectProperty', graphql_name='objectProperty')


class CreateOrUpdateResource(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('resource',)
    resource = sgqlc.types.Field('Resource', graphql_name='resource')


class CreateOrUpdateSamlIdentityProvider(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('account',)
    account = sgqlc.types.Field(Account, graphql_name='account')


class CreateOrUpdateVolumeRule(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')


class CreateUnifiedUserAssignment(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('unified_user_assignment',)
    unified_user_assignment = sgqlc.types.Field('UnifiedUserAssignment', graphql_name='unifiedUserAssignment')


class CustomRuleComparison(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('comparison_type', 'full_table_id', 'full_table_ids', 'field', 'metric', 'operator', 'threshold', 'baseline_agg_function', 'baseline_interval_minutes', 'is_threshold_relative', 'threshold_lookback_minutes', 'threshold_ref', 'min_buffer', 'max_buffer', 'number_of_agg_periods', 'data_collection_interval_minutes', 'rule_interval_minutes')
    comparison_type = sgqlc.types.Field(sgqlc.types.non_null(ComparisonType), graphql_name='comparisonType')
    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')
    full_table_ids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='fullTableIds')
    field = sgqlc.types.Field(String, graphql_name='field')
    metric = sgqlc.types.Field(String, graphql_name='metric')
    operator = sgqlc.types.Field(sgqlc.types.non_null(CustomRuleComparisonOperator), graphql_name='operator')
    threshold = sgqlc.types.Field(Float, graphql_name='threshold')
    baseline_agg_function = sgqlc.types.Field(AggregationFunction, graphql_name='baselineAggFunction')
    baseline_interval_minutes = sgqlc.types.Field(Int, graphql_name='baselineIntervalMinutes')
    is_threshold_relative = sgqlc.types.Field(Boolean, graphql_name='isThresholdRelative')
    threshold_lookback_minutes = sgqlc.types.Field(Int, graphql_name='thresholdLookbackMinutes')
    threshold_ref = sgqlc.types.Field(String, graphql_name='thresholdRef')
    min_buffer = sgqlc.types.Field('ThresholdModifier', graphql_name='minBuffer')
    max_buffer = sgqlc.types.Field('ThresholdModifier', graphql_name='maxBuffer')
    number_of_agg_periods = sgqlc.types.Field(Int, graphql_name='numberOfAggPeriods')
    data_collection_interval_minutes = sgqlc.types.Field(Int, graphql_name='dataCollectionIntervalMinutes')
    rule_interval_minutes = sgqlc.types.Field(Int, graphql_name='ruleIntervalMinutes')


class CustomRuleConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('CustomRuleEdge')), graphql_name='edges')


class CustomRuleEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('CustomRule', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class CustomSQLOutputSample(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('columns', 'rows', 'sampling_disabled')
    columns = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='columns')
    rows = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of(String)), graphql_name='rows')
    sampling_disabled = sgqlc.types.Field(Boolean, graphql_name='samplingDisabled')


class CustomUserConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('CustomUserEdge')), graphql_name='edges')


class CustomUserEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('CustomUser', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class DataAssetDashboard(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('data_sources_count', 'project_count', 'schema_count', 'table_count', 'view_count', 'external_table_count')
    data_sources_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dataSourcesCount')
    project_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='projectCount')
    schema_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='schemaCount')
    table_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='tableCount')
    view_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='viewCount')
    external_table_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='externalTableCount')


class DataCollector(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id', 'account', 'uuid', 'api_gateway_id', 'kinesis_endpoint_id', 'cloudwatch_log_endpoint_id', 'cross_account_role_arn', 'stack_arn', 'customer_aws_account_id', 'customer_aws_region', 'template_launch_url', 'template_provider', 'template_variant', 'template_version', 'template_parameters', 'code_version', 'kinesis_access_role', 'active', 'last_updated', 'is_custom', 'oauth_credentials_s3_key', 'release_channel', 'warehouses', 'bi_container', 'tableau_collector')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    api_gateway_id = sgqlc.types.Field(String, graphql_name='apiGatewayId')
    kinesis_endpoint_id = sgqlc.types.Field(String, graphql_name='kinesisEndpointId')
    cloudwatch_log_endpoint_id = sgqlc.types.Field(String, graphql_name='cloudwatchLogEndpointId')
    cross_account_role_arn = sgqlc.types.Field(String, graphql_name='crossAccountRoleArn')
    stack_arn = sgqlc.types.Field(String, graphql_name='stackArn')
    customer_aws_account_id = sgqlc.types.Field(String, graphql_name='customerAwsAccountId')
    customer_aws_region = sgqlc.types.Field(String, graphql_name='customerAwsRegion')
    template_launch_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='templateLaunchUrl')
    template_provider = sgqlc.types.Field(String, graphql_name='templateProvider')
    template_variant = sgqlc.types.Field(String, graphql_name='templateVariant')
    template_version = sgqlc.types.Field(String, graphql_name='templateVersion')
    template_parameters = sgqlc.types.Field(JSONString, graphql_name='templateParameters')
    code_version = sgqlc.types.Field(String, graphql_name='codeVersion')
    kinesis_access_role = sgqlc.types.Field(String, graphql_name='kinesisAccessRole')
    active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='active')
    last_updated = sgqlc.types.Field(DateTime, graphql_name='lastUpdated')
    is_custom = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCustom')
    oauth_credentials_s3_key = sgqlc.types.Field(String, graphql_name='oauthCredentialsS3Key')
    release_channel = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='releaseChannel')
    warehouses = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Warehouse'))), graphql_name='warehouses')
    bi_container = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BiContainer))), graphql_name='biContainer')
    tableau_collector = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TableauAccount'))), graphql_name='tableauCollector')


class DataCollectorSchedule(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id', 'uuid', 'dc_id', 'resource_id', 'connection_id', 'project_id', 'output_stream', 'last_job_id', 'job_type', 'schedule_type', 'created_on', 'last_run', 'interval_in_seconds', 'override', 'skip', 'is_deleted', 'friendly_name', 'notes', 'limits', 'interval_crontab', 'start_time', 'prev_execution_time', 'next_execution_time', 'is_dynamic_schedule_poller', 'min_interval_seconds', 'delete_reason', 'metric_monitors')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    dc_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='dcId')
    resource_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceId')
    connection_id = sgqlc.types.Field(UUID, graphql_name='connectionId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    output_stream = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='outputStream')
    last_job_id = sgqlc.types.Field(String, graphql_name='lastJobId')
    job_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='jobType')
    schedule_type = sgqlc.types.Field(sgqlc.types.non_null(DataCollectorScheduleModelScheduleType), graphql_name='scheduleType')
    created_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdOn')
    last_run = sgqlc.types.Field(DateTime, graphql_name='lastRun')
    interval_in_seconds = sgqlc.types.Field(Int, graphql_name='intervalInSeconds')
    override = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='override')
    skip = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='skip')
    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')
    friendly_name = sgqlc.types.Field(String, graphql_name='friendlyName')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    limits = sgqlc.types.Field(JSONString, graphql_name='limits')
    interval_crontab = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='intervalCrontab')
    start_time = sgqlc.types.Field(DateTime, graphql_name='startTime')
    prev_execution_time = sgqlc.types.Field(DateTime, graphql_name='prevExecutionTime')
    next_execution_time = sgqlc.types.Field(DateTime, graphql_name='nextExecutionTime')
    is_dynamic_schedule_poller = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDynamicSchedulePoller')
    min_interval_seconds = sgqlc.types.Field(Int, graphql_name='minIntervalSeconds')
    delete_reason = sgqlc.types.Field(DataCollectorScheduleModelDeleteReason, graphql_name='deleteReason')
    metric_monitors = sgqlc.types.Field(sgqlc.types.non_null('MetricMonitoringConnection'), graphql_name='metricMonitors', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )


class DataProfileField(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name', 'type', 'min', 'max', 'p25', 'p50', 'p75', 'dist')
    name = sgqlc.types.Field(String, graphql_name='name')
    type = sgqlc.types.Field(String, graphql_name='type')
    min = sgqlc.types.Field(Float, graphql_name='min')
    max = sgqlc.types.Field(Float, graphql_name='max')
    p25 = sgqlc.types.Field(Float, graphql_name='p25')
    p50 = sgqlc.types.Field(Float, graphql_name='p50')
    p75 = sgqlc.types.Field(Float, graphql_name='p75')
    dist = sgqlc.types.Field(JSONString, graphql_name='dist')


class DataProfileResult(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('sample_size', 'fields')
    sample_size = sgqlc.types.Field(Int, graphql_name='sampleSize')
    fields = sgqlc.types.Field(sgqlc.types.list_of(DataProfileField), graphql_name='fields')


class DataQualityWarningsRef(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name', 'author', 'is_severe', 'is_active', 'warning_type', 'message', 'created_at', 'updated_at')
    name = sgqlc.types.Field(String, graphql_name='name')
    author = sgqlc.types.Field(AuthorRef, graphql_name='author')
    is_severe = sgqlc.types.Field(String, graphql_name='isSevere')
    is_active = sgqlc.types.Field(String, graphql_name='isActive')
    warning_type = sgqlc.types.Field(String, graphql_name='warningType')
    message = sgqlc.types.Field(String, graphql_name='message')
    created_at = sgqlc.types.Field(String, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(String, graphql_name='updatedAt')


class DatabricksClusterResponse(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('cluster_id', 'state')
    cluster_id = sgqlc.types.Field(String, graphql_name='clusterId')
    state = sgqlc.types.Field(String, graphql_name='state')


class DatabricksJobResponse(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('workspace_job_id', 'workspace_job_name', 'workspace_notebook_path', 'notebook_source')
    workspace_job_id = sgqlc.types.Field(String, graphql_name='workspaceJobId')
    workspace_job_name = sgqlc.types.Field(String, graphql_name='workspaceJobName')
    workspace_notebook_path = sgqlc.types.Field(String, graphql_name='workspaceNotebookPath')
    notebook_source = sgqlc.types.Field(String, graphql_name='notebookSource')


class DatabricksNotebookLink(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('presigned_url', 'notebook_source')
    presigned_url = sgqlc.types.Field(String, graphql_name='presignedUrl')
    notebook_source = sgqlc.types.Field(String, graphql_name='notebookSource')


class DatasetConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DatasetEdge')), graphql_name='edges')


class DatasetEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('Dataset', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class DbtEdgeConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DbtEdgeEdge')), graphql_name='edges')


class DbtEdgeEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DbtEdge', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class DbtModelResultsConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges', 'edge_count', 'total_count')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DbtModelResultsEdge')), graphql_name='edges')
    edge_count = sgqlc.types.Field(Int, graphql_name='edgeCount')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')


class DbtModelResultsEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DbtRunResult', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class DbtNodeConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DbtNodeEdge')), graphql_name='edges')


class DbtNodeEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DbtNode', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class DbtProjectConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DbtProjectEdge')), graphql_name='edges')


class DbtProjectEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DbtProject', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class DbtRunConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DbtRunEdge')), graphql_name='edges')


class DbtRunEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DbtRun', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class DbtRunResult(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node_id', 'node_name', 'run_started_at', 'started_at', 'execution_time', 'status', 'run_uuid', 'mcon')
    node_id = sgqlc.types.Field(String, graphql_name='nodeId')
    node_name = sgqlc.types.Field(String, graphql_name='nodeName')
    run_started_at = sgqlc.types.Field(DateTime, graphql_name='runStartedAt')
    started_at = sgqlc.types.Field(DateTime, graphql_name='startedAt')
    execution_time = sgqlc.types.Field(Float, graphql_name='executionTime')
    status = sgqlc.types.Field(String, graphql_name='status')
    run_uuid = sgqlc.types.Field(UUID, graphql_name='runUuid')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')


class DbtRunStepConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DbtRunStepEdge')), graphql_name='edges')


class DbtRunStepEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DbtRunStep', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class DbtTestResultsConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges', 'edge_count', 'total_count')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DbtTestResultsEdge')), graphql_name='edges')
    edge_count = sgqlc.types.Field(Int, graphql_name='edgeCount')
    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')


class DbtTestResultsEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DbtTestRunResult', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class DbtTestRunResult(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node_id', 'node_name', 'run_started_at', 'started_at', 'execution_time', 'status', 'run_uuid', 'mcon', 'model_id', 'model_name')
    node_id = sgqlc.types.Field(String, graphql_name='nodeId')
    node_name = sgqlc.types.Field(String, graphql_name='nodeName')
    run_started_at = sgqlc.types.Field(DateTime, graphql_name='runStartedAt')
    started_at = sgqlc.types.Field(DateTime, graphql_name='startedAt')
    execution_time = sgqlc.types.Field(Float, graphql_name='executionTime')
    status = sgqlc.types.Field(String, graphql_name='status')
    run_uuid = sgqlc.types.Field(UUID, graphql_name='runUuid')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    model_id = sgqlc.types.Field(String, graphql_name='modelId')
    model_name = sgqlc.types.Field(String, graphql_name='modelName')


class DeauthorizeSlackAppMutation(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class DeleteAccessToken(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class DeleteAuthorizationGroup(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('deleted',)
    deleted = sgqlc.types.Field(Int, graphql_name='deleted')


class DeleteCatalogObjectMetadata(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class DeleteCustomRule(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('uuid',)
    uuid = sgqlc.types.Field(UUID, graphql_name='uuid')


class DeleteDoc(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class DeleteDomain(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('deleted',)
    deleted = sgqlc.types.Field(Int, graphql_name='deleted')


class DeleteEventOnboardingData(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class DeleteIncidentComment(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class DeleteIntegrationKey(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('deleted',)
    deleted = sgqlc.types.Field(Boolean, graphql_name='deleted')


class DeleteLineageNode(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('objects_deleted',)
    objects_deleted = sgqlc.types.Field(Int, graphql_name='objectsDeleted')


class DeleteLineageNodeBlockPattern(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('pattern',)
    pattern = sgqlc.types.Field('LineageNodeBlockPattern', graphql_name='pattern')


class DeleteMonteCarloConfigTemplate(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('response',)
    response = sgqlc.types.Field('MonteCarloConfigTemplateDeleteResponse', graphql_name='response')


class DeleteNotificationSetting(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('deleted',)
    deleted = sgqlc.types.Field(Int, graphql_name='deleted')


class DeleteObjectProperty(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class DeleteSamlIdentityProvider(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('account',)
    account = sgqlc.types.Field(Account, graphql_name='account')


class DeleteUnifiedUserAssignment(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class DeleteUserInvite(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class DerivedTablePartialLineage(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('mcon', 'columns', 'source_column_used_as_non_selected', 'display_name')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    columns = sgqlc.types.Field(sgqlc.types.list_of('SourceColumn'), graphql_name='columns')
    source_column_used_as_non_selected = sgqlc.types.Field(Boolean, graphql_name='sourceColumnUsedAsNonSelected')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')


class DerivedTablesLineageResult(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('mcon', 'source_column', 'destinations', 'is_last_page', 'cursor')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    source_column = sgqlc.types.Field(String, graphql_name='sourceColumn')
    destinations = sgqlc.types.Field(sgqlc.types.list_of(DerivedTablePartialLineage), graphql_name='destinations')
    is_last_page = sgqlc.types.Field(Boolean, graphql_name='isLastPage')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')


class DimensionLabel(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('timestamp', 'label', 'value')
    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')
    label = sgqlc.types.Field(String, graphql_name='label')
    value = sgqlc.types.Field(Int, graphql_name='value')


class DimensionLabelList(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('timestamp', 'label', 'values')
    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')
    label = sgqlc.types.Field(String, graphql_name='label')
    values = sgqlc.types.Field(sgqlc.types.list_of('DimensionLabelListItem'), graphql_name='values')


class DimensionLabelListItem(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('measurement_timestamp', 'value')
    measurement_timestamp = sgqlc.types.Field(DateTime, graphql_name='measurementTimestamp')
    value = sgqlc.types.Field(Int, graphql_name='value')


class DimensionTracking(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('value', 'mn_cnt', 'mx_cnt', 'mn_fld', 'mn_fq', 'mx_fq', 'reason')
    value = sgqlc.types.Field(String, graphql_name='value')
    mn_cnt = sgqlc.types.Field(Int, graphql_name='mnCnt')
    mx_cnt = sgqlc.types.Field(Int, graphql_name='mxCnt')
    mn_fld = sgqlc.types.Field(Float, graphql_name='mnFld')
    mn_fq = sgqlc.types.Field(Float, graphql_name='mnFq')
    mx_fq = sgqlc.types.Field(Float, graphql_name='mxFq')
    reason = sgqlc.types.Field(String, graphql_name='reason')


class DimensionTrackingSuggestionsConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DimensionTrackingSuggestionsEdge')), graphql_name='edges')


class DimensionTrackingSuggestionsEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DimensionTrackingSuggestions', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class DirectLineage(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('workbook_id', 'friendly_name', 'content_url', 'owner_id', 'project_id', 'project_name', 'created', 'updated', 'total_views', 'workbook_creators', 'view_id', 'category', 'mcon', 'name', 'display_name', 'table_id', 'data_set', 'node_id', 'resource', 'sampling')
    workbook_id = sgqlc.types.Field(String, graphql_name='workbookId')
    friendly_name = sgqlc.types.Field(String, graphql_name='friendlyName')
    content_url = sgqlc.types.Field(String, graphql_name='contentUrl')
    owner_id = sgqlc.types.Field(String, graphql_name='ownerId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    project_name = sgqlc.types.Field(String, graphql_name='projectName')
    created = sgqlc.types.Field(DateTime, graphql_name='created')
    updated = sgqlc.types.Field(DateTime, graphql_name='updated')
    total_views = sgqlc.types.Field(Int, graphql_name='totalViews')
    workbook_creators = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='workbookCreators')
    view_id = sgqlc.types.Field(String, graphql_name='viewId')
    category = sgqlc.types.Field(String, graphql_name='category')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    name = sgqlc.types.Field(String, graphql_name='name')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    table_id = sgqlc.types.Field(String, graphql_name='tableId')
    data_set = sgqlc.types.Field(String, graphql_name='dataSet')
    node_id = sgqlc.types.Field(String, graphql_name='nodeId')
    resource = sgqlc.types.Field(String, graphql_name='resource')
    sampling = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='sampling')


class DirectedGraph(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('vertices', 'edges')
    vertices = sgqlc.types.Field(String, graphql_name='vertices')
    edges = sgqlc.types.Field(String, graphql_name='edges')


class DocAuthorConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DocAuthorEdge')), graphql_name='edges')


class DocAuthorEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DocAuthor', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class DocConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DocEdge')), graphql_name='edges')


class DocEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('Doc', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class DocLinkConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DocLinkEdge')), graphql_name='edges')


class DocLinkEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DocLink', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class DomainOutput(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('uuid', 'name', 'assignments', 'tags')
    uuid = sgqlc.types.Field(UUID, graphql_name='uuid')
    name = sgqlc.types.Field(String, graphql_name='name')
    assignments = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='assignments')
    tags = sgqlc.types.Field(sgqlc.types.list_of('TagKeyValuePairOutput'), graphql_name='tags')


class DomainRestrictionConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DomainRestrictionEdge')), graphql_name='edges')


class DomainRestrictionEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DomainRestriction', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class DownstreamBI(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node_id', 'full_table_id', 'downstream_bi')
    node_id = sgqlc.types.Field(String, graphql_name='nodeId')
    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')
    downstream_bi = sgqlc.types.Field(sgqlc.types.list_of(BiLineage), graphql_name='downstreamBi')


class Dynamic(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('min', 'max', 'reason')
    min = sgqlc.types.Field(Float, graphql_name='min')
    max = sgqlc.types.Field(Float, graphql_name='max')
    reason = sgqlc.types.Field(String, graphql_name='reason')


class EventCommentConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EventCommentEdge')), graphql_name='edges')


class EventCommentEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('EventComment', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class EventConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EventEdge')), graphql_name='edges')


class EventEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('Event', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class EventMutingRule(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id', 'uuid', 'warehouse', 'rule_type', 'rule', 'is_active', 'created_time', 'last_update_time')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    warehouse = sgqlc.types.Field(sgqlc.types.non_null('Warehouse'), graphql_name='warehouse')
    rule_type = sgqlc.types.Field(sgqlc.types.non_null(EventMutingRuleModelRuleType), graphql_name='ruleType')
    rule = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='rule')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    last_update_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='lastUpdateTime')


class EventOnbardingConfig(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('account_uuid', 'config')
    account_uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountUuid')
    config = sgqlc.types.Field(JSONString, graphql_name='config')


class EventStateSummary(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('open', 'false_positive', 'no_action_required', 'notified', 'resolved', 'user_resolved', 'system_resolved', 'muted', 'stale')
    open = sgqlc.types.Field(Int, graphql_name='open')
    false_positive = sgqlc.types.Field(Int, graphql_name='falsePositive')
    no_action_required = sgqlc.types.Field(Int, graphql_name='noActionRequired')
    notified = sgqlc.types.Field(Int, graphql_name='notified')
    resolved = sgqlc.types.Field(Int, graphql_name='resolved')
    user_resolved = sgqlc.types.Field(Int, graphql_name='userResolved')
    system_resolved = sgqlc.types.Field(Int, graphql_name='systemResolved')
    muted = sgqlc.types.Field(Int, graphql_name='muted')
    stale = sgqlc.types.Field(Int, graphql_name='stale')


class EventTypeSummary(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('schema_change', 'fresh_anom', 'unchanged_size_anom', 'json_schema_change', 'delete_table', 'size_anom', 'size_diff', 'metric_anom', 'custom_rule_anom', 'dist_anom', 'query_runtime_anom', 'dbt_model_error', 'dbt_test_failure')
    schema_change = sgqlc.types.Field(Int, graphql_name='schemaChange')
    fresh_anom = sgqlc.types.Field(Int, graphql_name='freshAnom')
    unchanged_size_anom = sgqlc.types.Field(Int, graphql_name='unchangedSizeAnom')
    json_schema_change = sgqlc.types.Field(Int, graphql_name='jsonSchemaChange')
    delete_table = sgqlc.types.Field(Int, graphql_name='deleteTable')
    size_anom = sgqlc.types.Field(Int, graphql_name='sizeAnom')
    size_diff = sgqlc.types.Field(Int, graphql_name='sizeDiff')
    metric_anom = sgqlc.types.Field(Int, graphql_name='metricAnom')
    custom_rule_anom = sgqlc.types.Field(Int, graphql_name='customRuleAnom')
    dist_anom = sgqlc.types.Field(Int, graphql_name='distAnom')
    query_runtime_anom = sgqlc.types.Field(Int, graphql_name='queryRuntimeAnom')
    dbt_model_error = sgqlc.types.Field(Int, graphql_name='dbtModelError')
    dbt_test_failure = sgqlc.types.Field(Int, graphql_name='dbtTestFailure')


class FacetEntry(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'count')
    key = sgqlc.types.Field(String, graphql_name='key')
    count = sgqlc.types.Field(Int, graphql_name='count')


class FacetResults(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('facet_type', 'entries')
    facet_type = sgqlc.types.Field(FacetType, graphql_name='facetType')
    entries = sgqlc.types.Field(sgqlc.types.list_of(FacetEntry), graphql_name='entries')


class FieldDistRcaData(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('time_field', 'anom_time', 'explanatory_field', 'val')
    time_field = sgqlc.types.Field(String, graphql_name='timeField')
    anom_time = sgqlc.types.Field(DateTime, graphql_name='anomTime')
    explanatory_field = sgqlc.types.Field(String, graphql_name='explanatoryField')
    val = sgqlc.types.Field(String, graphql_name='val')


class FieldDistRcaResult(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('rca', 'plot_data', 'low_card_fields_wo_rca')
    rca = sgqlc.types.Field(sgqlc.types.list_of(FieldDistRcaData), graphql_name='rca')
    plot_data = sgqlc.types.Field(sgqlc.types.list_of('RcaPlotData'), graphql_name='plotData', args=sgqlc.types.ArgDict((
        ('field_name', sgqlc.types.Arg(String, graphql_name='fieldName', default=None)),
))
    )
    low_card_fields_wo_rca = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lowCardFieldsWoRca')


class FieldDownstreamBi(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('bi_account_id', 'bi_identifier', 'bi_name', 'bi_type', 'bi_node_id', 'last_seen')
    bi_account_id = sgqlc.types.Field(String, graphql_name='biAccountId')
    bi_identifier = sgqlc.types.Field(String, graphql_name='biIdentifier')
    bi_name = sgqlc.types.Field(String, graphql_name='biName')
    bi_type = sgqlc.types.Field(String, graphql_name='biType')
    bi_node_id = sgqlc.types.Field(String, graphql_name='biNodeId')
    last_seen = sgqlc.types.Field(DateTime, graphql_name='lastSeen')


class FieldHealth(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('lower', 'upper', 'reason')
    lower = sgqlc.types.Field(Float, graphql_name='lower')
    upper = sgqlc.types.Field(Float, graphql_name='upper')
    reason = sgqlc.types.Field(String, graphql_name='reason')


class FieldHealthSuggestionsConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('FieldHealthSuggestionsEdge')), graphql_name='edges')


class FieldHealthSuggestionsEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('FieldHealthSuggestions', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class FieldMetadata(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('field_type', 'table')
    field_type = sgqlc.types.Field(String, graphql_name='fieldType')
    table = sgqlc.types.Field('TableRef', graphql_name='table')


class FieldValueCorrelation(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('field', 'value', 'norm_rate', 'anom_rate')
    field = sgqlc.types.Field(String, graphql_name='field')
    value = sgqlc.types.Field(String, graphql_name='value')
    norm_rate = sgqlc.types.Field(Float, graphql_name='normRate')
    anom_rate = sgqlc.types.Field(Float, graphql_name='anomRate')


class Freshness(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('status', 'expected', 'breach', 'reason', 'last_update')
    status = sgqlc.types.Field(DetectorStatus, graphql_name='status')
    expected = sgqlc.types.Field(Float, graphql_name='expected')
    breach = sgqlc.types.Field(Float, graphql_name='breach')
    reason = sgqlc.types.Field(String, graphql_name='reason')
    last_update = sgqlc.types.Field(DateTime, graphql_name='lastUpdate')


class FreshnessCycleData(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('periodic', 'usual_update_cycle_hours', 'maximal_update_cycle_hours')
    periodic = sgqlc.types.Field(Boolean, graphql_name='periodic')
    usual_update_cycle_hours = sgqlc.types.Field(Int, graphql_name='usualUpdateCycleHours')
    maximal_update_cycle_hours = sgqlc.types.Field(Int, graphql_name='maximalUpdateCycleHours')


class GenerateCollectorTemplate(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('dc',)
    dc = sgqlc.types.Field(DataCollector, graphql_name='dc')


class HighlightSnippets(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('field_name', 'snippets')
    field_name = sgqlc.types.Field(String, graphql_name='fieldName')
    snippets = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='snippets')


class HourlyRowCount(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('timestamp', 'row_count')
    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')
    row_count = sgqlc.types.Field(Int, graphql_name='rowCount')


class HourlyRowCountsResponse(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('hourly_counts', 'time_axis')
    hourly_counts = sgqlc.types.Field(sgqlc.types.list_of(HourlyRowCount), graphql_name='hourlyCounts')
    time_axis = sgqlc.types.Field('TimeAxis', graphql_name='timeAxis')


class ICustomRulesMonitor(sgqlc.types.Interface):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('has_custom_rule_name', 'rule_description', 'rule_comparisons', 'rule_notes', 'rule_variables', 'is_snoozed', 'snooze_until_time', 'slack_snooze_user', 'breach_rate', 'interval_minutes')
    has_custom_rule_name = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasCustomRuleName')
    rule_description = sgqlc.types.Field(String, graphql_name='ruleDescription')
    rule_comparisons = sgqlc.types.Field(sgqlc.types.list_of(CustomRuleComparison), graphql_name='ruleComparisons')
    rule_notes = sgqlc.types.Field(String, graphql_name='ruleNotes')
    rule_variables = sgqlc.types.Field(JSONString, graphql_name='ruleVariables')
    is_snoozed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSnoozed')
    snooze_until_time = sgqlc.types.Field(DateTime, graphql_name='snoozeUntilTime')
    slack_snooze_user = sgqlc.types.Field(String, graphql_name='slackSnoozeUser')
    breach_rate = sgqlc.types.Field(String, graphql_name='breachRate')
    interval_minutes = sgqlc.types.Field(Int, graphql_name='intervalMinutes')


class IMetricsMonitor(sgqlc.types.Interface):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('monitor_fields', 'monitor_time_axis_field_name', 'monitor_time_axis_field_type', 'where_condition', 'segmented_expressions', 'history_days', 'select_expressions', 'agg_time_interval')
    monitor_fields = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='monitorFields')
    monitor_time_axis_field_name = sgqlc.types.Field(String, graphql_name='monitorTimeAxisFieldName')
    monitor_time_axis_field_type = sgqlc.types.Field(String, graphql_name='monitorTimeAxisFieldType')
    where_condition = sgqlc.types.Field(String, graphql_name='whereCondition')
    segmented_expressions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='segmentedExpressions')
    history_days = sgqlc.types.Field(Int, graphql_name='historyDays')
    select_expressions = sgqlc.types.Field(sgqlc.types.list_of('MetricMonitorSelectExpression'), graphql_name='selectExpressions')
    agg_time_interval = sgqlc.types.Field(MonitorAggTimeInterval, graphql_name='aggTimeInterval')


class IMonitor(sgqlc.types.Interface):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('uuid', 'monitor_type', 'created_time', 'creator_id', 'resource_id', 'entities', 'schedule_type', 'rule_name', 'description', 'notes', 'labels', 'is_snoozeable', 'is_paused', 'is_template_managed', 'namespace', 'next_execution_time', 'prev_execution_time', 'is_transitioning_data_provider', 'schedule_config')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    monitor_type = sgqlc.types.Field(sgqlc.types.non_null(UserDefinedMonitors), graphql_name='monitorType')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    creator_id = sgqlc.types.Field(String, graphql_name='creatorId')
    resource_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceId')
    entities = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='entities')
    schedule_type = sgqlc.types.Field(String, graphql_name='scheduleType')
    rule_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ruleName')
    description = sgqlc.types.Field(String, graphql_name='description')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    labels = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='labels')
    is_snoozeable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSnoozeable')
    is_paused = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPaused')
    is_template_managed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTemplateManaged')
    namespace = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='namespace')
    next_execution_time = sgqlc.types.Field(DateTime, graphql_name='nextExecutionTime')
    prev_execution_time = sgqlc.types.Field(DateTime, graphql_name='prevExecutionTime')
    is_transitioning_data_provider = sgqlc.types.Field(Boolean, graphql_name='isTransitioningDataProvider')
    schedule_config = sgqlc.types.Field('ScheduleConfigOutput', graphql_name='scheduleConfig')


class IMonitorStatus(sgqlc.types.Interface):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('monitor_status', 'exceptions')
    monitor_status = sgqlc.types.Field(sgqlc.types.non_null(MonitorStatusType), graphql_name='monitorStatus')
    exceptions = sgqlc.types.Field(String, graphql_name='exceptions')


class ImportDbtManifest(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('response',)
    response = sgqlc.types.Field('ImportDbtManifestResponse', graphql_name='response')


class ImportDbtManifestResponse(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node_ids_imported', 'node_import_info')
    node_ids_imported = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nodeIdsImported')
    node_import_info = sgqlc.types.Field(sgqlc.types.list_of('NodeImportInfo'), graphql_name='nodeImportInfo')


class ImportDbtRunResults(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('response',)
    response = sgqlc.types.Field('ImportDbtRunResultsResponse', graphql_name='response')


class ImportDbtRunResultsResponse(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('num_results_imported',)
    num_results_imported = sgqlc.types.Field(Int, graphql_name='numResultsImported')


class IncidentConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('IncidentEdge')), graphql_name='edges')


class IncidentDashboardData(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('total_incident_count', 'no_status_count', 'investigating_count', 'fixed_count', 'expected_and_no_action_count')
    total_incident_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalIncidentCount')
    no_status_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='noStatusCount')
    investigating_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='investigatingCount')
    fixed_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fixedCount')
    expected_and_no_action_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='expectedAndNoActionCount')


class IncidentEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('Incident', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class IncidentReactionConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('IncidentReactionEdge')), graphql_name='edges')


class IncidentReactionEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('IncidentReaction', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class IncidentSummary(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('incident_id', 'types', 'states', 'tables', 'key_assets', 'has_rca')
    incident_id = sgqlc.types.Field(UUID, graphql_name='incidentId')
    types = sgqlc.types.Field(EventTypeSummary, graphql_name='types')
    states = sgqlc.types.Field(EventStateSummary, graphql_name='states')
    tables = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tables')
    key_assets = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='keyAssets')
    has_rca = sgqlc.types.Field(Boolean, graphql_name='hasRca')


class IncidentTableMcons(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('tables',)
    tables = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tables')


class IncidentTimePeriodAggregateData(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('start_date', 'end_date', 'values')
    start_date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='startDate')
    end_date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='endDate')
    values = sgqlc.types.Field(sgqlc.types.list_of('LabelCount'), graphql_name='values')


class IncidentTypeSummary(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('anomalies', 'schema_changes', 'deleted_tables', 'metric_anomalies', 'custom_rule_anomalies', 'performance_anomalies', 'dbt_errors', 'pseudo_integration_test')
    anomalies = sgqlc.types.Field(Int, graphql_name='anomalies')
    schema_changes = sgqlc.types.Field(Int, graphql_name='schemaChanges')
    deleted_tables = sgqlc.types.Field(Int, graphql_name='deletedTables')
    metric_anomalies = sgqlc.types.Field(Int, graphql_name='metricAnomalies')
    custom_rule_anomalies = sgqlc.types.Field(Int, graphql_name='customRuleAnomalies')
    performance_anomalies = sgqlc.types.Field(Int, graphql_name='performanceAnomalies')
    dbt_errors = sgqlc.types.Field(Int, graphql_name='dbtErrors')
    pseudo_integration_test = sgqlc.types.Field(Int, graphql_name='pseudoIntegrationTest')


class IncidentWeeklyDataDashboard(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('weekly_data',)
    weekly_data = sgqlc.types.Field(sgqlc.types.list_of(IncidentTimePeriodAggregateData), graphql_name='weeklyData')


class Insight(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name', 'title', 'usage', 'description', 'reports', 'available')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    usage = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='usage')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    reports = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Report')), graphql_name='reports')
    available = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='available')


class IntegrationKey(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id', 'secret')
    id = sgqlc.types.Field(String, graphql_name='id')
    secret = sgqlc.types.Field(String, graphql_name='secret')


class IntegrationKeyMetadata(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id', 'description', 'scope', 'warehouses', 'created_time', 'created_by')
    id = sgqlc.types.Field(String, graphql_name='id')
    description = sgqlc.types.Field(String, graphql_name='description')
    scope = sgqlc.types.Field(String, graphql_name='scope')
    warehouses = sgqlc.types.Field(sgqlc.types.list_of('Warehouse'), graphql_name='warehouses')
    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    created_by = sgqlc.types.Field('User', graphql_name='createdBy')


class InternalNotifications(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('type', 'friendly_message', 'details', 'is_urgent', 'expiration_date')
    type = sgqlc.types.Field(String, graphql_name='type')
    friendly_message = sgqlc.types.Field(String, graphql_name='friendlyMessage')
    details = sgqlc.types.Field(JSONString, graphql_name='details')
    is_urgent = sgqlc.types.Field(Boolean, graphql_name='isUrgent')
    expiration_date = sgqlc.types.Field(DateTime, graphql_name='expirationDate')


class InvestigationQuery(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('query', 'has_error')
    query = sgqlc.types.Field(String, graphql_name='query')
    has_error = sgqlc.types.Field(Boolean, graphql_name='hasError')


class InviteUsersPayload(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('users', 'client_mutation_id')
    users = sgqlc.types.Field(sgqlc.types.list_of('UserInvite'), graphql_name='users')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class InviteUsersV2(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('invites', 'existing_users', 'already_invited')
    invites = sgqlc.types.Field(sgqlc.types.list_of('UserInvite'), graphql_name='invites')
    existing_users = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='existingUsers')
    already_invited = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='alreadyInvited')


class JobError(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('message', 'job_execution_uuid', 'dc_schedule_uuid', 'timestamp', 'result_count', 'job_type', 'stack_name', 'data_collector_uuid')
    message = sgqlc.types.Field(String, graphql_name='message')
    job_execution_uuid = sgqlc.types.Field(UUID, graphql_name='jobExecutionUuid')
    dc_schedule_uuid = sgqlc.types.Field(UUID, graphql_name='dcScheduleUuid')
    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')
    result_count = sgqlc.types.Field(Int, graphql_name='resultCount')
    job_type = sgqlc.types.Field(String, graphql_name='jobType')
    stack_name = sgqlc.types.Field(String, graphql_name='stackName')
    data_collector_uuid = sgqlc.types.Field(UUID, graphql_name='dataCollectorUuid')


class JobExecutionException(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('type', 'description', 'sql_query')
    type = sgqlc.types.Field(String, graphql_name='type')
    description = sgqlc.types.Field(String, graphql_name='description')
    sql_query = sgqlc.types.Field(String, graphql_name='sqlQuery')


class JobExecutionHistoryLog(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('job_execution_uuid', 'start_time', 'status', 'end_time', 'exceptions', 'exceptions_detail')
    job_execution_uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='jobExecutionUuid')
    start_time = sgqlc.types.Field(DateTime, graphql_name='startTime')
    status = sgqlc.types.Field(JobExecutionStatus, graphql_name='status')
    end_time = sgqlc.types.Field(DateTime, graphql_name='endTime')
    exceptions = sgqlc.types.Field(String, graphql_name='exceptions')
    exceptions_detail = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(JobExecutionException)), graphql_name='exceptionsDetail')


class LabelCount(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('label', 'count')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')


class LastSizeChange(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('timestamp', 'size')
    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')
    size = sgqlc.types.Field(Float, graphql_name='size')


class LastUpdates(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('last_updates', 'time_interval_in_sec')
    last_updates = sgqlc.types.Field(sgqlc.types.list_of('TableUpdateTime'), graphql_name='lastUpdates')
    time_interval_in_sec = sgqlc.types.Field(Int, graphql_name='timeIntervalInSec')


class LineageEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('edge_id', 'source', 'dest', 'account_id', 'version', 'job_ts', 'expire_at', 'created_time', 'last_update_user', 'last_update_time')
    edge_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='edgeId')
    source = sgqlc.types.Field(sgqlc.types.non_null('LineageNode'), graphql_name='source')
    dest = sgqlc.types.Field(sgqlc.types.non_null('LineageNode'), graphql_name='dest')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='version')
    job_ts = sgqlc.types.Field(DateTime, graphql_name='jobTs')
    expire_at = sgqlc.types.Field(DateTime, graphql_name='expireAt')
    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    last_update_user = sgqlc.types.Field('User', graphql_name='lastUpdateUser')
    last_update_time = sgqlc.types.Field(DateTime, graphql_name='lastUpdateTime')


class LineageNode(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node_id', 'mcon', 'account_id', 'resource_id', 'object_type', 'name', 'display_name', 'version', 'job_ts', 'extra', 'created_time', 'last_update_user', 'last_update_time')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nodeId')
    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    resource_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceId')
    object_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='objectType')
    name = sgqlc.types.Field(String, graphql_name='name')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='version')
    job_ts = sgqlc.types.Field(DateTime, graphql_name='jobTs')
    extra = sgqlc.types.Field(JSONString, graphql_name='extra')
    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    last_update_user = sgqlc.types.Field('User', graphql_name='lastUpdateUser')
    last_update_time = sgqlc.types.Field(DateTime, graphql_name='lastUpdateTime')


class LineageNodeBlockPattern(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id', 'uuid', 'account_id', 'resource_id', 'dataset_regexp', 'project_regexp', 'table_regexp', 'created_time', 'last_update_user', 'last_update_time')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    resource_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceId')
    dataset_regexp = sgqlc.types.Field(String, graphql_name='datasetRegexp')
    project_regexp = sgqlc.types.Field(String, graphql_name='projectRegexp')
    table_regexp = sgqlc.types.Field(String, graphql_name='tableRegexp')
    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    last_update_user = sgqlc.types.Field('User', graphql_name='lastUpdateUser')
    last_update_time = sgqlc.types.Field(DateTime, graphql_name='lastUpdateTime')


class LineageSources(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('mcon', 'source_columns')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    source_columns = sgqlc.types.Field(sgqlc.types.list_of('SourceColumn'), graphql_name='sourceColumns')


class LookerDashboardTileRef(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('tile_id', 'tile_title')
    tile_id = sgqlc.types.Field(String, graphql_name='tileId')
    tile_title = sgqlc.types.Field(String, graphql_name='tileTitle')


class MetricAnomalyCorrelation(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('field', 'metric', 'correlations')
    field = sgqlc.types.Field(String, graphql_name='field')
    metric = sgqlc.types.Field(String, graphql_name='metric')
    correlations = sgqlc.types.Field(sgqlc.types.list_of(FieldValueCorrelation), graphql_name='correlations')


class MetricCorrelationResult(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('metric_anomalies',)
    metric_anomalies = sgqlc.types.Field(sgqlc.types.list_of(MetricAnomalyCorrelation), graphql_name='metricAnomalies')


class MetricDimensions(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('rank', 'label')
    rank = sgqlc.types.Field(Float, graphql_name='rank')
    label = sgqlc.types.Field(String, graphql_name='label')


class MetricMonitorSelectExpression(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id', 'metric_monitor', 'expression', 'data_type', 'is_raw_column_name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    metric_monitor = sgqlc.types.Field(sgqlc.types.non_null('MetricMonitoring'), graphql_name='metricMonitor')
    expression = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='expression')
    data_type = sgqlc.types.Field(MetricMonitorSelectExpressionModelDataType, graphql_name='dataType')
    is_raw_column_name = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRawColumnName')


class MetricMonitoringConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('MetricMonitoringEdge')), graphql_name='edges')


class MetricMonitoringEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('MetricMonitoring', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class MetricSampling(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('columns', 'rows', 'query', 'has_error')
    columns = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='columns')
    rows = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of(String)), graphql_name='rows')
    query = sgqlc.types.Field(String, graphql_name='query')
    has_error = sgqlc.types.Field(Boolean, graphql_name='hasError')


class MetricValueByTable(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('value', 'full_table_id', 'resource_id')
    value = sgqlc.types.Field(DateTime, graphql_name='value')
    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')
    resource_id = sgqlc.types.Field(String, graphql_name='resourceId')


class Metrics(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('metrics', 'is_partial_date_range')
    metrics = sgqlc.types.Field(sgqlc.types.list_of('TableMetricV2'), graphql_name='metrics')
    is_partial_date_range = sgqlc.types.Field(Boolean, graphql_name='isPartialDateRange')


class MigrateCollectorResources(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class MonitorConfiguration(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('time_field', 'aggregation_type', 'lookback_days')
    time_field = sgqlc.types.Field(String, graphql_name='timeField')
    aggregation_type = sgqlc.types.Field(MonitorAggTimeInterval, graphql_name='aggregationType')
    lookback_days = sgqlc.types.Field(Int, graphql_name='lookbackDays')


class MonitorDashboardData(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('total_monitor_count', 'paused_count', 'snoozed_count', 'active_count', 'training_count', 'misconfigured_count', 'error_count', 'in_progress_count', 'no_status_count')
    total_monitor_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalMonitorCount')
    paused_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pausedCount')
    snoozed_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='snoozedCount')
    active_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='activeCount')
    training_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='trainingCount')
    misconfigured_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='misconfiguredCount')
    error_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='errorCount')
    in_progress_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='inProgressCount')
    no_status_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='noStatusCount')


class MonitorLabel(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('label',)
    label = sgqlc.types.Field(String, graphql_name='label')


class MonitorLabelObject(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('uuid', 'label', 'metricmonitoringmodel_set', 'customrulemodel_set')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    metricmonitoringmodel_set = sgqlc.types.Field(sgqlc.types.non_null(MetricMonitoringConnection), graphql_name='metricmonitoringmodelSet', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    customrulemodel_set = sgqlc.types.Field(sgqlc.types.non_null(CustomRuleConnection), graphql_name='customrulemodelSet', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('rule_type', sgqlc.types.Arg(String, graphql_name='ruleType', default=None)),
))
    )


class MonitorSchedulingConfiguration(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('schedule_type', 'interval_minutes', 'start_time')
    schedule_type = sgqlc.types.Field(String, graphql_name='scheduleType')
    interval_minutes = sgqlc.types.Field(Int, graphql_name='intervalMinutes')
    start_time = sgqlc.types.Field(DateTime, graphql_name='startTime')


class MonitorSummary(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('resources', 'stats', 'categories', 'hourly_stats', 'json_schema', 'custom_sql', 'table_metric')
    resources = sgqlc.types.Field('TableResources', graphql_name='resources')
    stats = sgqlc.types.Field(Int, graphql_name='stats')
    categories = sgqlc.types.Field(Int, graphql_name='categories')
    hourly_stats = sgqlc.types.Field(Int, graphql_name='hourlyStats')
    json_schema = sgqlc.types.Field(Int, graphql_name='jsonSchema')
    custom_sql = sgqlc.types.Field(Int, graphql_name='customSql')
    table_metric = sgqlc.types.Field(Int, graphql_name='tableMetric')


class MonteCarloConfigTemplateConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('MonteCarloConfigTemplateEdge')), graphql_name='edges')


class MonteCarloConfigTemplateDeleteResponse(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('num_deleted', 'changes_applied')
    num_deleted = sgqlc.types.Field(Int, graphql_name='numDeleted')
    changes_applied = sgqlc.types.Field(Boolean, graphql_name='changesApplied')


class MonteCarloConfigTemplateEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('MonteCarloConfigTemplate', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class MonteCarloConfigTemplateUpdateResponse(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('resource_modifications', 'changes_applied', 'errors_as_json')
    resource_modifications = sgqlc.types.Field(sgqlc.types.list_of('ResourceModification'), graphql_name='resourceModifications')
    changes_applied = sgqlc.types.Field(Boolean, graphql_name='changesApplied')
    errors_as_json = sgqlc.types.Field(String, graphql_name='errorsAsJson')


class MultipleDirectLineage(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('workbook_id', 'friendly_name', 'content_url', 'owner_id', 'project_id', 'project_name', 'created', 'updated', 'total_views', 'workbook_creators', 'view_id', 'category', 'mcon', 'name', 'display_name', 'table_id', 'data_set', 'node_id', 'resource', 'sampling', 'downstream', 'upstream')
    workbook_id = sgqlc.types.Field(String, graphql_name='workbookId')
    friendly_name = sgqlc.types.Field(String, graphql_name='friendlyName')
    content_url = sgqlc.types.Field(String, graphql_name='contentUrl')
    owner_id = sgqlc.types.Field(String, graphql_name='ownerId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    project_name = sgqlc.types.Field(String, graphql_name='projectName')
    created = sgqlc.types.Field(DateTime, graphql_name='created')
    updated = sgqlc.types.Field(DateTime, graphql_name='updated')
    total_views = sgqlc.types.Field(Int, graphql_name='totalViews')
    workbook_creators = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='workbookCreators')
    view_id = sgqlc.types.Field(String, graphql_name='viewId')
    category = sgqlc.types.Field(String, graphql_name='category')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    name = sgqlc.types.Field(String, graphql_name='name')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    table_id = sgqlc.types.Field(String, graphql_name='tableId')
    data_set = sgqlc.types.Field(String, graphql_name='dataSet')
    node_id = sgqlc.types.Field(String, graphql_name='nodeId')
    resource = sgqlc.types.Field(String, graphql_name='resource')
    sampling = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='sampling')
    downstream = sgqlc.types.Field(sgqlc.types.list_of(DirectLineage), graphql_name='downstream')
    upstream = sgqlc.types.Field(sgqlc.types.list_of(DirectLineage), graphql_name='upstream')


class Mutation(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('update_monitor_name', 'update_monitor_notes', 'update_monitor_labels', 'create_or_update_doc', 'delete_doc', 'create_custom_user', 'create_unified_user_assignment', 'delete_unified_user_assignment', 'import_dbt_manifest', 'upload_dbt_manifest', 'import_dbt_run_results', 'upload_dbt_run_results', 'create_dbt_project', 'set_generates_incidents', 'create_or_update_monte_carlo_config_template', 'delete_monte_carlo_config_template', 'set_sensitivity', 'create_custom_rule', 'create_or_update_custom_rule', 'create_or_update_volume_rule', 'create_custom_metric_rule', 'create_or_update_custom_metric_rule', 'update_custom_metric_rule_notes', 'create_or_update_freshness_custom_rule', 'snooze_custom_rule', 'unsnooze_custom_rule', 'delete_custom_rule', 'trigger_custom_rule', 'trigger_circuit_breaker_rule', 'run_sql_rule', 'create_or_update_lineage_node', 'create_or_update_lineage_edge', 'create_or_update_lineage_node_block_pattern', 'delete_lineage_node', 'delete_lineage_node_block_pattern', 'create_or_update_catalog_object_metadata', 'delete_catalog_object_metadata', 'create_or_update_object_property', 'delete_object_property', 'bulk_create_or_update_object_properties', 'stop_monitor', 'trigger_monitor', 'create_or_update_monitor', 'pause_monitor', 'validate_cron', 'create_event_comment', 'update_event_comment', 'delete_event_comment', 'set_incident_feedback', 'set_incident_reaction', 'set_incident_severity', 'set_incident_owner', 'create_or_update_incident_comment', 'delete_incident_comment', 'create_or_update_domain', 'delete_domain', 'create_or_update_authorization_group', 'delete_authorization_group', 'update_user_authorization_group_membership', 'create_or_update_resource', 'toggle_disable_sampling', 'toggle_disable_value_ingestion', 'toggle_enable_full_distribution_metrics', 'save_table_importance_stats', 'set_default_incident_group_interval', 'update_user_state', 'set_account_name', 'set_warehouse_name', 'create_or_update_saml_identity_provider', 'delete_saml_identity_provider', 'invite_users', 'invite_users_v2', 'delete_user_invite', 'resend_user_invite', 'remove_user_from_account', 'track_table', 'upload_credentials', 'save_slack_credentials', 'deauthorize_slack_app', 'test_credentials', 'test_database_credentials', 'test_presto_credentials', 'test_snowflake_credentials', 'test_hive_credentials', 'test_s3_credentials', 'test_glue_credentials', 'test_athena_credentials', 'test_looker_credentials', 'test_looker_git_credentials', 'test_looker_git_ssh_credentials', 'test_looker_git_clone_credentials', 'test_dbt_cloud_credentials', 'test_bq_credentials', 'test_spark_credentials', 'test_self_hosted_credentials', 'add_tableau_account', 'test_tableau_credentials', 'test_power_bi_credentials', 'toggle_mute_dataset', 'toggle_mute_table', 'toggle_mute_datasets', 'toggle_mute_tables', 'toggle_mute_with_regex', 'delete_notification_settings', 'add_connection', 'remove_connection', 'add_bi_connection', 'toggle_event_config', 'create_access_token', 'delete_access_token', 'generate_collector_template', 'create_or_update_notification_setting', 'update_credentials', 'create_collector_record', 'cleanup_collector_record', 'migrate_collector_resources', 'update_slack_channels', 'create_integration_key', 'delete_integration_key', 'create_databricks_secret', 'create_databricks_notebook_job', 'update_databricks_notebook_job', 'update_databricks_notebook', 'start_databricks_cluster', 'test_databricks_credentials', 'test_delta_credentials', 'add_databricks_connection', 'save_event_onboarding_data', 'delete_event_onboarding_data')
    update_monitor_name = sgqlc.types.Field('UpdateMonitorName', graphql_name='updateMonitorName', args=sgqlc.types.ArgDict((
        ('monitor_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='monitorType', default=None)),
        ('monitor_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='monitorUuid', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    update_monitor_notes = sgqlc.types.Field('UpdateMonitorNotes', graphql_name='updateMonitorNotes', args=sgqlc.types.ArgDict((
        ('monitor_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='monitorType', default=None)),
        ('monitor_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='monitorUuid', default=None)),
        ('notes', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='notes', default=None)),
))
    )
    update_monitor_labels = sgqlc.types.Field('UpdateMonitorLabels', graphql_name='updateMonitorLabels', args=sgqlc.types.ArgDict((
        ('labels', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='labels', default=None)),
        ('monitor_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='monitorType', default=None)),
        ('monitor_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='monitorUuid', default=None)),
))
    )
    create_or_update_doc = sgqlc.types.Field(CreateOrUpdateDoc, graphql_name='createOrUpdateDoc', args=sgqlc.types.ArgDict((
        ('content', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='content', default=None)),
        ('doc_mcon', sgqlc.types.Arg(String, graphql_name='docMcon', default=None)),
        ('parent_doc_mcon', sgqlc.types.Arg(String, graphql_name='parentDocMcon', default=None)),
        ('title', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='title', default=None)),
))
    )
    delete_doc = sgqlc.types.Field(DeleteDoc, graphql_name='deleteDoc', args=sgqlc.types.ArgDict((
        ('doc_mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='docMcon', default=None)),
))
    )
    create_custom_user = sgqlc.types.Field(CreateCustomUser, graphql_name='createCustomUser', args=sgqlc.types.ArgDict((
        ('email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='email', default=None)),
        ('first_name', sgqlc.types.Arg(String, graphql_name='firstName', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='lastName', default=None)),
))
    )
    create_unified_user_assignment = sgqlc.types.Field(CreateUnifiedUserAssignment, graphql_name='createUnifiedUserAssignment', args=sgqlc.types.ArgDict((
        ('object_mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='objectMcon', default=None)),
        ('relationship_type', sgqlc.types.Arg(sgqlc.types.non_null(RelationshipType), graphql_name='relationshipType', default=None)),
        ('unified_user_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='unifiedUserId', default=None)),
))
    )
    delete_unified_user_assignment = sgqlc.types.Field(DeleteUnifiedUserAssignment, graphql_name='deleteUnifiedUserAssignment', args=sgqlc.types.ArgDict((
        ('object_mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='objectMcon', default=None)),
        ('unified_user_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='unifiedUserId', default=None)),
))
    )
    import_dbt_manifest = sgqlc.types.Field(ImportDbtManifest, graphql_name='importDbtManifest', args=sgqlc.types.ArgDict((
        ('dbt_schema_version', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='dbtSchemaVersion', default=None)),
        ('default_resource', sgqlc.types.Arg(String, graphql_name='defaultResource', default=None)),
        ('manifest_nodes_json', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='manifestNodesJson', default=None)),
        ('project_name', sgqlc.types.Arg(String, graphql_name='projectName', default=None)),
))
    )
    upload_dbt_manifest = sgqlc.types.Field('UploadDbtManifest', graphql_name='uploadDbtManifest', args=sgqlc.types.ArgDict((
        ('batch', sgqlc.types.Arg(Int, graphql_name='batch', default=1)),
        ('dbt_schema_version', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='dbtSchemaVersion', default=None)),
        ('default_resource', sgqlc.types.Arg(String, graphql_name='defaultResource', default=None)),
        ('invocation_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='invocationId', default=None)),
        ('manifest_nodes_json', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='manifestNodesJson', default=None)),
        ('project_name', sgqlc.types.Arg(String, graphql_name='projectName', default=None)),
))
    )
    import_dbt_run_results = sgqlc.types.Field(ImportDbtRunResults, graphql_name='importDbtRunResults', args=sgqlc.types.ArgDict((
        ('dbt_schema_version', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='dbtSchemaVersion', default=None)),
        ('project_name', sgqlc.types.Arg(String, graphql_name='projectName', default=None)),
        ('run_id', sgqlc.types.Arg(String, graphql_name='runId', default=None)),
        ('run_logs', sgqlc.types.Arg(String, graphql_name='runLogs', default=None)),
        ('run_results_json', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='runResultsJson', default=None)),
))
    )
    upload_dbt_run_results = sgqlc.types.Field('UploadDbtRunResults', graphql_name='uploadDbtRunResults', args=sgqlc.types.ArgDict((
        ('batch', sgqlc.types.Arg(Int, graphql_name='batch', default=1)),
        ('dbt_schema_version', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='dbtSchemaVersion', default=None)),
        ('invocation_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='invocationId', default=None)),
        ('project_name', sgqlc.types.Arg(String, graphql_name='projectName', default=None)),
        ('run_id', sgqlc.types.Arg(String, graphql_name='runId', default=None)),
        ('run_logs', sgqlc.types.Arg(String, graphql_name='runLogs', default=None)),
        ('run_results_json', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='runResultsJson', default=None)),
))
    )
    create_dbt_project = sgqlc.types.Field(CreateDbtProject, graphql_name='createDbtProject', args=sgqlc.types.ArgDict((
        ('project_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='projectName', default=None)),
        ('source', sgqlc.types.Arg(sgqlc.types.non_null(DbtProjectSource), graphql_name='source', default=None)),
))
    )
    set_generates_incidents = sgqlc.types.Field('SetGeneratesIncidents', graphql_name='setGeneratesIncidents', args=sgqlc.types.ArgDict((
        ('generates_incidents', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='generatesIncidents', default=None)),
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='uuid', default=None)),
))
    )
    create_or_update_monte_carlo_config_template = sgqlc.types.Field(CreateOrUpdateMonteCarloConfigTemplate, graphql_name='createOrUpdateMonteCarloConfigTemplate', args=sgqlc.types.ArgDict((
        ('config_template_json', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='configTemplateJson', default=None)),
        ('dry_run', sgqlc.types.Arg(Boolean, graphql_name='dryRun', default=None)),
        ('namespace', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='namespace', default=None)),
        ('resource', sgqlc.types.Arg(String, graphql_name='resource', default=None)),
))
    )
    delete_monte_carlo_config_template = sgqlc.types.Field(DeleteMonteCarloConfigTemplate, graphql_name='deleteMonteCarloConfigTemplate', args=sgqlc.types.ArgDict((
        ('dry_run', sgqlc.types.Arg(Boolean, graphql_name='dryRun', default=None)),
        ('namespace', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='namespace', default=None)),
))
    )
    set_sensitivity = sgqlc.types.Field('SetSensitivity', graphql_name='setSensitivity', args=sgqlc.types.ArgDict((
        ('event_type', sgqlc.types.Arg(String, graphql_name='eventType', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('monitor_uuid', sgqlc.types.Arg(UUID, graphql_name='monitorUuid', default=None)),
        ('threshold', sgqlc.types.Arg(SensitivityInput, graphql_name='threshold', default=None)),
))
    )
    create_custom_rule = sgqlc.types.Field(CreateCustomRule, graphql_name='createCustomRule', args=sgqlc.types.ArgDict((
        ('comparisons', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(CustomRuleComparisonInput)), graphql_name='comparisons', default=None)),
        ('custom_rule_uuid', sgqlc.types.Arg(UUID, graphql_name='customRuleUuid', default=None)),
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('interval_minutes', sgqlc.types.Arg(Int, graphql_name='intervalMinutes', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('notes', sgqlc.types.Arg(String, graphql_name='notes', default=None)),
        ('schedule_config', sgqlc.types.Arg(ScheduleConfigInput, graphql_name='scheduleConfig', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('timezone', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='timezone', default=None)),
))
    )
    create_or_update_custom_rule = sgqlc.types.Field(CreateOrUpdateCustomRule, graphql_name='createOrUpdateCustomRule', args=sgqlc.types.ArgDict((
        ('comparisons', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(CustomRuleComparisonInput)), graphql_name='comparisons', default=None)),
        ('custom_rule_uuid', sgqlc.types.Arg(UUID, graphql_name='customRuleUuid', default=None)),
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('interval_minutes', sgqlc.types.Arg(Int, graphql_name='intervalMinutes', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('notes', sgqlc.types.Arg(String, graphql_name='notes', default=None)),
        ('schedule_config', sgqlc.types.Arg(ScheduleConfigInput, graphql_name='scheduleConfig', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('timezone', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='timezone', default=None)),
))
    )
    create_or_update_volume_rule = sgqlc.types.Field(CreateOrUpdateVolumeRule, graphql_name='createOrUpdateVolumeRule', args=sgqlc.types.ArgDict((
        ('comparisons', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(CustomRuleComparisonInput)), graphql_name='comparisons', default=None)),
        ('custom_rule_uuid', sgqlc.types.Arg(UUID, graphql_name='customRuleUuid', default=None)),
        ('data_collection_schedule_config', sgqlc.types.Arg(ScheduleConfigInput, graphql_name='dataCollectionScheduleConfig', default=None)),
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('notes', sgqlc.types.Arg(String, graphql_name='notes', default=None)),
        ('override', sgqlc.types.Arg(Boolean, graphql_name='override', default=None)),
        ('schedule_config', sgqlc.types.Arg(sgqlc.types.non_null(ScheduleConfigInput), graphql_name='scheduleConfig', default=None)),
        ('timezone', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='timezone', default=None)),
))
    )
    create_custom_metric_rule = sgqlc.types.Field(CreateCustomMetricRule, graphql_name='createCustomMetricRule', args=sgqlc.types.ArgDict((
        ('comparisons', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(CustomRuleComparisonInput)), graphql_name='comparisons', default=None)),
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
        ('custom_rule_uuid', sgqlc.types.Arg(UUID, graphql_name='customRuleUuid', default=None)),
        ('custom_sampling_sql', sgqlc.types.Arg(String, graphql_name='customSamplingSql', default=None)),
        ('custom_sql', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='customSql', default=None)),
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
        ('interval_minutes', sgqlc.types.Arg(Int, graphql_name='intervalMinutes', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('notes', sgqlc.types.Arg(String, graphql_name='notes', default=None)),
        ('query_result_type', sgqlc.types.Arg(QueryResultType, graphql_name='queryResultType', default=None)),
        ('schedule_config', sgqlc.types.Arg(ScheduleConfigInput, graphql_name='scheduleConfig', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('timezone', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='timezone', default=None)),
        ('variables', sgqlc.types.Arg(JSONString, graphql_name='variables', default=None)),
))
    )
    create_or_update_custom_metric_rule = sgqlc.types.Field(CreateOrUpdateCustomMetricRule, graphql_name='createOrUpdateCustomMetricRule', args=sgqlc.types.ArgDict((
        ('comparisons', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(CustomRuleComparisonInput)), graphql_name='comparisons', default=None)),
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
        ('custom_rule_uuid', sgqlc.types.Arg(UUID, graphql_name='customRuleUuid', default=None)),
        ('custom_sampling_sql', sgqlc.types.Arg(String, graphql_name='customSamplingSql', default=None)),
        ('custom_sql', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='customSql', default=None)),
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
        ('interval_minutes', sgqlc.types.Arg(Int, graphql_name='intervalMinutes', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('notes', sgqlc.types.Arg(String, graphql_name='notes', default=None)),
        ('query_result_type', sgqlc.types.Arg(QueryResultType, graphql_name='queryResultType', default=None)),
        ('schedule_config', sgqlc.types.Arg(ScheduleConfigInput, graphql_name='scheduleConfig', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('timezone', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='timezone', default=None)),
        ('variables', sgqlc.types.Arg(JSONString, graphql_name='variables', default=None)),
))
    )
    update_custom_metric_rule_notes = sgqlc.types.Field('UpdateCustomMetricRuleNotes', graphql_name='updateCustomMetricRuleNotes', args=sgqlc.types.ArgDict((
        ('custom_rule_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='customRuleUuid', default=None)),
        ('notes', sgqlc.types.Arg(String, graphql_name='notes', default=None)),
))
    )
    create_or_update_freshness_custom_rule = sgqlc.types.Field(CreateOrUpdateFreshnessCustomRule, graphql_name='createOrUpdateFreshnessCustomRule', args=sgqlc.types.ArgDict((
        ('comparisons', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(CustomRuleComparisonInput)), graphql_name='comparisons', default=None)),
        ('custom_rule_uuid', sgqlc.types.Arg(UUID, graphql_name='customRuleUuid', default=None)),
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('interval_minutes', sgqlc.types.Arg(Int, graphql_name='intervalMinutes', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('notes', sgqlc.types.Arg(String, graphql_name='notes', default=None)),
        ('schedule_config', sgqlc.types.Arg(ScheduleConfigInput, graphql_name='scheduleConfig', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('timezone', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='timezone', default=None)),
))
    )
    snooze_custom_rule = sgqlc.types.Field('SnoozeCustomRule', graphql_name='snoozeCustomRule', args=sgqlc.types.ArgDict((
        ('snooze_minutes', sgqlc.types.Arg(Int, graphql_name='snoozeMinutes', default=None)),
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
))
    )
    unsnooze_custom_rule = sgqlc.types.Field('UnsnoozeCustomRule', graphql_name='unsnoozeCustomRule', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
))
    )
    delete_custom_rule = sgqlc.types.Field(DeleteCustomRule, graphql_name='deleteCustomRule', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
        ('warehouse_uuid', sgqlc.types.Arg(UUID, graphql_name='warehouseUuid', default=None)),
))
    )
    trigger_custom_rule = sgqlc.types.Field('TriggerCustomRule', graphql_name='triggerCustomRule', args=sgqlc.types.ArgDict((
        ('custom_sql_contains', sgqlc.types.Arg(String, graphql_name='customSqlContains', default=None)),
        ('description_contains', sgqlc.types.Arg(String, graphql_name='descriptionContains', default=None)),
        ('rule_id', sgqlc.types.Arg(UUID, graphql_name='ruleId', default=None)),
))
    )
    trigger_circuit_breaker_rule = sgqlc.types.Field('TriggerCircuitBreakerRule', graphql_name='triggerCircuitBreakerRule', args=sgqlc.types.ArgDict((
        ('namespace', sgqlc.types.Arg(String, graphql_name='namespace', default=None)),
        ('rule_name', sgqlc.types.Arg(String, graphql_name='ruleName', default=None)),
        ('rule_uuid', sgqlc.types.Arg(UUID, graphql_name='ruleUuid', default=None)),
))
    )
    run_sql_rule = sgqlc.types.Field('RunSqlRule', graphql_name='runSqlRule', args=sgqlc.types.ArgDict((
        ('rule_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='ruleUuid', default=None)),
))
    )
    create_or_update_lineage_node = sgqlc.types.Field(CreateOrUpdateLineageNode, graphql_name='createOrUpdateLineageNode', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('object_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='objectId', default=None)),
        ('object_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='objectType', default=None)),
        ('properties', sgqlc.types.Arg(sgqlc.types.list_of(ObjectPropertyInput), graphql_name='properties', default=None)),
        ('resource_id', sgqlc.types.Arg(UUID, graphql_name='resourceId', default=None)),
        ('resource_name', sgqlc.types.Arg(String, graphql_name='resourceName', default=None)),
))
    )
    create_or_update_lineage_edge = sgqlc.types.Field(CreateOrUpdateLineageEdge, graphql_name='createOrUpdateLineageEdge', args=sgqlc.types.ArgDict((
        ('destination', sgqlc.types.Arg(sgqlc.types.non_null(NodeInput), graphql_name='destination', default=None)),
        ('expire_at', sgqlc.types.Arg(DateTime, graphql_name='expireAt', default=None)),
        ('source', sgqlc.types.Arg(sgqlc.types.non_null(NodeInput), graphql_name='source', default=None)),
))
    )
    create_or_update_lineage_node_block_pattern = sgqlc.types.Field(CreateOrUpdateLineageNodeBlockPattern, graphql_name='createOrUpdateLineageNodeBlockPattern', args=sgqlc.types.ArgDict((
        ('dataset_regexp', sgqlc.types.Arg(String, graphql_name='datasetRegexp', default=None)),
        ('project_regexp', sgqlc.types.Arg(String, graphql_name='projectRegexp', default=None)),
        ('resource_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='resourceId', default=None)),
        ('table_regexp', sgqlc.types.Arg(String, graphql_name='tableRegexp', default=None)),
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
))
    )
    delete_lineage_node = sgqlc.types.Field(DeleteLineageNode, graphql_name='deleteLineageNode', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
))
    )
    delete_lineage_node_block_pattern = sgqlc.types.Field(DeleteLineageNodeBlockPattern, graphql_name='deleteLineageNodeBlockPattern', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='uuid', default=None)),
))
    )
    create_or_update_catalog_object_metadata = sgqlc.types.Field(CreateOrUpdateCatalogObjectMetadata, graphql_name='createOrUpdateCatalogObjectMetadata', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
))
    )
    delete_catalog_object_metadata = sgqlc.types.Field(DeleteCatalogObjectMetadata, graphql_name='deleteCatalogObjectMetadata', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
))
    )
    create_or_update_object_property = sgqlc.types.Field(CreateOrUpdateObjectProperty, graphql_name='createOrUpdateObjectProperty', args=sgqlc.types.ArgDict((
        ('mcon_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mconId', default=None)),
        ('property_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='propertyName', default=None)),
        ('property_source_type', sgqlc.types.Arg(String, graphql_name='propertySourceType', default='dashboard')),
        ('property_value', sgqlc.types.Arg(String, graphql_name='propertyValue', default=None)),
))
    )
    delete_object_property = sgqlc.types.Field(DeleteObjectProperty, graphql_name='deleteObjectProperty', args=sgqlc.types.ArgDict((
        ('mcon_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mconId', default=None)),
        ('property_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='propertyName', default=None)),
        ('property_source_type', sgqlc.types.Arg(String, graphql_name='propertySourceType', default='dashboard')),
))
    )
    bulk_create_or_update_object_properties = sgqlc.types.Field(BulkCreateOrUpdateObjectProperties, graphql_name='bulkCreateOrUpdateObjectProperties', args=sgqlc.types.ArgDict((
        ('input_object_properties', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(InputObjectProperty)), graphql_name='inputObjectProperties', default=None)),
))
    )
    stop_monitor = sgqlc.types.Field('StopMonitor', graphql_name='stopMonitor', args=sgqlc.types.ArgDict((
        ('monitor_id', sgqlc.types.Arg(UUID, graphql_name='monitorId', default=None)),
))
    )
    trigger_monitor = sgqlc.types.Field('TriggerMonitor', graphql_name='triggerMonitor', args=sgqlc.types.ArgDict((
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('monitor_type', sgqlc.types.Arg(String, graphql_name='monitorType', default=None)),
        ('resource_id', sgqlc.types.Arg(UUID, graphql_name='resourceId', default=None)),
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
))
    )
    create_or_update_monitor = sgqlc.types.Field(CreateOrUpdateMonitor, graphql_name='createOrUpdateMonitor', args=sgqlc.types.ArgDict((
        ('agg_select_expression', sgqlc.types.Arg(String, graphql_name='aggSelectExpression', default=None)),
        ('agg_time_interval', sgqlc.types.Arg(MonitorAggTimeInterval, graphql_name='aggTimeInterval', default=None)),
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('disable_look_back_bootstrap', sgqlc.types.Arg(Boolean, graphql_name='disableLookBackBootstrap', default=False)),
        ('failed_schedule_account_notification_id', sgqlc.types.Arg(UUID, graphql_name='failedScheduleAccountNotificationId', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='fields', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('lookback_days', sgqlc.types.Arg(Int, graphql_name='lookbackDays', default=1)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('monitor_type', sgqlc.types.Arg(String, graphql_name='monitorType', default=None)),
        ('notes', sgqlc.types.Arg(String, graphql_name='notes', default=None)),
        ('resource_id', sgqlc.types.Arg(UUID, graphql_name='resourceId', default=None)),
        ('schedule_config', sgqlc.types.Arg(ScheduleConfigInput, graphql_name='scheduleConfig', default=None)),
        ('segmented_expressions', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='segmentedExpressions', default=None)),
        ('select_expressions', sgqlc.types.Arg(sgqlc.types.list_of(MonitorSelectExpressionInput), graphql_name='selectExpressions', default=None)),
        ('time_axis_name', sgqlc.types.Arg(String, graphql_name='timeAxisName', default=None)),
        ('time_axis_type', sgqlc.types.Arg(String, graphql_name='timeAxisType', default=None)),
        ('unnest_fields', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='unnestFields', default=None)),
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
        ('where_condition', sgqlc.types.Arg(String, graphql_name='whereCondition', default=None)),
))
    )
    pause_monitor = sgqlc.types.Field('PauseMonitor', graphql_name='pauseMonitor', args=sgqlc.types.ArgDict((
        ('pause', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='pause', default=None)),
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='uuid', default=None)),
))
    )
    validate_cron = sgqlc.types.Field('ValidateCron', graphql_name='validateCron', args=sgqlc.types.ArgDict((
        ('allow_multiple', sgqlc.types.Arg(Boolean, graphql_name='allowMultiple', default=None)),
        ('cron', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='cron', default=None)),
))
    )
    create_event_comment = sgqlc.types.Field('createEventComment', graphql_name='createEventComment', args=sgqlc.types.ArgDict((
        ('event_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='eventId', default=None)),
        ('event_text', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='eventText', default=None)),
))
    )
    update_event_comment = sgqlc.types.Field('updateEventComment', graphql_name='updateEventComment', args=sgqlc.types.ArgDict((
        ('event_comment_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='eventCommentId', default=None)),
        ('event_text', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='eventText', default=None)),
))
    )
    delete_event_comment = sgqlc.types.Field('deleteEventComment', graphql_name='deleteEventComment', args=sgqlc.types.ArgDict((
        ('event_comment_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='eventCommentId', default=None)),
))
    )
    set_incident_feedback = sgqlc.types.Field('SetIncidentFeedbackPayload', graphql_name='setIncidentFeedback', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetIncidentFeedbackInput), graphql_name='input', default=None)),
))
    )
    set_incident_reaction = sgqlc.types.Field('SetIncidentReaction', graphql_name='setIncidentReaction', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('reaction', sgqlc.types.Arg(sgqlc.types.non_null(IncidentReactionInput), graphql_name='reaction', default=None)),
))
    )
    set_incident_severity = sgqlc.types.Field('SetIncidentSeverity', graphql_name='setIncidentSeverity', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('severity', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='severity', default=None)),
))
    )
    set_incident_owner = sgqlc.types.Field('SetIncidentOwner', graphql_name='setIncidentOwner', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('owner', sgqlc.types.Arg(String, graphql_name='owner', default=None)),
))
    )
    create_or_update_incident_comment = sgqlc.types.Field(CreateOrUpdateIncidentComment, graphql_name='createOrUpdateIncidentComment', args=sgqlc.types.ArgDict((
        ('comment', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='comment', default=None)),
        ('comment_id', sgqlc.types.Arg(UUID, graphql_name='commentId', default=None)),
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
))
    )
    delete_incident_comment = sgqlc.types.Field(DeleteIncidentComment, graphql_name='deleteIncidentComment', args=sgqlc.types.ArgDict((
        ('comment_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='commentId', default=None)),
))
    )
    create_or_update_domain = sgqlc.types.Field(CreateOrUpdateDomain, graphql_name='createOrUpdateDomain', args=sgqlc.types.ArgDict((
        ('assignments', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='assignments', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(TagKeyValuePairInput), graphql_name='tags', default=None)),
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
))
    )
    delete_domain = sgqlc.types.Field(DeleteDomain, graphql_name='deleteDomain', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='uuid', default=None)),
))
    )
    create_or_update_authorization_group = sgqlc.types.Field(CreateOrUpdateAuthorizationGroup, graphql_name='createOrUpdateAuthorizationGroup', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('domain_restriction_ids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='domainRestrictionIds', default=None)),
        ('label', sgqlc.types.Arg(String, graphql_name='label', default=None)),
        ('member_user_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='memberUserIds', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('roles', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='roles', default=None)),
        ('version', sgqlc.types.Arg(String, graphql_name='version', default=None)),
))
    )
    delete_authorization_group = sgqlc.types.Field(DeleteAuthorizationGroup, graphql_name='deleteAuthorizationGroup', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
))
    )
    update_user_authorization_group_membership = sgqlc.types.Field('UpdateUserAuthorizationGroupMembership', graphql_name='updateUserAuthorizationGroupMembership', args=sgqlc.types.ArgDict((
        ('group_names', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='groupNames', default=None)),
        ('member_user_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='memberUserId', default=None)),
))
    )
    create_or_update_resource = sgqlc.types.Field(CreateOrUpdateResource, graphql_name='createOrUpdateResource', args=sgqlc.types.ArgDict((
        ('is_default', sgqlc.types.Arg(Boolean, graphql_name='isDefault', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
))
    )
    toggle_disable_sampling = sgqlc.types.Field('ToggleDisableSampling', graphql_name='toggleDisableSampling', args=sgqlc.types.ArgDict((
        ('disable', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='disable', default=None)),
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
))
    )
    toggle_disable_value_ingestion = sgqlc.types.Field('ToggleDisableValueIngestion', graphql_name='toggleDisableValueIngestion', args=sgqlc.types.ArgDict((
        ('disable', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='disable', default=None)),
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
))
    )
    toggle_enable_full_distribution_metrics = sgqlc.types.Field('ToggleFullDistributionMetrics', graphql_name='toggleEnableFullDistributionMetrics', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
        ('enable', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='enable', default=None)),
))
    )
    save_table_importance_stats = sgqlc.types.Field('SaveTableImportanceStats', graphql_name='saveTableImportanceStats', args=sgqlc.types.ArgDict((
        ('importance_score', sgqlc.types.Arg(Float, graphql_name='importanceScore', default=None)),
        ('is_important', sgqlc.types.Arg(Boolean, graphql_name='isImportant', default=None)),
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
))
    )
    set_default_incident_group_interval = sgqlc.types.Field('SetDefaultIncidentGroupInterval', graphql_name='setDefaultIncidentGroupInterval', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
        ('interval', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='interval', default=None)),
))
    )
    update_user_state = sgqlc.types.Field('UpdateUserStatePayload', graphql_name='updateUserState', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserStateInput), graphql_name='input', default=None)),
))
    )
    set_account_name = sgqlc.types.Field('SetAccountName', graphql_name='setAccountName', args=sgqlc.types.ArgDict((
        ('account_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='accountName', default=None)),
))
    )
    set_warehouse_name = sgqlc.types.Field('SetWarehouseName', graphql_name='setWarehouseName', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    create_or_update_saml_identity_provider = sgqlc.types.Field(CreateOrUpdateSamlIdentityProvider, graphql_name='createOrUpdateSamlIdentityProvider', args=sgqlc.types.ArgDict((
        ('default_authorization_groups', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='defaultAuthorizationGroups', default=None)),
        ('domains', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='domains', default=None)),
        ('metadata', sgqlc.types.Arg(String, graphql_name='metadata', default=None)),
        ('metadata_url', sgqlc.types.Arg(String, graphql_name='metadataUrl', default=None)),
))
    )
    delete_saml_identity_provider = sgqlc.types.Field(DeleteSamlIdentityProvider, graphql_name='deleteSamlIdentityProvider')
    invite_users = sgqlc.types.Field(InviteUsersPayload, graphql_name='inviteUsers', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(InviteUsersInput), graphql_name='input', default=None)),
))
    )
    invite_users_v2 = sgqlc.types.Field(InviteUsersV2, graphql_name='inviteUsersV2', args=sgqlc.types.ArgDict((
        ('auth_groups', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='authGroups', default=None)),
        ('emails', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='emails', default=None)),
        ('invitation_type', sgqlc.types.Arg(InvitationType, graphql_name='invitationType', default=None)),
))
    )
    delete_user_invite = sgqlc.types.Field(DeleteUserInvite, graphql_name='deleteUserInvite', args=sgqlc.types.ArgDict((
        ('emails', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='emails', default=None)),
))
    )
    resend_user_invite = sgqlc.types.Field('ReInviteUsers', graphql_name='resendUserInvite', args=sgqlc.types.ArgDict((
        ('emails', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='emails', default=None)),
))
    )
    remove_user_from_account = sgqlc.types.Field('RemoveUserFromAccount', graphql_name='removeUserFromAccount', args=sgqlc.types.ArgDict((
        ('email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='email', default=None)),
))
    )
    track_table = sgqlc.types.Field('TrackTablePayload', graphql_name='trackTable', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TrackTableInput), graphql_name='input', default=None)),
))
    )
    upload_credentials = sgqlc.types.Field('UploadWarehouseCredentialsMutation', graphql_name='uploadCredentials', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='file', default=None)),
))
    )
    save_slack_credentials = sgqlc.types.Field('SaveSlackCredentialsMutation', graphql_name='saveSlackCredentials', args=sgqlc.types.ArgDict((
        ('key', sgqlc.types.Arg(String, graphql_name='key', default=None)),
        ('slack_app_type', sgqlc.types.Arg(SlackAppType, graphql_name='slackAppType', default=None)),
        ('slack_installation_uuid', sgqlc.types.Arg(String, graphql_name='slackInstallationUuid', default=None)),
))
    )
    deauthorize_slack_app = sgqlc.types.Field(DeauthorizeSlackAppMutation, graphql_name='deauthorizeSlackApp', args=sgqlc.types.ArgDict((
        ('slack_app_type', sgqlc.types.Arg(sgqlc.types.non_null(SlackAppType), graphql_name='slackAppType', default=None)),
))
    )
    test_credentials = sgqlc.types.Field('TestCredentialsMutation', graphql_name='testCredentials', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('connection_type', sgqlc.types.Arg(String, graphql_name='connectionType', default='bigquery')),
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
        ('project_id', sgqlc.types.Arg(String, graphql_name='projectId', default=None)),
))
    )
    test_database_credentials = sgqlc.types.Field('TestDatabaseCredentials', graphql_name='testDatabaseCredentials', args=sgqlc.types.ArgDict((
        ('assumable_role', sgqlc.types.Arg(String, graphql_name='assumableRole', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('connection_type', sgqlc.types.Arg(String, graphql_name='connectionType', default=None)),
        ('db_name', sgqlc.types.Arg(String, graphql_name='dbName', default=None)),
        ('external_id', sgqlc.types.Arg(String, graphql_name='externalId', default=None)),
        ('host', sgqlc.types.Arg(String, graphql_name='host', default=None)),
        ('password', sgqlc.types.Arg(String, graphql_name='password', default=None)),
        ('port', sgqlc.types.Arg(Int, graphql_name='port', default=None)),
        ('ssl_options', sgqlc.types.Arg(SslInputOptions, graphql_name='sslOptions', default=None)),
        ('user', sgqlc.types.Arg(String, graphql_name='user', default=None)),
))
    )
    test_presto_credentials = sgqlc.types.Field('TestPrestoCredentials', graphql_name='testPrestoCredentials', args=sgqlc.types.ArgDict((
        ('catalog', sgqlc.types.Arg(String, graphql_name='catalog', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('host', sgqlc.types.Arg(String, graphql_name='host', default=None)),
        ('http_scheme', sgqlc.types.Arg(String, graphql_name='httpScheme', default=None)),
        ('password', sgqlc.types.Arg(String, graphql_name='password', default=None)),
        ('port', sgqlc.types.Arg(Int, graphql_name='port', default=None)),
        ('schema', sgqlc.types.Arg(String, graphql_name='schema', default=None)),
        ('ssl_options', sgqlc.types.Arg(SslInputOptions, graphql_name='sslOptions', default=None)),
        ('user', sgqlc.types.Arg(String, graphql_name='user', default=None)),
))
    )
    test_snowflake_credentials = sgqlc.types.Field('TestSnowflakeCredentials', graphql_name='testSnowflakeCredentials', args=sgqlc.types.ArgDict((
        ('account', sgqlc.types.Arg(String, graphql_name='account', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('password', sgqlc.types.Arg(String, graphql_name='password', default=None)),
        ('private_key', sgqlc.types.Arg(String, graphql_name='privateKey', default=None)),
        ('private_key_passphrase', sgqlc.types.Arg(String, graphql_name='privateKeyPassphrase', default=None)),
        ('user', sgqlc.types.Arg(String, graphql_name='user', default=None)),
        ('warehouse', sgqlc.types.Arg(String, graphql_name='warehouse', default=None)),
))
    )
    test_hive_credentials = sgqlc.types.Field('TestHiveCredentials', graphql_name='testHiveCredentials', args=sgqlc.types.ArgDict((
        ('auth_mode', sgqlc.types.Arg(String, graphql_name='authMode', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('database', sgqlc.types.Arg(String, graphql_name='database', default=None)),
        ('host', sgqlc.types.Arg(String, graphql_name='host', default=None)),
        ('port', sgqlc.types.Arg(Int, graphql_name='port', default=None)),
        ('username', sgqlc.types.Arg(String, graphql_name='username', default=None)),
))
    )
    test_s3_credentials = sgqlc.types.Field('TestS3Credentials', graphql_name='testS3Credentials', args=sgqlc.types.ArgDict((
        ('assumable_role', sgqlc.types.Arg(String, graphql_name='assumableRole', default=None)),
        ('bucket', sgqlc.types.Arg(String, graphql_name='bucket', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('connection_type', sgqlc.types.Arg(String, graphql_name='connectionType', default='s3')),
        ('external_id', sgqlc.types.Arg(String, graphql_name='externalId', default=None)),
        ('prefix', sgqlc.types.Arg(String, graphql_name='prefix', default=None)),
))
    )
    test_glue_credentials = sgqlc.types.Field('TestGlueCredentials', graphql_name='testGlueCredentials', args=sgqlc.types.ArgDict((
        ('assumable_role', sgqlc.types.Arg(String, graphql_name='assumableRole', default=None)),
        ('aws_region', sgqlc.types.Arg(String, graphql_name='awsRegion', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('external_id', sgqlc.types.Arg(String, graphql_name='externalId', default=None)),
))
    )
    test_athena_credentials = sgqlc.types.Field('TestAthenaCredentials', graphql_name='testAthenaCredentials', args=sgqlc.types.ArgDict((
        ('assumable_role', sgqlc.types.Arg(String, graphql_name='assumableRole', default=None)),
        ('aws_region', sgqlc.types.Arg(String, graphql_name='awsRegion', default=None)),
        ('catalog', sgqlc.types.Arg(String, graphql_name='catalog', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('external_id', sgqlc.types.Arg(String, graphql_name='externalId', default=None)),
        ('workgroup', sgqlc.types.Arg(String, graphql_name='workgroup', default=None)),
))
    )
    test_looker_credentials = sgqlc.types.Field('TestLookerCredentials', graphql_name='testLookerCredentials', args=sgqlc.types.ArgDict((
        ('base_url', sgqlc.types.Arg(String, graphql_name='baseUrl', default=None)),
        ('client_id', sgqlc.types.Arg(String, graphql_name='clientId', default=None)),
        ('client_secret', sgqlc.types.Arg(String, graphql_name='clientSecret', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('verify_ssl', sgqlc.types.Arg(Boolean, graphql_name='verifySsl', default=None)),
))
    )
    test_looker_git_credentials = sgqlc.types.Field('TestLookerGitCredentials', graphql_name='testLookerGitCredentials', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('installation_id', sgqlc.types.Arg(Int, graphql_name='installationId', default=None)),
))
    )
    test_looker_git_ssh_credentials = sgqlc.types.Field('TestLookerGitSshCredentials', graphql_name='testLookerGitSshCredentials', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('repo_url', sgqlc.types.Arg(String, graphql_name='repoUrl', default=None)),
        ('ssh_key', sgqlc.types.Arg(String, graphql_name='sshKey', default=None)),
))
    )
    test_looker_git_clone_credentials = sgqlc.types.Field('TestLookerGitCloneCredentials', graphql_name='testLookerGitCloneCredentials', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('repo_url', sgqlc.types.Arg(String, graphql_name='repoUrl', default=None)),
        ('ssh_key', sgqlc.types.Arg(String, graphql_name='sshKey', default=None)),
        ('token', sgqlc.types.Arg(String, graphql_name='token', default=None)),
        ('username', sgqlc.types.Arg(String, graphql_name='username', default=None)),
))
    )
    test_dbt_cloud_credentials = sgqlc.types.Field('TestDbtCloudCredentials', graphql_name='testDbtCloudCredentials', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('dbt_cloud_account_id', sgqlc.types.Arg(String, graphql_name='dbtCloudAccountId', default=None)),
        ('dbt_cloud_api_token', sgqlc.types.Arg(String, graphql_name='dbtCloudApiToken', default=None)),
        ('dbt_cloud_base_url', sgqlc.types.Arg(String, graphql_name='dbtCloudBaseUrl', default=None)),
))
    )
    test_bq_credentials = sgqlc.types.Field('TestBqCredentials', graphql_name='testBqCredentials', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('service_json', sgqlc.types.Arg(String, graphql_name='serviceJson', default=None)),
))
    )
    test_spark_credentials = sgqlc.types.Field('TestSparkCredentials', graphql_name='testSparkCredentials', args=sgqlc.types.ArgDict((
        ('binary_mode', sgqlc.types.Arg(SparkBinaryInput, graphql_name='binaryMode', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('databricks', sgqlc.types.Arg(SparkDatabricksInput, graphql_name='databricks', default=None)),
        ('http_mode', sgqlc.types.Arg(SparkHttpInput, graphql_name='httpMode', default=None)),
))
    )
    test_self_hosted_credentials = sgqlc.types.Field('TestSelfHostedCredentials', graphql_name='testSelfHostedCredentials', args=sgqlc.types.ArgDict((
        ('assumable_role', sgqlc.types.Arg(String, graphql_name='assumableRole', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('connection_type', sgqlc.types.Arg(String, graphql_name='connectionType', default=None)),
        ('external_id', sgqlc.types.Arg(String, graphql_name='externalId', default=None)),
        ('region', sgqlc.types.Arg(String, graphql_name='region', default=None)),
        ('self_hosting_key', sgqlc.types.Arg(String, graphql_name='selfHostingKey', default=None)),
        ('self_hosting_mechanism', sgqlc.types.Arg(String, graphql_name='selfHostingMechanism', default=None)),
))
    )
    add_tableau_account = sgqlc.types.Field(AddTableauAccountMutation, graphql_name='addTableauAccount', args=sgqlc.types.ArgDict((
        ('dc_id', sgqlc.types.Arg(UUID, graphql_name='dcId', default=None)),
        ('password', sgqlc.types.Arg(String, graphql_name='password', default=None)),
        ('server_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='serverName', default=None)),
        ('site_name', sgqlc.types.Arg(String, graphql_name='siteName', default=None)),
        ('token_name', sgqlc.types.Arg(String, graphql_name='tokenName', default=None)),
        ('token_value', sgqlc.types.Arg(String, graphql_name='tokenValue', default=None)),
        ('username', sgqlc.types.Arg(String, graphql_name='username', default=None)),
        ('verify_ssl', sgqlc.types.Arg(Boolean, graphql_name='verifySsl', default=True)),
))
    )
    test_tableau_credentials = sgqlc.types.Field('TestTableauCredentialsMutation', graphql_name='testTableauCredentials', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('password', sgqlc.types.Arg(String, graphql_name='password', default=None)),
        ('server_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='serverName', default=None)),
        ('site_name', sgqlc.types.Arg(String, graphql_name='siteName', default=None)),
        ('token_name', sgqlc.types.Arg(String, graphql_name='tokenName', default=None)),
        ('token_value', sgqlc.types.Arg(String, graphql_name='tokenValue', default=None)),
        ('username', sgqlc.types.Arg(String, graphql_name='username', default=None)),
        ('verify_ssl', sgqlc.types.Arg(Boolean, graphql_name='verifySsl', default=True)),
))
    )
    test_power_bi_credentials = sgqlc.types.Field('TestPowerBICredentials', graphql_name='testPowerBiCredentials', args=sgqlc.types.ArgDict((
        ('auth_mode', sgqlc.types.Arg(sgqlc.types.non_null(PowerBIAuthModeEnum), graphql_name='authMode', default=None)),
        ('client_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='clientId', default=None)),
        ('client_secret', sgqlc.types.Arg(String, graphql_name='clientSecret', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('password', sgqlc.types.Arg(String, graphql_name='password', default=None)),
        ('tenant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tenantId', default=None)),
        ('username', sgqlc.types.Arg(String, graphql_name='username', default=None)),
))
    )
    toggle_mute_dataset = sgqlc.types.Field('ToggleMuteDatasetPayload', graphql_name='toggleMuteDataset', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ToggleMuteDatasetInput), graphql_name='input', default=None)),
))
    )
    toggle_mute_table = sgqlc.types.Field('ToggleMuteTablePayload', graphql_name='toggleMuteTable', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ToggleMuteTableInput), graphql_name='input', default=None)),
))
    )
    toggle_mute_datasets = sgqlc.types.Field('ToggleMuteDatasetsPayload', graphql_name='toggleMuteDatasets', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ToggleMuteDatasetsInput), graphql_name='input', default=None)),
))
    )
    toggle_mute_tables = sgqlc.types.Field('ToggleMuteTablesPayload', graphql_name='toggleMuteTables', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ToggleMuteTablesInput), graphql_name='input', default=None)),
))
    )
    toggle_mute_with_regex = sgqlc.types.Field('ToggleMuteWithRegexPayload', graphql_name='toggleMuteWithRegex', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ToggleMuteWithRegexInput), graphql_name='input', default=None)),
))
    )
    delete_notification_settings = sgqlc.types.Field(DeleteNotificationSetting, graphql_name='deleteNotificationSettings', args=sgqlc.types.ArgDict((
        ('uuids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(UUID)), graphql_name='uuids', default=None)),
))
    )
    add_connection = sgqlc.types.Field(AddConnectionMutation, graphql_name='addConnection', args=sgqlc.types.ArgDict((
        ('connection_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='connectionType', default=None)),
        ('create_warehouse_type', sgqlc.types.Arg(String, graphql_name='createWarehouseType', default=None)),
        ('dc_id', sgqlc.types.Arg(UUID, graphql_name='dcId', default=None)),
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('job_limits', sgqlc.types.Arg(JSONString, graphql_name='jobLimits', default=None)),
        ('job_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='jobTypes', default=None)),
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
))
    )
    remove_connection = sgqlc.types.Field('RemoveConnectionMutation', graphql_name='removeConnection', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='connectionId', default=None)),
))
    )
    add_bi_connection = sgqlc.types.Field(AddBiConnectionMutation, graphql_name='addBiConnection', args=sgqlc.types.ArgDict((
        ('connection_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='connectionType', default=None)),
        ('dc_id', sgqlc.types.Arg(UUID, graphql_name='dcId', default=None)),
        ('job_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='jobTypes', default=None)),
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
        ('resource_id', sgqlc.types.Arg(UUID, graphql_name='resourceId', default=None)),
))
    )
    toggle_event_config = sgqlc.types.Field('ToggleEventConfig', graphql_name='toggleEventConfig', args=sgqlc.types.ArgDict((
        ('assumable_role', sgqlc.types.Arg(String, graphql_name='assumableRole', default=None)),
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
        ('connection_type', sgqlc.types.Arg(String, graphql_name='connectionType', default=None)),
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('enable', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='enable', default=None)),
        ('event_type', sgqlc.types.Arg(sgqlc.types.non_null(DataCollectorEventTypes), graphql_name='eventType', default=None)),
        ('external_id', sgqlc.types.Arg(String, graphql_name='externalId', default=None)),
        ('format_type', sgqlc.types.Arg(String, graphql_name='formatType', default=None)),
        ('location', sgqlc.types.Arg(String, graphql_name='location', default=None)),
        ('mapping', sgqlc.types.Arg(JSONString, graphql_name='mapping', default=None)),
        ('source_format', sgqlc.types.Arg(String, graphql_name='sourceFormat', default=None)),
))
    )
    create_access_token = sgqlc.types.Field(CreateAccessToken, graphql_name='createAccessToken', args=sgqlc.types.ArgDict((
        ('comment', sgqlc.types.Arg(String, graphql_name='comment', default=None)),
        ('expiration_in_days', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='expirationInDays', default=None)),
))
    )
    delete_access_token = sgqlc.types.Field(DeleteAccessToken, graphql_name='deleteAccessToken', args=sgqlc.types.ArgDict((
        ('token_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tokenId', default=None)),
))
    )
    generate_collector_template = sgqlc.types.Field(GenerateCollectorTemplate, graphql_name='generateCollectorTemplate', args=sgqlc.types.ArgDict((
        ('dc_id', sgqlc.types.Arg(UUID, graphql_name='dcId', default=None)),
        ('region', sgqlc.types.Arg(String, graphql_name='region', default='us-east-1')),
        ('template_variant', sgqlc.types.Arg(String, graphql_name='templateVariant', default=None)),
))
    )
    create_or_update_notification_setting = sgqlc.types.Field(CreateOrUpdateNotificationSetting, graphql_name='createOrUpdateNotificationSetting', args=sgqlc.types.ArgDict((
        ('anomaly_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='anomalyTypes', default=None)),
        ('custom_message', sgqlc.types.Arg(String, graphql_name='customMessage', default=None)),
        ('digest_settings', sgqlc.types.Arg(NotificationDigestSettings, graphql_name='digestSettings', default=None)),
        ('dry', sgqlc.types.Arg(Boolean, graphql_name='dry', default=False)),
        ('extra', sgqlc.types.Arg(NotificationExtra, graphql_name='extra', default=None)),
        ('incident_sub_types', sgqlc.types.Arg(sgqlc.types.list_of(IncidentSubType), graphql_name='incidentSubTypes', default=None)),
        ('notification_schedule_type', sgqlc.types.Arg(String, graphql_name='notificationScheduleType', default=None)),
        ('notification_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='notificationType', default=None)),
        ('recipient', sgqlc.types.Arg(String, graphql_name='recipient', default=None)),
        ('recipients', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='recipients', default=None)),
        ('rules', sgqlc.types.Arg(NotificationRoutingRules, graphql_name='rules', default=None)),
        ('setting_id', sgqlc.types.Arg(UUID, graphql_name='settingId', default=None)),
))
    )
    update_credentials = sgqlc.types.Field('UpdateCredentials', graphql_name='updateCredentials', args=sgqlc.types.ArgDict((
        ('changes', sgqlc.types.Arg(sgqlc.types.non_null(JSONString), graphql_name='changes', default=None)),
        ('connection_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='connectionId', default=None)),
        ('should_replace', sgqlc.types.Arg(Boolean, graphql_name='shouldReplace', default=False)),
        ('should_validate', sgqlc.types.Arg(Boolean, graphql_name='shouldValidate', default=True)),
))
    )
    create_collector_record = sgqlc.types.Field(CreateCollectorRecord, graphql_name='createCollectorRecord', args=sgqlc.types.ArgDict((
        ('region', sgqlc.types.Arg(String, graphql_name='region', default='us-east-1')),
        ('template_provider', sgqlc.types.Arg(String, graphql_name='templateProvider', default='cloudformation')),
        ('template_variant', sgqlc.types.Arg(String, graphql_name='templateVariant', default='hephaestus')),
))
    )
    cleanup_collector_record = sgqlc.types.Field(CleanupCollectorRecordInAccount, graphql_name='cleanupCollectorRecord', args=sgqlc.types.ArgDict((
        ('dc_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dcId', default=None)),
))
    )
    migrate_collector_resources = sgqlc.types.Field(MigrateCollectorResources, graphql_name='migrateCollectorResources', args=sgqlc.types.ArgDict((
        ('resource_ids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='resourceIds', default=None)),
        ('source_dc_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='sourceDcId', default=None)),
        ('target_dc_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='targetDcId', default=None)),
))
    )
    update_slack_channels = sgqlc.types.Field('UpdateSlackChannelsMutation', graphql_name='updateSlackChannels')
    create_integration_key = sgqlc.types.Field(CreateIntegrationKey, graphql_name='createIntegrationKey', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
        ('scope', sgqlc.types.Arg(sgqlc.types.non_null(IntegrationKeyScope), graphql_name='scope', default=None)),
        ('warehouse_ids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='warehouseIds', default=None)),
))
    )
    delete_integration_key = sgqlc.types.Field(DeleteIntegrationKey, graphql_name='deleteIntegrationKey', args=sgqlc.types.ArgDict((
        ('key_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='keyId', default=None)),
))
    )
    create_databricks_secret = sgqlc.types.Field(CreateDatabricksSecret, graphql_name='createDatabricksSecret', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('databricks_config', sgqlc.types.Arg(sgqlc.types.non_null(SparkDatabricksInput), graphql_name='databricksConfig', default=None)),
        ('scope_name', sgqlc.types.Arg(String, graphql_name='scopeName', default=None)),
        ('scope_principal', sgqlc.types.Arg(String, graphql_name='scopePrincipal', default=None)),
        ('secret_name', sgqlc.types.Arg(String, graphql_name='secretName', default=None)),
))
    )
    create_databricks_notebook_job = sgqlc.types.Field(CreateDatabricksNotebookJob, graphql_name='createDatabricksNotebookJob', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('databricks_config', sgqlc.types.Arg(sgqlc.types.non_null(SparkDatabricksInput), graphql_name='databricksConfig', default=None)),
))
    )
    update_databricks_notebook_job = sgqlc.types.Field('UpdateDatabricksNotebookJob', graphql_name='updateDatabricksNotebookJob', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
))
    )
    update_databricks_notebook = sgqlc.types.Field('UpdateDatabricksNotebook', graphql_name='updateDatabricksNotebook', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
))
    )
    start_databricks_cluster = sgqlc.types.Field('StartDatabricksCluster', graphql_name='startDatabricksCluster', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
))
    )
    test_databricks_credentials = sgqlc.types.Field('TestDatabricksCredentials', graphql_name='testDatabricksCredentials', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('databricks_config', sgqlc.types.Arg(sgqlc.types.non_null(SparkDatabricksInput), graphql_name='databricksConfig', default=None)),
))
    )
    test_delta_credentials = sgqlc.types.Field('TestDatabricksCredentials', graphql_name='testDeltaCredentials', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('databricks_config', sgqlc.types.Arg(sgqlc.types.non_null(SparkDatabricksInput), graphql_name='databricksConfig', default=None)),
))
    )
    add_databricks_connection = sgqlc.types.Field(AddDatabricksConnectionMutation, graphql_name='addDatabricksConnection', args=sgqlc.types.ArgDict((
        ('connection_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='connectionType', default=None)),
        ('create_warehouse_type', sgqlc.types.Arg(String, graphql_name='createWarehouseType', default=None)),
        ('dc_id', sgqlc.types.Arg(UUID, graphql_name='dcId', default=None)),
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('job_limits', sgqlc.types.Arg(sgqlc.types.non_null(JSONString), graphql_name='jobLimits', default=None)),
        ('job_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='jobTypes', default=None)),
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
))
    )
    save_event_onboarding_data = sgqlc.types.Field('SaveEventOnboardingData', graphql_name='saveEventOnboardingData', args=sgqlc.types.ArgDict((
        ('config', sgqlc.types.Arg(sgqlc.types.non_null(JSONString), graphql_name='config', default=None)),
))
    )
    delete_event_onboarding_data = sgqlc.types.Field(DeleteEventOnboardingData, graphql_name='deleteEventOnboardingData')


class NameRef(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(String, graphql_name='name')


class NestedHighlightSnippets(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('offset', 'inner_hit_snippets')
    offset = sgqlc.types.Field(Int, graphql_name='offset')
    inner_hit_snippets = sgqlc.types.Field(sgqlc.types.list_of(HighlightSnippets), graphql_name='innerHitSnippets')


class Node(sgqlc.types.Interface):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class NodeImportInfo(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node_id', 'resource_type', 'global_id', 'description_imported', 'tags_imported', 'columns_description_imported', 'columns_tags_imported')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nodeId')
    resource_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='resourceType')
    global_id = sgqlc.types.Field(String, graphql_name='globalId')
    description_imported = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='descriptionImported')
    tags_imported = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='tagsImported')
    columns_description_imported = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='columnsDescriptionImported')
    columns_tags_imported = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='columnsTagsImported')


class NodeProperties(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('workbook_id', 'friendly_name', 'content_url', 'owner_id', 'project_id', 'project_name', 'created', 'updated', 'total_views', 'workbook_creators', 'view_id', 'category', 'mcon', 'name', 'display_name', 'table_id', 'data_set', 'node_id', 'resource', 'sampling')
    workbook_id = sgqlc.types.Field(String, graphql_name='workbookId')
    friendly_name = sgqlc.types.Field(String, graphql_name='friendlyName')
    content_url = sgqlc.types.Field(String, graphql_name='contentUrl')
    owner_id = sgqlc.types.Field(String, graphql_name='ownerId')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    project_name = sgqlc.types.Field(String, graphql_name='projectName')
    created = sgqlc.types.Field(DateTime, graphql_name='created')
    updated = sgqlc.types.Field(DateTime, graphql_name='updated')
    total_views = sgqlc.types.Field(Int, graphql_name='totalViews')
    workbook_creators = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='workbookCreators')
    view_id = sgqlc.types.Field(String, graphql_name='viewId')
    category = sgqlc.types.Field(String, graphql_name='category')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    name = sgqlc.types.Field(String, graphql_name='name')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    table_id = sgqlc.types.Field(String, graphql_name='tableId')
    data_set = sgqlc.types.Field(String, graphql_name='dataSet')
    node_id = sgqlc.types.Field(String, graphql_name='nodeId')
    resource = sgqlc.types.Field(String, graphql_name='resource')
    sampling = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='sampling')


class NonTableMetric(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('metric', 'value', 'measurement_timestamp', 'dimensions', 'job_execution_uuid')
    metric = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='metric')
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')
    measurement_timestamp = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='measurementTimestamp')
    dimensions = sgqlc.types.Field(MetricDimensions, graphql_name='dimensions')
    job_execution_uuid = sgqlc.types.Field(UUID, graphql_name='jobExecutionUuid')


class NonTableMetrics(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('metrics', 'is_partial_date_range')
    metrics = sgqlc.types.Field(sgqlc.types.list_of(NonTableMetric), graphql_name='metrics')
    is_partial_date_range = sgqlc.types.Field(Boolean, graphql_name='isPartialDateRange')


class ObjectDocument(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('mcon', 'resource_id', 'object_id', 'object_type', 'display_name', 'field_metadata', 'table_metadata', 'bi_metadata', 'properties')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    resource_id = sgqlc.types.Field(String, graphql_name='resourceId')
    object_id = sgqlc.types.Field(String, graphql_name='objectId')
    object_type = sgqlc.types.Field(String, graphql_name='objectType')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    field_metadata = sgqlc.types.Field(FieldMetadata, graphql_name='fieldMetadata')
    table_metadata = sgqlc.types.Field('TableMetadata', graphql_name='tableMetadata')
    bi_metadata = sgqlc.types.Field(BiMetadata, graphql_name='biMetadata')
    properties = sgqlc.types.Field(sgqlc.types.list_of('ObjectPropertyEntry'), graphql_name='properties')


class ObjectPropertyConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ObjectPropertyEdge')), graphql_name='edges')


class ObjectPropertyEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('ObjectProperty', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class ObjectPropertyEntry(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(String, graphql_name='name')
    value = sgqlc.types.Field(String, graphql_name='value')


class OwnerRef(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name', 'username', 'email')
    name = sgqlc.types.Field(String, graphql_name='name')
    username = sgqlc.types.Field(String, graphql_name='username')
    email = sgqlc.types.Field(String, graphql_name='email')


class PageInfo(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('has_next_page', 'has_previous_page', 'start_cursor', 'end_cursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')


class PaginateQueriesBlastRadius(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('after_key', 'data')
    after_key = sgqlc.types.Field('QueryAfterKey', graphql_name='afterKey')
    data = sgqlc.types.Field(sgqlc.types.list_of('QueryBlastRadius'), graphql_name='data')


class PaginateQueriesBlastRadius2(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('after_key', 'data')
    after_key = sgqlc.types.Field('UserAfterKey2', graphql_name='afterKey')
    data = sgqlc.types.Field(sgqlc.types.list_of('QueryBlastRadius2'), graphql_name='data')


class PaginateQueriesBlastRadiusSummary(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('after_key', 'data')
    after_key = sgqlc.types.Field('UserAfterKey2', graphql_name='afterKey')
    data = sgqlc.types.Field(sgqlc.types.list_of('QueryBlastRadiusSummary'), graphql_name='data')


class PaginateUsersBlastRadius(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('after_key', 'data')
    after_key = sgqlc.types.Field('UserAfterKey', graphql_name='afterKey')
    data = sgqlc.types.Field(sgqlc.types.list_of('UserBlastRadius'), graphql_name='data')


class PaginateUsersBlastRadius2(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('after_key', 'data')
    after_key = sgqlc.types.Field('UserAfterKey2', graphql_name='afterKey')
    data = sgqlc.types.Field(sgqlc.types.list_of('UserBlastRadius2'), graphql_name='data')


class ParsedQueryResult(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('parsed_query',)
    parsed_query = sgqlc.types.Field(String, graphql_name='parsedQuery')


class PauseMonitor(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('monitor',)
    monitor = sgqlc.types.Field('MetricMonitoring', graphql_name='monitor')


class PipelineFreshness(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('metric_values_by_table', 'is_partial_date_range')
    metric_values_by_table = sgqlc.types.Field(sgqlc.types.list_of(MetricValueByTable), graphql_name='metricValuesByTable')
    is_partial_date_range = sgqlc.types.Field(Boolean, graphql_name='isPartialDateRange')


class PlatformRegionProperties(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('gateway_endpoint', 'gateway_vpce', 'linker_arn', 'log_arn', 'template_launch_url')
    gateway_endpoint = sgqlc.types.Field(String, graphql_name='gatewayEndpoint')
    gateway_vpce = sgqlc.types.Field(String, graphql_name='gatewayVpce')
    linker_arn = sgqlc.types.Field(String, graphql_name='linkerArn')
    log_arn = sgqlc.types.Field(String, graphql_name='logArn')
    template_launch_url = sgqlc.types.Field(String, graphql_name='templateLaunchUrl')


class PowerBIDashboardTileRef(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('tile_id', 'tile_title', 'tile_sub_title', 'report_name', 'report_id')
    tile_id = sgqlc.types.Field(String, graphql_name='tileId')
    tile_title = sgqlc.types.Field(String, graphql_name='tileTitle')
    tile_sub_title = sgqlc.types.Field(String, graphql_name='tileSubTitle')
    report_name = sgqlc.types.Field(String, graphql_name='reportName')
    report_id = sgqlc.types.Field(String, graphql_name='reportId')


class PowerBIWorkSpaceRef(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name', 'id', 'type', 'state', 'description')
    name = sgqlc.types.Field(String, graphql_name='name')
    id = sgqlc.types.Field(String, graphql_name='id')
    type = sgqlc.types.Field(String, graphql_name='type')
    state = sgqlc.types.Field(String, graphql_name='state')
    description = sgqlc.types.Field(String, graphql_name='description')


class Projects(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('projects',)
    projects = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='projects')


class PropertyNameValue(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(String, graphql_name='name')
    value = sgqlc.types.Field(String, graphql_name='value')


class PropertyNameValues(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('property_name_values', 'has_next_page')
    property_name_values = sgqlc.types.Field(sgqlc.types.list_of(PropertyNameValue), graphql_name='propertyNameValues')
    has_next_page = sgqlc.types.Field(Boolean, graphql_name='hasNextPage')


class PropertyNames(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('property_names',)
    property_names = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='propertyNames')


class PropertyValues(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('property_values',)
    property_values = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='propertyValues')


class Query(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('get_dbt_projects', 'get_dbt_nodes', 'get_dbt_runs', 'get_dbt_model_results', 'get_dbt_test_results', 'get_custom_users', 'get_docs', 'get_unified_users', 'get_unified_user_assignments', 'get_monte_carlo_config_templates', 'get_rca_result', 'get_sensitivity', 'thresholds', 'get_thresholds', 'get_table_columns_lineage', 'get_derived_tables_partial_lineage', 'get_parsed_query', 'get_job_execution_history_logs', 'get_dimension_tracking_monitor_suggestions', 'get_field_health_monitor_suggestions', 'monitor_labels', 'get_account_monitor_labels', 'get_monitors', 'get_all_user_defined_monitors_v2', 'get_all_user_defined_monitors', 'get_custom_metrics', 'get_custom_rule', 'get_custom_rules', 'get_generated_rules', 'get_circuit_breaker_rule_state', 'get_run_sql_rule_state', 'get_insights', 'get_insight', 'get_reports', 'get_report_url', 'get_lineage_node', 'get_lineage_edge', 'get_lineage_node_block_pattern', 'get_lineage_node_block_patterns', 'get_catalog_object_metadata', 'get_object_properties', 'get_object_property_name_values', 'get_object_property_names', 'get_object_property_values', 'get_active_monitors', 'get_monitor_summary', 'get_monitors_by_type', 'get_monitor', 'get_monitor_configuration', 'get_monitor_scheduling_configuration', 'get_time_axis_sql_expressions', 'get_data_assets_dashboard', 'get_incident_dashboard_data', 'get_incident_data_weekly', 'get_monitor_dashboard_data', 'get_blast_radius_direct_users', 'get_blast_radius_direct_users_v2', 'get_blast_radius_direct_queries', 'get_blast_radius_direct_queries_v2', 'get_blast_radius_direct_queries_summary', 'get_incident_tables', 'get_incident_warehouse_tables', 'get_direct_blast_radius_counts', 'get_blast_radius_direct_queries_for_user', 'get_airflow_tasks', 'get_airflow_task_attempts', 'get_airflow_task_logs', 'get_events', 'get_comments_for_monitor_incidents', 'get_event', 'get_event_comments', 'get_event_type_summary', 'get_incidents', 'get_incident_reaction', 'get_incident_summaries', 'get_incident_type_summary', 'get_slack_messages_for_incident', 'get_slack_engagements_for_incident', 'get_all_domains', 'get_domain', 'get_account_roles', 'get_authorization_groups', 'get_user_authorization', 'search', 'get_object', 'get_metadata', 'get_metrics_v3', 'get_non_table_metrics', 'get_aggregated_metrics', 'get_latest_table_access_timestamp_metrics', 'get_top_category_labels', 'get_segmented_where_condition_labels', 'get_first_seen_dimensions_by_labels', 'get_first_and_last_seen_dimensions_by_labels', 'get_direct_lineage', 'get_downstream_bi', 'get_query_list', 'get_query_by_id', 'get_query_by_query_hash', 'get_query_data_by_query_hash', 'get_query_data', 'get_query_log_hashes_that_affect_these_tables', 'get_query_log_hashes_on_these_tables', 'get_related_users', 'get_lineage_node_properties', 'get_recent_timestamp', 'get_hourly_row_counts', 'get_digraph', 'get_pipeline_freshness_v2', 'get_custom_sql_output_sample', 'get_metric_sampling', 'get_dt_sampling', 'get_fh_reproduction_query', 'get_dt_reproduction_query', 'run_custom_query', 'test_sql_query_part', 'test_sql_query_where_expression', 'get_table_stats', 'get_resource', 'get_resources', 'get_table_fields_importance', 'get_user', 'get_user_by_id', 'get_warehouse', 'get_collection_properties', 'get_table', 'get_tables', 'get_bq_projects', 'get_slack_oauth_url', 'get_slack_channels', 'get_projects', 'get_datasets', 'get_field_bi_lineage', 'get_event_muting_rules', 'get_users_in_account', 'get_invites_in_account', 'get_token_metadata', 'get_integration_keys', 'test_existing_connection', 'test_telnet_connection', 'test_tcp_open_connection', 'test_notification_integration', 'get_databricks_cluster_info', 'get_databricks_notebook_link', 'validate_connection_type', 'get_event_onboarding_data')
    get_dbt_projects = sgqlc.types.Field(DbtProjectConnection, graphql_name='getDbtProjects', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(String, graphql_name='uuid', default=None)),
        ('project_name', sgqlc.types.Arg(String, graphql_name='projectName', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    get_dbt_nodes = sgqlc.types.Field(DbtNodeConnection, graphql_name='getDbtNodes', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(String, graphql_name='uuid', default=None)),
        ('dbt_project_uuid', sgqlc.types.Arg(String, graphql_name='dbtProjectUuid', default=None)),
        ('table_mcon', sgqlc.types.Arg(String, graphql_name='tableMcon', default=None)),
        ('table_mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tableMcons', default=None)),
        ('dbt_unique_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='dbtUniqueIds', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    get_dbt_runs = sgqlc.types.Field(DbtRunConnection, graphql_name='getDbtRuns', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(String, graphql_name='uuid', default=None)),
        ('dbt_project_uuid', sgqlc.types.Arg(String, graphql_name='dbtProjectUuid', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    get_dbt_model_results = sgqlc.types.Field(DbtModelResultsConnection, graphql_name='getDbtModelResults', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('run_start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='runStartTime', default=None)),
        ('run_end_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='runEndTime', default=None)),
        ('status', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='status', default=None)),
        ('model', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='model', default=None)),
        ('mcon', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcon', default=None)),
))
    )
    get_dbt_test_results = sgqlc.types.Field(DbtTestResultsConnection, graphql_name='getDbtTestResults', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('run_start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='runStartTime', default=None)),
        ('run_end_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='runEndTime', default=None)),
        ('status', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='status', default=None)),
        ('model', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='model', default=None)),
        ('mcon', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcon', default=None)),
))
    )
    get_custom_users = sgqlc.types.Field(CustomUserConnection, graphql_name='getCustomUsers', args=sgqlc.types.ArgDict((
        ('custom_user_id', sgqlc.types.Arg(String, graphql_name='customUserId', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    get_docs = sgqlc.types.Field(DocConnection, graphql_name='getDocs', args=sgqlc.types.ArgDict((
        ('doc_mcon', sgqlc.types.Arg(String, graphql_name='docMcon', default=None)),
        ('linked_mcon', sgqlc.types.Arg(String, graphql_name='linkedMcon', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    get_unified_users = sgqlc.types.Field('UnifiedUserConnection', graphql_name='getUnifiedUsers', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(String, graphql_name='uuid', default=None)),
        ('display_name_search', sgqlc.types.Arg(String, graphql_name='displayNameSearch', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    get_unified_user_assignments = sgqlc.types.Field('UnifiedUserAssignmentConnection', graphql_name='getUnifiedUserAssignments', args=sgqlc.types.ArgDict((
        ('unified_user_id', sgqlc.types.Arg(String, graphql_name='unifiedUserId', default=None)),
        ('object_mcon', sgqlc.types.Arg(String, graphql_name='objectMcon', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    get_monte_carlo_config_templates = sgqlc.types.Field(MonteCarloConfigTemplateConnection, graphql_name='getMonteCarloConfigTemplates', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('namespace', sgqlc.types.Arg(String, graphql_name='namespace', default=None)),
))
    )
    get_rca_result = sgqlc.types.Field('RcaResult', graphql_name='getRcaResult', args=sgqlc.types.ArgDict((
        ('event_uuid', sgqlc.types.Arg(UUID, graphql_name='eventUuid', default=None)),
))
    )
    get_sensitivity = sgqlc.types.Field('SensitivityThreshold', graphql_name='getSensitivity', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('event_type', sgqlc.types.Arg(String, graphql_name='eventType', default=None)),
        ('monitor_uuid', sgqlc.types.Arg(UUID, graphql_name='monitorUuid', default=None)),
))
    )
    thresholds = sgqlc.types.Field('ThresholdsData', graphql_name='thresholds')
    get_thresholds = sgqlc.types.Field('ThresholdsData', graphql_name='getThresholds')
    get_table_columns_lineage = sgqlc.types.Field('TableColumnsLineageResult', graphql_name='getTableColumnsLineage', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
))
    )
    get_derived_tables_partial_lineage = sgqlc.types.Field(DerivedTablesLineageResult, graphql_name='getDerivedTablesPartialLineage', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('column', sgqlc.types.Arg(String, graphql_name='column', default=None)),
        ('cursor', sgqlc.types.Arg(String, graphql_name='cursor', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=20)),
))
    )
    get_parsed_query = sgqlc.types.Field(ParsedQueryResult, graphql_name='getParsedQuery', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
))
    )
    get_job_execution_history_logs = sgqlc.types.Field(sgqlc.types.list_of(JobExecutionHistoryLog), graphql_name='getJobExecutionHistoryLogs', args=sgqlc.types.ArgDict((
        ('job_schedule_uuid', sgqlc.types.Arg(String, graphql_name='jobScheduleUuid', default=None)),
        ('monitor_uuid', sgqlc.types.Arg(String, graphql_name='monitorUuid', default=None)),
        ('custom_rule_uuid', sgqlc.types.Arg(String, graphql_name='customRuleUuid', default=None)),
        ('history_days', sgqlc.types.Arg(Int, graphql_name='historyDays', default=None)),
))
    )
    get_dimension_tracking_monitor_suggestions = sgqlc.types.Field(DimensionTrackingSuggestionsConnection, graphql_name='getDimensionTrackingMonitorSuggestions', args=sgqlc.types.ArgDict((
        ('entities', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='entities', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    get_field_health_monitor_suggestions = sgqlc.types.Field(FieldHealthSuggestionsConnection, graphql_name='getFieldHealthMonitorSuggestions', args=sgqlc.types.ArgDict((
        ('entities', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='entities', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    monitor_labels = sgqlc.types.Field(sgqlc.types.list_of(MonitorLabel), graphql_name='monitorLabels')
    get_account_monitor_labels = sgqlc.types.Field(sgqlc.types.list_of(MonitorLabelObject), graphql_name='getAccountMonitorLabels')
    get_monitors = sgqlc.types.Field(sgqlc.types.list_of('Monitor'), graphql_name='getMonitors', args=sgqlc.types.ArgDict((
        ('monitor_types', sgqlc.types.Arg(sgqlc.types.list_of(UserDefinedMonitors), graphql_name='monitorTypes', default=None)),
        ('status_types', sgqlc.types.Arg(sgqlc.types.list_of(MonitorStatusType), graphql_name='statusTypes', default=None)),
        ('description_field_or_table', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='descriptionFieldOrTable', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('uuids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='uuids', default=None)),
        ('created_by_filters', sgqlc.types.Arg(CreatedByFilters, graphql_name='createdByFilters', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('search', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='search', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    get_all_user_defined_monitors_v2 = sgqlc.types.Field('UserDefinedMonitorConnectionV2Connection', graphql_name='getAllUserDefinedMonitorsV2', args=sgqlc.types.ArgDict((
        ('user_defined_monitor_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='userDefinedMonitorTypes', default=None)),
        ('created_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='createdBy', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('entities', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='entities', default=None)),
        ('description_field_or_table', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='descriptionFieldOrTable', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('is_template_managed', sgqlc.types.Arg(Boolean, graphql_name='isTemplateManaged', default=None)),
        ('namespace', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='namespace', default=None)),
        ('rule_name', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='ruleName', default=None)),
        ('search', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='search', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    get_all_user_defined_monitors = sgqlc.types.Field('UserDefinedMonitorConnection', graphql_name='getAllUserDefinedMonitors', args=sgqlc.types.ArgDict((
        ('user_defined_monitor_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='userDefinedMonitorTypes', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    get_custom_metrics = sgqlc.types.Field(Metrics, graphql_name='getCustomMetrics', args=sgqlc.types.ArgDict((
        ('rule_uuid', sgqlc.types.Arg(UUID, graphql_name='ruleUuid', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=5000)),
))
    )
    get_custom_rule = sgqlc.types.Field('CustomRule', graphql_name='getCustomRule', args=sgqlc.types.ArgDict((
        ('rule_id', sgqlc.types.Arg(UUID, graphql_name='ruleId', default=None)),
        ('description_contains', sgqlc.types.Arg(String, graphql_name='descriptionContains', default=None)),
        ('custom_sql_contains', sgqlc.types.Arg(String, graphql_name='customSqlContains', default=None)),
))
    )
    get_custom_rules = sgqlc.types.Field(CustomRuleConnection, graphql_name='getCustomRules', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('rule_type', sgqlc.types.Arg(String, graphql_name='ruleType', default=None)),
))
    )
    get_generated_rules = sgqlc.types.Field(sgqlc.types.list_of('CustomRule'), graphql_name='getGeneratedRules', args=sgqlc.types.ArgDict((
        ('generated_by_uuid', sgqlc.types.Arg(UUID, graphql_name='generatedByUuid', default=None)),
))
    )
    get_circuit_breaker_rule_state = sgqlc.types.Field(CircuitBreakerState, graphql_name='getCircuitBreakerRuleState', args=sgqlc.types.ArgDict((
        ('job_execution_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='jobExecutionUuid', default=None)),
))
    )
    get_run_sql_rule_state = sgqlc.types.Field(sgqlc.types.list_of(CircuitBreakerState), graphql_name='getRunSqlRuleState', args=sgqlc.types.ArgDict((
        ('job_execution_uuids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(UUID)), graphql_name='jobExecutionUuids', default=None)),
))
    )
    get_insights = sgqlc.types.Field(sgqlc.types.list_of(Insight), graphql_name='getInsights')
    get_insight = sgqlc.types.Field(Insight, graphql_name='getInsight', args=sgqlc.types.ArgDict((
        ('insight_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='insightName', default=None)),
))
    )
    get_reports = sgqlc.types.Field(sgqlc.types.list_of('Report'), graphql_name='getReports', args=sgqlc.types.ArgDict((
        ('insight_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='insightName', default=None)),
))
    )
    get_report_url = sgqlc.types.Field('ResponseURL', graphql_name='getReportUrl', args=sgqlc.types.ArgDict((
        ('insight_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='insightName', default=None)),
        ('report_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='reportName', default=None)),
        ('created_before', sgqlc.types.Arg(DateTime, graphql_name='createdBefore', default=None)),
))
    )
    get_lineage_node = sgqlc.types.Field(LineageNode, graphql_name='getLineageNode', args=sgqlc.types.ArgDict((
        ('object_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='objectType', default=None)),
        ('object_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='objectId', default=None)),
        ('resource_id', sgqlc.types.Arg(UUID, graphql_name='resourceId', default=None)),
        ('resource_name', sgqlc.types.Arg(String, graphql_name='resourceName', default=None)),
))
    )
    get_lineage_edge = sgqlc.types.Field(LineageEdge, graphql_name='getLineageEdge', args=sgqlc.types.ArgDict((
        ('source', sgqlc.types.Arg(NodeInput, graphql_name='source', default=None)),
        ('destination', sgqlc.types.Arg(NodeInput, graphql_name='destination', default=None)),
))
    )
    get_lineage_node_block_pattern = sgqlc.types.Field(LineageNodeBlockPattern, graphql_name='getLineageNodeBlockPattern', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='uuid', default=None)),
))
    )
    get_lineage_node_block_patterns = sgqlc.types.Field(sgqlc.types.list_of(LineageNodeBlockPattern), graphql_name='getLineageNodeBlockPatterns', args=sgqlc.types.ArgDict((
        ('resource_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='resourceId', default=None)),
))
    )
    get_catalog_object_metadata = sgqlc.types.Field(CatalogObjectMetadataConnection, graphql_name='getCatalogObjectMetadata', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
))
    )
    get_object_properties = sgqlc.types.Field(ObjectPropertyConnection, graphql_name='getObjectProperties', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('mcon_id', sgqlc.types.Arg(String, graphql_name='mconId', default=None)),
))
    )
    get_object_property_name_values = sgqlc.types.Field(PropertyNameValues, graphql_name='getObjectPropertyNameValues', args=sgqlc.types.ArgDict((
        ('search_string', sgqlc.types.Arg(String, graphql_name='searchString', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    get_object_property_names = sgqlc.types.Field(PropertyNames, graphql_name='getObjectPropertyNames', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=100)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('search_string', sgqlc.types.Arg(String, graphql_name='searchString', default=None)),
))
    )
    get_object_property_values = sgqlc.types.Field(PropertyValues, graphql_name='getObjectPropertyValues', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=100)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('property_name', sgqlc.types.Arg(String, graphql_name='propertyName', default=None)),
        ('search_string', sgqlc.types.Arg(String, graphql_name='searchString', default=None)),
))
    )
    get_active_monitors = sgqlc.types.Field(MetricMonitoringConnection, graphql_name='getActiveMonitors', args=sgqlc.types.ArgDict((
        ('entities', sgqlc.types.Arg(String, graphql_name='entities', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    get_monitor_summary = sgqlc.types.Field(MonitorSummary, graphql_name='getMonitorSummary', args=sgqlc.types.ArgDict((
        ('resource_id', sgqlc.types.Arg(UUID, graphql_name='resourceId', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
))
    )
    get_monitors_by_type = sgqlc.types.Field(MetricMonitoringConnection, graphql_name='getMonitorsByType', args=sgqlc.types.ArgDict((
        ('monitor_type', sgqlc.types.Arg(String, graphql_name='monitorType', default=None)),
        ('monitor_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='monitorTypes', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    get_monitor = sgqlc.types.Field('MetricMonitoring', graphql_name='getMonitor', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
        ('resource_id', sgqlc.types.Arg(UUID, graphql_name='resourceId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('monitor_type', sgqlc.types.Arg(String, graphql_name='monitorType', default=None)),
))
    )
    get_monitor_configuration = sgqlc.types.Field(MonitorConfiguration, graphql_name='getMonitorConfiguration', args=sgqlc.types.ArgDict((
        ('configuration_data', sgqlc.types.Arg(MonitorConfigurationInput, graphql_name='configurationData', default=None)),
))
    )
    get_monitor_scheduling_configuration = sgqlc.types.Field(MonitorSchedulingConfiguration, graphql_name='getMonitorSchedulingConfiguration', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
))
    )
    get_time_axis_sql_expressions = sgqlc.types.Field(sgqlc.types.list_of('SqlExpression'), graphql_name='getTimeAxisSqlExpressions')
    get_data_assets_dashboard = sgqlc.types.Field(DataAssetDashboard, graphql_name='getDataAssetsDashboard', args=sgqlc.types.ArgDict((
        ('domain_uuid', sgqlc.types.Arg(UUID, graphql_name='domainUuid', default=None)),
))
    )
    get_incident_dashboard_data = sgqlc.types.Field(IncidentDashboardData, graphql_name='getIncidentDashboardData', args=sgqlc.types.ArgDict((
        ('domain_uuid', sgqlc.types.Arg(UUID, graphql_name='domainUuid', default=None)),
        ('lookback_weeks', sgqlc.types.Arg(Int, graphql_name='lookbackWeeks', default=None)),
))
    )
    get_incident_data_weekly = sgqlc.types.Field(IncidentWeeklyDataDashboard, graphql_name='getIncidentDataWeekly', args=sgqlc.types.ArgDict((
        ('group_by', sgqlc.types.Arg(sgqlc.types.non_null(IncidentGroupBy), graphql_name='groupBy', default=None)),
        ('domain_uuid', sgqlc.types.Arg(UUID, graphql_name='domainUuid', default=None)),
        ('lookback_weeks', sgqlc.types.Arg(Int, graphql_name='lookbackWeeks', default=None)),
))
    )
    get_monitor_dashboard_data = sgqlc.types.Field(MonitorDashboardData, graphql_name='getMonitorDashboardData', args=sgqlc.types.ArgDict((
        ('domain_uuid', sgqlc.types.Arg(UUID, graphql_name='domainUuid', default=None)),
))
    )
    get_blast_radius_direct_users = sgqlc.types.Field(PaginateUsersBlastRadius, graphql_name='getBlastRadiusDirectUsers', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('lookback', sgqlc.types.Arg(sgqlc.types.non_null(LookbackRange), graphql_name='lookback', default=None)),
        ('after_key', sgqlc.types.Arg(UserAfterKeyInput, graphql_name='afterKey', default=None)),
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    get_blast_radius_direct_users_v2 = sgqlc.types.Field(PaginateUsersBlastRadius2, graphql_name='getBlastRadiusDirectUsersV2', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('lookback', sgqlc.types.Arg(sgqlc.types.non_null(LookbackRange), graphql_name='lookback', default=None)),
        ('after_key', sgqlc.types.Arg(UserAfterKeyInput2, graphql_name='afterKey', default=None)),
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    get_blast_radius_direct_queries = sgqlc.types.Field(PaginateQueriesBlastRadius, graphql_name='getBlastRadiusDirectQueries', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('lookback', sgqlc.types.Arg(sgqlc.types.non_null(LookbackRange), graphql_name='lookback', default=None)),
        ('after_key', sgqlc.types.Arg(QueryAfterKeyInput, graphql_name='afterKey', default=None)),
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    get_blast_radius_direct_queries_v2 = sgqlc.types.Field(PaginateQueriesBlastRadius2, graphql_name='getBlastRadiusDirectQueriesV2', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('lookback', sgqlc.types.Arg(sgqlc.types.non_null(LookbackRange), graphql_name='lookback', default=None)),
        ('after_key', sgqlc.types.Arg(UserAfterKeyInput2, graphql_name='afterKey', default=None)),
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    get_blast_radius_direct_queries_summary = sgqlc.types.Field(PaginateQueriesBlastRadiusSummary, graphql_name='getBlastRadiusDirectQueriesSummary', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('lookback', sgqlc.types.Arg(sgqlc.types.non_null(LookbackRange), graphql_name='lookback', default=None)),
        ('after_key', sgqlc.types.Arg(UserAfterKeyInput2, graphql_name='afterKey', default=None)),
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    get_incident_tables = sgqlc.types.Field(IncidentTableMcons, graphql_name='getIncidentTables', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
))
    )
    get_incident_warehouse_tables = sgqlc.types.Field(sgqlc.types.list_of('WarehouseTable'), graphql_name='getIncidentWarehouseTables', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
))
    )
    get_direct_blast_radius_counts = sgqlc.types.Field(BlastRadiusCount, graphql_name='getDirectBlastRadiusCounts', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('lookback', sgqlc.types.Arg(sgqlc.types.non_null(LookbackRange), graphql_name='lookback', default=None)),
))
    )
    get_blast_radius_direct_queries_for_user = sgqlc.types.Field(sgqlc.types.list_of(BlastRadiusUserQuery), graphql_name='getBlastRadiusDirectQueriesForUser', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('username', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='username', default=None)),
        ('lookback', sgqlc.types.Arg(sgqlc.types.non_null(LookbackRange), graphql_name='lookback', default=None)),
))
    )
    get_airflow_tasks = sgqlc.types.Field(AirflowTaskInstanceConnection, graphql_name='getAirflowTasks', args=sgqlc.types.ArgDict((
        ('task_states', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='taskStates', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('table_mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tableMcons', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    get_airflow_task_attempts = sgqlc.types.Field(AirflowTaskInstanceConnection, graphql_name='getAirflowTaskAttempts', args=sgqlc.types.ArgDict((
        ('dag_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='dagId', default=None)),
        ('execution_date', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='executionDate', default=None)),
        ('task_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='taskId', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    get_airflow_task_logs = sgqlc.types.Field(AirflowTaskLog, graphql_name='getAirflowTaskLogs', args=sgqlc.types.ArgDict((
        ('dag_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='dagId', default=None)),
        ('execution_date', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='executionDate', default=None)),
        ('task_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='taskId', default=None)),
        ('try_number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='tryNumber', default=None)),
        ('task_timestamp', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='taskTimestamp', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=1000)),
))
    )
    get_events = sgqlc.types.Field(EventConnection, graphql_name='getEvents', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('event_type', sgqlc.types.Arg(String, graphql_name='eventType', default=None)),
        ('event_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='eventTypes', default=None)),
        ('dataset', sgqlc.types.Arg(String, graphql_name='dataset', default=None)),
        ('tables_older_than_days', sgqlc.types.Arg(Int, graphql_name='tablesOlderThanDays', default=None)),
        ('event_states', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='eventStates', default=None)),
        ('exclude_state', sgqlc.types.Arg(String, graphql_name='excludeState', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('incident_id', sgqlc.types.Arg(UUID, graphql_name='incidentId', default=None)),
        ('include_timeline_events', sgqlc.types.Arg(Boolean, graphql_name='includeTimelineEvents', default=None)),
        ('include_anomaly_events', sgqlc.types.Arg(Boolean, graphql_name='includeAnomalyEvents', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    get_comments_for_monitor_incidents = sgqlc.types.Field(EventConnection, graphql_name='getCommentsForMonitorIncidents', args=sgqlc.types.ArgDict((
        ('monitor_uuids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='monitorUuids', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    get_event = sgqlc.types.Field('Event', graphql_name='getEvent', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
))
    )
    get_event_comments = sgqlc.types.Field(EventCommentConnection, graphql_name='getEventComments', args=sgqlc.types.ArgDict((
        ('event_id', sgqlc.types.Arg(UUID, graphql_name='eventId', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    get_event_type_summary = sgqlc.types.Field(EventTypeSummary, graphql_name='getEventTypeSummary', args=sgqlc.types.ArgDict((
        ('resource_id', sgqlc.types.Arg(UUID, graphql_name='resourceId', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
))
    )
    get_incidents = sgqlc.types.Field(IncidentConnection, graphql_name='getIncidents', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('incident_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='incidentTypes', default=None)),
        ('incident_sub_types', sgqlc.types.Arg(sgqlc.types.list_of(IncidentSubType), graphql_name='incidentSubTypes', default=None)),
        ('event_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='eventTypes', default=None)),
        ('event_states', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='eventStates', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('incident_ids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='incidentIds', default=None)),
        ('include_feedback', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='includeFeedback', default=None)),
        ('exclude_feedback', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='excludeFeedback', default=None)),
        ('projects', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='projects', default=None)),
        ('datasets', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='datasets', default=None)),
        ('tables', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tables', default=None)),
        ('full_table_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='fullTableIds', default=None)),
        ('include_timeline_events', sgqlc.types.Arg(Boolean, graphql_name='includeTimelineEvents', default=None)),
        ('include_anomaly_events', sgqlc.types.Arg(Boolean, graphql_name='includeAnomalyEvents', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('monitor_ids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='monitorIds', default=None)),
        ('reaction_types', sgqlc.types.Arg(sgqlc.types.list_of(IncidentReactionType), graphql_name='reactionTypes', default=None)),
        ('rule_id', sgqlc.types.Arg(UUID, graphql_name='ruleId', default=None)),
        ('tag_key_values', sgqlc.types.Arg(sgqlc.types.list_of(TagPair), graphql_name='tagKeyValues', default=None)),
        ('tag_keys', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tagKeys', default=None)),
        ('min_event_count', sgqlc.types.Arg(Int, graphql_name='minEventCount', default=None)),
        ('max_event_count', sgqlc.types.Arg(Int, graphql_name='maxEventCount', default=None)),
        ('contains_key_asset', sgqlc.types.Arg(Boolean, graphql_name='containsKeyAsset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    get_incident_reaction = sgqlc.types.Field('IncidentReaction', graphql_name='getIncidentReaction', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(UUID, graphql_name='incidentId', default=None)),
))
    )
    get_incident_summaries = sgqlc.types.Field(sgqlc.types.list_of(IncidentSummary), graphql_name='getIncidentSummaries', args=sgqlc.types.ArgDict((
        ('incident_ids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='incidentIds', default=None)),
))
    )
    get_incident_type_summary = sgqlc.types.Field(IncidentTypeSummary, graphql_name='getIncidentTypeSummary', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
))
    )
    get_slack_messages_for_incident = sgqlc.types.Field(sgqlc.types.list_of('SlackMessageDetails'), graphql_name='getSlackMessagesForIncident', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
))
    )
    get_slack_engagements_for_incident = sgqlc.types.Field(sgqlc.types.list_of('SlackEngagement'), graphql_name='getSlackEngagementsForIncident', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('event_types', sgqlc.types.Arg(sgqlc.types.list_of(SlackEngagementEventType), graphql_name='eventTypes', default=None)),
        ('exclude_bot_engagements', sgqlc.types.Arg(Boolean, graphql_name='excludeBotEngagements', default=None)),
))
    )
    get_all_domains = sgqlc.types.Field(sgqlc.types.list_of(DomainOutput), graphql_name='getAllDomains')
    get_domain = sgqlc.types.Field(DomainOutput, graphql_name='getDomain', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='uuid', default=None)),
))
    )
    get_account_roles = sgqlc.types.Field(sgqlc.types.list_of('RoleOutput'), graphql_name='getAccountRoles')
    get_authorization_groups = sgqlc.types.Field(sgqlc.types.list_of(AuthorizationGroupOutput), graphql_name='getAuthorizationGroups')
    get_user_authorization = sgqlc.types.Field('UserAuthorizationOutput', graphql_name='getUserAuthorization')
    search = sgqlc.types.Field('SearchResponse', graphql_name='search', args=sgqlc.types.ArgDict((
        ('object_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='objectTypes', default=None)),
        ('ignore_object_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='ignoreObjectTypes', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=50)),
        ('full_results', sgqlc.types.Arg(Boolean, graphql_name='fullResults', default=True)),
        ('operator', sgqlc.types.Arg(String, graphql_name='operator', default='OR')),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('parent_mcon', sgqlc.types.Arg(String, graphql_name='parentMcon', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('tags_only', sgqlc.types.Arg(Boolean, graphql_name='tagsOnly', default=False)),
        ('include_facet_types', sgqlc.types.Arg(sgqlc.types.list_of(FacetType), graphql_name='includeFacetTypes', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
        ('tag_name_query', sgqlc.types.Arg(String, graphql_name='tagNameQuery', default=None)),
        ('tag_value_query', sgqlc.types.Arg(String, graphql_name='tagValueQuery', default=None)),
        ('resource_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='resourceIds', default=None)),
))
    )
    get_object = sgqlc.types.Field(ObjectDocument, graphql_name='getObject', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
))
    )
    get_metadata = sgqlc.types.Field(sgqlc.types.list_of(ObjectDocument), graphql_name='getMetadata', args=sgqlc.types.ArgDict((
        ('mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcons', default=None)),
))
    )
    get_metrics_v3 = sgqlc.types.Field(Metrics, graphql_name='getMetricsV3', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('metric', sgqlc.types.Arg(String, graphql_name='metric', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('field', sgqlc.types.Arg(String, graphql_name='field', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('dimension_filters', sgqlc.types.Arg(sgqlc.types.list_of(MetricDimensionFilter), graphql_name='dimensionFilters', default=None)),
))
    )
    get_non_table_metrics = sgqlc.types.Field(NonTableMetrics, graphql_name='getNonTableMetrics', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('metric', sgqlc.types.Arg(String, graphql_name='metric', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('dimension_filters', sgqlc.types.Arg(sgqlc.types.list_of(MetricDimensionFilter), graphql_name='dimensionFilters', default=None)),
))
    )
    get_aggregated_metrics = sgqlc.types.Field(Metrics, graphql_name='getAggregatedMetrics', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
        ('full_table_id_list', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='fullTableIdList', default=None)),
        ('metric', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='metric', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('date_aggregation_bucket_size', sgqlc.types.Arg(String, graphql_name='dateAggregationBucketSize', default='day')),
))
    )
    get_latest_table_access_timestamp_metrics = sgqlc.types.Field(Metrics, graphql_name='getLatestTableAccessTimestampMetrics', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
        ('full_table_id_list', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='fullTableIdList', default=None)),
        ('metric', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='metric', default=None)),
))
    )
    get_top_category_labels = sgqlc.types.Field(sgqlc.types.list_of(CategoryLabelRank), graphql_name='getTopCategoryLabels', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('monitor_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='monitorIds', default=None)),
        ('field', sgqlc.types.Arg(String, graphql_name='field', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
))
    )
    get_segmented_where_condition_labels = sgqlc.types.Field(sgqlc.types.list_of('WhereConditionSegments'), graphql_name='getSegmentedWhereConditionLabels', args=sgqlc.types.ArgDict((
        ('monitor_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='monitorUuid', default=None)),
        ('warehouse_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='warehouseUuid', default=None)),
        ('full_table_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='fullTableId', default=None)),
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
))
    )
    get_first_seen_dimensions_by_labels = sgqlc.types.Field(sgqlc.types.list_of(DimensionLabel), graphql_name='getFirstSeenDimensionsByLabels', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('field', sgqlc.types.Arg(String, graphql_name='field', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('dimensions_filter', sgqlc.types.Arg(sgqlc.types.list_of(MetricDimensionFilter), graphql_name='dimensionsFilter', default=None)),
))
    )
    get_first_and_last_seen_dimensions_by_labels = sgqlc.types.Field(sgqlc.types.list_of(DimensionLabelList), graphql_name='getFirstAndLastSeenDimensionsByLabels', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('field', sgqlc.types.Arg(String, graphql_name='field', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('dimensions_filter', sgqlc.types.Arg(sgqlc.types.list_of(MetricDimensionFilter), graphql_name='dimensionsFilter', default=None)),
))
    )
    get_direct_lineage = sgqlc.types.Field(sgqlc.types.list_of(MultipleDirectLineage), graphql_name='getDirectLineage', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('node_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='nodeIds', default=None)),
        ('mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcons', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
))
    )
    get_downstream_bi = sgqlc.types.Field(sgqlc.types.list_of(DownstreamBI), graphql_name='getDownstreamBi', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('node_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='nodeIds', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
))
    )
    get_query_list = sgqlc.types.Field(sgqlc.types.list_of('QueryListResponse'), graphql_name='getQueryList', args=sgqlc.types.ArgDict((
        ('query_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='queryType', default=None)),
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='endTime', default=None)),
        ('user_name', sgqlc.types.Arg(String, graphql_name='userName', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    get_query_by_id = sgqlc.types.Field(sgqlc.types.list_of('QueryDataObject'), graphql_name='getQueryById', args=sgqlc.types.ArgDict((
        ('query_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='queryId', default=None)),
        ('timestamp', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='timestamp', default=None)),
        ('query_format', sgqlc.types.Arg(String, graphql_name='queryFormat', default=None)),
))
    )
    get_query_by_query_hash = sgqlc.types.Field(sgqlc.types.list_of('QueryDataObject'), graphql_name='getQueryByQueryHash', args=sgqlc.types.ArgDict((
        ('query_hash', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='queryHash', default=None)),
        ('day', sgqlc.types.Arg(sgqlc.types.non_null(Date), graphql_name='day', default=None)),
        ('query_format', sgqlc.types.Arg(String, graphql_name='queryFormat', default=None)),
))
    )
    get_query_data_by_query_hash = sgqlc.types.Field(sgqlc.types.list_of('QueryLogResponse'), graphql_name='getQueryDataByQueryHash', args=sgqlc.types.ArgDict((
        ('query_hash', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='queryHash', default=None)),
        ('day', sgqlc.types.Arg(sgqlc.types.non_null(Date), graphql_name='day', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    get_query_data = sgqlc.types.Field(sgqlc.types.list_of('QueryLogResponse'), graphql_name='getQueryData', args=sgqlc.types.ArgDict((
        ('query_id', sgqlc.types.Arg(String, graphql_name='queryId', default=None)),
        ('query_hash', sgqlc.types.Arg(String, graphql_name='queryHash', default=None)),
        ('day', sgqlc.types.Arg(sgqlc.types.non_null(Date), graphql_name='day', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    get_query_log_hashes_that_affect_these_tables = sgqlc.types.Field(sgqlc.types.list_of('QueryLogHashes'), graphql_name='getQueryLogHashesThatAffectTheseTables', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='fullTableIds', default=None)),
        ('mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcons', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('users', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='users', default=None)),
))
    )
    get_query_log_hashes_on_these_tables = sgqlc.types.Field(sgqlc.types.list_of('QueryLogHashes'), graphql_name='getQueryLogHashesOnTheseTables', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='fullTableIds', default=None)),
        ('mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcons', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('users', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='users', default=None)),
))
    )
    get_related_users = sgqlc.types.Field(sgqlc.types.list_of('RelatedUserCount'), graphql_name='getRelatedUsers', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('query_type', sgqlc.types.Arg(String, graphql_name='queryType', default=None)),
))
    )
    get_lineage_node_properties = sgqlc.types.Field(sgqlc.types.list_of(NodeProperties), graphql_name='getLineageNodeProperties', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('node_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='nodeIds', default=None)),
        ('mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcons', default=None)),
))
    )
    get_recent_timestamp = sgqlc.types.Field(sgqlc.types.list_of('RecentTimestamp'), graphql_name='getRecentTimestamp', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
))
    )
    get_hourly_row_counts = sgqlc.types.Field(HourlyRowCountsResponse, graphql_name='getHourlyRowCounts', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('interval_days', sgqlc.types.Arg(Int, graphql_name='intervalDays', default=2)),
        ('field_name', sgqlc.types.Arg(String, graphql_name='fieldName', default=None)),
))
    )
    get_digraph = sgqlc.types.Field(DirectedGraph, graphql_name='getDigraph', args=sgqlc.types.ArgDict((
        ('metadata_version', sgqlc.types.Arg(String, graphql_name='metadataVersion', default=None)),
))
    )
    get_pipeline_freshness_v2 = sgqlc.types.Field(PipelineFreshness, graphql_name='getPipelineFreshnessV2', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='fullTableIds', default=None)),
        ('mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcons', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
))
    )
    get_custom_sql_output_sample = sgqlc.types.Field(CustomSQLOutputSample, graphql_name='getCustomSqlOutputSample', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
        ('job_execution_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='jobExecutionUuid', default=None)),
))
    )
    get_metric_sampling = sgqlc.types.Field(MetricSampling, graphql_name='getMetricSampling', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('time_axis', sgqlc.types.Arg(String, graphql_name='timeAxis', default=None)),
        ('field', sgqlc.types.Arg(String, graphql_name='field', default=None)),
        ('metric', sgqlc.types.Arg(String, graphql_name='metric', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('dry_run', sgqlc.types.Arg(Boolean, graphql_name='dryRun', default=False)),
        ('monitor_uuid', sgqlc.types.Arg(UUID, graphql_name='monitorUuid', default=None)),
))
    )
    get_dt_sampling = sgqlc.types.Field(MetricSampling, graphql_name='getDtSampling', args=sgqlc.types.ArgDict((
        ('monitor_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='monitorUuid', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('dry_run', sgqlc.types.Arg(Boolean, graphql_name='dryRun', default=False)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    get_fh_reproduction_query = sgqlc.types.Field(InvestigationQuery, graphql_name='getFhReproductionQuery', args=sgqlc.types.ArgDict((
        ('monitor_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='monitorUuid', default=None)),
        ('event_created_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='eventCreatedTime', default=None)),
        ('field', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='field', default=None)),
        ('metric', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='metric', default=None)),
        ('dry_run', sgqlc.types.Arg(Boolean, graphql_name='dryRun', default=True)),
))
    )
    get_dt_reproduction_query = sgqlc.types.Field(InvestigationQuery, graphql_name='getDtReproductionQuery', args=sgqlc.types.ArgDict((
        ('monitor_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='monitorUuid', default=None)),
        ('event_created_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='eventCreatedTime', default=None)),
        ('field', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='field', default=None)),
        ('field_val', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='fieldVal', default=None)),
        ('dry_run', sgqlc.types.Arg(Boolean, graphql_name='dryRun', default=True)),
))
    )
    run_custom_query = sgqlc.types.Field('SQLResponse', graphql_name='runCustomQuery', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('variables', sgqlc.types.Arg(JSONString, graphql_name='variables', default=None)),
        ('query_result_type', sgqlc.types.Arg(QueryResultType, graphql_name='queryResultType', default=None)),
))
    )
    test_sql_query_part = sgqlc.types.Field('SQLResponse', graphql_name='testSqlQueryPart', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('query_part', sgqlc.types.Arg(String, graphql_name='queryPart', default=None)),
))
    )
    test_sql_query_where_expression = sgqlc.types.Field('SQLResponse', graphql_name='testSqlQueryWhereExpression', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('where_expression', sgqlc.types.Arg(String, graphql_name='whereExpression', default=None)),
))
    )
    get_table_stats = sgqlc.types.Field('TableStatsConnection', graphql_name='getTableStats', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='fullTableIds', default=None)),
        ('mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcons', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    get_resource = sgqlc.types.Field('Resource', graphql_name='getResource', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
))
    )
    get_resources = sgqlc.types.Field(sgqlc.types.list_of('Resource'), graphql_name='getResources')
    get_table_fields_importance = sgqlc.types.Field('TableFieldsImportance', graphql_name='getTableFieldsImportance', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
))
    )
    get_user = sgqlc.types.Field('User', graphql_name='getUser')
    get_user_by_id = sgqlc.types.Field('User', graphql_name='getUserById')
    get_warehouse = sgqlc.types.Field('Warehouse', graphql_name='getWarehouse', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
))
    )
    get_collection_properties = sgqlc.types.Field(CollectionProperties, graphql_name='getCollectionProperties', args=sgqlc.types.ArgDict((
        ('region', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='region', default=None)),
))
    )
    get_table = sgqlc.types.Field('WarehouseTable', graphql_name='getTable', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
))
    )
    get_tables = sgqlc.types.Field('WarehouseTableConnection', graphql_name='getTables', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('status', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='status', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('table_id', sgqlc.types.Arg(String, graphql_name='tableId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('warehouse', sgqlc.types.Arg(ID, graphql_name='warehouse', default=None)),
        ('discovered_time', sgqlc.types.Arg(DateTime, graphql_name='discoveredTime', default=None)),
        ('friendly_name', sgqlc.types.Arg(String, graphql_name='friendlyName', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('location', sgqlc.types.Arg(String, graphql_name='location', default=None)),
        ('project_name', sgqlc.types.Arg(String, graphql_name='projectName', default=None)),
        ('dataset', sgqlc.types.Arg(String, graphql_name='dataset', default=None)),
        ('table_type', sgqlc.types.Arg(String, graphql_name='tableType', default=None)),
        ('is_encrypted', sgqlc.types.Arg(Boolean, graphql_name='isEncrypted', default=None)),
        ('created_time', sgqlc.types.Arg(DateTime, graphql_name='createdTime', default=None)),
        ('last_modified', sgqlc.types.Arg(DateTime, graphql_name='lastModified', default=None)),
        ('view_query', sgqlc.types.Arg(String, graphql_name='viewQuery', default=None)),
        ('path', sgqlc.types.Arg(String, graphql_name='path', default=None)),
        ('priority', sgqlc.types.Arg(Int, graphql_name='priority', default=None)),
        ('tracked', sgqlc.types.Arg(Boolean, graphql_name='tracked', default=None)),
        ('freshness_anomaly', sgqlc.types.Arg(Boolean, graphql_name='freshnessAnomaly', default=None)),
        ('size_anomaly', sgqlc.types.Arg(Boolean, graphql_name='sizeAnomaly', default=None)),
        ('freshness_size_anomaly', sgqlc.types.Arg(Boolean, graphql_name='freshnessSizeAnomaly', default=None)),
        ('metric_anomaly', sgqlc.types.Arg(Boolean, graphql_name='metricAnomaly', default=None)),
        ('dynamic_table', sgqlc.types.Arg(Boolean, graphql_name='dynamicTable', default=None)),
        ('is_deleted', sgqlc.types.Arg(Boolean, graphql_name='isDeleted', default=None)),
        ('last_observed', sgqlc.types.Arg(DateTime, graphql_name='lastObserved', default=None)),
        ('data_provider', sgqlc.types.Arg(String, graphql_name='dataProvider', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('last_observed__gt', sgqlc.types.Arg(DateTime, graphql_name='lastObserved_Gt', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
))
    )
    get_bq_projects = sgqlc.types.Field(sgqlc.types.list_of(BigQueryProject), graphql_name='getBqProjects', args=sgqlc.types.ArgDict((
        ('credentials_key', sgqlc.types.Arg(String, graphql_name='credentialsKey', default=None)),
))
    )
    get_slack_oauth_url = sgqlc.types.Field('SlackOauthUrlResponse', graphql_name='getSlackOauthUrl', args=sgqlc.types.ArgDict((
        ('slack_app_type', sgqlc.types.Arg(SlackAppType, graphql_name='slackAppType', default=None)),
))
    )
    get_slack_channels = sgqlc.types.Field('SlackChannelResponse', graphql_name='getSlackChannels', args=sgqlc.types.ArgDict((
        ('exclude_archived', sgqlc.types.Arg(Boolean, graphql_name='excludeArchived', default=None)),
        ('ignore_cached', sgqlc.types.Arg(Boolean, graphql_name='ignoreCached', default=None)),
))
    )
    get_projects = sgqlc.types.Field(Projects, graphql_name='getProjects', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('warehouse_type', sgqlc.types.Arg(String, graphql_name='warehouseType', default=None)),
))
    )
    get_datasets = sgqlc.types.Field(DatasetConnection, graphql_name='getDatasets', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('include_table_count', sgqlc.types.Arg(Boolean, graphql_name='includeTableCount', default=False)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('dataset', sgqlc.types.Arg(String, graphql_name='dataset', default=None)),
))
    )
    get_field_bi_lineage = sgqlc.types.Field(sgqlc.types.list_of(FieldDownstreamBi), graphql_name='getFieldBiLineage', args=sgqlc.types.ArgDict((
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('field_name', sgqlc.types.Arg(String, graphql_name='fieldName', default=None)),
        ('last_seen_range_start', sgqlc.types.Arg(DateTime, graphql_name='lastSeenRangeStart', default=None)),
))
    )
    get_event_muting_rules = sgqlc.types.Field(sgqlc.types.list_of(EventMutingRule), graphql_name='getEventMutingRules', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
))
    )
    get_users_in_account = sgqlc.types.Field('UserConnection', graphql_name='getUsersInAccount', args=sgqlc.types.ArgDict((
        ('roles', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='roles', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('email', sgqlc.types.Arg(String, graphql_name='email', default=None)),
        ('first_name', sgqlc.types.Arg(String, graphql_name='firstName', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='lastName', default=None)),
        ('role', sgqlc.types.Arg(String, graphql_name='role', default=None)),
))
    )
    get_invites_in_account = sgqlc.types.Field('UserInviteConnection', graphql_name='getInvitesInAccount', args=sgqlc.types.ArgDict((
        ('roles', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='roles', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('state', sgqlc.types.Arg(String, graphql_name='state', default=None)),
))
    )
    get_token_metadata = sgqlc.types.Field(sgqlc.types.list_of('TokenMetadata'), graphql_name='getTokenMetadata', args=sgqlc.types.ArgDict((
        ('index', sgqlc.types.Arg(sgqlc.types.non_null(AccessKeyIndexEnum), graphql_name='index', default=None)),
))
    )
    get_integration_keys = sgqlc.types.Field(sgqlc.types.list_of(IntegrationKeyMetadata), graphql_name='getIntegrationKeys')
    test_existing_connection = sgqlc.types.Field('TestConnectionResponse', graphql_name='testExistingConnection', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
))
    )
    test_telnet_connection = sgqlc.types.Field('TestConnectionResponse', graphql_name='testTelnetConnection', args=sgqlc.types.ArgDict((
        ('host', sgqlc.types.Arg(String, graphql_name='host', default=None)),
        ('port', sgqlc.types.Arg(Int, graphql_name='port', default=None)),
        ('timeout', sgqlc.types.Arg(Int, graphql_name='timeout', default=None)),
        ('dc_id', sgqlc.types.Arg(UUID, graphql_name='dcId', default=None)),
))
    )
    test_tcp_open_connection = sgqlc.types.Field('TestConnectionResponse', graphql_name='testTcpOpenConnection', args=sgqlc.types.ArgDict((
        ('host', sgqlc.types.Arg(String, graphql_name='host', default=None)),
        ('port', sgqlc.types.Arg(Int, graphql_name='port', default=None)),
        ('timeout', sgqlc.types.Arg(Int, graphql_name='timeout', default=None)),
        ('dc_id', sgqlc.types.Arg(UUID, graphql_name='dcId', default=None)),
))
    )
    test_notification_integration = sgqlc.types.Field(Boolean, graphql_name='testNotificationIntegration', args=sgqlc.types.ArgDict((
        ('setting_id', sgqlc.types.Arg(UUID, graphql_name='settingId', default=None)),
))
    )
    get_databricks_cluster_info = sgqlc.types.Field(DatabricksClusterResponse, graphql_name='getDatabricksClusterInfo', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
))
    )
    get_databricks_notebook_link = sgqlc.types.Field(DatabricksNotebookLink, graphql_name='getDatabricksNotebookLink')
    validate_connection_type = sgqlc.types.Field(Boolean, graphql_name='validateConnectionType', args=sgqlc.types.ArgDict((
        ('warehouse_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='warehouseType', default=None)),
        ('connection_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='connectionType', default=None)),
))
    )
    get_event_onboarding_data = sgqlc.types.Field(EventOnbardingConfig, graphql_name='getEventOnboardingData')


class QueryAfterKey(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('user', 'date', 'query_hash')
    user = sgqlc.types.Field(String, graphql_name='user')
    date = sgqlc.types.Field(String, graphql_name='date')
    query_hash = sgqlc.types.Field(String, graphql_name='queryHash')


class QueryBlastRadius(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('date', 'username', 'query_hash', 'query_count', 'tables')
    date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='date')
    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')
    query_hash = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='queryHash')
    query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='queryCount')
    tables = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='tables')


class QueryBlastRadius2(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('username', 'last_accessed_date', 'distinct_query_count', 'query_count', 'queries')
    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')
    last_accessed_date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastAccessedDate')
    distinct_query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='distinctQueryCount')
    query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='queryCount')
    queries = sgqlc.types.Field(sgqlc.types.list_of('QueryBlastRadiusData'), graphql_name='queries')


class QueryBlastRadiusData(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('date', 'query_hash', 'query_count', 'tables')
    date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='date')
    query_hash = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='queryHash')
    query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='queryCount')
    tables = sgqlc.types.Field(sgqlc.types.list_of('TableInfo'), graphql_name='tables')


class QueryBlastRadiusSummary(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('username', 'last_accessed_date', 'distinct_query_count', 'query_count')
    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')
    last_accessed_date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastAccessedDate')
    distinct_query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='distinctQueryCount')
    query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='queryCount')


class QueryDataObject(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('query_id', 'user_name', 'timestamp', 'query', 'source_display_name', 'destination_display_name')
    query_id = sgqlc.types.Field(String, graphql_name='queryId')
    user_name = sgqlc.types.Field(String, graphql_name='userName')
    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')
    query = sgqlc.types.Field(String, graphql_name='query')
    source_display_name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='sourceDisplayName')
    destination_display_name = sgqlc.types.Field(String, graphql_name='destinationDisplayName')


class QueryListObject(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('query_id', 'user_name', 'timestamp', 'query_length', 'query_hash', 'sub_category')
    query_id = sgqlc.types.Field(String, graphql_name='queryId')
    user_name = sgqlc.types.Field(String, graphql_name='userName')
    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')
    query_length = sgqlc.types.Field(Int, graphql_name='queryLength')
    query_hash = sgqlc.types.Field(String, graphql_name='queryHash')
    sub_category = sgqlc.types.Field(String, graphql_name='subCategory')


class QueryListResponse(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('queries', 'queries_by_type', 'offset')
    queries = sgqlc.types.Field(sgqlc.types.list_of(QueryListObject), graphql_name='queries')
    queries_by_type = sgqlc.types.Field(sgqlc.types.list_of('QueryMapObject'), graphql_name='queriesByType')
    offset = sgqlc.types.Field(Int, graphql_name='offset')


class QueryLogHash(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('query_hash', 'user_email', 'day', 'count', 'category')
    query_hash = sgqlc.types.Field(String, graphql_name='queryHash')
    user_email = sgqlc.types.Field(String, graphql_name='userEmail')
    day = sgqlc.types.Field(DateTime, graphql_name='day')
    count = sgqlc.types.Field(Int, graphql_name='count')
    category = sgqlc.types.Field(String, graphql_name='category')


class QueryLogHashes(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('full_table_id', 'offset', 'query_hashes')
    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')
    offset = sgqlc.types.Field(Int, graphql_name='offset')
    query_hashes = sgqlc.types.Field(sgqlc.types.list_of(QueryLogHash), graphql_name='queryHashes')


class QueryLogMetadata(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('metadata', 'timestamp')
    metadata = sgqlc.types.Field(String, graphql_name='metadata')
    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')


class QueryLogResponse(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('query_data', 'queries', 'offset')
    query_data = sgqlc.types.Field(QueryDataObject, graphql_name='queryData')
    queries = sgqlc.types.Field(sgqlc.types.list_of(QueryLogMetadata), graphql_name='queries')
    offset = sgqlc.types.Field(Int, graphql_name='offset')


class QueryMapObject(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('queries', 'query_length')
    queries = sgqlc.types.Field(sgqlc.types.list_of(QueryListObject), graphql_name='queries')
    query_length = sgqlc.types.Field(Int, graphql_name='queryLength')


class QueryRef(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('dynamic_fields', 'fields', 'filters', 'model', 'query_timezone', 'url', 'view')
    dynamic_fields = sgqlc.types.Field(String, graphql_name='dynamicFields')
    fields = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='fields')
    filters = sgqlc.types.Field(String, graphql_name='filters')
    model = sgqlc.types.Field(String, graphql_name='model')
    query_timezone = sgqlc.types.Field(String, graphql_name='queryTimezone')
    url = sgqlc.types.Field(String, graphql_name='url')
    view = sgqlc.types.Field(String, graphql_name='view')


class RcaJob(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id', 'uuid', 'job_type', 'event', 'set_ts', 'status', 'execution_stats')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    job_type = sgqlc.types.Field(sgqlc.types.non_null(RcaJobsModelJobType), graphql_name='jobType')
    event = sgqlc.types.Field(sgqlc.types.non_null('Event'), graphql_name='event')
    set_ts = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='setTs')
    status = sgqlc.types.Field(RcaJobsModelStatus, graphql_name='status')
    execution_stats = sgqlc.types.Field(JSONString, graphql_name='executionStats')


class RcaPlotData(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('label', 'timestamp', 'value')
    label = sgqlc.types.Field(String, graphql_name='label')
    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')
    value = sgqlc.types.Field(Int, graphql_name='value')


class RcaResult(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('status', 'job_type', 'rca_data', 'rca_data_v2')
    status = sgqlc.types.Field(RcaStatus, graphql_name='status')
    job_type = sgqlc.types.Field(RcaJobType, graphql_name='jobType')
    rca_data = sgqlc.types.Field(FieldDistRcaResult, graphql_name='rcaData')
    rca_data_v2 = sgqlc.types.Field('RcaData', graphql_name='rcaDataV2')


class ReInviteUsers(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('invites', 'existing_users')
    invites = sgqlc.types.Field(sgqlc.types.list_of('UserInvite'), graphql_name='invites')
    existing_users = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='existingUsers')


class ReadWriteStatsData(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('table_read_percentile', 'table_write_percentile')
    table_read_percentile = sgqlc.types.Field(Float, graphql_name='tableReadPercentile')
    table_write_percentile = sgqlc.types.Field(Float, graphql_name='tableWritePercentile')


class RecentTimestamp(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('field_name', 'timestamp', 'is_time_axis')
    field_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fieldName')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='timestamp')
    is_time_axis = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTimeAxis')


class RelatedUserCount(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('user', 'count')
    user = sgqlc.types.Field(String, graphql_name='user')
    count = sgqlc.types.Field(Int, graphql_name='count')


class RemoveConnectionMutation(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class RemoveUserFromAccount(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('user',)
    user = sgqlc.types.Field('User', graphql_name='user')


class Report(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name', 'description')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')


class ResourceConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ResourceEdge')), graphql_name='edges')


class ResourceEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('Resource', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class ResourceModification(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('type', 'description', 'resource_as_json')
    type = sgqlc.types.Field(String, graphql_name='type')
    description = sgqlc.types.Field(String, graphql_name='description')
    resource_as_json = sgqlc.types.Field(String, graphql_name='resourceAsJson')


class ResponseURL(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('url', 'created_at')
    url = sgqlc.types.Field(String, graphql_name='url')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')


class RoleOutput(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name', 'version', 'is_managed', 'label', 'description')
    name = sgqlc.types.Field(String, graphql_name='name')
    version = sgqlc.types.Field(String, graphql_name='version')
    is_managed = sgqlc.types.Field(Boolean, graphql_name='isManaged')
    label = sgqlc.types.Field(String, graphql_name='label')
    description = sgqlc.types.Field(String, graphql_name='description')


class RunSqlRule(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('job_execution_uuids',)
    job_execution_uuids = sgqlc.types.Field(sgqlc.types.list_of(UUID), graphql_name='jobExecutionUuids')


class SQLQueryResult(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('columns', 'rows')
    columns = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='columns')
    rows = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of(String)), graphql_name='rows')


class SQLResponse(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('columns', 'rows', 'query', 'has_error', 'error', 'sampling_disabled')
    columns = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='columns')
    rows = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of(String)), graphql_name='rows')
    query = sgqlc.types.Field(String, graphql_name='query')
    has_error = sgqlc.types.Field(Boolean, graphql_name='hasError')
    error = sgqlc.types.Field(String, graphql_name='error')
    sampling_disabled = sgqlc.types.Field(Boolean, graphql_name='samplingDisabled')


class SamlIdentityProvider(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('federation_type', 'domains', 'default_authorization_groups', 'metadata_url', 'metadata')
    federation_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='federationType')
    domains = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='domains')
    default_authorization_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='defaultAuthorizationGroups')
    metadata_url = sgqlc.types.Field(String, graphql_name='metadataUrl')
    metadata = sgqlc.types.Field(String, graphql_name='metadata')


class SaveEventOnboardingData(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class SaveSlackCredentialsMutation(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('slack_credentials',)
    slack_credentials = sgqlc.types.Field('SlackCredentialsV2', graphql_name='slackCredentials')


class SaveTableImportanceStats(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('stats',)
    stats = sgqlc.types.Field('TableImportanceStatsResponse', graphql_name='stats')


class ScheduleConfigOutput(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('schedule_type', 'interval_minutes', 'interval_crontab', 'start_time', 'min_interval_minutes')
    schedule_type = sgqlc.types.Field(sgqlc.types.non_null(ScheduleType), graphql_name='scheduleType')
    interval_minutes = sgqlc.types.Field(Int, graphql_name='intervalMinutes')
    interval_crontab = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='intervalCrontab')
    start_time = sgqlc.types.Field(DateTime, graphql_name='startTime')
    min_interval_minutes = sgqlc.types.Field(Int, graphql_name='minIntervalMinutes')


class SearchResponse(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('total_hits', 'offset', 'results', 'facet_results')
    total_hits = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalHits')
    offset = sgqlc.types.Field(Int, graphql_name='offset')
    results = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('SearchResult')), graphql_name='results')
    facet_results = sgqlc.types.Field(sgqlc.types.list_of(FacetResults), graphql_name='facetResults')


class SearchResult(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('mcon', 'lineage_node_id', 'object_type', 'object_id', 'display_name', 'parent_mcon', 'path', 'project_id', 'dataset', 'table_id', 'properties', 'resource_id', 'warehouse_display_name', 'description', 'field_type', 'highlight', 'highlight_properties', 'field_names', 'is_important', 'upstream_resource_ids')
    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')
    lineage_node_id = sgqlc.types.Field(String, graphql_name='lineageNodeId')
    object_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='objectType')
    object_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='objectId')
    display_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='displayName')
    parent_mcon = sgqlc.types.Field(String, graphql_name='parentMcon')
    path = sgqlc.types.Field(String, graphql_name='path')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    dataset = sgqlc.types.Field(String, graphql_name='dataset')
    table_id = sgqlc.types.Field(String, graphql_name='tableId')
    properties = sgqlc.types.Field(sgqlc.types.list_of('SearchResultProperty'), graphql_name='properties')
    resource_id = sgqlc.types.Field(String, graphql_name='resourceId')
    warehouse_display_name = sgqlc.types.Field(String, graphql_name='warehouseDisplayName')
    description = sgqlc.types.Field(String, graphql_name='description')
    field_type = sgqlc.types.Field(String, graphql_name='fieldType')
    highlight = sgqlc.types.Field(sgqlc.types.list_of(HighlightSnippets), graphql_name='highlight')
    highlight_properties = sgqlc.types.Field(sgqlc.types.list_of(NestedHighlightSnippets), graphql_name='highlightProperties')
    field_names = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='fieldNames')
    is_important = sgqlc.types.Field(Boolean, graphql_name='isImportant')
    upstream_resource_ids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='upstreamResourceIds')


class SearchResultProperty(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(String, graphql_name='value')


class SensitivityThreshold(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('min_delay', 'level')
    min_delay = sgqlc.types.Field(Int, graphql_name='minDelay')
    level = sgqlc.types.Field(SensitivityLevels, graphql_name='level')


class SetAccountName(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('account',)
    account = sgqlc.types.Field(Account, graphql_name='account')


class SetDefaultIncidentGroupInterval(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('warehouse_config',)
    warehouse_config = sgqlc.types.Field(JSONString, graphql_name='warehouseConfig')


class SetGeneratesIncidents(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('dbt_project',)
    dbt_project = sgqlc.types.Field('DbtProject', graphql_name='dbtProject')


class SetIncidentFeedbackPayload(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('incident', 'client_mutation_id')
    incident = sgqlc.types.Field('Incident', graphql_name='incident')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class SetIncidentOwner(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('incident',)
    incident = sgqlc.types.Field('Incident', graphql_name='incident')


class SetIncidentReaction(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('incident',)
    incident = sgqlc.types.Field('Incident', graphql_name='incident')


class SetIncidentSeverity(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('incident',)
    incident = sgqlc.types.Field('Incident', graphql_name='incident')


class SetSensitivity(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class SetWarehouseName(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('warehouse',)
    warehouse = sgqlc.types.Field('Warehouse', graphql_name='warehouse')


class SheetDashboardRef(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name', 'path', 'created_at', 'updated_at', 'id', 'dashboard_id', 'dashboard_title')
    name = sgqlc.types.Field(String, graphql_name='name')
    path = sgqlc.types.Field(String, graphql_name='path')
    created_at = sgqlc.types.Field(String, graphql_name='createdAt')
    updated_at = sgqlc.types.Field(String, graphql_name='updatedAt')
    id = sgqlc.types.Field(String, graphql_name='id')
    dashboard_id = sgqlc.types.Field(String, graphql_name='dashboardId')
    dashboard_title = sgqlc.types.Field(String, graphql_name='dashboardTitle')


class SiteRef(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name', 'uri')
    name = sgqlc.types.Field(String, graphql_name='name')
    uri = sgqlc.types.Field(String, graphql_name='uri')


class Size(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('metric', 'ucs_upper', 'ucs_lower', 'ucs_min_size_change', 'ucs_reason', 'ucs_status', 'sd_upper', 'sd_lower', 'sd_reason', 'sd_status', 'last_size_change')
    metric = sgqlc.types.Field(String, graphql_name='metric')
    ucs_upper = sgqlc.types.Field(Float, graphql_name='ucsUpper')
    ucs_lower = sgqlc.types.Field(Float, graphql_name='ucsLower')
    ucs_min_size_change = sgqlc.types.Field(Float, graphql_name='ucsMinSizeChange')
    ucs_reason = sgqlc.types.Field(String, graphql_name='ucsReason')
    ucs_status = sgqlc.types.Field(DetectorStatus, graphql_name='ucsStatus')
    sd_upper = sgqlc.types.Field(Float, graphql_name='sdUpper')
    sd_lower = sgqlc.types.Field(Float, graphql_name='sdLower')
    sd_reason = sgqlc.types.Field(String, graphql_name='sdReason')
    sd_status = sgqlc.types.Field(DetectorStatus, graphql_name='sdStatus')
    last_size_change = sgqlc.types.Field(LastSizeChange, graphql_name='lastSizeChange')


class SlackChannel(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name', 'id', 'topic', 'purpose')
    name = sgqlc.types.Field(String, graphql_name='name')
    id = sgqlc.types.Field(String, graphql_name='id')
    topic = sgqlc.types.Field(String, graphql_name='topic')
    purpose = sgqlc.types.Field(String, graphql_name='purpose')


class SlackChannelResponse(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('channels',)
    channels = sgqlc.types.Field(sgqlc.types.list_of(SlackChannel), graphql_name='channels')


class SlackCredentials(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id', 'account', 'credentials_s3_key')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')
    credentials_s3_key = sgqlc.types.Field(String, graphql_name='credentialsS3Key')


class SlackCredentialsV2(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id', 'account', 'installed_by', 'slack_app_type')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')
    installed_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='installedBy')
    slack_app_type = sgqlc.types.Field(sgqlc.types.non_null(SlackCredentialsV2ModelSlackAppType), graphql_name='slackAppType')


class SlackEngagementConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('SlackEngagementEdge')), graphql_name='edges')


class SlackEngagementEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('SlackEngagement', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class SlackMessageDetailsConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('SlackMessageDetailsEdge')), graphql_name='edges')


class SlackMessageDetailsEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('SlackMessageDetails', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class SlackOauthUrlResponse(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('url',)
    url = sgqlc.types.Field(String, graphql_name='url')


class SnoozeCustomRule(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')


class SourceColumn(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('column_name', 'column_type')
    column_name = sgqlc.types.Field(String, graphql_name='columnName')
    column_type = sgqlc.types.Field(String, graphql_name='columnType')


class SqlExpression(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('expression',)
    expression = sgqlc.types.Field(String, graphql_name='expression')


class StartDatabricksCluster(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class StopMonitor(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class TableAnomalyConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('TableAnomalyEdge')), graphql_name='edges')


class TableAnomalyEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('TableAnomaly', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class TableCapabilitiesResponse(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('has_freshness', 'has_rows_and_bytes', 'has_bytes', 'has_rows', 'has_volume_sli', 'has_write_throughput', 'has_query_logs', 'has_lineage', 'has_field_lineage', 'has_objects_deleted', 'has_total_row_count_change')
    has_freshness = sgqlc.types.Field(Boolean, graphql_name='hasFreshness')
    has_rows_and_bytes = sgqlc.types.Field(Boolean, graphql_name='hasRowsAndBytes')
    has_bytes = sgqlc.types.Field(Boolean, graphql_name='hasBytes')
    has_rows = sgqlc.types.Field(Boolean, graphql_name='hasRows')
    has_volume_sli = sgqlc.types.Field(Boolean, graphql_name='hasVolumeSli')
    has_write_throughput = sgqlc.types.Field(Boolean, graphql_name='hasWriteThroughput')
    has_query_logs = sgqlc.types.Field(Boolean, graphql_name='hasQueryLogs')
    has_lineage = sgqlc.types.Field(Boolean, graphql_name='hasLineage')
    has_field_lineage = sgqlc.types.Field(Boolean, graphql_name='hasFieldLineage')
    has_objects_deleted = sgqlc.types.Field(Boolean, graphql_name='hasObjectsDeleted')
    has_total_row_count_change = sgqlc.types.Field(Boolean, graphql_name='hasTotalRowCountChange')


class TableColumnsLineageResult(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('mcon', 'columns_lineage', 'non_selected_source_columns', 'timestamp', 'display_name')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    columns_lineage = sgqlc.types.Field(sgqlc.types.list_of(ColumnLineage), graphql_name='columnsLineage')
    non_selected_source_columns = sgqlc.types.Field(sgqlc.types.list_of(LineageSources), graphql_name='nonSelectedSourceColumns')
    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')


class TableFieldConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('TableFieldEdge')), graphql_name='edges')


class TableFieldEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('TableField', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class TableFieldImportance(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('field_name', 'is_important', 'field_type_db', 'field_type')
    field_name = sgqlc.types.Field(String, graphql_name='fieldName')
    is_important = sgqlc.types.Field(Boolean, graphql_name='isImportant')
    field_type_db = sgqlc.types.Field(String, graphql_name='fieldTypeDb')
    field_type = sgqlc.types.Field(FieldType, graphql_name='fieldType')


class TableFieldToBiConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('TableFieldToBiEdge')), graphql_name='edges')


class TableFieldToBiEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('TableFieldToBi', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class TableFieldsImportance(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('table_fields',)
    table_fields = sgqlc.types.Field(sgqlc.types.list_of(TableFieldImportance), graphql_name='tableFields')


class TableImportanceStatsResponse(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('is_important', 'importance_score')
    is_important = sgqlc.types.Field(Boolean, graphql_name='isImportant')
    importance_score = sgqlc.types.Field(Float, graphql_name='importanceScore')


class TableInfo(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('full_table_id', 'mcon')
    full_table_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullTableId')
    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')


class TableMetadata(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('table_path', 'is_wildcard', 'view_query', 'external_data_sources', 'created_on')
    table_path = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tablePath')
    is_wildcard = sgqlc.types.Field(Boolean, graphql_name='isWildcard')
    view_query = sgqlc.types.Field(String, graphql_name='viewQuery')
    external_data_sources = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='externalDataSources')
    created_on = sgqlc.types.Field(String, graphql_name='createdOn')


class TableMetricExistence(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('metric_name', 'exist')
    metric_name = sgqlc.types.Field(String, graphql_name='metricName')
    exist = sgqlc.types.Field(Boolean, graphql_name='exist')


class TableMetricV2(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('full_table_id', 'metric', 'value', 'field', 'timestamp', 'measurement_timestamp', 'dimensions', 'thresholds')
    full_table_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullTableId')
    metric = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='metric')
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')
    field = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='field')
    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')
    measurement_timestamp = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='measurementTimestamp')
    dimensions = sgqlc.types.Field(MetricDimensions, graphql_name='dimensions')
    thresholds = sgqlc.types.Field(sgqlc.types.list_of('Threshold'), graphql_name='thresholds')


class TableObjectsDeleted(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('value', 'measurement_timestamp')
    value = sgqlc.types.Field(Float, graphql_name='value')
    measurement_timestamp = sgqlc.types.Field(DateTime, graphql_name='measurementTimestamp')


class TableRef(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('full_table_id', 'table_path')
    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')
    table_path = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tablePath')


class TableResources(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('table', 'view', 'external')
    table = sgqlc.types.Field(Int, graphql_name='table')
    view = sgqlc.types.Field(Int, graphql_name='view')
    external = sgqlc.types.Field(Int, graphql_name='external')


class TableSchemaVersionConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('TableSchemaVersionEdge')), graphql_name='edges')


class TableSchemaVersionEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('TableSchemaVersion', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class TableStatsConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('TableStatsEdge')), graphql_name='edges')


class TableStatsEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('TableStats', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class TableTagConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('TableTagEdge')), graphql_name='edges')


class TableTagEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('TableTag', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class TableTotalByteCount(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('value', 'measurement_timestamp', 'thresholds')
    value = sgqlc.types.Field(Float, graphql_name='value')
    measurement_timestamp = sgqlc.types.Field(DateTime, graphql_name='measurementTimestamp')
    thresholds = sgqlc.types.Field(sgqlc.types.list_of('Threshold'), graphql_name='thresholds')


class TableTotalRowCount(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('value', 'measurement_timestamp', 'thresholds')
    value = sgqlc.types.Field(Float, graphql_name='value')
    measurement_timestamp = sgqlc.types.Field(DateTime, graphql_name='measurementTimestamp')
    thresholds = sgqlc.types.Field(sgqlc.types.list_of('Threshold'), graphql_name='thresholds')


class TableUpdateTime(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('value', 'measurement_timestamp')
    value = sgqlc.types.Field(DateTime, graphql_name='value')
    measurement_timestamp = sgqlc.types.Field(DateTime, graphql_name='measurementTimestamp')


class TableUsageStatsData(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('freshness_cycle', 'read_write_stats')
    freshness_cycle = sgqlc.types.Field(FreshnessCycleData, graphql_name='freshnessCycle')
    read_write_stats = sgqlc.types.Field(ReadWriteStatsData, graphql_name='readWriteStats')


class TableWriteThroughputInBytes(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('value', 'measurement_timestamp')
    value = sgqlc.types.Field(Float, graphql_name='value')
    measurement_timestamp = sgqlc.types.Field(DateTime, graphql_name='measurementTimestamp')


class TableauAccount(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id', 'uuid', 'server_name', 'username', 'token_name', 'site_name', 'verify_ssl', 'account', 'created_on', 'data_collector')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    server_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='serverName')
    username = sgqlc.types.Field(String, graphql_name='username')
    token_name = sgqlc.types.Field(String, graphql_name='tokenName')
    site_name = sgqlc.types.Field(String, graphql_name='siteName')
    verify_ssl = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='verifySsl')
    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')
    created_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdOn')
    data_collector = sgqlc.types.Field(DataCollector, graphql_name='dataCollector')


class TagKeyValuePairOutput(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(String, graphql_name='name')
    value = sgqlc.types.Field(String, graphql_name='value')


class TestAthenaCredentials(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'success', 'validations', 'warnings')
    key = sgqlc.types.Field(String, graphql_name='key')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    validations = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='validations')
    warnings = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='warnings')


class TestBqCredentials(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'success', 'validations', 'warnings')
    key = sgqlc.types.Field(String, graphql_name='key')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    validations = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='validations')
    warnings = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='warnings')


class TestConnectionResponse(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success', 'validations', 'warnings')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    validations = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='validations')
    warnings = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='warnings')


class TestCredentialsMutation(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success', 'validations', 'warnings')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    validations = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='validations')
    warnings = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='warnings')


class TestDatabaseCredentials(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'success', 'validations', 'warnings')
    key = sgqlc.types.Field(String, graphql_name='key')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    validations = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='validations')
    warnings = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='warnings')


class TestDatabricksCredentials(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class TestDbtCloudCredentials(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class TestGlueCredentials(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'success', 'validations', 'warnings')
    key = sgqlc.types.Field(String, graphql_name='key')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    validations = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='validations')
    warnings = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='warnings')


class TestHiveCredentials(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class TestLookerCredentials(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class TestLookerGitCloneCredentials(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class TestLookerGitCredentials(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class TestLookerGitSshCredentials(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class TestPowerBICredentials(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class TestPrestoCredentials(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class TestS3Credentials(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class TestSelfHostedCredentials(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'success', 'validations', 'warnings')
    key = sgqlc.types.Field(String, graphql_name='key')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    validations = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='validations')
    warnings = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='warnings')


class TestSnowflakeCredentials(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'success', 'validations', 'warnings')
    key = sgqlc.types.Field(String, graphql_name='key')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    validations = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='validations')
    warnings = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='warnings')


class TestSparkCredentials(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class TestTableauCredentialsMutation(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key', 'success', 'validations', 'warnings')
    key = sgqlc.types.Field(String, graphql_name='key')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    validations = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='validations')
    warnings = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='warnings')


class Threshold(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('type', 'upper', 'lower', 'reason', 'status')
    type = sgqlc.types.Field(sgqlc.types.non_null(ThresholdType), graphql_name='type')
    upper = sgqlc.types.Field(Float, graphql_name='upper')
    lower = sgqlc.types.Field(Float, graphql_name='lower')
    reason = sgqlc.types.Field(String, graphql_name='reason')
    status = sgqlc.types.Field(sgqlc.types.non_null(ThresholdStatus), graphql_name='status')


class ThresholdModifier(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('modifier_type', 'value')
    modifier_type = sgqlc.types.Field(sgqlc.types.non_null(ThresholdModifierType), graphql_name='modifierType')
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')


class ThresholdsData(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('freshness', 'size', 'field_health', 'dimension_tracking', 'dynamic')
    freshness = sgqlc.types.Field(Freshness, graphql_name='freshness')
    size = sgqlc.types.Field(Size, graphql_name='size')
    field_health = sgqlc.types.Field(FieldHealth, graphql_name='fieldHealth', args=sgqlc.types.ArgDict((
        ('monitor', sgqlc.types.Arg(String, graphql_name='monitor', default=None)),
        ('field', sgqlc.types.Arg(String, graphql_name='field', default=None)),
        ('metric', sgqlc.types.Arg(String, graphql_name='metric', default=None)),
))
    )
    dimension_tracking = sgqlc.types.Field(sgqlc.types.list_of(DimensionTracking), graphql_name='dimensionTracking', args=sgqlc.types.ArgDict((
        ('monitor', sgqlc.types.Arg(String, graphql_name='monitor', default=None)),
))
    )
    dynamic = sgqlc.types.Field(Dynamic, graphql_name='dynamic', args=sgqlc.types.ArgDict((
        ('rule', sgqlc.types.Arg(String, graphql_name='rule', default=None)),
))
    )


class TimeAxis(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('name', 'type')
    name = sgqlc.types.Field(String, graphql_name='name')
    type = sgqlc.types.Field(String, graphql_name='type')


class ToggleDisableSampling(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('disabled',)
    disabled = sgqlc.types.Field(Boolean, graphql_name='disabled')


class ToggleDisableValueIngestion(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('disabled',)
    disabled = sgqlc.types.Field(Boolean, graphql_name='disabled')


class ToggleEventConfig(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class ToggleFullDistributionMetrics(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('enabled',)
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')


class ToggleMuteDatasetPayload(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('muted', 'client_mutation_id')
    muted = sgqlc.types.Field('Dataset', graphql_name='muted')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class ToggleMuteDatasetsPayload(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('muted', 'client_mutation_id')
    muted = sgqlc.types.Field(sgqlc.types.list_of('Dataset'), graphql_name='muted')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class ToggleMuteTablePayload(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('muted', 'client_mutation_id')
    muted = sgqlc.types.Field('WarehouseTable', graphql_name='muted')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class ToggleMuteTablesPayload(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('muted', 'client_mutation_id')
    muted = sgqlc.types.Field(sgqlc.types.list_of('WarehouseTable'), graphql_name='muted')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class ToggleMuteWithRegexPayload(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('muted', 'client_mutation_id')
    muted = sgqlc.types.Field('Dataset', graphql_name='muted')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class TokenMetadata(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id', 'first_name', 'last_name', 'email', 'creation_time', 'expiration_time', 'comment')
    id = sgqlc.types.Field(String, graphql_name='id')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    email = sgqlc.types.Field(String, graphql_name='email')
    creation_time = sgqlc.types.Field(DateTime, graphql_name='creationTime')
    expiration_time = sgqlc.types.Field(DateTime, graphql_name='expirationTime')
    comment = sgqlc.types.Field(String, graphql_name='comment')


class TrackTablePayload(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('table', 'client_mutation_id')
    table = sgqlc.types.Field('WarehouseTable', graphql_name='table')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class TriggerCircuitBreakerRule(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('job_execution_uuid',)
    job_execution_uuid = sgqlc.types.Field(UUID, graphql_name='jobExecutionUuid')


class TriggerCustomRule(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')


class TriggerMonitor(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('monitor',)
    monitor = sgqlc.types.Field('MetricMonitoring', graphql_name='monitor')


class UnifiedUserAssignmentConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('UnifiedUserAssignmentEdge')), graphql_name='edges')


class UnifiedUserAssignmentEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('UnifiedUserAssignment', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class UnifiedUserConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('UnifiedUserEdge')), graphql_name='edges')


class UnifiedUserEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('UnifiedUser', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class UnsnoozeCustomRule(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')


class UpdateCredentials(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class UpdateCustomMetricRuleNotes(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')


class UpdateDatabricksNotebook(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class UpdateDatabricksNotebookJob(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class UpdateMonitorLabels(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class UpdateMonitorName(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class UpdateMonitorNotes(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class UpdateSlackChannelsMutation(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class UpdateUserAuthorizationGroupMembership(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('added_to_groups', 'removed_from_groups')
    added_to_groups = sgqlc.types.Field(sgqlc.types.list_of(AuthorizationGroupOutput), graphql_name='addedToGroups')
    removed_from_groups = sgqlc.types.Field(sgqlc.types.list_of(AuthorizationGroupOutput), graphql_name='removedFromGroups')


class UpdateUserStatePayload(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('user', 'client_mutation_id')
    user = sgqlc.types.Field('User', graphql_name='user')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UploadDbtManifest(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('ok',)
    ok = sgqlc.types.Field(Boolean, graphql_name='ok')


class UploadDbtRunResults(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('ok',)
    ok = sgqlc.types.Field(Boolean, graphql_name='ok')


class UploadWarehouseCredentialsMutation(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('key',)
    key = sgqlc.types.Field(String, graphql_name='key')


class UserAfterKey(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('user', 'source')
    user = sgqlc.types.Field(String, graphql_name='user')
    source = sgqlc.types.Field(String, graphql_name='source')


class UserAfterKey2(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('user',)
    user = sgqlc.types.Field(String, graphql_name='user')


class UserAuthorizationOutput(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('groups', 'domain_restrictions', 'permissions')
    groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='groups')
    domain_restrictions = sgqlc.types.Field(sgqlc.types.list_of('DomainRestriction'), graphql_name='domainRestrictions')
    permissions = sgqlc.types.Field(sgqlc.types.list_of('UserPermission'), graphql_name='permissions')


class UserBlastRadius(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('username', 'query_count', 'table')
    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')
    query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='queryCount')
    table = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='table')


class UserBlastRadius2(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('username', 'query_count', 'tables')
    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')
    query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='queryCount')
    tables = sgqlc.types.Field(sgqlc.types.list_of('UserTableBlastRadius'), graphql_name='tables')


class UserConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('UserEdge')), graphql_name='edges')


class UserDefinedMonitorConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('UserDefinedMonitorEdge')), graphql_name='edges')


class UserDefinedMonitorConnectionV2Connection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('UserDefinedMonitorConnectionV2Edge')), graphql_name='edges')


class UserDefinedMonitorConnectionV2Edge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('UserDefinedMonitorV2', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class UserDefinedMonitorEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('UserDefinedMonitor', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class UserEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('User', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class UserInviteConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('UserInviteEdge')), graphql_name='edges')


class UserInviteEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('UserInvite', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class UserPermission(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('permission', 'effect', 'domain_restriction_ids')
    permission = sgqlc.types.Field(Permission, graphql_name='permission')
    effect = sgqlc.types.Field(PermissionEffect, graphql_name='effect')
    domain_restriction_ids = sgqlc.types.Field(sgqlc.types.list_of(UUID), graphql_name='domainRestrictionIds')


class UserTableBlastRadius(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('full_table_id', 'query_count', 'mcon')
    full_table_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullTableId')
    query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='queryCount')
    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')


class ValidateCron(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success', 'error')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    error = sgqlc.types.Field(String, graphql_name='error')


class Warehouse(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('id', 'uuid', 'name', 'connection_type', 'credentials_s3_key', 'bq_project_id', 'account', 'data_collector', 'created_on', 'config', 'connections', 'tables', 'incidents', 'events', 'datasets', 'mute_rule', 'data_sampling_enabled', 'value_ingestion_enabled', 'value_based_threshold_enabled', 'custom_sql_sampling_supported', 'custom_sql_sampling_enabled')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    name = sgqlc.types.Field(String, graphql_name='name')
    connection_type = sgqlc.types.Field(sgqlc.types.non_null(WarehouseModelConnectionType), graphql_name='connectionType')
    credentials_s3_key = sgqlc.types.Field(String, graphql_name='credentialsS3Key')
    bq_project_id = sgqlc.types.Field(String, graphql_name='bqProjectId')
    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')
    data_collector = sgqlc.types.Field(DataCollector, graphql_name='dataCollector')
    created_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdOn')
    config = sgqlc.types.Field(JSONString, graphql_name='config')
    connections = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Connection))), graphql_name='connections')
    tables = sgqlc.types.Field(sgqlc.types.non_null('WarehouseTableConnection'), graphql_name='tables', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
))
    )
    incidents = sgqlc.types.Field(sgqlc.types.non_null(IncidentConnection), graphql_name='incidents', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    events = sgqlc.types.Field(sgqlc.types.non_null(EventConnection), graphql_name='events', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    datasets = sgqlc.types.Field(sgqlc.types.non_null(DatasetConnection), graphql_name='datasets', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('dataset', sgqlc.types.Arg(String, graphql_name='dataset', default=None)),
))
    )
    mute_rule = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EventMutingRule))), graphql_name='muteRule')
    data_sampling_enabled = sgqlc.types.Field(Boolean, graphql_name='dataSamplingEnabled')
    value_ingestion_enabled = sgqlc.types.Field(Boolean, graphql_name='valueIngestionEnabled')
    value_based_threshold_enabled = sgqlc.types.Field(Boolean, graphql_name='valueBasedThresholdEnabled')
    custom_sql_sampling_supported = sgqlc.types.Field(Boolean, graphql_name='customSqlSamplingSupported')
    custom_sql_sampling_enabled = sgqlc.types.Field(Boolean, graphql_name='customSqlSamplingEnabled')


class WarehouseTableConnection(sgqlc.types.relay.Connection):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('WarehouseTableEdge')), graphql_name='edges')


class WarehouseTableEdge(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('WarehouseTable', graphql_name='node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')


class WhereConditionSegments(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('where_conditions',)
    where_conditions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='whereConditions')


class createEventComment(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class deleteEventComment(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class updateEventComment(sgqlc.types.Type):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class AirflowTaskInstance(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('created_time', 'updated_time', 'account_uuid', 'dag_id', 'execution_date', 'task_id', 'try_number', 'state')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')
    account_uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountUuid')
    dag_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='dagId')
    execution_date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='executionDate')
    task_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='taskId')
    try_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='tryNumber')
    state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='state')


class AuthUser(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('cognito_user_id', 'email', 'first_name', 'last_name', 'state', 'created_on', 'is_sso', 'notification_settings_added', 'notification_settings_modified', 'invitees', 'eventmodel_set', 'incident_reactions_created', 'incident_reactions_modified', 'user_comments', 'creator', 'combinedtablestatsmodel_set', 'object_properties', 'catalog_object_metadata', 'docs', 'doc_authors', 'lineage_nodes', 'lineage_edges', 'resources', 'lineage_block_patterns', 'monte_carlo_config_templates', 'slack_credentials_v2', 'custom_users', 'unified_users', 'last_updated_unified_users')
    cognito_user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cognitoUserId')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    state = sgqlc.types.Field(sgqlc.types.non_null(UserModelState), graphql_name='state')
    created_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdOn')
    is_sso = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSso')
    notification_settings_added = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AccountNotificationSetting))), graphql_name='notificationSettingsAdded')
    notification_settings_modified = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AccountNotificationSetting))), graphql_name='notificationSettingsModified')
    invitees = sgqlc.types.Field(sgqlc.types.non_null(UserInviteConnection), graphql_name='invitees', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('state', sgqlc.types.Arg(String, graphql_name='state', default=None)),
))
    )
    eventmodel_set = sgqlc.types.Field(sgqlc.types.non_null(EventConnection), graphql_name='eventmodelSet', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    incident_reactions_created = sgqlc.types.Field(sgqlc.types.non_null(IncidentReactionConnection), graphql_name='incidentReactionsCreated', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    incident_reactions_modified = sgqlc.types.Field(sgqlc.types.non_null(IncidentReactionConnection), graphql_name='incidentReactionsModified', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    user_comments = sgqlc.types.Field(sgqlc.types.non_null(EventCommentConnection), graphql_name='userComments', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    creator = sgqlc.types.Field(sgqlc.types.non_null(MetricMonitoringConnection), graphql_name='creator', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    combinedtablestatsmodel_set = sgqlc.types.Field(sgqlc.types.non_null(TableStatsConnection), graphql_name='combinedtablestatsmodelSet', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    object_properties = sgqlc.types.Field(sgqlc.types.non_null(ObjectPropertyConnection), graphql_name='objectProperties', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('mcon_id', sgqlc.types.Arg(String, graphql_name='mconId', default=None)),
))
    )
    catalog_object_metadata = sgqlc.types.Field(sgqlc.types.non_null(CatalogObjectMetadataConnection), graphql_name='catalogObjectMetadata', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
))
    )
    docs = sgqlc.types.Field(sgqlc.types.non_null(DocConnection), graphql_name='docs', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    doc_authors = sgqlc.types.Field(sgqlc.types.non_null(DocAuthorConnection), graphql_name='docAuthors', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    lineage_nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LineageNode))), graphql_name='lineageNodes')
    lineage_edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LineageEdge))), graphql_name='lineageEdges')
    resources = sgqlc.types.Field(sgqlc.types.non_null(ResourceConnection), graphql_name='resources', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    lineage_block_patterns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LineageNodeBlockPattern))), graphql_name='lineageBlockPatterns')
    monte_carlo_config_templates = sgqlc.types.Field(sgqlc.types.non_null(MonteCarloConfigTemplateConnection), graphql_name='monteCarloConfigTemplates', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('namespace', sgqlc.types.Arg(String, graphql_name='namespace', default=None)),
))
    )
    slack_credentials_v2 = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SlackCredentialsV2))), graphql_name='slackCredentialsV2')
    custom_users = sgqlc.types.Field(sgqlc.types.non_null(CustomUserConnection), graphql_name='customUsers', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    unified_users = sgqlc.types.Field(sgqlc.types.non_null(UnifiedUserConnection), graphql_name='unifiedUsers', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    last_updated_unified_users = sgqlc.types.Field(sgqlc.types.non_null(UnifiedUserConnection), graphql_name='lastUpdatedUnifiedUsers', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class CatalogObjectMetadata(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('mcon', 'account_id', 'resource_id', 'description', 'created_time', 'last_update_user', 'last_update_time', 'source')
    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    resource_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceId')
    description = sgqlc.types.Field(String, graphql_name='description')
    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    last_update_user = sgqlc.types.Field('User', graphql_name='lastUpdateUser')
    last_update_time = sgqlc.types.Field(DateTime, graphql_name='lastUpdateTime')
    source = sgqlc.types.Field(String, graphql_name='source')


class CustomRule(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('uuid', 'rule_type', 'warehouse_uuid', 'comparisons', 'interval_minutes', 'interval_crontab', 'start_time', 'timezone', 'creator_id', 'description', 'notes', 'prev_execution_time', 'next_execution_time', 'last_check_timestamp', 'created_time', 'updated_time', 'is_deleted', 'snooze_until_time', 'slack_snooze_user', 'dc_schedule_uuid', 'data_collection_dc_schedule_uuid', 'custom_sql', 'override', 'variables', 'generated_by', 'account_uuid', 'entities', 'projects', 'datasets', 'rule_name', 'namespace', 'is_template_managed', 'sequence_number', 'labels', 'system_snooze_until_time', 'query_result_type', 'custom_sampling_sql', 'generated_rules', 'rendered_custom_sql', 'schedule_config', 'data_collection_schedule_config', 'is_snoozed')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    rule_type = sgqlc.types.Field(CustomRuleModelRuleType, graphql_name='ruleType')
    warehouse_uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='warehouseUuid')
    comparisons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(CustomRuleComparison)), graphql_name='comparisons')
    interval_minutes = sgqlc.types.Field(Int, graphql_name='intervalMinutes')
    interval_crontab = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='intervalCrontab')
    start_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startTime')
    timezone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='timezone')
    creator_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='creatorId')
    description = sgqlc.types.Field(String, graphql_name='description')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    prev_execution_time = sgqlc.types.Field(DateTime, graphql_name='prevExecutionTime')
    next_execution_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='nextExecutionTime')
    last_check_timestamp = sgqlc.types.Field(DateTime, graphql_name='lastCheckTimestamp')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')
    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')
    snooze_until_time = sgqlc.types.Field(DateTime, graphql_name='snoozeUntilTime')
    slack_snooze_user = sgqlc.types.Field(String, graphql_name='slackSnoozeUser')
    dc_schedule_uuid = sgqlc.types.Field(UUID, graphql_name='dcScheduleUuid')
    data_collection_dc_schedule_uuid = sgqlc.types.Field(UUID, graphql_name='dataCollectionDcScheduleUuid')
    custom_sql = sgqlc.types.Field(String, graphql_name='customSql')
    override = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='override')
    variables = sgqlc.types.Field(JSONString, graphql_name='variables')
    generated_by = sgqlc.types.Field('CustomRule', graphql_name='generatedBy')
    account_uuid = sgqlc.types.Field(UUID, graphql_name='accountUuid')
    entities = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='entities')
    projects = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='projects')
    datasets = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='datasets')
    rule_name = sgqlc.types.Field(String, graphql_name='ruleName')
    namespace = sgqlc.types.Field(String, graphql_name='namespace')
    is_template_managed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTemplateManaged')
    sequence_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='sequenceNumber')
    labels = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='labels')
    system_snooze_until_time = sgqlc.types.Field(DateTime, graphql_name='systemSnoozeUntilTime')
    query_result_type = sgqlc.types.Field(CustomRuleModelQueryResultType, graphql_name='queryResultType')
    custom_sampling_sql = sgqlc.types.Field(String, graphql_name='customSamplingSql')
    generated_rules = sgqlc.types.Field(sgqlc.types.non_null(CustomRuleConnection), graphql_name='generatedRules', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('rule_type', sgqlc.types.Arg(String, graphql_name='ruleType', default=None)),
))
    )
    rendered_custom_sql = sgqlc.types.Field(String, graphql_name='renderedCustomSql')
    schedule_config = sgqlc.types.Field(ScheduleConfigOutput, graphql_name='scheduleConfig')
    data_collection_schedule_config = sgqlc.types.Field(ScheduleConfigOutput, graphql_name='dataCollectionScheduleConfig')
    is_snoozed = sgqlc.types.Field(Boolean, graphql_name='isSnoozed')


class CustomUser(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('uuid', 'account_id', 'email', 'first_name', 'last_name', 'created_time', 'last_update_user', 'last_update_time', 'is_deleted', 'unified_users')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    email = sgqlc.types.Field(String, graphql_name='email')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    last_update_user = sgqlc.types.Field('User', graphql_name='lastUpdateUser')
    last_update_time = sgqlc.types.Field(DateTime, graphql_name='lastUpdateTime')
    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')
    unified_users = sgqlc.types.Field(sgqlc.types.non_null(UnifiedUserConnection), graphql_name='unifiedUsers', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class Dataset(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('uuid', 'warehouse', 'project', 'dataset', 'is_muted', 'table_count')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    warehouse = sgqlc.types.Field(sgqlc.types.non_null(Warehouse), graphql_name='warehouse')
    project = sgqlc.types.Field(String, graphql_name='project')
    dataset = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='dataset')
    is_muted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMuted')
    table_count = sgqlc.types.Field(Int, graphql_name='tableCount')


class DbtEdge(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('created_time', 'updated_time', 'uuid', 'account_id', 'source_unique_id', 'destination_unique_id', 'dbt_project')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    source_unique_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sourceUniqueId')
    destination_unique_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='destinationUniqueId')
    dbt_project = sgqlc.types.Field(sgqlc.types.non_null('DbtProject'), graphql_name='dbtProject')


class DbtNode(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('created_time', 'updated_time', 'uuid', 'account_id', 'unique_id', 'database', 'schema', 'name', 'alias', 'description', 'path', 'resource_type', 'raw_sql', 'raw_node_json', 'dbt_project', 'table', 'dbt_run_steps', 'test_dbt_run_steps')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    unique_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uniqueId')
    database = sgqlc.types.Field(String, graphql_name='database')
    schema = sgqlc.types.Field(String, graphql_name='schema')
    name = sgqlc.types.Field(String, graphql_name='name')
    alias = sgqlc.types.Field(String, graphql_name='alias')
    description = sgqlc.types.Field(String, graphql_name='description')
    path = sgqlc.types.Field(String, graphql_name='path')
    resource_type = sgqlc.types.Field(String, graphql_name='resourceType')
    raw_sql = sgqlc.types.Field(String, graphql_name='rawSql')
    raw_node_json = sgqlc.types.Field(String, graphql_name='rawNodeJson')
    dbt_project = sgqlc.types.Field(sgqlc.types.non_null('DbtProject'), graphql_name='dbtProject')
    table = sgqlc.types.Field('WarehouseTable', graphql_name='table')
    dbt_run_steps = sgqlc.types.Field(DbtRunStepConnection, graphql_name='dbtRunSteps', args=sgqlc.types.ArgDict((
        ('run_start_time', sgqlc.types.Arg(DateTime, graphql_name='runStartTime', default=None)),
        ('run_end_time', sgqlc.types.Arg(DateTime, graphql_name='runEndTime', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    test_dbt_run_steps = sgqlc.types.Field(DbtRunStepConnection, graphql_name='testDbtRunSteps', args=sgqlc.types.ArgDict((
        ('run_start_time', sgqlc.types.Arg(DateTime, graphql_name='runStartTime', default=None)),
        ('run_end_time', sgqlc.types.Arg(DateTime, graphql_name='runEndTime', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class DbtProject(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('created_time', 'updated_time', 'uuid', 'account_id', 'project_name', 'source', 'generates_incidents', 'last_model_import', 'last_test_import', 'dbt_nodes', 'dbt_edges', 'dbt_runs')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    project_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectName')
    source = sgqlc.types.Field(sgqlc.types.non_null(DbtProjectModelSource), graphql_name='source')
    generates_incidents = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='generatesIncidents')
    last_model_import = sgqlc.types.Field(DateTime, graphql_name='lastModelImport')
    last_test_import = sgqlc.types.Field(DateTime, graphql_name='lastTestImport')
    dbt_nodes = sgqlc.types.Field(sgqlc.types.non_null(DbtNodeConnection), graphql_name='dbtNodes', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    dbt_edges = sgqlc.types.Field(sgqlc.types.non_null(DbtEdgeConnection), graphql_name='dbtEdges', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    dbt_runs = sgqlc.types.Field(sgqlc.types.non_null(DbtRunConnection), graphql_name='dbtRuns', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class DbtRun(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('created_time', 'updated_time', 'uuid', 'account_id', 'dbt_project', 'dbt_job_definition_id', 'dbt_run_id', 'git_branch', 'run_logs', 'created_at', 'finished_at', 'duration', 'queued_duration', 'run_duration', 'generated_at', 'started_at', 'in_progress', 'is_complete', 'is_success', 'is_error', 'is_cancelled', 'status_raw', 'status_humanized', 'status_message', 'command', 'dbt_run_steps')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    dbt_project = sgqlc.types.Field(sgqlc.types.non_null(DbtProject), graphql_name='dbtProject')
    dbt_job_definition_id = sgqlc.types.Field(String, graphql_name='dbtJobDefinitionId')
    dbt_run_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='dbtRunId')
    git_branch = sgqlc.types.Field(String, graphql_name='gitBranch')
    run_logs = sgqlc.types.Field(String, graphql_name='runLogs')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    finished_at = sgqlc.types.Field(DateTime, graphql_name='finishedAt')
    duration = sgqlc.types.Field(Float, graphql_name='duration')
    queued_duration = sgqlc.types.Field(Float, graphql_name='queuedDuration')
    run_duration = sgqlc.types.Field(Float, graphql_name='runDuration')
    generated_at = sgqlc.types.Field(DateTime, graphql_name='generatedAt')
    started_at = sgqlc.types.Field(DateTime, graphql_name='startedAt')
    in_progress = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='inProgress')
    is_complete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isComplete')
    is_success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSuccess')
    is_error = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isError')
    is_cancelled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCancelled')
    status_raw = sgqlc.types.Field(Int, graphql_name='statusRaw')
    status_humanized = sgqlc.types.Field(String, graphql_name='statusHumanized')
    status_message = sgqlc.types.Field(String, graphql_name='statusMessage')
    command = sgqlc.types.Field(String, graphql_name='command')
    dbt_run_steps = sgqlc.types.Field(sgqlc.types.non_null(DbtRunStepConnection), graphql_name='dbtRunSteps', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class DbtRunStep(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('created_time', 'updated_time', 'uuid', 'account_id', 'status', 'started_at', 'completed_at', 'thread_id', 'execution_time', 'message', 'raw_json', 'dbt_run', 'node_unique_id')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    status = sgqlc.types.Field(String, graphql_name='status')
    started_at = sgqlc.types.Field(DateTime, graphql_name='startedAt')
    completed_at = sgqlc.types.Field(DateTime, graphql_name='completedAt')
    thread_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='threadId')
    execution_time = sgqlc.types.Field(Float, graphql_name='executionTime')
    message = sgqlc.types.Field(String, graphql_name='message')
    raw_json = sgqlc.types.Field(String, graphql_name='rawJson')
    dbt_run = sgqlc.types.Field(sgqlc.types.non_null(DbtRun), graphql_name='dbtRun')
    node_unique_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nodeUniqueId')


class DimensionTrackingSuggestions(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('account_uuid', 'mcon', 'resource_id', 'full_table_id', 'project_name', 'dataset_name', 'table_name', 'table_type', 'field', 'type', 'table_importance_score', 'field_score', 'analytics_export_ts')
    account_uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountUuid')
    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')
    resource_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceId')
    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')
    project_name = sgqlc.types.Field(String, graphql_name='projectName')
    dataset_name = sgqlc.types.Field(String, graphql_name='datasetName')
    table_name = sgqlc.types.Field(String, graphql_name='tableName')
    table_type = sgqlc.types.Field(String, graphql_name='tableType')
    field = sgqlc.types.Field(String, graphql_name='field')
    type = sgqlc.types.Field(String, graphql_name='type')
    table_importance_score = sgqlc.types.Field(Float, graphql_name='tableImportanceScore')
    field_score = sgqlc.types.Field(String, graphql_name='fieldScore')
    analytics_export_ts = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='analyticsExportTs')


class Doc(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('created_time', 'updated_time', 'mcon', 'account_id', 'title', 'content', 'is_deleted', 'last_update_user', 'parent_doc', 'children', 'doc_authors', 'doc_links')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')
    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    title = sgqlc.types.Field(String, graphql_name='title')
    content = sgqlc.types.Field(String, graphql_name='content')
    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')
    last_update_user = sgqlc.types.Field('User', graphql_name='lastUpdateUser')
    parent_doc = sgqlc.types.Field('Doc', graphql_name='parentDoc')
    children = sgqlc.types.Field(sgqlc.types.non_null(DocConnection), graphql_name='children', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    doc_authors = sgqlc.types.Field(DocAuthorConnection, graphql_name='docAuthors', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    doc_links = sgqlc.types.Field(DocLinkConnection, graphql_name='docLinks', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class DocAuthor(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('account_id', 'doc', 'user')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    doc = sgqlc.types.Field(Doc, graphql_name='doc')
    user = sgqlc.types.Field('User', graphql_name='user')


class DocLink(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('account_id', 'doc', 'object_mcon')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    doc = sgqlc.types.Field(Doc, graphql_name='doc')
    object_mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='objectMcon')


class DomainRestriction(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('created_time', 'updated_time', 'uuid', 'name')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class Event(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('event_type', 'created_time', 'anomaly', 'data', 'ack_by', 'ack_timestamp', 'event_state', 'notified_users', 'total_comments', 'importance_score', 'is_child', 'uuid', 'warehouse', 'table', 'monitor_id', 'custom_rule_entities', 'custom_rule_projects', 'custom_rule_datasets', 'incident', 'event_generated_time', 'event_comments', 'rca_jobs', 'table_stats')
    event_type = sgqlc.types.Field(sgqlc.types.non_null(EventModelEventType), graphql_name='eventType')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    anomaly = sgqlc.types.Field('TableAnomaly', graphql_name='anomaly')
    data = sgqlc.types.Field(JSONString, graphql_name='data')
    ack_by = sgqlc.types.Field('User', graphql_name='ackBy')
    ack_timestamp = sgqlc.types.Field(DateTime, graphql_name='ackTimestamp')
    event_state = sgqlc.types.Field(sgqlc.types.non_null(EventModelEventState), graphql_name='eventState')
    notified_users = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='notifiedUsers')
    total_comments = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalComments')
    importance_score = sgqlc.types.Field(Float, graphql_name='importanceScore')
    is_child = sgqlc.types.Field(Boolean, graphql_name='isChild')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    warehouse = sgqlc.types.Field(sgqlc.types.non_null(Warehouse), graphql_name='warehouse')
    table = sgqlc.types.Field('WarehouseTable', graphql_name='table')
    monitor_id = sgqlc.types.Field(UUID, graphql_name='monitorId')
    custom_rule_entities = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='customRuleEntities')
    custom_rule_projects = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='customRuleProjects')
    custom_rule_datasets = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='customRuleDatasets')
    incident = sgqlc.types.Field('Incident', graphql_name='incident')
    event_generated_time = sgqlc.types.Field(DateTime, graphql_name='eventGeneratedTime')
    event_comments = sgqlc.types.Field(sgqlc.types.non_null(EventCommentConnection), graphql_name='eventComments', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    rca_jobs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RcaJob))), graphql_name='rcaJobs')
    table_stats = sgqlc.types.Field('TableStats', graphql_name='tableStats')


class EventComment(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('event', 'user', 'uuid', 'text', 'created_on', 'updated_on', 'is_deleted')
    event = sgqlc.types.Field(sgqlc.types.non_null(Event), graphql_name='event')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')
    created_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdOn')
    updated_on = sgqlc.types.Field(DateTime, graphql_name='updatedOn')
    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')


class FieldHealthSuggestions(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('account_uuid', 'mcon', 'resource_id', 'full_table_id', 'project_name', 'dataset_name', 'table_name', 'table_type', 'importance_score', 'has_time_field', 'has_txt_field', 'has_num_field', 'has_bool_field', 'analytics_export_ts')
    account_uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountUuid')
    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')
    resource_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceId')
    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')
    project_name = sgqlc.types.Field(String, graphql_name='projectName')
    dataset_name = sgqlc.types.Field(String, graphql_name='datasetName')
    table_name = sgqlc.types.Field(String, graphql_name='tableName')
    table_type = sgqlc.types.Field(String, graphql_name='tableType')
    importance_score = sgqlc.types.Field(Float, graphql_name='importanceScore')
    has_time_field = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasTimeField')
    has_txt_field = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasTxtField')
    has_num_field = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNumField')
    has_bool_field = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasBoolField')
    analytics_export_ts = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='analyticsExportTs')


class Incident(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('uuid', 'warehouse', 'created_time', 'updated_time', 'owner', 'severity', 'feedback', 'feedback_time', 'last_update_user', 'project', 'dataset', 'incident_type', 'incident_sub_types', 'incident_time', 'events', 'incident_reaction', 'slack_msg_details', 'reaction_type', 'summary')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    warehouse = sgqlc.types.Field(sgqlc.types.non_null(Warehouse), graphql_name='warehouse')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    updated_time = sgqlc.types.Field(DateTime, graphql_name='updatedTime')
    owner = sgqlc.types.Field(String, graphql_name='owner')
    severity = sgqlc.types.Field(String, graphql_name='severity')
    feedback = sgqlc.types.Field(IncidentModelFeedback, graphql_name='feedback')
    feedback_time = sgqlc.types.Field(DateTime, graphql_name='feedbackTime')
    last_update_user = sgqlc.types.Field(JSONString, graphql_name='lastUpdateUser')
    project = sgqlc.types.Field(String, graphql_name='project')
    dataset = sgqlc.types.Field(String, graphql_name='dataset')
    incident_type = sgqlc.types.Field(IncidentModelIncidentType, graphql_name='incidentType')
    incident_sub_types = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='incidentSubTypes')
    incident_time = sgqlc.types.Field(DateTime, graphql_name='incidentTime')
    events = sgqlc.types.Field(EventConnection, graphql_name='events', args=sgqlc.types.ArgDict((
        ('event_type', sgqlc.types.Arg(String, graphql_name='eventType', default=None)),
        ('event_state', sgqlc.types.Arg(String, graphql_name='eventState', default=None)),
        ('include_timeline_events', sgqlc.types.Arg(Boolean, graphql_name='includeTimelineEvents', default=None)),
        ('include_anomaly_events', sgqlc.types.Arg(Boolean, graphql_name='includeAnomalyEvents', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
))
    )
    incident_reaction = sgqlc.types.Field('IncidentReaction', graphql_name='incidentReaction')
    slack_msg_details = sgqlc.types.Field(sgqlc.types.non_null(SlackMessageDetailsConnection), graphql_name='slackMsgDetails', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    reaction_type = sgqlc.types.Field(IncidentReactionType, graphql_name='reactionType')
    summary = sgqlc.types.Field(IncidentSummary, graphql_name='summary')


class IncidentReaction(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('uuid', 'incident', 'type', 'reasons', 'notes', 'created_by', 'last_updated_by', 'created_time', 'updated_time')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    incident = sgqlc.types.Field(sgqlc.types.non_null(Incident), graphql_name='incident')
    type = sgqlc.types.Field(sgqlc.types.non_null(IncidentReactionType), graphql_name='type')
    reasons = sgqlc.types.Field(sgqlc.types.list_of(IncidentReactionReason), graphql_name='reasons')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    created_by = sgqlc.types.Field('User', graphql_name='createdBy')
    last_updated_by = sgqlc.types.Field('User', graphql_name='lastUpdatedBy')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')


class MetricMonitoring(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('uuid', 'type', 'fields', 'entities', 'projects', 'datasets', 'created_by', 'time_axis_field_name', 'time_axis_field_type', 'unnest_fields', 'agg_time_interval', 'history_days', 'agg_select_expression', 'where_condition', 'schedule', 'created_time', 'namespace', 'account_uuid', 'monitor_name', 'is_template_managed', 'is_paused', 'disable_look_back_bootstrap', 'segmented_expressions', 'description', 'notes', 'labels', 'table', 'select_expressions', 'mcon', 'full_table_id', 'monitor_type', 'schedule_config')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    type = sgqlc.types.Field(sgqlc.types.non_null(MetricMonitoringModelType), graphql_name='type')
    fields = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='fields')
    entities = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='entities')
    projects = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='projects')
    datasets = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='datasets')
    created_by = sgqlc.types.Field('User', graphql_name='createdBy')
    time_axis_field_name = sgqlc.types.Field(String, graphql_name='timeAxisFieldName')
    time_axis_field_type = sgqlc.types.Field(String, graphql_name='timeAxisFieldType')
    unnest_fields = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='unnestFields')
    agg_time_interval = sgqlc.types.Field(String, graphql_name='aggTimeInterval')
    history_days = sgqlc.types.Field(Int, graphql_name='historyDays')
    agg_select_expression = sgqlc.types.Field(String, graphql_name='aggSelectExpression')
    where_condition = sgqlc.types.Field(String, graphql_name='whereCondition')
    schedule = sgqlc.types.Field(sgqlc.types.non_null(DataCollectorSchedule), graphql_name='schedule')
    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    namespace = sgqlc.types.Field(String, graphql_name='namespace')
    account_uuid = sgqlc.types.Field(UUID, graphql_name='accountUuid')
    monitor_name = sgqlc.types.Field(String, graphql_name='monitorName')
    is_template_managed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTemplateManaged')
    is_paused = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPaused')
    disable_look_back_bootstrap = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='disableLookBackBootstrap')
    segmented_expressions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='segmentedExpressions')
    description = sgqlc.types.Field(String, graphql_name='description')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    labels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MonitorLabelObject))), graphql_name='labels')
    table = sgqlc.types.Field('WarehouseTable', graphql_name='table')
    select_expressions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MetricMonitorSelectExpression))), graphql_name='selectExpressions')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')
    monitor_type = sgqlc.types.Field(String, graphql_name='monitorType')
    schedule_config = sgqlc.types.Field(ScheduleConfigOutput, graphql_name='scheduleConfig')


class Monitor(sgqlc.types.Type, IMonitor, IMetricsMonitor, ICustomRulesMonitor, IMonitorStatus):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ()


class MonteCarloConfigTemplate(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('namespace', 'template', 'resolved_template', 'created_time', 'last_update_user', 'last_update_time')
    namespace = sgqlc.types.Field(String, graphql_name='namespace')
    template = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='template')
    resolved_template = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='resolvedTemplate')
    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    last_update_user = sgqlc.types.Field('User', graphql_name='lastUpdateUser')
    last_update_time = sgqlc.types.Field(DateTime, graphql_name='lastUpdateTime')


class ObjectProperty(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('mcon_id', 'property_name', 'property_value', 'property_source_type', 'property_source')
    mcon_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mconId')
    property_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='propertyName')
    property_value = sgqlc.types.Field(String, graphql_name='propertyValue')
    property_source_type = sgqlc.types.Field(sgqlc.types.non_null(ObjectPropertyModelPropertySourceType), graphql_name='propertySourceType')
    property_source = sgqlc.types.Field(String, graphql_name='propertySource')


class Resource(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('uuid', 'account', 'name', 'type', 'is_user_provided', 'is_default', 'created_time', 'last_update_user', 'last_update_time')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    type = sgqlc.types.Field(String, graphql_name='type')
    is_user_provided = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isUserProvided')
    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')
    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    last_update_user = sgqlc.types.Field('User', graphql_name='lastUpdateUser')
    last_update_time = sgqlc.types.Field(DateTime, graphql_name='lastUpdateTime')


class SlackEngagement(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('message', 'uuid', 'event_type', 'event_ts', 'data', 'created_time', 'updated_time')
    message = sgqlc.types.Field(sgqlc.types.non_null('SlackMessageDetails'), graphql_name='message')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    event_type = sgqlc.types.Field(SlackEngagementEventType, graphql_name='eventType')
    event_ts = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='eventTs')
    data = sgqlc.types.Field(JSONString, graphql_name='data')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')


class SlackMessageDetails(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('incident', 'notification_setting', 'account', 'permalink', 'msg_ts', 'engagements')
    incident = sgqlc.types.Field(sgqlc.types.non_null(Incident), graphql_name='incident')
    notification_setting = sgqlc.types.Field(sgqlc.types.non_null(AccountNotificationSetting), graphql_name='notificationSetting')
    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    msg_ts = sgqlc.types.Field(String, graphql_name='msgTs')
    engagements = sgqlc.types.Field(sgqlc.types.non_null(SlackEngagementConnection), graphql_name='engagements', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class TableAnomaly(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('uuid', 'warehouse_uuid', 'table', 'rule_uuid', 'anomaly_id', 'detected_on', 'start_time', 'end_time', 'is_active', 'is_false_positive', 'reason', 'data', 'eventmodel_set')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    warehouse_uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='warehouseUuid')
    table = sgqlc.types.Field('WarehouseTable', graphql_name='table')
    rule_uuid = sgqlc.types.Field(UUID, graphql_name='ruleUuid')
    anomaly_id = sgqlc.types.Field(String, graphql_name='anomalyId')
    detected_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='detectedOn')
    start_time = sgqlc.types.Field(DateTime, graphql_name='startTime')
    end_time = sgqlc.types.Field(DateTime, graphql_name='endTime')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    is_false_positive = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFalsePositive')
    reason = sgqlc.types.Field(sgqlc.types.non_null(TableAnomalyModelReason), graphql_name='reason')
    data = sgqlc.types.Field(JSONString, graphql_name='data')
    eventmodel_set = sgqlc.types.Field(sgqlc.types.non_null(EventConnection), graphql_name='eventmodelSet', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class TableField(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('version', 'name', 'field_type', 'mode', 'description', 'original_name', 'data_metric_time_field', 'downstream_bi', 'is_time_field', 'is_text_field', 'is_numeric_field', 'is_boolean_field', 'most_recent_use_in_same_table', 'most_recent_use_in_another_table', 'field_mcon', 'object_properties', 'object_metadata')
    version = sgqlc.types.Field(sgqlc.types.non_null('TableSchemaVersion'), graphql_name='version')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fieldType')
    mode = sgqlc.types.Field(String, graphql_name='mode')
    description = sgqlc.types.Field(String, graphql_name='description')
    original_name = sgqlc.types.Field(String, graphql_name='originalName')
    data_metric_time_field = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='dataMetricTimeField')
    downstream_bi = sgqlc.types.Field(sgqlc.types.non_null(TableFieldToBiConnection), graphql_name='downstreamBi', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    is_time_field = sgqlc.types.Field(Boolean, graphql_name='isTimeField')
    is_text_field = sgqlc.types.Field(Boolean, graphql_name='isTextField')
    is_numeric_field = sgqlc.types.Field(Boolean, graphql_name='isNumericField')
    is_boolean_field = sgqlc.types.Field(Boolean, graphql_name='isBooleanField')
    most_recent_use_in_same_table = sgqlc.types.Field(DateTime, graphql_name='mostRecentUseInSameTable')
    most_recent_use_in_another_table = sgqlc.types.Field(DateTime, graphql_name='mostRecentUseInAnotherTable')
    field_mcon = sgqlc.types.Field(String, graphql_name='fieldMcon')
    object_properties = sgqlc.types.Field(sgqlc.types.list_of(ObjectProperty), graphql_name='objectProperties')
    object_metadata = sgqlc.types.Field(CatalogObjectMetadata, graphql_name='objectMetadata')


class TableFieldToBi(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('field', 'bi_account_id', 'bi_identifier', 'bi_name', 'bi_type', 'bi_node_id', 'created_on', 'last_seen')
    field = sgqlc.types.Field(sgqlc.types.non_null(TableField), graphql_name='field')
    bi_account_id = sgqlc.types.Field(UUID, graphql_name='biAccountId')
    bi_identifier = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='biIdentifier')
    bi_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='biName')
    bi_type = sgqlc.types.Field(sgqlc.types.non_null(TableFieldToBiModelBiType), graphql_name='biType')
    bi_node_id = sgqlc.types.Field(String, graphql_name='biNodeId')
    created_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdOn')
    last_seen = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='lastSeen')


class TableSchemaVersion(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('table', 'version_id', 'timestamp', 'fields')
    table = sgqlc.types.Field(sgqlc.types.non_null('WarehouseTable'), graphql_name='table')
    version_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='versionId')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='timestamp')
    fields = sgqlc.types.Field(TableFieldConnection, graphql_name='fields', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('search_fields', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='searchFields', default=None)),
        ('is_time_field', sgqlc.types.Arg(Boolean, graphql_name='isTimeField', default=None)),
        ('is_text_field', sgqlc.types.Arg(Boolean, graphql_name='isTextField', default=None)),
        ('is_numeric_field', sgqlc.types.Arg(Boolean, graphql_name='isNumericField', default=None)),
        ('is_boolean_field', sgqlc.types.Arg(Boolean, graphql_name='isBooleanField', default=None)),
        ('suggest_time_axis', sgqlc.types.Arg(Boolean, graphql_name='suggestTimeAxis', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('version', sgqlc.types.Arg(ID, graphql_name='version', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('field_type', sgqlc.types.Arg(String, graphql_name='fieldType', default=None)),
        ('mode', sgqlc.types.Arg(String, graphql_name='mode', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('original_name', sgqlc.types.Arg(String, graphql_name='originalName', default=None)),
        ('data_metric_time_field', sgqlc.types.Arg(Boolean, graphql_name='dataMetricTimeField', default=None)),
))
    )


class TableStats(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('resource_uuid', 'full_table_id', 'project_name', 'dataset_name', 'table_name', 'is_important', 'importance_score', 'avg_reads_per_active_day', 'total_users', 'degree_out', 'avg_writes_per_active_day')
    resource_uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceUuid')
    full_table_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullTableId')
    project_name = sgqlc.types.Field(String, graphql_name='projectName')
    dataset_name = sgqlc.types.Field(String, graphql_name='datasetName')
    table_name = sgqlc.types.Field(String, graphql_name='tableName')
    is_important = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isImportant')
    importance_score = sgqlc.types.Field(Float, graphql_name='importanceScore')
    avg_reads_per_active_day = sgqlc.types.Field(Float, graphql_name='avgReadsPerActiveDay')
    total_users = sgqlc.types.Field(Float, graphql_name='totalUsers')
    degree_out = sgqlc.types.Field(Float, graphql_name='degreeOut')
    avg_writes_per_active_day = sgqlc.types.Field(Float, graphql_name='avgWritesPerActiveDay')


class TableTag(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('table', 'tag', 'is_active')
    table = sgqlc.types.Field(sgqlc.types.non_null('WarehouseTable'), graphql_name='table')
    tag = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tag')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')


class UnifiedUser(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('uuid', 'account_id', 'display_name', 'created_time', 'mc_user', 'custom_user', 'last_update_user', 'last_update_time', 'is_deleted', 'unified_user_assignments')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    mc_user = sgqlc.types.Field('User', graphql_name='mcUser')
    custom_user = sgqlc.types.Field(CustomUser, graphql_name='customUser')
    last_update_user = sgqlc.types.Field('User', graphql_name='lastUpdateUser')
    last_update_time = sgqlc.types.Field(DateTime, graphql_name='lastUpdateTime')
    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')
    unified_user_assignments = sgqlc.types.Field(sgqlc.types.non_null(UnifiedUserAssignmentConnection), graphql_name='unifiedUserAssignments', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class UnifiedUserAssignment(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('account_id', 'unified_user', 'relationship_type', 'created_time', 'is_deleted', 'object_mcon')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    unified_user = sgqlc.types.Field(sgqlc.types.non_null(UnifiedUser), graphql_name='unifiedUser')
    relationship_type = sgqlc.types.Field(UnifiedUserAssignmentModelRelationshipType, graphql_name='relationshipType')
    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')
    object_mcon = sgqlc.types.Field(String, graphql_name='objectMcon')


class User(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('cognito_user_id', 'email', 'first_name', 'last_name', 'state', 'created_on', 'is_sso', 'notification_settings_added', 'notification_settings_modified', 'invitees', 'eventmodel_set', 'incident_reactions_created', 'incident_reactions_modified', 'user_comments', 'creator', 'combinedtablestatsmodel_set', 'object_properties', 'catalog_object_metadata', 'docs', 'doc_authors', 'lineage_nodes', 'lineage_edges', 'resources', 'lineage_block_patterns', 'monte_carlo_config_templates', 'slack_credentials_v2', 'custom_users', 'unified_users', 'last_updated_unified_users', 'account', 'role', 'auth')
    cognito_user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cognitoUserId')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    state = sgqlc.types.Field(sgqlc.types.non_null(UserModelState), graphql_name='state')
    created_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdOn')
    is_sso = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSso')
    notification_settings_added = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AccountNotificationSetting))), graphql_name='notificationSettingsAdded')
    notification_settings_modified = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AccountNotificationSetting))), graphql_name='notificationSettingsModified')
    invitees = sgqlc.types.Field(sgqlc.types.non_null(UserInviteConnection), graphql_name='invitees', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('state', sgqlc.types.Arg(String, graphql_name='state', default=None)),
))
    )
    eventmodel_set = sgqlc.types.Field(sgqlc.types.non_null(EventConnection), graphql_name='eventmodelSet', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    incident_reactions_created = sgqlc.types.Field(sgqlc.types.non_null(IncidentReactionConnection), graphql_name='incidentReactionsCreated', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    incident_reactions_modified = sgqlc.types.Field(sgqlc.types.non_null(IncidentReactionConnection), graphql_name='incidentReactionsModified', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    user_comments = sgqlc.types.Field(sgqlc.types.non_null(EventCommentConnection), graphql_name='userComments', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    creator = sgqlc.types.Field(sgqlc.types.non_null(MetricMonitoringConnection), graphql_name='creator', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    combinedtablestatsmodel_set = sgqlc.types.Field(sgqlc.types.non_null(TableStatsConnection), graphql_name='combinedtablestatsmodelSet', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    object_properties = sgqlc.types.Field(sgqlc.types.non_null(ObjectPropertyConnection), graphql_name='objectProperties', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('mcon_id', sgqlc.types.Arg(String, graphql_name='mconId', default=None)),
))
    )
    catalog_object_metadata = sgqlc.types.Field(sgqlc.types.non_null(CatalogObjectMetadataConnection), graphql_name='catalogObjectMetadata', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
))
    )
    docs = sgqlc.types.Field(sgqlc.types.non_null(DocConnection), graphql_name='docs', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    doc_authors = sgqlc.types.Field(sgqlc.types.non_null(DocAuthorConnection), graphql_name='docAuthors', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    lineage_nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LineageNode))), graphql_name='lineageNodes')
    lineage_edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LineageEdge))), graphql_name='lineageEdges')
    resources = sgqlc.types.Field(sgqlc.types.non_null(ResourceConnection), graphql_name='resources', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    lineage_block_patterns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LineageNodeBlockPattern))), graphql_name='lineageBlockPatterns')
    monte_carlo_config_templates = sgqlc.types.Field(sgqlc.types.non_null(MonteCarloConfigTemplateConnection), graphql_name='monteCarloConfigTemplates', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('namespace', sgqlc.types.Arg(String, graphql_name='namespace', default=None)),
))
    )
    slack_credentials_v2 = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SlackCredentialsV2))), graphql_name='slackCredentialsV2')
    custom_users = sgqlc.types.Field(sgqlc.types.non_null(CustomUserConnection), graphql_name='customUsers', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    unified_users = sgqlc.types.Field(sgqlc.types.non_null(UnifiedUserConnection), graphql_name='unifiedUsers', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    last_updated_unified_users = sgqlc.types.Field(sgqlc.types.non_null(UnifiedUserConnection), graphql_name='lastUpdatedUnifiedUsers', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    account = sgqlc.types.Field(Account, graphql_name='account')
    role = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='role')
    auth = sgqlc.types.Field(UserAuthorizationOutput, graphql_name='auth')


class UserDefinedMonitorV2(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('uuid', 'udm_type', 'resource_id', 'creator_id', 'entities', 'projects', 'datasets', 'rule_comparisons', 'rule_description', 'rule_variables', 'monitor_type', 'monitor_fields', 'monitor_time_axis_field_name', 'monitor_time_axis_field_type', 'created_time', 'schedule_type', 'last_run', 'interval_in_seconds', 'prev_execution_time', 'next_execution_time', 'is_deleted', 'is_template_managed', 'is_snoozeable', 'is_snoozed', 'snooze_until_time', 'is_paused', 'where_condition', 'namespace', 'rule_name', 'rule_notes', 'history_days', 'segmented_expressions', 'interval_minutes', 'agg_time_interval', 'has_custom_rule_name', 'is_transitioning_data_provider')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    udm_type = sgqlc.types.Field(sgqlc.types.non_null(UserDefinedMonitorModelUdmType), graphql_name='udmType')
    resource_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceId')
    creator_id = sgqlc.types.Field(String, graphql_name='creatorId')
    entities = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='entities')
    projects = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='projects')
    datasets = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='datasets')
    rule_comparisons = sgqlc.types.Field(sgqlc.types.list_of(CustomRuleComparison), graphql_name='ruleComparisons')
    rule_description = sgqlc.types.Field(String, graphql_name='ruleDescription')
    rule_variables = sgqlc.types.Field(JSONString, graphql_name='ruleVariables')
    monitor_type = sgqlc.types.Field(sgqlc.types.non_null(UserDefinedMonitorModelMonitorType), graphql_name='monitorType')
    monitor_fields = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='monitorFields')
    monitor_time_axis_field_name = sgqlc.types.Field(String, graphql_name='monitorTimeAxisFieldName')
    monitor_time_axis_field_type = sgqlc.types.Field(String, graphql_name='monitorTimeAxisFieldType')
    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    schedule_type = sgqlc.types.Field(UserDefinedMonitorModelScheduleType, graphql_name='scheduleType')
    last_run = sgqlc.types.Field(DateTime, graphql_name='lastRun')
    interval_in_seconds = sgqlc.types.Field(Int, graphql_name='intervalInSeconds')
    prev_execution_time = sgqlc.types.Field(DateTime, graphql_name='prevExecutionTime')
    next_execution_time = sgqlc.types.Field(DateTime, graphql_name='nextExecutionTime')
    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')
    is_template_managed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTemplateManaged')
    is_snoozeable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSnoozeable')
    is_snoozed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSnoozed')
    snooze_until_time = sgqlc.types.Field(DateTime, graphql_name='snoozeUntilTime')
    is_paused = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPaused')
    where_condition = sgqlc.types.Field(String, graphql_name='whereCondition')
    namespace = sgqlc.types.Field(String, graphql_name='namespace')
    rule_name = sgqlc.types.Field(String, graphql_name='ruleName')
    rule_notes = sgqlc.types.Field(String, graphql_name='ruleNotes')
    history_days = sgqlc.types.Field(Int, graphql_name='historyDays')
    segmented_expressions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='segmentedExpressions')
    interval_minutes = sgqlc.types.Field(Int, graphql_name='intervalMinutes')
    agg_time_interval = sgqlc.types.Field(String, graphql_name='aggTimeInterval')
    has_custom_rule_name = sgqlc.types.Field(Boolean, graphql_name='hasCustomRuleName')
    is_transitioning_data_provider = sgqlc.types.Field(Boolean, graphql_name='isTransitioningDataProvider')


class UserInvite(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('uuid', 'email', 'state', 'account', 'created_by', 'created_on', 'accepted_on', 'role', 'auth_groups', 'invite_type', 'last_sent_time', 'attempts', 'expires_at')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    state = sgqlc.types.Field(sgqlc.types.non_null(UserInviteModelState), graphql_name='state')
    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')
    created_by = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='createdBy')
    created_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdOn')
    accepted_on = sgqlc.types.Field(DateTime, graphql_name='acceptedOn')
    role = sgqlc.types.Field(String, graphql_name='role')
    auth_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='authGroups')
    invite_type = sgqlc.types.Field(UserInviteModelInviteType, graphql_name='inviteType')
    last_sent_time = sgqlc.types.Field(DateTime, graphql_name='lastSentTime')
    attempts = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='attempts')
    expires_at = sgqlc.types.Field(DateTime, graphql_name='expiresAt')


class WarehouseTable(sgqlc.types.Type, Node):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __field_names__ = ('table_id', 'full_table_id', 'warehouse', 'discovered_time', 'friendly_name', 'description', 'location', 'project_name', 'dataset', 'table_type', 'is_encrypted', 'created_time', 'last_modified', 'view_query', 'labels', 'path', 'priority', 'tracked', 'status', 'freshness_anomaly', 'size_anomaly', 'freshness_size_anomaly', 'metric_anomaly', 'dynamic_table', 'is_deleted', 'last_observed', 'data_provider', 'mcon', 'anomalies', 'tags', 'versions', 'events', 'monitors', 'dbt_nodes', 'usage_stats', 'thresholds', 'get_thresholds', 'schema_change_count', 'status_scalar', 'node_id', 'is_partial_date_range', 'last_updates', 'last_updates_v2', 'total_row_counts', 'total_byte_counts', 'write_throughput', 'objects_deleted', 'check_table_metrics_existence', 'is_muted', 'table_stats', 'object_properties', 'is_transitioning_data_provider', 'table_capabilities')
    table_id = sgqlc.types.Field(String, graphql_name='tableId')
    full_table_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullTableId')
    warehouse = sgqlc.types.Field(sgqlc.types.non_null(Warehouse), graphql_name='warehouse')
    discovered_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='discoveredTime')
    friendly_name = sgqlc.types.Field(String, graphql_name='friendlyName')
    description = sgqlc.types.Field(String, graphql_name='description')
    location = sgqlc.types.Field(String, graphql_name='location')
    project_name = sgqlc.types.Field(String, graphql_name='projectName')
    dataset = sgqlc.types.Field(String, graphql_name='dataset')
    table_type = sgqlc.types.Field(String, graphql_name='tableType')
    is_encrypted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEncrypted')
    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    last_modified = sgqlc.types.Field(DateTime, graphql_name='lastModified')
    view_query = sgqlc.types.Field(String, graphql_name='viewQuery')
    labels = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='labels')
    path = sgqlc.types.Field(String, graphql_name='path')
    priority = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='priority')
    tracked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='tracked')
    status = sgqlc.types.Field(WarehouseTableModelStatus, graphql_name='status')
    freshness_anomaly = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='freshnessAnomaly')
    size_anomaly = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='sizeAnomaly')
    freshness_size_anomaly = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='freshnessSizeAnomaly')
    metric_anomaly = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='metricAnomaly')
    dynamic_table = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='dynamicTable')
    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')
    last_observed = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='lastObserved')
    data_provider = sgqlc.types.Field(String, graphql_name='dataProvider')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    anomalies = sgqlc.types.Field(TableAnomalyConnection, graphql_name='anomalies', args=sgqlc.types.ArgDict((
        ('reasons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='reasons', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
        ('warehouse_uuid', sgqlc.types.Arg(UUID, graphql_name='warehouseUuid', default=None)),
        ('table', sgqlc.types.Arg(ID, graphql_name='table', default=None)),
        ('rule_uuid', sgqlc.types.Arg(UUID, graphql_name='ruleUuid', default=None)),
        ('anomaly_id', sgqlc.types.Arg(String, graphql_name='anomalyId', default=None)),
        ('detected_on', sgqlc.types.Arg(DateTime, graphql_name='detectedOn', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('is_active', sgqlc.types.Arg(Boolean, graphql_name='isActive', default=None)),
        ('is_false_positive', sgqlc.types.Arg(Boolean, graphql_name='isFalsePositive', default=None)),
        ('reason', sgqlc.types.Arg(String, graphql_name='reason', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
))
    )
    tags = sgqlc.types.Field(sgqlc.types.non_null(TableTagConnection), graphql_name='tags', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    versions = sgqlc.types.Field(TableSchemaVersionConnection, graphql_name='versions', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('table', sgqlc.types.Arg(ID, graphql_name='table', default=None)),
        ('version_id', sgqlc.types.Arg(String, graphql_name='versionId', default=None)),
        ('timestamp', sgqlc.types.Arg(DateTime, graphql_name='timestamp', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
))
    )
    events = sgqlc.types.Field(sgqlc.types.non_null(EventConnection), graphql_name='events', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    monitors = sgqlc.types.Field(sgqlc.types.non_null(MetricMonitoringConnection), graphql_name='monitors', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    dbt_nodes = sgqlc.types.Field(sgqlc.types.non_null(DbtNodeConnection), graphql_name='dbtNodes', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    usage_stats = sgqlc.types.Field(TableUsageStatsData, graphql_name='usageStats')
    thresholds = sgqlc.types.Field(ThresholdsData, graphql_name='thresholds')
    get_thresholds = sgqlc.types.Field(ThresholdsData, graphql_name='getThresholds')
    schema_change_count = sgqlc.types.Field(Int, graphql_name='schemaChangeCount')
    status_scalar = sgqlc.types.Field(Int, graphql_name='statusScalar')
    node_id = sgqlc.types.Field(String, graphql_name='nodeId')
    is_partial_date_range = sgqlc.types.Field(Boolean, graphql_name='isPartialDateRange', args=sgqlc.types.ArgDict((
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
))
    )
    last_updates = sgqlc.types.Field(sgqlc.types.list_of(TableUpdateTime), graphql_name='lastUpdates', args=sgqlc.types.ArgDict((
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
))
    )
    last_updates_v2 = sgqlc.types.Field(LastUpdates, graphql_name='lastUpdatesV2', args=sgqlc.types.ArgDict((
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
))
    )
    total_row_counts = sgqlc.types.Field(sgqlc.types.list_of(TableTotalRowCount), graphql_name='totalRowCounts', args=sgqlc.types.ArgDict((
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('eliminate_gaps', sgqlc.types.Arg(Boolean, graphql_name='eliminateGaps', default=None)),
))
    )
    total_byte_counts = sgqlc.types.Field(sgqlc.types.list_of(TableTotalByteCount), graphql_name='totalByteCounts', args=sgqlc.types.ArgDict((
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('eliminate_gaps', sgqlc.types.Arg(Boolean, graphql_name='eliminateGaps', default=None)),
))
    )
    write_throughput = sgqlc.types.Field(sgqlc.types.list_of(TableWriteThroughputInBytes), graphql_name='writeThroughput', args=sgqlc.types.ArgDict((
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('granularity', sgqlc.types.Arg(String, graphql_name='granularity', default=None)),
))
    )
    objects_deleted = sgqlc.types.Field(sgqlc.types.list_of(TableObjectsDeleted), graphql_name='objectsDeleted', args=sgqlc.types.ArgDict((
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('granularity', sgqlc.types.Arg(String, graphql_name='granularity', default=None)),
))
    )
    check_table_metrics_existence = sgqlc.types.Field(sgqlc.types.list_of(TableMetricExistence), graphql_name='checkTableMetricsExistence', args=sgqlc.types.ArgDict((
        ('metric_names', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='metricNames', default=None)),
))
    )
    is_muted = sgqlc.types.Field(Boolean, graphql_name='isMuted')
    table_stats = sgqlc.types.Field(TableStats, graphql_name='tableStats')
    object_properties = sgqlc.types.Field(sgqlc.types.list_of(ObjectProperty), graphql_name='objectProperties')
    is_transitioning_data_provider = sgqlc.types.Field(Boolean, graphql_name='isTransitioningDataProvider')
    table_capabilities = sgqlc.types.Field(TableCapabilitiesResponse, graphql_name='tableCapabilities')



########################################################################
# Unions
########################################################################
class RcaData(sgqlc.types.Union):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __types__ = (FieldDistRcaResult, DataProfileResult, MetricCorrelationResult, SQLQueryResult)


class UserDefinedMonitor(sgqlc.types.Union):
    """
    See source code for more info.
    """
    __schema__ = graphql_schema
    __types__ = (MetricMonitoring, CustomRule)



########################################################################
# Schema Entry Points
########################################################################
graphql_schema.query_type = Query
graphql_schema.mutation_type = Mutation
graphql_schema.subscription_type = None

