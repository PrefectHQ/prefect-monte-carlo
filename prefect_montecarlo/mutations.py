"""
This is a module containing:
Montecarlo mutation tasks

"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable

from prefect import task
from sgqlc.operation import Operation

from prefect_montecarlo import MontecarloCredentials
from prefect_montecarlo.graphql import _execute_graphql_op, _subset_return_fields
from prefect_montecarlo.schemas import graphql_schema
from prefect_montecarlo.utils import initialize_return_fields_defaults, strip_kwargs

config_dir = Path(__file__).parent.resolve() / "configs" / "mutation"
return_fields_defaults = {}
for config_path in config_dir.glob("*.json"):
    return_fields_defaults.update(
        initialize_return_fields_defaults(config_path)
    )





@task
async def create_or_update_custom_metric_rule(  # noqa
    operator: graphql_schema.CustomRuleComparisonOperator,
    custom_sql: str,
    description: str,
    dw_id: datetime,
    schedule_type: graphql_schema.ScheduleType,
    timezone: str,
    montecarlo_credentials: MontecarloCredentials,
    comparison_type: graphql_schema.ComparisonType = None,
    full_table_id: str = None,
    full_table_ids: Iterable[str] = None,
    mcon: str = None,
    field: str = None,
    metric: str = None,
    threshold: float = None,
    baseline_agg_function: graphql_schema.AggregationFunction = None,
    baseline_interval_minutes: int = None,
    is_threshold_relative: bool = None,
    threshold_lookback_minutes: int = None,
    threshold_ref: str = None,
    min_buffer: graphql_schema.ThresholdModifierInput = None,
    max_buffer: graphql_schema.ThresholdModifierInput = None,
    number_of_agg_periods: int = None,
    connection_id: datetime = None,
    custom_rule_uuid: datetime = None,
    custom_sampling_sql: str = None,
    interval_minutes: int = None,
    labels: Iterable[str] = None,
    notes: str = None,
    query_result_type: graphql_schema.QueryResultType = None,
    interval_crontab: Iterable[str] = None,
    start_time: datetime = None,
    min_interval_minutes: int = None,
    variables: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a custom metric rule.

    Args:
        operator: None.
        custom_sql: Custom SQL query to run.
        description: Description of rule.
        dw_id: Warehouse UUID.
        schedule_type: None.
        timezone: Timezone.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        comparison_type: None.
        full_table_id: None.
        full_table_ids: None.
        mcon: None.
        field: None.
        metric: None.
        threshold: None.
        baseline_agg_function: None.
        baseline_interval_minutes: None.
        is_threshold_relative: None.
        threshold_lookback_minutes: None.
        threshold_ref: None.
        min_buffer: None.
        max_buffer: None.
        number_of_agg_periods: None.
        connection_id: Specify a connection (e.g. query-engine) to use.
        custom_rule_uuid: UUID of custom rule, to update existing rule.
        custom_sampling_sql: Custom sampling SQL query to run on breach.
        interval_minutes: How often to run scheduled custom rule check
            (DEPRECATED, use schedule instead).
        labels: The monitor labels.
        notes: Additional context for the rule.
        query_result_type: How the query result is used for the metric. Uses row
            count if unset.
        interval_minutes: How often to run scheduled custom rule check
            (DEPRECATED, use schedule instead).
        interval_crontab: None.
        start_time: Start time of schedule (DEPRECATED, use schedule instead).
        min_interval_minutes: None.
        start_time: Start time of schedule (DEPRECATED, use schedule instead).
        variables: Possible variable values for SQL query.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_custom_metric_rule(
            **strip_kwargs(
                operator=operator,custom_sql=custom_sql,description=description,dw_id=dw_id,schedule_type=schedule_type,timezone=timezone,comparison_type=comparison_type,full_table_id=full_table_id,full_table_ids=full_table_ids,mcon=mcon,field=field,metric=metric,threshold=threshold,baseline_agg_function=baseline_agg_function,baseline_interval_minutes=baseline_interval_minutes,is_threshold_relative=is_threshold_relative,threshold_lookback_minutes=threshold_lookback_minutes,threshold_ref=threshold_ref,min_buffer=min_buffer,max_buffer=max_buffer,number_of_agg_periods=number_of_agg_periods,connection_id=connection_id,custom_rule_uuid=custom_rule_uuid,custom_sampling_sql=custom_sampling_sql,interval_minutes=interval_minutes,labels=labels,notes=notes,query_result_type=query_result_type,interval_crontab=interval_crontab,start_time=start_time,min_interval_minutes=min_interval_minutes,variables=variables,
            )
        )
    )

    op_stack = ("createOrUpdateCustomMetricRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateCustomMetricRule"]



@task
async def create_or_update_custom_metric_rule_custom_rule(  # noqa
    operator: graphql_schema.CustomRuleComparisonOperator,
    custom_sql: str,
    description: str,
    dw_id: datetime,
    schedule_type: graphql_schema.ScheduleType,
    timezone: str,
    montecarlo_credentials: MontecarloCredentials,
    comparison_type: graphql_schema.ComparisonType = None,
    full_table_id: str = None,
    full_table_ids: Iterable[str] = None,
    mcon: str = None,
    field: str = None,
    metric: str = None,
    threshold: float = None,
    baseline_agg_function: graphql_schema.AggregationFunction = None,
    baseline_interval_minutes: int = None,
    is_threshold_relative: bool = None,
    threshold_lookback_minutes: int = None,
    threshold_ref: str = None,
    min_buffer: graphql_schema.ThresholdModifierInput = None,
    max_buffer: graphql_schema.ThresholdModifierInput = None,
    number_of_agg_periods: int = None,
    connection_id: datetime = None,
    custom_rule_uuid: datetime = None,
    custom_sampling_sql: str = None,
    interval_minutes: int = None,
    labels: Iterable[str] = None,
    notes: str = None,
    query_result_type: graphql_schema.QueryResultType = None,
    interval_crontab: Iterable[str] = None,
    start_time: datetime = None,
    min_interval_minutes: int = None,
    variables: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a custom metric rule.

    Args:
        operator: None.
        custom_sql: Custom SQL query to run.
        description: Description of rule.
        dw_id: Warehouse UUID.
        schedule_type: None.
        timezone: Timezone.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        comparison_type: None.
        full_table_id: None.
        full_table_ids: None.
        mcon: None.
        field: None.
        metric: None.
        threshold: None.
        baseline_agg_function: None.
        baseline_interval_minutes: None.
        is_threshold_relative: None.
        threshold_lookback_minutes: None.
        threshold_ref: None.
        min_buffer: None.
        max_buffer: None.
        number_of_agg_periods: None.
        connection_id: Specify a connection
            (e.g. query-engine) to use.
        custom_rule_uuid: UUID of custom
            rule, to update existing rule.
        custom_sampling_sql: Custom sampling
            SQL query to run on breach.
        interval_minutes: How often to run
            scheduled custom rule check (DEPRECATED, use schedule
            instead).
        labels: The monitor labels.
        notes: Additional context for the
            rule.
        query_result_type: How the query
            result is used for the metric. Uses row count if unset.
        interval_minutes: How often to run scheduled custom rule check
            (DEPRECATED, use schedule instead).
        interval_crontab: None.
        start_time: Start time of schedule (DEPRECATED, use schedule instead).
        min_interval_minutes: None.
        start_time: Start time of schedule
            (DEPRECATED, use schedule instead).
        variables: Possible variable values
            for SQL query.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_custom_metric_rule(
            **strip_kwargs(
                operator=operator,custom_sql=custom_sql,description=description,dw_id=dw_id,schedule_type=schedule_type,timezone=timezone,comparison_type=comparison_type,full_table_id=full_table_id,full_table_ids=full_table_ids,mcon=mcon,field=field,metric=metric,threshold=threshold,baseline_agg_function=baseline_agg_function,baseline_interval_minutes=baseline_interval_minutes,is_threshold_relative=is_threshold_relative,threshold_lookback_minutes=threshold_lookback_minutes,threshold_ref=threshold_ref,min_buffer=min_buffer,max_buffer=max_buffer,number_of_agg_periods=number_of_agg_periods,connection_id=connection_id,custom_rule_uuid=custom_rule_uuid,custom_sampling_sql=custom_sampling_sql,interval_minutes=interval_minutes,labels=labels,notes=notes,query_result_type=query_result_type,interval_minutes=interval_minutes,interval_crontab=interval_crontab,start_time=start_time,min_interval_minutes=min_interval_minutes,start_time=start_time,variables=variables,
            )
        ).custom_rule(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createOrUpdateCustomMetricRule","customRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateCustomMetricRule"]["customRule"]




@task
async def run_sql_rule(  # noqa
    rule_uuid: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Run a SQL Rule manually.

    Args:
        rule_uuid: Rule UUID.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.run_sql_rule(
            **strip_kwargs(
                rule_uuid=rule_uuid,
            )
        )
    )

    op_stack = ("runSqlRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["runSqlRule"]




@task
async def delete_monte_carlo_config_template(  # noqa
    namespace: str,
    montecarlo_credentials: MontecarloCredentials,
    dry_run: bool = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Delete a Monte Carlo Config Template.

    Args:
        namespace: Namespace of config template.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dry_run: Dry run?.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_monte_carlo_config_template(
            **strip_kwargs(
                namespace=namespace,dry_run=dry_run,
            )
        )
    )

    op_stack = ("deleteMonteCarloConfigTemplate",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteMonteCarloConfigTemplate"]



@task
async def delete_monte_carlo_config_template_response(  # noqa
    namespace: str,
    montecarlo_credentials: MontecarloCredentials,
    dry_run: bool = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Delete a Monte Carlo Config Template.

    Args:
        namespace: Namespace of config
            template.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dry_run: Dry run?.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_monte_carlo_config_template(
            **strip_kwargs(
                namespace=namespace,dry_run=dry_run,
            )
        ).response(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("deleteMonteCarloConfigTemplate","response",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteMonteCarloConfigTemplate"]["response"]



@task
async def delete_integration_key(  # noqa
    key_id: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Delete an integration key.

    Args:
        key_id: Integration key id.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_integration_key(
            **strip_kwargs(
                key_id=key_id,
            )
        )
    )

    op_stack = ("deleteIntegrationKey",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteIntegrationKey"]



@task
async def delete_lineage_node_block_pattern(  # noqa
    uuid: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Delete a lineage node block pattern.

    Args:
        uuid: The UUID of the pattern to delete.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_lineage_node_block_pattern(
            **strip_kwargs(
                uuid=uuid,
            )
        )
    )

    op_stack = ("deleteLineageNodeBlockPattern",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteLineageNodeBlockPattern"]



@task
async def delete_lineage_node_block_pattern_pattern(  # noqa
    uuid: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Delete a lineage node block pattern.

    Args:
        uuid: The UUID of the pattern to
            delete.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_lineage_node_block_pattern(
            **strip_kwargs(
                uuid=uuid,
            )
        ).pattern(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("deleteLineageNodeBlockPattern","pattern",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteLineageNodeBlockPattern"]["pattern"]




@task
async def create_databricks_notebook_job(  # noqa
    databricks_workspace_url: str,
    databricks_workspace_id: str,
    databricks_cluster_id: str,
    databricks_token: str,
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create Databricks directory, upload the collection notebook and setup a job.

    Args:
        databricks_workspace_url: None.
        databricks_workspace_id: None.
        databricks_cluster_id: None.
        databricks_token: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_databricks_notebook_job(
            **strip_kwargs(
                databricks_workspace_url=databricks_workspace_url,databricks_workspace_id=databricks_workspace_id,databricks_cluster_id=databricks_cluster_id,databricks_token=databricks_token,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,
            )
        )
    )

    op_stack = ("createDatabricksNotebookJob",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createDatabricksNotebookJob"]



@task
async def create_databricks_notebook_job_databricks(  # noqa
    databricks_workspace_url: str,
    databricks_workspace_id: str,
    databricks_cluster_id: str,
    databricks_token: str,
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create Databricks directory, upload the collection notebook and setup a job.

    Args:
        databricks_workspace_url: None.
        databricks_workspace_id: None.
        databricks_cluster_id: None.
        databricks_token: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_databricks_notebook_job(
            **strip_kwargs(
                databricks_workspace_url=databricks_workspace_url,databricks_workspace_id=databricks_workspace_id,databricks_cluster_id=databricks_cluster_id,databricks_token=databricks_token,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,
            )
        ).databricks(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createDatabricksNotebookJob","databricks",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createDatabricksNotebookJob"]["databricks"]




@task
async def update_credentials(  # noqa
    changes: datetime,
    connection_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    should_replace: bool = False,
    should_validate: bool = True,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update credentials for a connection.

    Args:
        changes: JSON Key/values with fields to update.
        connection_id: ID for connection to update.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        should_replace: Set true to replace all credentials with changes.
            Otherwise inserts/replaces.
        should_validate: Set to true to test changes before saving.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.update_credentials(
            **strip_kwargs(
                changes=changes,connection_id=connection_id,should_replace=should_replace,should_validate=should_validate,
            )
        )
    )

    op_stack = ("updateCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["updateCredentials"]




@task
async def toggle_event_config(  # noqa
    enable: bool,
    event_type: graphql_schema.DataCollectorEventTypes,
    montecarlo_credentials: MontecarloCredentials,
    assumable_role: str = None,
    connection_id: datetime = None,
    connection_type: str = None,
    dw_id: datetime = None,
    external_id: str = None,
    format_type: str = None,
    location: str = None,
    mapping: datetime = None,
    source_format: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Enable / disable the configuration for data collection via events.

    Args:
        enable: If true enable the connection, otherwise disable it.
        event_type: Type of event (e.g. metadata).
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        assumable_role: AWS role that can be assumed by the DC.
        connection_id: The connection id. Cannot be present with DW ID.
        connection_type: Type of connection (e.g. hive-s3), required if
            connection id not set.
        dw_id: The warehouse id. Cannot be present with connection ID.
        external_id: An external id, per assumable role conditions.
        format_type: Log file format (e.g. hive-emr).
        location: Location of the log files.
        mapping: A map where keys are the attributes in the destinationschema
            and values are the keys in the source schema.
        source_format: File format (e.g. 'json').
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.toggle_event_config(
            **strip_kwargs(
                enable=enable,event_type=event_type,assumable_role=assumable_role,connection_id=connection_id,connection_type=connection_type,dw_id=dw_id,external_id=external_id,format_type=format_type,location=location,mapping=mapping,source_format=source_format,
            )
        )
    )

    op_stack = ("toggleEventConfig",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["toggleEventConfig"]




@task
async def delete_saml_identity_provider(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_saml_identity_provider(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("deleteSamlIdentityProvider",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteSamlIdentityProvider"]



@task
async def delete_saml_identity_provider_account(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_saml_identity_provider(
            **strip_kwargs(
                
            )
        ).account(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("deleteSamlIdentityProvider","account",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteSamlIdentityProvider"]["account"]



@task
async def set_incident_reaction(  # noqa
    incident_id: datetime,
    type: graphql_schema.IncidentReactionType,
    montecarlo_credentials: MontecarloCredentials,
    reasons: Iterable[graphql_schema.IncidentReactionReason] = None,
    notes: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        incident_id: The incident's UUID.
        type: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        reasons: None.
        notes: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.set_incident_reaction(
            **strip_kwargs(
                incident_id=incident_id,type=type,reasons=reasons,notes=notes,
            )
        )
    )

    op_stack = ("setIncidentReaction",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["setIncidentReaction"]



@task
async def set_incident_reaction_incident(  # noqa
    incident_id: datetime,
    type: graphql_schema.IncidentReactionType,
    montecarlo_credentials: MontecarloCredentials,
    reasons: Iterable[graphql_schema.IncidentReactionReason] = None,
    notes: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        incident_id: The incident's UUID.
        type: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        reasons: None.
        notes: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.set_incident_reaction(
            **strip_kwargs(
                incident_id=incident_id,type=type,reasons=reasons,notes=notes,
            )
        ).incident(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("setIncidentReaction","incident",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["setIncidentReaction"]["incident"]




@task
async def create_custom_rule(  # noqa
    operator: graphql_schema.CustomRuleComparisonOperator,
    description: str,
    schedule_type: graphql_schema.ScheduleType,
    timezone: str,
    montecarlo_credentials: MontecarloCredentials,
    comparison_type: graphql_schema.ComparisonType = None,
    full_table_id: str = None,
    full_table_ids: Iterable[str] = None,
    mcon: str = None,
    field: str = None,
    metric: str = None,
    threshold: float = None,
    baseline_agg_function: graphql_schema.AggregationFunction = None,
    baseline_interval_minutes: int = None,
    is_threshold_relative: bool = None,
    threshold_lookback_minutes: int = None,
    threshold_ref: str = None,
    min_buffer: graphql_schema.ThresholdModifierInput = None,
    max_buffer: graphql_schema.ThresholdModifierInput = None,
    number_of_agg_periods: int = None,
    custom_rule_uuid: datetime = None,
    dw_id: datetime = None,
    interval_minutes: int = None,
    labels: Iterable[str] = None,
    notes: str = None,
    interval_minutes: int = None,
    interval_crontab: Iterable[str] = None,
    start_time: datetime = None,
    min_interval_minutes: int = None,
    start_time: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Deprecated, use CreateOrUpdateCustomRule instead.

    Args:
        operator: None.
        description: Description of rule.
        schedule_type: None.
        timezone: Timezone.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        comparison_type: None.
        full_table_id: None.
        full_table_ids: None.
        mcon: None.
        field: None.
        metric: None.
        threshold: None.
        baseline_agg_function: None.
        baseline_interval_minutes: None.
        is_threshold_relative: None.
        threshold_lookback_minutes: None.
        threshold_ref: None.
        min_buffer: None.
        max_buffer: None.
        number_of_agg_periods: None.
        custom_rule_uuid: UUID of custom rule, to update existing rule.
        dw_id: Warehouse the tables are contained in. Required when using
            fullTableIds.
        interval_minutes: How often to run scheduled custom rule check
            (DEPRECATED, use schedule instead).
        labels: The monitor labels.
        notes: Additional context for the rule.
        interval_minutes: How often to run scheduled custom rule check
            (DEPRECATED, use schedule instead).
        interval_crontab: None.
        start_time: Start time of schedule (DEPRECATED, use schedule instead).
        min_interval_minutes: None.
        start_time: Start time of schedule (DEPRECATED, use schedule instead).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_custom_rule(
            **strip_kwargs(
                operator=operator,description=description,schedule_type=schedule_type,timezone=timezone,comparison_type=comparison_type,full_table_id=full_table_id,full_table_ids=full_table_ids,mcon=mcon,field=field,metric=metric,threshold=threshold,baseline_agg_function=baseline_agg_function,baseline_interval_minutes=baseline_interval_minutes,is_threshold_relative=is_threshold_relative,threshold_lookback_minutes=threshold_lookback_minutes,threshold_ref=threshold_ref,min_buffer=min_buffer,max_buffer=max_buffer,number_of_agg_periods=number_of_agg_periods,custom_rule_uuid=custom_rule_uuid,dw_id=dw_id,interval_minutes=interval_minutes,labels=labels,notes=notes,interval_minutes=interval_minutes,interval_crontab=interval_crontab,start_time=start_time,min_interval_minutes=min_interval_minutes,start_time=start_time,
            )
        )
    )

    op_stack = ("createCustomRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createCustomRule"]



@task
async def create_custom_rule_custom_rule(  # noqa
    operator: graphql_schema.CustomRuleComparisonOperator,
    description: str,
    schedule_type: graphql_schema.ScheduleType,
    timezone: str,
    montecarlo_credentials: MontecarloCredentials,
    comparison_type: graphql_schema.ComparisonType = None,
    full_table_id: str = None,
    full_table_ids: Iterable[str] = None,
    mcon: str = None,
    field: str = None,
    metric: str = None,
    threshold: float = None,
    baseline_agg_function: graphql_schema.AggregationFunction = None,
    baseline_interval_minutes: int = None,
    is_threshold_relative: bool = None,
    threshold_lookback_minutes: int = None,
    threshold_ref: str = None,
    min_buffer: graphql_schema.ThresholdModifierInput = None,
    max_buffer: graphql_schema.ThresholdModifierInput = None,
    number_of_agg_periods: int = None,
    custom_rule_uuid: datetime = None,
    dw_id: datetime = None,
    interval_minutes: int = None,
    labels: Iterable[str] = None,
    notes: str = None,
    interval_minutes: int = None,
    interval_crontab: Iterable[str] = None,
    start_time: datetime = None,
    min_interval_minutes: int = None,
    start_time: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Deprecated, use CreateOrUpdateCustomRule instead.

    Args:
        operator: None.
        description: Description of rule.
        schedule_type: None.
        timezone: Timezone.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        comparison_type: None.
        full_table_id: None.
        full_table_ids: None.
        mcon: None.
        field: None.
        metric: None.
        threshold: None.
        baseline_agg_function: None.
        baseline_interval_minutes: None.
        is_threshold_relative: None.
        threshold_lookback_minutes: None.
        threshold_ref: None.
        min_buffer: None.
        max_buffer: None.
        number_of_agg_periods: None.
        custom_rule_uuid: UUID of custom rule, to update
            existing rule.
        dw_id: Warehouse the tables are contained in.
            Required when using fullTableIds.
        interval_minutes: How often to run scheduled custom
            rule check (DEPRECATED, use schedule instead).
        labels: The monitor labels.
        notes: Additional context for the rule.
        interval_minutes: How often to run scheduled custom rule check
            (DEPRECATED, use schedule instead).
        interval_crontab: None.
        start_time: Start time of schedule (DEPRECATED, use schedule instead).
        min_interval_minutes: None.
        start_time: Start time of schedule (DEPRECATED, use
            schedule instead).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_custom_rule(
            **strip_kwargs(
                operator=operator,description=description,schedule_type=schedule_type,timezone=timezone,comparison_type=comparison_type,full_table_id=full_table_id,full_table_ids=full_table_ids,mcon=mcon,field=field,metric=metric,threshold=threshold,baseline_agg_function=baseline_agg_function,baseline_interval_minutes=baseline_interval_minutes,is_threshold_relative=is_threshold_relative,threshold_lookback_minutes=threshold_lookback_minutes,threshold_ref=threshold_ref,min_buffer=min_buffer,max_buffer=max_buffer,number_of_agg_periods=number_of_agg_periods,custom_rule_uuid=custom_rule_uuid,dw_id=dw_id,interval_minutes=interval_minutes,labels=labels,notes=notes,interval_minutes=interval_minutes,interval_crontab=interval_crontab,start_time=start_time,min_interval_minutes=min_interval_minutes,start_time=start_time,
            )
        ).custom_rule(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createCustomRule","customRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createCustomRule"]["customRule"]




@task
async def create_or_update_monitor(  # noqa
    schedule_type: graphql_schema.ScheduleType,
    expression: str,
    montecarlo_credentials: MontecarloCredentials,
    agg_select_expression: str = None,
    agg_time_interval: graphql_schema.MonitorAggTimeInterval = None,
    connection_id: datetime = None,
    description: str = None,
    disable_look_back_bootstrap: bool = False,
    failed_schedule_account_notification_id: datetime = None,
    fields: Iterable[str] = None,
    full_table_id: str = None,
    labels: Iterable[str] = None,
    lookback_days: int = 1,
    mcon: str = None,
    monitor_type: str = None,
    notes: str = None,
    resource_id: datetime = None,
    interval_minutes: int = None,
    interval_crontab: Iterable[str] = None,
    start_time: datetime = None,
    min_interval_minutes: int = None,
    segmented_expressions: Iterable[str] = None,
    data_type: str = None,
    time_axis_name: str = None,
    time_axis_type: str = None,
    unnest_fields: Iterable[str] = None,
    uuid: datetime = None,
    where_condition: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        schedule_type: None.
        expression: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        agg_select_expression: For dimension monitoring, the aggregation select
            expression to use (defaults to COUNT(*)).
        agg_time_interval: For field health and dimension monitoring, the
            aggregation time interval to use. Either HOUR or DAY
            (defaults to HOUR).
        connection_id: Specify a connection (e.g. query-engine) to use.
        description: Used as the name in the UI.
        disable_look_back_bootstrap: The flag decides whether to disable look
            back bootstrap for new monitors. By default, it's False.
        failed_schedule_account_notification_id: Account notification to be used
            when the monitor's scheduled executions fail.
        fields: Fields to monitor. DEPRECATED, use select_expressions instead.
        full_table_id: Deprecated - use mcon. Ignored if mcon is present.
        labels: The monitor labels.
        lookback_days: Look-back period in days (to be applied by time axis).
        mcon: Mcon of table to create monitor for.
        monitor_type: Type of monitor to create.
        notes: Additional context for the monitor.
        resource_id: Resource (e.g. warehouse) the table is contained in.
            Required when using a fullTableId.
        interval_minutes: None.
        interval_crontab: None.
        start_time: None.
        min_interval_minutes: None.
        segmented_expressions: Fields or expressions used to segment the
            monitored field (currently supports one such value).
        data_type: None.
        time_axis_name: Time axis name.
        time_axis_type: Time axis type.
        unnest_fields: Fields to unnest.
        uuid: UUID of the monitor. If specified, it means the request is for
            update.
        where_condition: SQL WHERE condition to apply to query.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_monitor(
            **strip_kwargs(
                schedule_type=schedule_type,expression=expression,agg_select_expression=agg_select_expression,agg_time_interval=agg_time_interval,connection_id=connection_id,description=description,disable_look_back_bootstrap=disable_look_back_bootstrap,failed_schedule_account_notification_id=failed_schedule_account_notification_id,fields=fields,full_table_id=full_table_id,labels=labels,lookback_days=lookback_days,mcon=mcon,monitor_type=monitor_type,notes=notes,resource_id=resource_id,interval_minutes=interval_minutes,interval_crontab=interval_crontab,start_time=start_time,min_interval_minutes=min_interval_minutes,segmented_expressions=segmented_expressions,data_type=data_type,time_axis_name=time_axis_name,time_axis_type=time_axis_type,unnest_fields=unnest_fields,uuid=uuid,where_condition=where_condition,
            )
        )
    )

    op_stack = ("createOrUpdateMonitor",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateMonitor"]



@task
async def create_or_update_monitor_monitor(  # noqa
    schedule_type: graphql_schema.ScheduleType,
    expression: str,
    montecarlo_credentials: MontecarloCredentials,
    agg_select_expression: str = None,
    agg_time_interval: graphql_schema.MonitorAggTimeInterval = None,
    connection_id: datetime = None,
    description: str = None,
    disable_look_back_bootstrap: bool = False,
    failed_schedule_account_notification_id: datetime = None,
    fields: Iterable[str] = None,
    full_table_id: str = None,
    labels: Iterable[str] = None,
    lookback_days: int = 1,
    mcon: str = None,
    monitor_type: str = None,
    notes: str = None,
    resource_id: datetime = None,
    interval_minutes: int = None,
    interval_crontab: Iterable[str] = None,
    start_time: datetime = None,
    min_interval_minutes: int = None,
    segmented_expressions: Iterable[str] = None,
    data_type: str = None,
    time_axis_name: str = None,
    time_axis_type: str = None,
    unnest_fields: Iterable[str] = None,
    uuid: datetime = None,
    where_condition: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        schedule_type: None.
        expression: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        agg_select_expression: For dimension
            monitoring, the aggregation select expression to use
            (defaults to COUNT(*)).
        agg_time_interval: For field health and
            dimension monitoring, the aggregation time interval to use.
            Either HOUR or DAY (defaults to HOUR).
        connection_id: Specify a connection (e.g.
            query-engine) to use.
        description: Used as the name in the UI.
        disable_look_back_bootstrap: The flag decides
            whether to disable look back bootstrap for new monitors. By
            default, it's False.
        failed_schedule_account_notification_id:
            Account notification to be used when the monitor's scheduled
            executions fail.
        fields: Fields to monitor. DEPRECATED, use
            select_expressions instead.
        full_table_id: Deprecated - use mcon. Ignored
            if mcon is present.
        labels: The monitor labels.
        lookback_days: Look-back period in days (to be
            applied by time axis).
        mcon: Mcon of table to create monitor for.
        monitor_type: Type of monitor to create.
        notes: Additional context for the monitor.
        resource_id: Resource (e.g. warehouse) the
            table is contained in. Required when using a fullTableId.
        interval_minutes: None.
        interval_crontab: None.
        start_time: None.
        min_interval_minutes: None.
        segmented_expressions: Fields or expressions
            used to segment the monitored field (currently supports one
            such value).
        data_type: None.
        time_axis_name: Time axis name.
        time_axis_type: Time axis type.
        unnest_fields: Fields to unnest.
        uuid: UUID of the monitor. If specified, it
            means the request is for update.
        where_condition: SQL WHERE condition to apply
            to query.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_monitor(
            **strip_kwargs(
                schedule_type=schedule_type,expression=expression,agg_select_expression=agg_select_expression,agg_time_interval=agg_time_interval,connection_id=connection_id,description=description,disable_look_back_bootstrap=disable_look_back_bootstrap,failed_schedule_account_notification_id=failed_schedule_account_notification_id,fields=fields,full_table_id=full_table_id,labels=labels,lookback_days=lookback_days,mcon=mcon,monitor_type=monitor_type,notes=notes,resource_id=resource_id,interval_minutes=interval_minutes,interval_crontab=interval_crontab,start_time=start_time,min_interval_minutes=min_interval_minutes,segmented_expressions=segmented_expressions,data_type=data_type,time_axis_name=time_axis_name,time_axis_type=time_axis_type,unnest_fields=unnest_fields,uuid=uuid,where_condition=where_condition,
            )
        ).monitor(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createOrUpdateMonitor","monitor",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateMonitor"]["monitor"]




@task
async def toggle_disable_value_ingestion(  # noqa
    disable: bool,
    dw_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Enable/disable the value ingestion feature.

    Args:
        disable: If true, disable the value ingestion feature.
        dw_id: The warehouse's UUID.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.toggle_disable_value_ingestion(
            **strip_kwargs(
                disable=disable,dw_id=dw_id,
            )
        )
    )

    op_stack = ("toggleDisableValueIngestion",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["toggleDisableValueIngestion"]




@task
async def test_s3_credentials(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    assumable_role: str = None,
    bucket: str = None,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    connection_type: str = "s3",
    external_id: str = None,
    prefix: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a s3 based connection (e.g. presto query logs on s3).

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        assumable_role: AWS role that can be assumed by the DC.
        bucket: S3 Bucket where relevant objects are contained.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        connection_type: Type of connection.
        external_id: An external id, per assumable role conditions.
        prefix: Path to objects.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_s3_credentials(
            **strip_kwargs(
                assumable_role=assumable_role,bucket=bucket,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,connection_type=connection_type,external_id=external_id,prefix=prefix,
            )
        )
    )

    op_stack = ("testS3Credentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testS3Credentials"]




@task
async def set_incident_severity(  # noqa
    incident_id: datetime,
    severity: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Set severity for an existing incident.

    Args:
        incident_id: The incident's UUID.
        severity: Incident severity to set.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.set_incident_severity(
            **strip_kwargs(
                incident_id=incident_id,severity=severity,
            )
        )
    )

    op_stack = ("setIncidentSeverity",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["setIncidentSeverity"]



@task
async def set_incident_severity_incident(  # noqa
    incident_id: datetime,
    severity: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Set severity for an existing incident.

    Args:
        incident_id: The incident's UUID.
        severity: Incident severity to set.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.set_incident_severity(
            **strip_kwargs(
                incident_id=incident_id,severity=severity,
            )
        ).incident(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("setIncidentSeverity","incident",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["setIncidentSeverity"]["incident"]




@task
async def test_dbt_cloud_credentials(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    dbt_cloud_account_id: str = None,
    dbt_cloud_api_token: str = None,
    dbt_cloud_base_url: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a dbt Cloud connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        dbt_cloud_account_id: dbt Cloud account ID.
        dbt_cloud_api_token: dbt Cloud API token.
        dbt_cloud_base_url: dbt Cloud base URL.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_dbt_cloud_credentials(
            **strip_kwargs(
                dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,dbt_cloud_account_id=dbt_cloud_account_id,dbt_cloud_api_token=dbt_cloud_api_token,dbt_cloud_base_url=dbt_cloud_base_url,
            )
        )
    )

    op_stack = ("testDbtCloudCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testDbtCloudCredentials"]




@task
async def create_or_update_incident_comment(  # noqa
    comment: str,
    incident_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    comment_id: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Creates or updates a comment on an incident.

    Args:
        comment: Content of the comment.
        incident_id: The incident's UUID.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        comment_id: UUID of the comment. If set, this call is for updating the
            comment.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_incident_comment(
            **strip_kwargs(
                comment=comment,incident_id=incident_id,comment_id=comment_id,
            )
        )
    )

    op_stack = ("createOrUpdateIncidentComment",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateIncidentComment"]



@task
async def create_or_update_incident_comment_comment_event(  # noqa
    comment: str,
    incident_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    comment_id: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Creates or updates a comment on an incident.

    Args:
        comment: Content of the comment.
        incident_id: The incident's UUID.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        comment_id: UUID of the comment. If
            set, this call is for updating the comment.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_incident_comment(
            **strip_kwargs(
                comment=comment,incident_id=incident_id,comment_id=comment_id,
            )
        ).comment_event(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createOrUpdateIncidentComment","commentEvent",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateIncidentComment"]["commentEvent"]




@task
async def save_slack_credentials(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    key: str = None,
    slack_app_type: graphql_schema.SlackAppType = None,
    slack_installation_uuid: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        key: Slack installation UUID (deprecated, use slackInstallationUuid.
        slack_app_type: Slack App Type.
        slack_installation_uuid: Slack installation UUID.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.save_slack_credentials(
            **strip_kwargs(
                key=key,slack_app_type=slack_app_type,slack_installation_uuid=slack_installation_uuid,
            )
        )
    )

    op_stack = ("saveSlackCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["saveSlackCredentials"]



@task
async def save_slack_credentials_slack_credentials(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    key: str = None,
    slack_app_type: graphql_schema.SlackAppType = None,
    slack_installation_uuid: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        key: Slack installation UUID (deprecated, use
            slackInstallationUuid.
        slack_app_type: Slack App Type.
        slack_installation_uuid: Slack installation UUID.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.save_slack_credentials(
            **strip_kwargs(
                key=key,slack_app_type=slack_app_type,slack_installation_uuid=slack_installation_uuid,
            )
        ).slack_credentials(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("saveSlackCredentials","slackCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["saveSlackCredentials"]["slackCredentials"]



@task
async def create_access_token(  # noqa
    expiration_in_days: int,
    montecarlo_credentials: MontecarloCredentials,
    comment: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Generate an API Access Token and associate to user.

    Args:
        expiration_in_days: Number of days before the token auto expires.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        comment: Any comment or description to help identify the token.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_access_token(
            **strip_kwargs(
                expiration_in_days=expiration_in_days,comment=comment,
            )
        )
    )

    op_stack = ("createAccessToken",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createAccessToken"]



@task
async def create_access_token_access_token(  # noqa
    expiration_in_days: int,
    montecarlo_credentials: MontecarloCredentials,
    comment: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Generate an API Access Token and associate to user.

    Args:
        expiration_in_days: Number of days before the token
            auto expires.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        comment: Any comment or description to help identify
            the token.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_access_token(
            **strip_kwargs(
                expiration_in_days=expiration_in_days,comment=comment,
            )
        ).access_token(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createAccessToken","accessToken",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createAccessToken"]["accessToken"]



@task
async def create_databricks_secret(  # noqa
    databricks_workspace_url: str,
    databricks_workspace_id: str,
    databricks_cluster_id: str,
    databricks_token: str,
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    scope_name: str = None,
    scope_principal: str = None,
    secret_name: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create Databricks scope and secret for an integration key.

    Args:
        databricks_workspace_url: None.
        databricks_workspace_id: None.
        databricks_cluster_id: None.
        databricks_token: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        scope_name: Override default scope name from DC.
        scope_principal: Override default principal name from DC.
        secret_name: Override default secret name from DC.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_databricks_secret(
            **strip_kwargs(
                databricks_workspace_url=databricks_workspace_url,databricks_workspace_id=databricks_workspace_id,databricks_cluster_id=databricks_cluster_id,databricks_token=databricks_token,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,scope_name=scope_name,scope_principal=scope_principal,secret_name=secret_name,
            )
        )
    )

    op_stack = ("createDatabricksSecret",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createDatabricksSecret"]




@task
async def invite_users_v2(  # noqa
    auth_groups: Iterable[str],
    emails: Iterable[str],
    montecarlo_credentials: MontecarloCredentials,
    invitation_type: graphql_schema.InvitationType = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Invite users to the account.

    Args:
        auth_groups: Names of groups to add user to upon acceptance.
        emails: List of email addresses to invite.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        invitation_type: Type of invitation to send--typically maps to product.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.invite_users_v2(
            **strip_kwargs(
                auth_groups=auth_groups,emails=emails,invitation_type=invitation_type,
            )
        )
    )

    op_stack = ("inviteUsersV2",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["inviteUsersV2"]



@task
async def invite_users_v2_invites(  # noqa
    auth_groups: Iterable[str],
    emails: Iterable[str],
    montecarlo_credentials: MontecarloCredentials,
    invitation_type: graphql_schema.InvitationType = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Invite users to the account.

    Args:
        auth_groups: Names of groups to add user to upon
            acceptance.
        emails: List of email addresses to invite.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        invitation_type: Type of invitation to send--typically
            maps to product.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.invite_users_v2(
            **strip_kwargs(
                auth_groups=auth_groups,emails=emails,invitation_type=invitation_type,
            )
        ).invites(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("inviteUsersV2","invites",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["inviteUsersV2"]["invites"]



@task
async def add_connection(  # noqa
    connection_type: str,
    key: str,
    montecarlo_credentials: MontecarloCredentials,
    create_warehouse_type: str = None,
    dc_id: datetime = None,
    dw_id: datetime = None,
    job_limits: datetime = None,
    job_types: Iterable[str] = None,
    name: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Add a connection and setup any associated jobs. Creates a warehouse if not
    specified.

    Args:
        connection_type: The type of connection to add.
        key: Temp key from testing connections.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        create_warehouse_type: Create a new warehouse for the connection.
        dc_id: DC UUID. To disambiguate accounts with multiple collectors.
        dw_id: Add connection to an existing warehouse.
        job_limits: Customize job operations for all job types.
        job_types: Specify job types for the connection. Uses connection default
            otherwise.
        name: Provide a friendly name for the warehouse when creating.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.add_connection(
            **strip_kwargs(
                connection_type=connection_type,key=key,create_warehouse_type=create_warehouse_type,dc_id=dc_id,dw_id=dw_id,job_limits=job_limits,job_types=job_types,name=name,
            )
        )
    )

    op_stack = ("addConnection",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["addConnection"]



@task
async def add_connection_connection(  # noqa
    connection_type: str,
    key: str,
    montecarlo_credentials: MontecarloCredentials,
    create_warehouse_type: str = None,
    dc_id: datetime = None,
    dw_id: datetime = None,
    job_limits: datetime = None,
    job_types: Iterable[str] = None,
    name: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Add a connection and setup any associated jobs. Creates a warehouse if not
    specified.

    Args:
        connection_type: The type of connection to add.
        key: Temp key from testing connections.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        create_warehouse_type: Create a new warehouse for the
            connection.
        dc_id: DC UUID. To disambiguate accounts with multiple
            collectors.
        dw_id: Add connection to an existing warehouse.
        job_limits: Customize job operations for all job types.
        job_types: Specify job types for the connection. Uses
            connection default otherwise.
        name: Provide a friendly name for the warehouse when
            creating.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.add_connection(
            **strip_kwargs(
                connection_type=connection_type,key=key,create_warehouse_type=create_warehouse_type,dc_id=dc_id,dw_id=dw_id,job_limits=job_limits,job_types=job_types,name=name,
            )
        ).connection(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("addConnection","connection",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["addConnection"]["connection"]




@task
async def delete_user_invite(  # noqa
    emails: Iterable[str],
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Delete user invite.

    Args:
        emails: List of email addresses to invite.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_user_invite(
            **strip_kwargs(
                emails=emails,
            )
        )
    )

    op_stack = ("deleteUserInvite",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteUserInvite"]



@task
async def add_tableau_account(  # noqa
    server_name: str,
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    password: str = None,
    site_name: str = None,
    token_name: str = None,
    token_value: str = None,
    username: str = None,
    verify_ssl: bool = True,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Add Tableau credentials to the account.

    Args:
        server_name: The Tableau server name.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: DC UUID. To disambiguate accounts with multiple collectors.
        password: Password for the Tableau user if using username/password.
        site_name: The Tableau site name.
        token_name: The personal access token name.
        token_value: The personal access token value.
        username: Username for the Tableau user if using username/password.
        verify_ssl: Whether to verify the SSL connection to Tableau server.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.add_tableau_account(
            **strip_kwargs(
                server_name=server_name,dc_id=dc_id,password=password,site_name=site_name,token_name=token_name,token_value=token_value,username=username,verify_ssl=verify_ssl,
            )
        )
    )

    op_stack = ("addTableauAccount",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["addTableauAccount"]



@task
async def add_tableau_account_tableau_account(  # noqa
    server_name: str,
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    password: str = None,
    site_name: str = None,
    token_name: str = None,
    token_value: str = None,
    username: str = None,
    verify_ssl: bool = True,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Add Tableau credentials to the account.

    Args:
        server_name: The Tableau server name.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: DC UUID. To disambiguate accounts with
            multiple collectors.
        password: Password for the Tableau user if using
            username/password.
        site_name: The Tableau site name.
        token_name: The personal access token name.
        token_value: The personal access token value.
        username: Username for the Tableau user if using
            username/password.
        verify_ssl: Whether to verify the SSL connection to
            Tableau server.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.add_tableau_account(
            **strip_kwargs(
                server_name=server_name,dc_id=dc_id,password=password,site_name=site_name,token_name=token_name,token_value=token_value,username=username,verify_ssl=verify_ssl,
            )
        ).tableau_account(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("addTableauAccount","tableauAccount",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["addTableauAccount"]["tableauAccount"]




@task
async def delete_event_onboarding_data(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Delete stored event onboarding configuration.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_event_onboarding_data(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("deleteEventOnboardingData",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteEventOnboardingData"]



@task
async def invite_users(  # noqa
    emails: Iterable[str],
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    DEPRECATED: use inviteUsersV2.

    Args:
        emails: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op
        .invite_users(
            **strip_kwargs(
                input=dict(
                    emails=emails,
                )
            )
        )
    )

    op_stack = ("inviteUsers",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["inviteUsers"]



@task
async def create_or_update_saml_identity_provider(  # noqa
    domains: Iterable[str],
    montecarlo_credentials: MontecarloCredentials,
    default_authorization_groups: Iterable[str] = None,
    metadata: str = None,
    metadata_url: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        domains: A list of domains authorized by the IdP.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        default_authorization_groups: One or more authorization group names to
            assign to new SSO users who do not have an invite. If
            none/not set, it means new users must wait to be assigned
            group to gain any access.
        metadata: The metadata in XML format, encoded as base64.
        metadata_url: The URL of the metadata file.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_saml_identity_provider(
            **strip_kwargs(
                domains=domains,default_authorization_groups=default_authorization_groups,metadata=metadata,metadata_url=metadata_url,
            )
        )
    )

    op_stack = ("createOrUpdateSamlIdentityProvider",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateSamlIdentityProvider"]



@task
async def create_or_update_saml_identity_provider_account(  # noqa
    domains: Iterable[str],
    montecarlo_credentials: MontecarloCredentials,
    default_authorization_groups: Iterable[str] = None,
    metadata: str = None,
    metadata_url: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        domains: A list of domains
            authorized by the IdP.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        default_authorization_groups:
            One or more authorization group names to assign to new SSO
            users who do not have an invite. If none/not set, it means
            new users must wait to be assigned group to gain any access.
        metadata: The metadata in XML
            format, encoded as base64.
        metadata_url: The URL of the
            metadata file.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_saml_identity_provider(
            **strip_kwargs(
                domains=domains,default_authorization_groups=default_authorization_groups,metadata=metadata,metadata_url=metadata_url,
            )
        ).account(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createOrUpdateSamlIdentityProvider","account",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateSamlIdentityProvider"]["account"]



@task
async def trigger_custom_rule(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    custom_sql_contains: str = None,
    description_contains: str = None,
    rule_id: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Run a custom rule immediately.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        custom_sql_contains: String to completely or partially match the rule
            SQL, case-insensitive.
        description_contains: String to completely or partially match the rule
            description, case-insensitive.
        rule_id: Rule id.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.trigger_custom_rule(
            **strip_kwargs(
                custom_sql_contains=custom_sql_contains,description_contains=description_contains,rule_id=rule_id,
            )
        )
    )

    op_stack = ("triggerCustomRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["triggerCustomRule"]



@task
async def trigger_custom_rule_custom_rule(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    custom_sql_contains: str = None,
    description_contains: str = None,
    rule_id: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Run a custom rule immediately.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        custom_sql_contains: String to completely or
            partially match the rule SQL, case-insensitive.
        description_contains: String to completely or
            partially match the rule description, case-insensitive.
        rule_id: Rule id.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.trigger_custom_rule(
            **strip_kwargs(
                custom_sql_contains=custom_sql_contains,description_contains=description_contains,rule_id=rule_id,
            )
        ).custom_rule(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("triggerCustomRule","customRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["triggerCustomRule"]["customRule"]




@task
async def delete_domain(  # noqa
    uuid: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Delete a domain.

    Args:
        uuid: UUID of domain to delete.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_domain(
            **strip_kwargs(
                uuid=uuid,
            )
        )
    )

    op_stack = ("deleteDomain",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteDomain"]




@task
async def create_or_update_lineage_node_block_pattern(  # noqa
    resource_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    dataset_regexp: str = None,
    project_regexp: str = None,
    table_regexp: str = None,
    uuid: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a node block pattern.

    Args:
        resource_id: The id of the resource containing the node.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dataset_regexp: Block datasets matching the regexp.
        project_regexp: Block projects matching the regexp.
        table_regexp: Block tables matching the regexp.
        uuid: The pattern UUID (updates only).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_lineage_node_block_pattern(
            **strip_kwargs(
                resource_id=resource_id,dataset_regexp=dataset_regexp,project_regexp=project_regexp,table_regexp=table_regexp,uuid=uuid,
            )
        )
    )

    op_stack = ("createOrUpdateLineageNodeBlockPattern",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateLineageNodeBlockPattern"]



@task
async def create_or_update_lineage_node_block_pattern_pattern(  # noqa
    resource_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    dataset_regexp: str = None,
    project_regexp: str = None,
    table_regexp: str = None,
    uuid: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a node block pattern.

    Args:
        resource_id: The id of the
            resource containing the node.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dataset_regexp: Block
            datasets matching the regexp.
        project_regexp: Block
            projects matching the regexp.
        table_regexp: Block tables
            matching the regexp.
        uuid: The pattern UUID
            (updates only).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_lineage_node_block_pattern(
            **strip_kwargs(
                resource_id=resource_id,dataset_regexp=dataset_regexp,project_regexp=project_regexp,table_regexp=table_regexp,uuid=uuid,
            )
        ).pattern(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createOrUpdateLineageNodeBlockPattern","pattern",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateLineageNodeBlockPattern"]["pattern"]




@task
async def test_looker_credentials(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    base_url: str = None,
    client_id: str = None,
    client_secret: str = None,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    verify_ssl: bool = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a Looker API connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        base_url: Host url.
        client_id: Looker client id.
        client_secret: Looker client secret.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        verify_ssl: Verify SSL (uncheck for self-signed certs).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_looker_credentials(
            **strip_kwargs(
                base_url=base_url,client_id=client_id,client_secret=client_secret,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,verify_ssl=verify_ssl,
            )
        )
    )

    op_stack = ("testLookerCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testLookerCredentials"]




@task
async def create_or_update_notification_setting(  # noqa
    digest_type: str,
    notification_type: str,
    montecarlo_credentials: MontecarloCredentials,
    anomaly_types: Iterable[str] = None,
    custom_message: str = None,
    start_time: datetime = None,
    interval_minutes: int = None,
    dry: bool = False,
    slack_is_private: bool = None,
    webhook_shared_secret: str = None,
    webhook_encrypted_secret: str = None,
    priority: str = None,
    url: str = None,
    username: str = None,
    password: str = None,
    dc_proxy: bool = None,
    incident_sub_types: Iterable[graphql_schema.IncidentSubType] = None,
    notification_schedule_type: str = None,
    recipient: str = None,
    recipients: Iterable[str] = None,
    project_names: Iterable[str] = None,
    dataset_ids: Iterable[datetime] = None,
    full_table_ids: Iterable[str] = None,
    rule_ids: Iterable[datetime] = None,
    domain_ids: Iterable[datetime] = None,
    tag_keys: Iterable[str] = None,
    tag_key_values: Iterable[graphql_schema.NotificationTagPairs] = None,
    table_stats_rules: graphql_schema.TableStatsRules = None,
    monitor_labels: Iterable[datetime] = None,
    exclude_project_names: Iterable[str] = None,
    exclude_dataset_ids: Iterable[datetime] = None,
    exclude_full_table_ids: Iterable[str] = None,
    exclude_tag_keys: Iterable[str] = None,
    exclude_tag_key_values: Iterable[graphql_schema.NotificationTagPairs] = None,
    table_regex: str = None,
    setting_id: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a notification setting.

    Args:
        digest_type: None.
        notification_type: Specify the notification integration to use.
            Supported options include: email, mattermost, opsgenie,
            pagerduty, slack, slack_v2, webhook, msteams, alation.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        anomaly_types: Limit notifications to specific incident types
            (default=all). Supported options include: anomalies,
            schema_changes, deleted_tables, metric_anomalies,
            custom_rule_anomalies, performance_anomalies, dbt_errors,
            pseudo_integration_test.
        custom_message: A custom message to be sent with triggered notification.
        start_time: None.
        interval_minutes: None.
        dry: Test destination is reachable by sending a sample alert. Note -
            setting is not saved and rules are not evaluated.
        slack_is_private: None.
        webhook_shared_secret: None.
        webhook_encrypted_secret: None.
        priority: None.
        url: None.
        username: None.
        password: None.
        dc_proxy: None.
        incident_sub_types: Limit notifications to specific incident sub types
            (default=all).
        notification_schedule_type: Specify the notification schedule type.
            Supported values: realtime, digest, backup_or_failure.
        recipient: Deprecated.
        recipients: Destination to send notifications to.
        project_names: None.
        dataset_ids: None.
        full_table_ids: None.
        rule_ids: None.
        domain_ids: None.
        tag_keys: None.
        tag_key_values: None.
        table_stats_rules: None.
        monitor_labels: None.
        exclude_project_names: None.
        exclude_dataset_ids: None.
        exclude_full_table_ids: None.
        exclude_tag_keys: None.
        exclude_tag_key_values: None.
        table_regex: None.
        setting_id: For updating a notification setting.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_notification_setting(
            **strip_kwargs(
                digest_type=digest_type,notification_type=notification_type,anomaly_types=anomaly_types,custom_message=custom_message,start_time=start_time,interval_minutes=interval_minutes,dry=dry,slack_is_private=slack_is_private,webhook_shared_secret=webhook_shared_secret,webhook_encrypted_secret=webhook_encrypted_secret,priority=priority,url=url,username=username,password=password,dc_proxy=dc_proxy,incident_sub_types=incident_sub_types,notification_schedule_type=notification_schedule_type,recipient=recipient,recipients=recipients,project_names=project_names,dataset_ids=dataset_ids,full_table_ids=full_table_ids,rule_ids=rule_ids,domain_ids=domain_ids,tag_keys=tag_keys,tag_key_values=tag_key_values,table_stats_rules=table_stats_rules,monitor_labels=monitor_labels,exclude_project_names=exclude_project_names,exclude_dataset_ids=exclude_dataset_ids,exclude_full_table_ids=exclude_full_table_ids,exclude_tag_keys=exclude_tag_keys,exclude_tag_key_values=exclude_tag_key_values,table_regex=table_regex,setting_id=setting_id,
            )
        )
    )

    op_stack = ("createOrUpdateNotificationSetting",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateNotificationSetting"]



@task
async def create_or_update_notification_setting_notification_setting(  # noqa
    digest_type: str,
    notification_type: str,
    montecarlo_credentials: MontecarloCredentials,
    anomaly_types: Iterable[str] = None,
    custom_message: str = None,
    start_time: datetime = None,
    interval_minutes: int = None,
    dry: bool = False,
    slack_is_private: bool = None,
    webhook_shared_secret: str = None,
    webhook_encrypted_secret: str = None,
    priority: str = None,
    url: str = None,
    username: str = None,
    password: str = None,
    dc_proxy: bool = None,
    incident_sub_types: Iterable[graphql_schema.IncidentSubType] = None,
    notification_schedule_type: str = None,
    recipient: str = None,
    recipients: Iterable[str] = None,
    project_names: Iterable[str] = None,
    dataset_ids: Iterable[datetime] = None,
    full_table_ids: Iterable[str] = None,
    rule_ids: Iterable[datetime] = None,
    domain_ids: Iterable[datetime] = None,
    tag_keys: Iterable[str] = None,
    tag_key_values: Iterable[graphql_schema.NotificationTagPairs] = None,
    table_stats_rules: graphql_schema.TableStatsRules = None,
    monitor_labels: Iterable[datetime] = None,
    exclude_project_names: Iterable[str] = None,
    exclude_dataset_ids: Iterable[datetime] = None,
    exclude_full_table_ids: Iterable[str] = None,
    exclude_tag_keys: Iterable[str] = None,
    exclude_tag_key_values: Iterable[graphql_schema.NotificationTagPairs] = None,
    table_regex: str = None,
    setting_id: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a notification setting.

    Args:
        digest_type: None.
        notification_type: Specify the
            notification integration to use. Supported options include:
            email, mattermost, opsgenie, pagerduty, slack, slack_v2,
            webhook, msteams, alation.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        anomaly_types: Limit notifications
            to specific incident types (default=all). Supported options
            include: anomalies, schema_changes, deleted_tables,
            metric_anomalies, custom_rule_anomalies,
            performance_anomalies, dbt_errors, pseudo_integration_test.
        custom_message: A custom message
            to be sent with triggered notification.
        start_time: None.
        interval_minutes: None.
        dry: Test destination is reachable
            by sending a sample alert. Note - setting is not saved and
            rules are not evaluated.
        slack_is_private: None.
        webhook_shared_secret: None.
        webhook_encrypted_secret: None.
        priority: None.
        url: None.
        username: None.
        password: None.
        dc_proxy: None.
        incident_sub_types: Limit
            notifications to specific incident sub types (default=all).
        notification_schedule_type:
            Specify the notification schedule type. Supported values:
            realtime, digest, backup_or_failure.
        recipient: Deprecated.
        recipients: Destination to send
            notifications to.
        project_names: None.
        dataset_ids: None.
        full_table_ids: None.
        rule_ids: None.
        domain_ids: None.
        tag_keys: None.
        tag_key_values: None.
        table_stats_rules: None.
        monitor_labels: None.
        exclude_project_names: None.
        exclude_dataset_ids: None.
        exclude_full_table_ids: None.
        exclude_tag_keys: None.
        exclude_tag_key_values: None.
        table_regex: None.
        setting_id: For updating a
            notification setting.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_notification_setting(
            **strip_kwargs(
                digest_type=digest_type,notification_type=notification_type,anomaly_types=anomaly_types,custom_message=custom_message,start_time=start_time,interval_minutes=interval_minutes,dry=dry,slack_is_private=slack_is_private,webhook_shared_secret=webhook_shared_secret,webhook_encrypted_secret=webhook_encrypted_secret,priority=priority,url=url,username=username,password=password,dc_proxy=dc_proxy,incident_sub_types=incident_sub_types,notification_schedule_type=notification_schedule_type,recipient=recipient,recipients=recipients,project_names=project_names,dataset_ids=dataset_ids,full_table_ids=full_table_ids,rule_ids=rule_ids,domain_ids=domain_ids,tag_keys=tag_keys,tag_key_values=tag_key_values,table_stats_rules=table_stats_rules,monitor_labels=monitor_labels,exclude_project_names=exclude_project_names,exclude_dataset_ids=exclude_dataset_ids,exclude_full_table_ids=exclude_full_table_ids,exclude_tag_keys=exclude_tag_keys,exclude_tag_key_values=exclude_tag_key_values,table_regex=table_regex,setting_id=setting_id,
            )
        ).notification_setting(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createOrUpdateNotificationSetting","notificationSetting",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateNotificationSetting"]["notificationSetting"]




@task
async def create_or_update_resource(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    is_default: bool = None,
    name: str = None,
    type: str = None,
    uuid: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a resource.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        is_default: If the account's default resource.
        name: The resource name.
        type: The resource type.
        uuid: The resource id.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_resource(
            **strip_kwargs(
                is_default=is_default,name=name,type=type,uuid=uuid,
            )
        )
    )

    op_stack = ("createOrUpdateResource",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateResource"]



@task
async def create_or_update_resource_resource(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    is_default: bool = None,
    name: str = None,
    type: str = None,
    uuid: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a resource.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        is_default: If the account's default resource.
        name: The resource name.
        type: The resource type.
        uuid: The resource id.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_resource(
            **strip_kwargs(
                is_default=is_default,name=name,type=type,uuid=uuid,
            )
        ).resource(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createOrUpdateResource","resource",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateResource"]["resource"]




@task
async def pause_monitor(  # noqa
    pause: bool,
    uuid: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Pause a monitor from collecting data.'.

    Args:
        pause: Pause state of the monitor.
        uuid: UUID of the monitor whose skip status is being changed.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.pause_monitor(
            **strip_kwargs(
                pause=pause,uuid=uuid,
            )
        )
    )

    op_stack = ("pauseMonitor",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["pauseMonitor"]



@task
async def pause_monitor_monitor(  # noqa
    pause: bool,
    uuid: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Pause a monitor from collecting data.'.

    Args:
        pause: Pause state of the monitor.
        uuid: UUID of the monitor whose skip status is being
            changed.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.pause_monitor(
            **strip_kwargs(
                pause=pause,uuid=uuid,
            )
        ).monitor(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("pauseMonitor","monitor",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["pauseMonitor"]["monitor"]




@task
async def trigger_monitor(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    full_table_id: str = None,
    mcon: str = None,
    monitor_type: str = None,
    resource_id: datetime = None,
    uuid: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Run a monitor immediately.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        full_table_id: Deprecated - use mcon. Ignored if mcon is present.
        mcon: Trigger monitor by mcon.
        monitor_type: Specify the monitor type. Required when using an mcon or
            full table id.
        resource_id: Specify the resource uuid (e.g. warehouse the table is
            contained in) when using a fullTableId.
        uuid: Trigger monitor by a UUID.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.trigger_monitor(
            **strip_kwargs(
                full_table_id=full_table_id,mcon=mcon,monitor_type=monitor_type,resource_id=resource_id,uuid=uuid,
            )
        )
    )

    op_stack = ("triggerMonitor",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["triggerMonitor"]



@task
async def trigger_monitor_monitor(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    full_table_id: str = None,
    mcon: str = None,
    monitor_type: str = None,
    resource_id: datetime = None,
    uuid: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Run a monitor immediately.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        full_table_id: Deprecated - use mcon. Ignored if mcon is
            present.
        mcon: Trigger monitor by mcon.
        monitor_type: Specify the monitor type. Required when
            using an mcon or full table id.
        resource_id: Specify the resource uuid (e.g. warehouse
            the table is contained in) when using a fullTableId.
        uuid: Trigger monitor by a UUID.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.trigger_monitor(
            **strip_kwargs(
                full_table_id=full_table_id,mcon=mcon,monitor_type=monitor_type,resource_id=resource_id,uuid=uuid,
            )
        ).monitor(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("triggerMonitor","monitor",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["triggerMonitor"]["monitor"]




@task
async def test_looker_git_clone_credentials(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    repo_url: str = None,
    ssh_key: str = None,
    token: str = None,
    username: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test the connection to a Git repository using the SSH or HTTPS protocol.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        repo_url: Repository URL as ssh://[user@]server/project.git or the
            shorter form [user@]server:project.git SSH integrations and
            htts://server/project.git for HTTPS integrations.
        ssh_key: SSH key, base64-encoded.
        token: The access token for git HTTPS integrations.
        username: The git username for BitBucket integrations.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_looker_git_clone_credentials(
            **strip_kwargs(
                dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,repo_url=repo_url,ssh_key=ssh_key,token=token,username=username,
            )
        )
    )

    op_stack = ("testLookerGitCloneCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testLookerGitCloneCredentials"]




@task
async def test_databricks_credentials(  # noqa
    databricks_workspace_url: str,
    databricks_workspace_id: str,
    databricks_cluster_id: str,
    databricks_token: str,
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a Databricks connection.

    Args:
        databricks_workspace_url: None.
        databricks_workspace_id: None.
        databricks_cluster_id: None.
        databricks_token: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_databricks_credentials(
            **strip_kwargs(
                databricks_workspace_url=databricks_workspace_url,databricks_workspace_id=databricks_workspace_id,databricks_cluster_id=databricks_cluster_id,databricks_token=databricks_token,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,
            )
        )
    )

    op_stack = ("testDatabricksCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testDatabricksCredentials"]




@task
async def create_or_update_monte_carlo_config_template(  # noqa
    config_template_json: str,
    namespace: str,
    montecarlo_credentials: MontecarloCredentials,
    dry_run: bool = None,
    resource: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a Monte Carlo Config Template.

    Args:
        config_template_json: Monte Carlo Template in JSON format.
        namespace: Namespace of config template.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dry_run: Dry run?.
        resource: Default resource (warehouse) ID or name.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_monte_carlo_config_template(
            **strip_kwargs(
                config_template_json=config_template_json,namespace=namespace,dry_run=dry_run,resource=resource,
            )
        )
    )

    op_stack = ("createOrUpdateMonteCarloConfigTemplate",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateMonteCarloConfigTemplate"]



@task
async def create_or_update_monte_carlo_config_template_response(  # noqa
    config_template_json: str,
    namespace: str,
    montecarlo_credentials: MontecarloCredentials,
    dry_run: bool = None,
    resource: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a Monte Carlo Config Template.

    Args:
        config_template_json: Monte
            Carlo Template in JSON format.
        namespace: Namespace of
            config template.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dry_run: Dry run?.
        resource: Default resource
            (warehouse) ID or name.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_monte_carlo_config_template(
            **strip_kwargs(
                config_template_json=config_template_json,namespace=namespace,dry_run=dry_run,resource=resource,
            )
        ).response(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createOrUpdateMonteCarloConfigTemplate","response",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateMonteCarloConfigTemplate"]["response"]



@task
async def create_or_update_catalog_object_metadata(  # noqa
    description: str,
    mcon: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update catalog object metadata.

    Args:
        description: Description of object.
        mcon: Monte Carlo full identifier for an entity.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_catalog_object_metadata(
            **strip_kwargs(
                description=description,mcon=mcon,
            )
        )
    )

    op_stack = ("createOrUpdateCatalogObjectMetadata",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateCatalogObjectMetadata"]



@task
async def create_or_update_catalog_object_metadata_catalog_object_metadata(  # noqa
    description: str,
    mcon: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update catalog object metadata.

    Args:
        description: Description of
            object.
        mcon: Monte Carlo full
            identifier for an entity.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_catalog_object_metadata(
            **strip_kwargs(
                description=description,mcon=mcon,
            )
        ).catalog_object_metadata(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createOrUpdateCatalogObjectMetadata","catalogObjectMetadata",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateCatalogObjectMetadata"]["catalogObjectMetadata"]



@task
async def create_dbt_project(  # noqa
    project_name: str,
    source: graphql_schema.DbtProjectSource,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create a DBT project.

    Args:
        project_name: dbt project name.
        source: Source of project (cli or dbt-cloud).
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_dbt_project(
            **strip_kwargs(
                project_name=project_name,source=source,
            )
        )
    )

    op_stack = ("createDbtProject",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createDbtProject"]



@task
async def create_dbt_project_dbt_project(  # noqa
    project_name: str,
    source: graphql_schema.DbtProjectSource,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create a DBT project.

    Args:
        project_name: dbt project name.
        source: Source of project (cli or dbt-cloud).
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_dbt_project(
            **strip_kwargs(
                project_name=project_name,source=source,
            )
        ).dbt_project(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createDbtProject","dbtProject",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createDbtProject"]["dbtProject"]



@task
async def set_account_name(  # noqa
    account_name: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        account_name: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.set_account_name(
            **strip_kwargs(
                account_name=account_name,
            )
        )
    )

    op_stack = ("setAccountName",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["setAccountName"]



@task
async def set_account_name_account(  # noqa
    account_name: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        account_name: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.set_account_name(
            **strip_kwargs(
                account_name=account_name,
            )
        ).account(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("setAccountName","account",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["setAccountName"]["account"]



@task
async def update_slack_channels(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update the slack channels cache for the account.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.update_slack_channels(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("updateSlackChannels",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["updateSlackChannels"]



@task
async def delete_object_property(  # noqa
    mcon_id: str,
    property_name: str,
    montecarlo_credentials: MontecarloCredentials,
    property_source_type: str = "dashboard",
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Delete properties (tags) for objects (e.g. tables, fields, etc.).

    Args:
        mcon_id: Monte Carlo full identifier for an entity.
        property_name: Name of the property (AKA tag key).
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        property_source_type: Where property originated.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_object_property(
            **strip_kwargs(
                mcon_id=mcon_id,property_name=property_name,property_source_type=property_source_type,
            )
        )
    )

    op_stack = ("deleteObjectProperty",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteObjectProperty"]



@task
async def toggle_enable_full_distribution_metrics(  # noqa
    dw_id: datetime,
    enable: bool,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Enable/disable collection of full distribution metrics for a particular
    warehouse.

    Args:
        dw_id: The warehouse's UUID.
        enable: If true, enable full distribution metrics.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.toggle_enable_full_distribution_metrics(
            **strip_kwargs(
                dw_id=dw_id,enable=enable,
            )
        )
    )

    op_stack = ("toggleEnableFullDistributionMetrics",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["toggleEnableFullDistributionMetrics"]




@task
async def test_delta_credentials(  # noqa
    databricks_workspace_url: str,
    databricks_workspace_id: str,
    databricks_cluster_id: str,
    databricks_token: str,
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a Databricks connection.

    Args:
        databricks_workspace_url: None.
        databricks_workspace_id: None.
        databricks_cluster_id: None.
        databricks_token: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_delta_credentials(
            **strip_kwargs(
                databricks_workspace_url=databricks_workspace_url,databricks_workspace_id=databricks_workspace_id,databricks_cluster_id=databricks_cluster_id,databricks_token=databricks_token,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,
            )
        )
    )

    op_stack = ("testDeltaCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testDeltaCredentials"]




@task
async def delete_event_comment(  # noqa
    event_comment_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        event_comment_id: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_event_comment(
            **strip_kwargs(
                event_comment_id=event_comment_id,
            )
        )
    )

    op_stack = ("deleteEventComment",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteEventComment"]




@task
async def add_databricks_connection(  # noqa
    connection_type: str,
    job_limits: datetime,
    key: str,
    montecarlo_credentials: MontecarloCredentials,
    create_warehouse_type: str = None,
    dc_id: datetime = None,
    dw_id: datetime = None,
    job_types: Iterable[str] = None,
    name: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Add a databricks connection and setup any associated jobs. Creates a warehouse
    if not specified.

    Args:
        connection_type: The type of connection to add.
        job_limits: Customize job operations for all job types.
        key: Temp key from testing connections.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        create_warehouse_type: Create a new warehouse for the connection.
        dc_id: DC UUID. To disambiguate accounts with multiple collectors.
        dw_id: Add connection to an existing warehouse.
        job_types: Specify job types for the connection. Uses connection default
            otherwise.
        name: Provide a friendly name for the warehouse when creating.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.add_databricks_connection(
            **strip_kwargs(
                connection_type=connection_type,job_limits=job_limits,key=key,create_warehouse_type=create_warehouse_type,dc_id=dc_id,dw_id=dw_id,job_types=job_types,name=name,
            )
        )
    )

    op_stack = ("addDatabricksConnection",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["addDatabricksConnection"]



@task
async def add_databricks_connection_connection(  # noqa
    connection_type: str,
    job_limits: datetime,
    key: str,
    montecarlo_credentials: MontecarloCredentials,
    create_warehouse_type: str = None,
    dc_id: datetime = None,
    dw_id: datetime = None,
    job_types: Iterable[str] = None,
    name: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Add a databricks connection and setup any associated jobs. Creates a warehouse
    if not specified.

    Args:
        connection_type: The type of connection to add.
        job_limits: Customize job operations for all
            job types.
        key: Temp key from testing connections.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        create_warehouse_type: Create a new warehouse
            for the connection.
        dc_id: DC UUID. To disambiguate accounts with
            multiple collectors.
        dw_id: Add connection to an existing warehouse.
        job_types: Specify job types for the
            connection. Uses connection default otherwise.
        name: Provide a friendly name for the
            warehouse when creating.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.add_databricks_connection(
            **strip_kwargs(
                connection_type=connection_type,job_limits=job_limits,key=key,create_warehouse_type=create_warehouse_type,dc_id=dc_id,dw_id=dw_id,job_types=job_types,name=name,
            )
        ).connection(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("addDatabricksConnection","connection",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["addDatabricksConnection"]["connection"]




@task
async def delete_incident_comment(  # noqa
    comment_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Deletes an incident's comment.

    Args:
        comment_id: UUID of the comment for update.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_incident_comment(
            **strip_kwargs(
                comment_id=comment_id,
            )
        )
    )

    op_stack = ("deleteIncidentComment",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteIncidentComment"]




@task
async def bulk_create_or_update_object_properties(  # noqa
    mcon_id: str,
    property_name: str,
    montecarlo_credentials: MontecarloCredentials,
    property_value: str = None,
    property_source_type: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a list of properties (tags) for objects (e.g. tables, fields,
    etc.).

    Args:
        mcon_id: None.
        property_name: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        property_value: None.
        property_source_type: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.bulk_create_or_update_object_properties(
            **strip_kwargs(
                mcon_id=mcon_id,property_name=property_name,property_value=property_value,property_source_type=property_source_type,
            )
        )
    )

    op_stack = ("bulkCreateOrUpdateObjectProperties",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["bulkCreateOrUpdateObjectProperties"]



@task
async def bulk_create_or_update_object_properties_object_properties(  # noqa
    mcon_id: str,
    property_name: str,
    montecarlo_credentials: MontecarloCredentials,
    property_value: str = None,
    property_source_type: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a list of properties (tags) for objects (e.g. tables, fields,
    etc.).

    Args:
        mcon_id: None.
        property_name: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        property_value: None.
        property_source_type: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.bulk_create_or_update_object_properties(
            **strip_kwargs(
                mcon_id=mcon_id,property_name=property_name,property_value=property_value,property_source_type=property_source_type,
            )
        ).object_properties(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("bulkCreateOrUpdateObjectProperties","objectProperties",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["bulkCreateOrUpdateObjectProperties"]["objectProperties"]



@task
async def generate_collector_template(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    region: str = "us-east-1",
    template_variant: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Generate a data collector template (uploaded to S3).

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: DC UUID. To disambiguate accounts with multiple collectors.
        region: Region where the DC is hosted.
        template_variant: DC template variant.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.generate_collector_template(
            **strip_kwargs(
                dc_id=dc_id,region=region,template_variant=template_variant,
            )
        )
    )

    op_stack = ("generateCollectorTemplate",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["generateCollectorTemplate"]



@task
async def generate_collector_template_dc(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    region: str = "us-east-1",
    template_variant: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Generate a data collector template (uploaded to S3).

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: DC UUID. To disambiguate accounts
            with multiple collectors.
        region: Region where the DC is hosted.
        template_variant: DC template variant.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.generate_collector_template(
            **strip_kwargs(
                dc_id=dc_id,region=region,template_variant=template_variant,
            )
        ).dc(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("generateCollectorTemplate","dc",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["generateCollectorTemplate"]["dc"]




@task
async def upload_dbt_manifest(  # noqa
    dbt_schema_version: str,
    invocation_id: str,
    manifest_nodes_json: str,
    montecarlo_credentials: MontecarloCredentials,
    batch: int = 1,
    default_resource: str = None,
    project_name: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Upload DBT manifest.

    Args:
        dbt_schema_version: DBT manifest schema version.
        invocation_id: DBT invocation id.
        manifest_nodes_json: DBT manifest nodes in JSON format.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        batch: Batch number, if a manifest file is broken up into smaller
            subsets of nodes.
        default_resource: Associated warehouse name or uuid.
        project_name: dbt project name.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.upload_dbt_manifest(
            **strip_kwargs(
                dbt_schema_version=dbt_schema_version,invocation_id=invocation_id,manifest_nodes_json=manifest_nodes_json,batch=batch,default_resource=default_resource,project_name=project_name,
            )
        )
    )

    op_stack = ("uploadDbtManifest",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["uploadDbtManifest"]



@task
async def create_event_comment(  # noqa
    event_id: datetime,
    event_text: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        event_id: None.
        event_text: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_event_comment(
            **strip_kwargs(
                event_id=event_id,event_text=event_text,
            )
        )
    )

    op_stack = ("createEventComment",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createEventComment"]




@task
async def set_incident_feedback(  # noqa
    incident_id: datetime,
    feedback: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Provide feedback for an incident.

    Args:
        incident_id: UUID of incident to add feedback.
        feedback: The feedback to be added to an incident.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op
        .set_incident_feedback(
            **strip_kwargs(
                input=dict(
                    incident_id=incident_id,feedback=feedback,
                )
            )
        )
    )

    op_stack = ("setIncidentFeedback",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["setIncidentFeedback"]




@task
async def create_unified_user_assignment(  # noqa
    object_mcon: str,
    relationship_type: graphql_schema.RelationshipType,
    unified_user_id: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Associate a UnifiedUser with a CatalogObject.

    Args:
        object_mcon: MCON of catalog object.
        relationship_type: Type of relationship.
        unified_user_id: UUID of UnifiedUser.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_unified_user_assignment(
            **strip_kwargs(
                object_mcon=object_mcon,relationship_type=relationship_type,unified_user_id=unified_user_id,
            )
        )
    )

    op_stack = ("createUnifiedUserAssignment",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createUnifiedUserAssignment"]



@task
async def create_unified_user_assignment_unified_user_assignment(  # noqa
    object_mcon: str,
    relationship_type: graphql_schema.RelationshipType,
    unified_user_id: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Associate a UnifiedUser with a CatalogObject.

    Args:
        object_mcon: MCON of catalog object.
        relationship_type: Type of relationship.
        unified_user_id: UUID of UnifiedUser.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_unified_user_assignment(
            **strip_kwargs(
                object_mcon=object_mcon,relationship_type=relationship_type,unified_user_id=unified_user_id,
            )
        ).unified_user_assignment(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createUnifiedUserAssignment","unifiedUserAssignment",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createUnifiedUserAssignment"]["unifiedUserAssignment"]



@task
async def test_database_credentials(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    assumable_role: str = None,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    connection_type: str = None,
    db_name: str = None,
    external_id: str = None,
    host: str = None,
    password: str = None,
    port: int = None,
    ca: str = None,
    cert: str = None,
    key: str = None,
    mechanism: str = None,
    skip_verification: bool = None,
    user: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a generic warehouse connection (e.g. redshift).

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        assumable_role: AWS role that can be assumed by the DC.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        connection_type: Type of connection (e.g. snowflake, redshift).
        db_name: Name of database to add connection for.
        external_id: An external id, per assumable role conditions.
        host: Hostname of the warehouse.
        password: User's password.
        port: HTTP Port to use.
        ca: None.
        cert: None.
        key: None.
        mechanism: None.
        skip_verification: None.
        user: User with access to the database.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_database_credentials(
            **strip_kwargs(
                assumable_role=assumable_role,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,connection_type=connection_type,db_name=db_name,external_id=external_id,host=host,password=password,port=port,ca=ca,cert=cert,key=key,mechanism=mechanism,skip_verification=skip_verification,user=user,
            )
        )
    )

    op_stack = ("testDatabaseCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testDatabaseCredentials"]



@task
async def test_database_credentials_warnings(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    assumable_role: str = None,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    connection_type: str = None,
    db_name: str = None,
    external_id: str = None,
    host: str = None,
    password: str = None,
    port: int = None,
    ca: str = None,
    cert: str = None,
    key: str = None,
    mechanism: str = None,
    skip_verification: bool = None,
    user: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a generic warehouse connection (e.g. redshift).

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        assumable_role: AWS role that can be assumed
            by the DC.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        connection_type: Type of connection (e.g.
            snowflake, redshift).
        db_name: Name of database to add connection
            for.
        external_id: An external id, per assumable
            role conditions.
        host: Hostname of the warehouse.
        password: User's password.
        port: HTTP Port to use.
        ca: None.
        cert: None.
        key: None.
        mechanism: None.
        skip_verification: None.
        user: User with access to the database.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_database_credentials(
            **strip_kwargs(
                assumable_role=assumable_role,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,connection_type=connection_type,db_name=db_name,external_id=external_id,host=host,password=password,port=port,ca=ca,cert=cert,key=key,mechanism=mechanism,skip_verification=skip_verification,user=user,
            )
        ).warnings(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("testDatabaseCredentials","warnings",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testDatabaseCredentials"]["warnings"]



@task
async def test_database_credentials_validations(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    assumable_role: str = None,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    connection_type: str = None,
    db_name: str = None,
    external_id: str = None,
    host: str = None,
    password: str = None,
    port: int = None,
    ca: str = None,
    cert: str = None,
    key: str = None,
    mechanism: str = None,
    skip_verification: bool = None,
    user: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a generic warehouse connection (e.g. redshift).

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        assumable_role: AWS role that can be assumed
            by the DC.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        connection_type: Type of connection (e.g.
            snowflake, redshift).
        db_name: Name of database to add connection
            for.
        external_id: An external id, per assumable
            role conditions.
        host: Hostname of the warehouse.
        password: User's password.
        port: HTTP Port to use.
        ca: None.
        cert: None.
        key: None.
        mechanism: None.
        skip_verification: None.
        user: User with access to the database.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_database_credentials(
            **strip_kwargs(
                assumable_role=assumable_role,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,connection_type=connection_type,db_name=db_name,external_id=external_id,host=host,password=password,port=port,ca=ca,cert=cert,key=key,mechanism=mechanism,skip_verification=skip_verification,user=user,
            )
        ).validations(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("testDatabaseCredentials","validations",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testDatabaseCredentials"]["validations"]




@task
async def deauthorize_slack_app(  # noqa
    slack_app_type: graphql_schema.SlackAppType,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        slack_app_type: Slack App Type.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.deauthorize_slack_app(
            **strip_kwargs(
                slack_app_type=slack_app_type,
            )
        )
    )

    op_stack = ("deauthorizeSlackApp",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deauthorizeSlackApp"]



@task
async def update_user_state(  # noqa
    state: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        state: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op
        .update_user_state(
            **strip_kwargs(
                input=dict(
                    state=state,
                )
            )
        )
    )

    op_stack = ("updateUserState",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["updateUserState"]



@task
async def test_looker_git_credentials(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    installation_id: int = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Deprecated. Do not use.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        installation_id: ID response from Github.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_looker_git_credentials(
            **strip_kwargs(
                dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,installation_id=installation_id,
            )
        )
    )

    op_stack = ("testLookerGitCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testLookerGitCredentials"]




@task
async def add_bi_connection(  # noqa
    connection_type: str,
    key: str,
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    job_types: Iterable[str] = None,
    resource_id: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Add a bi connection and setup any associated jobs.

    Args:
        connection_type: The type of connection to add.
        key: Temp key from testing connections.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: DC UUID. To disambiguate accounts with multiple collectors.
        job_types: Specify job types for the connection. Uses connection default
            otherwise.
        resource_id: BI Container UUID. Add the connection under the same
            resource UUID.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.add_bi_connection(
            **strip_kwargs(
                connection_type=connection_type,key=key,dc_id=dc_id,job_types=job_types,resource_id=resource_id,
            )
        )
    )

    op_stack = ("addBiConnection",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["addBiConnection"]



@task
async def add_bi_connection_connection(  # noqa
    connection_type: str,
    key: str,
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    job_types: Iterable[str] = None,
    resource_id: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Add a bi connection and setup any associated jobs.

    Args:
        connection_type: The type of connection to add.
        key: Temp key from testing connections.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: DC UUID. To disambiguate accounts with multiple
            collectors.
        job_types: Specify job types for the connection. Uses
            connection default otherwise.
        resource_id: BI Container UUID. Add the connection
            under the same resource UUID.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.add_bi_connection(
            **strip_kwargs(
                connection_type=connection_type,key=key,dc_id=dc_id,job_types=job_types,resource_id=resource_id,
            )
        ).connection(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("addBiConnection","connection",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["addBiConnection"]["connection"]




@task
async def create_or_update_authorization_group(  # noqa
    member_user_ids: Iterable[str],
    name: str,
    roles: Iterable[str],
    montecarlo_credentials: MontecarloCredentials,
    description: str = None,
    domain_restriction_ids: Iterable[datetime] = None,
    label: str = None,
    version: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update an authorization group.

    Args:
        member_user_ids: User IDs of group members.
        name: Unique to the account, human-readable name (for use in code/policy
            reference).
        roles: Role names assigned to the group.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        description: Description/help text to help users understand the purpose
            of the group. If not provided on updates, will keep current
            value.
        domain_restriction_ids: Optional list of domain IDs to restrict access
            to. If not provided, will clear/apply no restrictions.
        label: UI/user-friendly display name, ex: Data Consumers. If not
            provided on updates, will keep current value.
        version: Version of the permissions definitions the group is designed
            for ex: 2022-03-17. Defaults to system current. If not
            provided on updates, will keep current value.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_authorization_group(
            **strip_kwargs(
                member_user_ids=member_user_ids,name=name,roles=roles,description=description,domain_restriction_ids=domain_restriction_ids,label=label,version=version,
            )
        )
    )

    op_stack = ("createOrUpdateAuthorizationGroup",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateAuthorizationGroup"]



@task
async def create_or_update_authorization_group_authorization_group(  # noqa
    member_user_ids: Iterable[str],
    name: str,
    roles: Iterable[str],
    montecarlo_credentials: MontecarloCredentials,
    description: str = None,
    domain_restriction_ids: Iterable[datetime] = None,
    label: str = None,
    version: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update an authorization group.

    Args:
        member_user_ids: User IDs of group
            members.
        name: Unique to the account, human-
            readable name (for use in code/policy reference).
        roles: Role names assigned to the
            group.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        description: Description/help text
            to help users understand the purpose of the group. If not
            provided on updates, will keep current value.
        domain_restriction_ids: Optional
            list of domain IDs to restrict access to. If not provided,
            will clear/apply no restrictions.
        label: UI/user-friendly display
            name, ex: Data Consumers. If not provided on updates, will
            keep current value.
        version: Version of the permissions
            definitions the group is designed for ex: 2022-03-17.
            Defaults to system current. If not provided on updates, will
            keep current value.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_authorization_group(
            **strip_kwargs(
                member_user_ids=member_user_ids,name=name,roles=roles,description=description,domain_restriction_ids=domain_restriction_ids,label=label,version=version,
            )
        ).authorization_group(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createOrUpdateAuthorizationGroup","authorizationGroup",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateAuthorizationGroup"]["authorizationGroup"]




@task
async def toggle_mute_table(  # noqa
    mute: bool,
    montecarlo_credentials: MontecarloCredentials,
    mcon: str = None,
    full_table_id: str = None,
    dw_id: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Start/Stop getting notifications for the given table.

    Args:
        mute: True for muting the table, False for un-muting.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        mcon: Mcon of table to toggle muting for.
        full_table_id: Deprecated - use mcon. Ignored if mcon is present.
        dw_id: Warehouse the table is contained in. Required when using a
            fullTableId.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op
        .toggle_mute_table(
            **strip_kwargs(
                input=dict(
                    mute=mute,mcon=mcon,full_table_id=full_table_id,dw_id=dw_id,
                )
            )
        )
    )

    op_stack = ("toggleMuteTable",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["toggleMuteTable"]




@task
async def delete_notification_settings(  # noqa
    uuids: Iterable[datetime],
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        uuids: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_notification_settings(
            **strip_kwargs(
                uuids=uuids,
            )
        )
    )

    op_stack = ("deleteNotificationSettings",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteNotificationSettings"]




@task
async def test_snowflake_credentials(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    account: str = None,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    password: str = None,
    private_key: str = None,
    private_key_passphrase: str = None,
    user: str = None,
    warehouse: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a Snowflake connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        account: Snowflake account name.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        password: User's password if using user/password basic auth.
        private_key: User's private key (base64 encoded) if using key pair auth.
        private_key_passphrase: User's private key passphrase if using key pair
            auth. This argument is only needed when the private key is
            encrypted.
        user: User with access to snowflake.
        warehouse: Name of the warehouse for the user.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_snowflake_credentials(
            **strip_kwargs(
                account=account,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,password=password,private_key=private_key,private_key_passphrase=private_key_passphrase,user=user,warehouse=warehouse,
            )
        )
    )

    op_stack = ("testSnowflakeCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testSnowflakeCredentials"]



@task
async def test_snowflake_credentials_warnings(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    account: str = None,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    password: str = None,
    private_key: str = None,
    private_key_passphrase: str = None,
    user: str = None,
    warehouse: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a Snowflake connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        account: Snowflake account name.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        password: User's password if using
            user/password basic auth.
        private_key: User's private key (base64
            encoded) if using key pair auth.
        private_key_passphrase: User's private key
            passphrase if using key pair auth. This argument is only
            needed when the private key is encrypted.
        user: User with access to snowflake.
        warehouse: Name of the warehouse for the user.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_snowflake_credentials(
            **strip_kwargs(
                account=account,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,password=password,private_key=private_key,private_key_passphrase=private_key_passphrase,user=user,warehouse=warehouse,
            )
        ).warnings(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("testSnowflakeCredentials","warnings",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testSnowflakeCredentials"]["warnings"]



@task
async def test_snowflake_credentials_validations(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    account: str = None,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    password: str = None,
    private_key: str = None,
    private_key_passphrase: str = None,
    user: str = None,
    warehouse: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a Snowflake connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        account: Snowflake account name.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        password: User's password if using
            user/password basic auth.
        private_key: User's private key (base64
            encoded) if using key pair auth.
        private_key_passphrase: User's private key
            passphrase if using key pair auth. This argument is only
            needed when the private key is encrypted.
        user: User with access to snowflake.
        warehouse: Name of the warehouse for the user.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_snowflake_credentials(
            **strip_kwargs(
                account=account,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,password=password,private_key=private_key,private_key_passphrase=private_key_passphrase,user=user,warehouse=warehouse,
            )
        ).validations(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("testSnowflakeCredentials","validations",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testSnowflakeCredentials"]["validations"]




@task
async def set_sensitivity(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    event_type: str = None,
    mcon: str = None,
    monitor_uuid: datetime = None,
    min_delay: int = None,
    level: graphql_schema.SensitivityLevels = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        event_type: event type for which to get/set sensitivity.
        mcon: MCON of the object (e.g. table) for which to get/set sensitivity.
        monitor_uuid: UUID of an associated monitor.
        min_delay: None.
        level: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.set_sensitivity(
            **strip_kwargs(
                event_type=event_type,mcon=mcon,monitor_uuid=monitor_uuid,min_delay=min_delay,level=level,
            )
        )
    )

    op_stack = ("setSensitivity",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["setSensitivity"]




@task
async def test_power_bi_credentials(  # noqa
    auth_mode: graphql_schema.PowerBIAuthModeEnum,
    client_id: str,
    tenant_id: str,
    montecarlo_credentials: MontecarloCredentials,
    client_secret: str = None,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    password: str = None,
    username: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test Power BI crendentials.

    Args:
        auth_mode: Authentication mode. We support two values here
            [service_principal, master_user].
        client_id: App Client uuid.
        tenant_id: Azure power bi tenant uuid.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        client_secret: Secret key for the client ID. Required if auth_mode is
            service_principal.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        password: Password when auth as a master user. Required if auth_mode is
            master_user.
        username: Username when auth as a master user. Required if auth_mode is
            master_user.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_power_bi_credentials(
            **strip_kwargs(
                auth_mode=auth_mode,client_id=client_id,tenant_id=tenant_id,client_secret=client_secret,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,password=password,username=username,
            )
        )
    )

    op_stack = ("testPowerBiCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testPowerBiCredentials"]




@task
async def create_or_update_lineage_edge(  # noqa
    object_type: str,
    object_id: str,
    object_type: str,
    object_id: str,
    montecarlo_credentials: MontecarloCredentials,
    resource_id: datetime = None,
    resource_name: str = None,
    expire_at: datetime = None,
    resource_id: datetime = None,
    resource_name: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a lineage edge.

    Args:
        object_type: None.
        object_id: None.
        object_type: None.
        object_id: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        resource_id: None.
        resource_name: None.
        expire_at: When the edge will expire.
        resource_id: None.
        resource_name: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_lineage_edge(
            **strip_kwargs(
                object_type=object_type,object_id=object_id,object_type=object_type,object_id=object_id,resource_id=resource_id,resource_name=resource_name,expire_at=expire_at,resource_id=resource_id,resource_name=resource_name,
            )
        )
    )

    op_stack = ("createOrUpdateLineageEdge",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateLineageEdge"]




@task
async def import_dbt_run_results(  # noqa
    dbt_schema_version: str,
    run_results_json: str,
    montecarlo_credentials: MontecarloCredentials,
    project_name: str = None,
    run_id: str = None,
    run_logs: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Import DBT run results.

    Args:
        dbt_schema_version: DBT run results schema version.
        run_results_json: DBT run results in JSON format.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        project_name: dbt project name.
        run_id: dbt run ID.
        run_logs: dbt run logs.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.import_dbt_run_results(
            **strip_kwargs(
                dbt_schema_version=dbt_schema_version,run_results_json=run_results_json,project_name=project_name,run_id=run_id,run_logs=run_logs,
            )
        )
    )

    op_stack = ("importDbtRunResults",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["importDbtRunResults"]



@task
async def import_dbt_run_results_response(  # noqa
    dbt_schema_version: str,
    run_results_json: str,
    montecarlo_credentials: MontecarloCredentials,
    project_name: str = None,
    run_id: str = None,
    run_logs: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Import DBT run results.

    Args:
        dbt_schema_version: DBT run results schema
            version.
        run_results_json: DBT run results in JSON format.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        project_name: dbt project name.
        run_id: dbt run ID.
        run_logs: dbt run logs.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.import_dbt_run_results(
            **strip_kwargs(
                dbt_schema_version=dbt_schema_version,run_results_json=run_results_json,project_name=project_name,run_id=run_id,run_logs=run_logs,
            )
        ).response(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("importDbtRunResults","response",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["importDbtRunResults"]["response"]



@task
async def test_looker_git_ssh_credentials(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    repo_url: str = None,
    ssh_key: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test the connection to a Git repository using the SSH protocol.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        repo_url: Repository URL as ssh://[user@]server/project.git or the
            shorter form [user@]server:project.git.
        ssh_key: SSH key, base64-encoded.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_looker_git_ssh_credentials(
            **strip_kwargs(
                dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,repo_url=repo_url,ssh_key=ssh_key,
            )
        )
    )

    op_stack = ("testLookerGitSshCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testLookerGitSshCredentials"]




@task
async def create_integration_key(  # noqa
    description: str,
    scope: graphql_schema.IntegrationKeyScope,
    montecarlo_credentials: MontecarloCredentials,
    warehouse_ids: Iterable[datetime] = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create an integration key.

    Args:
        description: Key description.
        scope: Key scope (integration it can be used for).
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        warehouse_ids: UUID(s) of warehouse(s) associated with key.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_integration_key(
            **strip_kwargs(
                description=description,scope=scope,warehouse_ids=warehouse_ids,
            )
        )
    )

    op_stack = ("createIntegrationKey",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createIntegrationKey"]



@task
async def create_integration_key_key(  # noqa
    description: str,
    scope: graphql_schema.IntegrationKeyScope,
    montecarlo_credentials: MontecarloCredentials,
    warehouse_ids: Iterable[datetime] = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create an integration key.

    Args:
        description: Key description.
        scope: Key scope (integration it can be used for).
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        warehouse_ids: UUID(s) of warehouse(s) associated
            with key.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_integration_key(
            **strip_kwargs(
                description=description,scope=scope,warehouse_ids=warehouse_ids,
            )
        ).key(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createIntegrationKey","key",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createIntegrationKey"]["key"]




@task
async def import_dbt_manifest(  # noqa
    dbt_schema_version: str,
    manifest_nodes_json: str,
    montecarlo_credentials: MontecarloCredentials,
    default_resource: str = None,
    project_name: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Import DBT manifest.

    Args:
        dbt_schema_version: DBT manifest schema version.
        manifest_nodes_json: DBT manifest nodes in JSON format.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        default_resource: Warehouse name or uuid to associate dbt models with.
        project_name: dbt project name.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.import_dbt_manifest(
            **strip_kwargs(
                dbt_schema_version=dbt_schema_version,manifest_nodes_json=manifest_nodes_json,default_resource=default_resource,project_name=project_name,
            )
        )
    )

    op_stack = ("importDbtManifest",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["importDbtManifest"]



@task
async def import_dbt_manifest_response(  # noqa
    dbt_schema_version: str,
    manifest_nodes_json: str,
    montecarlo_credentials: MontecarloCredentials,
    default_resource: str = None,
    project_name: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Import DBT manifest.

    Args:
        dbt_schema_version: DBT manifest schema version.
        manifest_nodes_json: DBT manifest nodes in JSON
            format.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        default_resource: Warehouse name or uuid to
            associate dbt models with.
        project_name: dbt project name.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.import_dbt_manifest(
            **strip_kwargs(
                dbt_schema_version=dbt_schema_version,manifest_nodes_json=manifest_nodes_json,default_resource=default_resource,project_name=project_name,
            )
        ).response(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("importDbtManifest","response",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["importDbtManifest"]["response"]



@task
async def upload_dbt_run_results(  # noqa
    dbt_schema_version: str,
    invocation_id: str,
    run_results_json: str,
    montecarlo_credentials: MontecarloCredentials,
    batch: int = 1,
    project_name: str = None,
    run_id: str = None,
    run_logs: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Upload DBT run results.

    Args:
        dbt_schema_version: DBT run results schema version.
        invocation_id: DBT invocation id.
        run_results_json: DBT run results in JSON format.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        batch: Batch number if run results are split across smaller files.
        project_name: dbt project name.
        run_id: dbt run ID.
        run_logs: dbt run logs.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.upload_dbt_run_results(
            **strip_kwargs(
                dbt_schema_version=dbt_schema_version,invocation_id=invocation_id,run_results_json=run_results_json,batch=batch,project_name=project_name,run_id=run_id,run_logs=run_logs,
            )
        )
    )

    op_stack = ("uploadDbtRunResults",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["uploadDbtRunResults"]



@task
async def upload_credentials(  # noqa
    file: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        file: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.upload_credentials(
            **strip_kwargs(
                file=file,
            )
        )
    )

    op_stack = ("uploadCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["uploadCredentials"]




@task
async def create_or_update_lineage_node(  # noqa
    object_id: str,
    object_type: str,
    property_name: str,
    property_value: str,
    montecarlo_credentials: MontecarloCredentials,
    name: str = None,
    resource_id: datetime = None,
    resource_name: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a lineage node.

    Args:
        object_id: Object identifier.
        object_type: Object type.
        property_name: None.
        property_value: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        name: Object name (table name, report name, etc).
        resource_id: The id of the resource containing the node.
        resource_name: The name of the resource containing the node.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_lineage_node(
            **strip_kwargs(
                object_id=object_id,object_type=object_type,property_name=property_name,property_value=property_value,name=name,resource_id=resource_id,resource_name=resource_name,
            )
        )
    )

    op_stack = ("createOrUpdateLineageNode",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateLineageNode"]




@task
async def test_credentials(  # noqa
    key: str,
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    connection_type: str = "bigquery",
    project_id: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test credentials where the temp key already exists (e.g. BQ).

    Args:
        key: Temp key from testing connections.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        connection_type: The type of connection to add.
        project_id: BQ project ID if adding for a specific project only (lists
            otherwise).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_credentials(
            **strip_kwargs(
                key=key,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,connection_type=connection_type,project_id=project_id,
            )
        )
    )

    op_stack = ("testCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testCredentials"]



@task
async def test_credentials_warnings(  # noqa
    key: str,
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    connection_type: str = "bigquery",
    project_id: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test credentials where the temp key already exists (e.g. BQ).

    Args:
        key: Temp key from testing connections.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        connection_type: The type of connection to add.
        project_id: BQ project ID if adding for a specific
            project only (lists otherwise).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_credentials(
            **strip_kwargs(
                key=key,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,connection_type=connection_type,project_id=project_id,
            )
        ).warnings(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("testCredentials","warnings",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testCredentials"]["warnings"]



@task
async def test_credentials_validations(  # noqa
    key: str,
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    connection_type: str = "bigquery",
    project_id: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test credentials where the temp key already exists (e.g. BQ).

    Args:
        key: Temp key from testing connections.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        connection_type: The type of connection to add.
        project_id: BQ project ID if adding for a specific
            project only (lists otherwise).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_credentials(
            **strip_kwargs(
                key=key,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,connection_type=connection_type,project_id=project_id,
            )
        ).validations(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("testCredentials","validations",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testCredentials"]["validations"]




@task
async def test_tableau_credentials(  # noqa
    server_name: str,
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    password: str = None,
    site_name: str = None,
    token_name: str = None,
    token_value: str = None,
    username: str = None,
    verify_ssl: bool = True,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test Tableau credentials.

    Args:
        server_name: The Tableau server name.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        password: Password for the Tableau user if using username/password.
        site_name: The Tableau site name.
        token_name: The personal access token name.
        token_value: The personal access token value.
        username: Username for the Tableau user if using username/password.
        verify_ssl: Whether to verify the SSL connection to Tableau server.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_tableau_credentials(
            **strip_kwargs(
                server_name=server_name,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,password=password,site_name=site_name,token_name=token_name,token_value=token_value,username=username,verify_ssl=verify_ssl,
            )
        )
    )

    op_stack = ("testTableauCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testTableauCredentials"]



@task
async def test_tableau_credentials_warnings(  # noqa
    server_name: str,
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    password: str = None,
    site_name: str = None,
    token_name: str = None,
    token_value: str = None,
    username: str = None,
    verify_ssl: bool = True,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test Tableau credentials.

    Args:
        server_name: The Tableau server name.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        password: Password for the Tableau user if
            using username/password.
        site_name: The Tableau site name.
        token_name: The personal access token name.
        token_value: The personal access token value.
        username: Username for the Tableau user if
            using username/password.
        verify_ssl: Whether to verify the SSL
            connection to Tableau server.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_tableau_credentials(
            **strip_kwargs(
                server_name=server_name,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,password=password,site_name=site_name,token_name=token_name,token_value=token_value,username=username,verify_ssl=verify_ssl,
            )
        ).warnings(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("testTableauCredentials","warnings",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testTableauCredentials"]["warnings"]



@task
async def test_tableau_credentials_validations(  # noqa
    server_name: str,
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    password: str = None,
    site_name: str = None,
    token_name: str = None,
    token_value: str = None,
    username: str = None,
    verify_ssl: bool = True,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test Tableau credentials.

    Args:
        server_name: The Tableau server name.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        password: Password for the Tableau user if
            using username/password.
        site_name: The Tableau site name.
        token_name: The personal access token name.
        token_value: The personal access token value.
        username: Username for the Tableau user if
            using username/password.
        verify_ssl: Whether to verify the SSL
            connection to Tableau server.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_tableau_credentials(
            **strip_kwargs(
                server_name=server_name,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,password=password,site_name=site_name,token_name=token_name,token_value=token_value,username=username,verify_ssl=verify_ssl,
            )
        ).validations(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("testTableauCredentials","validations",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testTableauCredentials"]["validations"]




@task
async def delete_catalog_object_metadata(  # noqa
    mcon: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Delete metadata for an object.

    Args:
        mcon: Monte Carlo full identifier for an entity.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_catalog_object_metadata(
            **strip_kwargs(
                mcon=mcon,
            )
        )
    )

    op_stack = ("deleteCatalogObjectMetadata",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteCatalogObjectMetadata"]



@task
async def create_custom_user(  # noqa
    email: str,
    montecarlo_credentials: MontecarloCredentials,
    first_name: str = None,
    last_name: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create a CustomUser.

    Args:
        email: Email.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        first_name: First name.
        last_name: Last name.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_custom_user(
            **strip_kwargs(
                email=email,first_name=first_name,last_name=last_name,
            )
        )
    )

    op_stack = ("createCustomUser",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createCustomUser"]



@task
async def create_custom_user_custom_user(  # noqa
    email: str,
    montecarlo_credentials: MontecarloCredentials,
    first_name: str = None,
    last_name: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create a CustomUser.

    Args:
        email: Email.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        first_name: First name.
        last_name: Last name.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_custom_user(
            **strip_kwargs(
                email=email,first_name=first_name,last_name=last_name,
            )
        ).custom_user(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createCustomUser","customUser",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createCustomUser"]["customUser"]



@task
async def start_databricks_cluster(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    connection_id: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Start Databricks Cluster.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        connection_id: A Databricks connection UUID.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.start_databricks_cluster(
            **strip_kwargs(
                connection_id=connection_id,
            )
        )
    )

    op_stack = ("startDatabricksCluster",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["startDatabricksCluster"]




@task
async def create_custom_metric_rule(  # noqa
    operator: graphql_schema.CustomRuleComparisonOperator,
    custom_sql: str,
    description: str,
    dw_id: datetime,
    schedule_type: graphql_schema.ScheduleType,
    timezone: str,
    montecarlo_credentials: MontecarloCredentials,
    comparison_type: graphql_schema.ComparisonType = None,
    full_table_id: str = None,
    full_table_ids: Iterable[str] = None,
    mcon: str = None,
    field: str = None,
    metric: str = None,
    threshold: float = None,
    baseline_agg_function: graphql_schema.AggregationFunction = None,
    baseline_interval_minutes: int = None,
    is_threshold_relative: bool = None,
    threshold_lookback_minutes: int = None,
    threshold_ref: str = None,
    min_buffer: graphql_schema.ThresholdModifierInput = None,
    max_buffer: graphql_schema.ThresholdModifierInput = None,
    number_of_agg_periods: int = None,
    connection_id: datetime = None,
    custom_rule_uuid: datetime = None,
    custom_sampling_sql: str = None,
    interval_minutes: int = None,
    labels: Iterable[str] = None,
    notes: str = None,
    query_result_type: graphql_schema.QueryResultType = None,
    interval_minutes: int = None,
    interval_crontab: Iterable[str] = None,
    start_time: datetime = None,
    min_interval_minutes: int = None,
    start_time: datetime = None,
    variables: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Deprecated, use CreateOrUpdateCustomMetricRule instead.

    Args:
        operator: None.
        custom_sql: Custom SQL query to run.
        description: Description of rule.
        dw_id: Warehouse UUID.
        schedule_type: None.
        timezone: Timezone.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        comparison_type: None.
        full_table_id: None.
        full_table_ids: None.
        mcon: None.
        field: None.
        metric: None.
        threshold: None.
        baseline_agg_function: None.
        baseline_interval_minutes: None.
        is_threshold_relative: None.
        threshold_lookback_minutes: None.
        threshold_ref: None.
        min_buffer: None.
        max_buffer: None.
        number_of_agg_periods: None.
        connection_id: Specify a connection (e.g. query-engine) to use.
        custom_rule_uuid: UUID of custom rule, to update existing rule.
        custom_sampling_sql: Custom sampling SQL query to run on breach.
        interval_minutes: How often to run scheduled custom rule check
            (DEPRECATED, use schedule instead).
        labels: The monitor labels.
        notes: Additional context for the rule.
        query_result_type: How the query result is used for the metric. Uses row
            count if unset.
        interval_minutes: How often to run scheduled custom rule check
            (DEPRECATED, use schedule instead).
        interval_crontab: None.
        start_time: Start time of schedule (DEPRECATED, use schedule instead).
        min_interval_minutes: None.
        start_time: Start time of schedule (DEPRECATED, use schedule instead).
        variables: Possible variable values for SQL query.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_custom_metric_rule(
            **strip_kwargs(
                operator=operator,custom_sql=custom_sql,description=description,dw_id=dw_id,schedule_type=schedule_type,timezone=timezone,comparison_type=comparison_type,full_table_id=full_table_id,full_table_ids=full_table_ids,mcon=mcon,field=field,metric=metric,threshold=threshold,baseline_agg_function=baseline_agg_function,baseline_interval_minutes=baseline_interval_minutes,is_threshold_relative=is_threshold_relative,threshold_lookback_minutes=threshold_lookback_minutes,threshold_ref=threshold_ref,min_buffer=min_buffer,max_buffer=max_buffer,number_of_agg_periods=number_of_agg_periods,connection_id=connection_id,custom_rule_uuid=custom_rule_uuid,custom_sampling_sql=custom_sampling_sql,interval_minutes=interval_minutes,labels=labels,notes=notes,query_result_type=query_result_type,interval_minutes=interval_minutes,interval_crontab=interval_crontab,start_time=start_time,min_interval_minutes=min_interval_minutes,start_time=start_time,variables=variables,
            )
        )
    )

    op_stack = ("createCustomMetricRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createCustomMetricRule"]



@task
async def create_custom_metric_rule_custom_rule(  # noqa
    operator: graphql_schema.CustomRuleComparisonOperator,
    custom_sql: str,
    description: str,
    dw_id: datetime,
    schedule_type: graphql_schema.ScheduleType,
    timezone: str,
    montecarlo_credentials: MontecarloCredentials,
    comparison_type: graphql_schema.ComparisonType = None,
    full_table_id: str = None,
    full_table_ids: Iterable[str] = None,
    mcon: str = None,
    field: str = None,
    metric: str = None,
    threshold: float = None,
    baseline_agg_function: graphql_schema.AggregationFunction = None,
    baseline_interval_minutes: int = None,
    is_threshold_relative: bool = None,
    threshold_lookback_minutes: int = None,
    threshold_ref: str = None,
    min_buffer: graphql_schema.ThresholdModifierInput = None,
    max_buffer: graphql_schema.ThresholdModifierInput = None,
    number_of_agg_periods: int = None,
    connection_id: datetime = None,
    custom_rule_uuid: datetime = None,
    custom_sampling_sql: str = None,
    interval_minutes: int = None,
    labels: Iterable[str] = None,
    notes: str = None,
    query_result_type: graphql_schema.QueryResultType = None,
    interval_minutes: int = None,
    interval_crontab: Iterable[str] = None,
    start_time: datetime = None,
    min_interval_minutes: int = None,
    start_time: datetime = None,
    variables: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Deprecated, use CreateOrUpdateCustomMetricRule instead.

    Args:
        operator: None.
        custom_sql: Custom SQL query to run.
        description: Description of rule.
        dw_id: Warehouse UUID.
        schedule_type: None.
        timezone: Timezone.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        comparison_type: None.
        full_table_id: None.
        full_table_ids: None.
        mcon: None.
        field: None.
        metric: None.
        threshold: None.
        baseline_agg_function: None.
        baseline_interval_minutes: None.
        is_threshold_relative: None.
        threshold_lookback_minutes: None.
        threshold_ref: None.
        min_buffer: None.
        max_buffer: None.
        number_of_agg_periods: None.
        connection_id: Specify a connection (e.g.
            query-engine) to use.
        custom_rule_uuid: UUID of custom rule, to
            update existing rule.
        custom_sampling_sql: Custom sampling SQL query
            to run on breach.
        interval_minutes: How often to run scheduled
            custom rule check (DEPRECATED, use schedule instead).
        labels: The monitor labels.
        notes: Additional context for the rule.
        query_result_type: How the query result is
            used for the metric. Uses row count if unset.
        interval_minutes: How often to run scheduled custom rule check
            (DEPRECATED, use schedule instead).
        interval_crontab: None.
        start_time: Start time of schedule (DEPRECATED, use schedule instead).
        min_interval_minutes: None.
        start_time: Start time of schedule
            (DEPRECATED, use schedule instead).
        variables: Possible variable values for SQL
            query.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_custom_metric_rule(
            **strip_kwargs(
                operator=operator,custom_sql=custom_sql,description=description,dw_id=dw_id,schedule_type=schedule_type,timezone=timezone,comparison_type=comparison_type,full_table_id=full_table_id,full_table_ids=full_table_ids,mcon=mcon,field=field,metric=metric,threshold=threshold,baseline_agg_function=baseline_agg_function,baseline_interval_minutes=baseline_interval_minutes,is_threshold_relative=is_threshold_relative,threshold_lookback_minutes=threshold_lookback_minutes,threshold_ref=threshold_ref,min_buffer=min_buffer,max_buffer=max_buffer,number_of_agg_periods=number_of_agg_periods,connection_id=connection_id,custom_rule_uuid=custom_rule_uuid,custom_sampling_sql=custom_sampling_sql,interval_minutes=interval_minutes,labels=labels,notes=notes,query_result_type=query_result_type,interval_minutes=interval_minutes,interval_crontab=interval_crontab,start_time=start_time,min_interval_minutes=min_interval_minutes,start_time=start_time,variables=variables,
            )
        ).custom_rule(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createCustomMetricRule","customRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createCustomMetricRule"]["customRule"]




@task
async def test_spark_credentials(  # noqa
    database: str,
    host: str,
    port: int,
    username: str,
    password: str,
    databricks_workspace_url: str,
    databricks_workspace_id: str,
    databricks_cluster_id: str,
    databricks_token: str,
    url: str,
    username: str,
    password: str,
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test Spark credentials.

    Args:
        database: None.
        host: None.
        port: None.
        username: None.
        password: None.
        databricks_workspace_url: None.
        databricks_workspace_id: None.
        databricks_cluster_id: None.
        databricks_token: None.
        url: None.
        username: None.
        password: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_spark_credentials(
            **strip_kwargs(
                database=database,host=host,port=port,username=username,password=password,databricks_workspace_url=databricks_workspace_url,databricks_workspace_id=databricks_workspace_id,databricks_cluster_id=databricks_cluster_id,databricks_token=databricks_token,url=url,username=username,password=password,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,
            )
        )
    )

    op_stack = ("testSparkCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testSparkCredentials"]




@task
async def unsnooze_custom_rule(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Un-snooze a custom rule.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: UUID for rule to un-snooze.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.unsnooze_custom_rule(
            **strip_kwargs(
                uuid=uuid,
            )
        )
    )

    op_stack = ("unsnoozeCustomRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["unsnoozeCustomRule"]



@task
async def unsnooze_custom_rule_custom_rule(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Un-snooze a custom rule.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: UUID for rule to un-snooze.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.unsnooze_custom_rule(
            **strip_kwargs(
                uuid=uuid,
            )
        ).custom_rule(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("unsnoozeCustomRule","customRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["unsnoozeCustomRule"]["customRule"]




@task
async def update_monitor_notes(  # noqa
    monitor_type: str,
    monitor_uuid: datetime,
    notes: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        monitor_type: Type of monitor.
        monitor_uuid: UUID of the metric monitor or custom rule.
        notes: The notes for the monitor.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.update_monitor_notes(
            **strip_kwargs(
                monitor_type=monitor_type,monitor_uuid=monitor_uuid,notes=notes,
            )
        )
    )

    op_stack = ("updateMonitorNotes",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["updateMonitorNotes"]




@task
async def create_or_update_volume_rule(  # noqa
    operator: graphql_schema.CustomRuleComparisonOperator,
    schedule_type: graphql_schema.ScheduleType,
    description: str,
    schedule_type: graphql_schema.ScheduleType,
    timezone: str,
    montecarlo_credentials: MontecarloCredentials,
    comparison_type: graphql_schema.ComparisonType = None,
    full_table_id: str = None,
    full_table_ids: Iterable[str] = None,
    mcon: str = None,
    field: str = None,
    metric: str = None,
    threshold: float = None,
    baseline_agg_function: graphql_schema.AggregationFunction = None,
    baseline_interval_minutes: int = None,
    is_threshold_relative: bool = None,
    threshold_lookback_minutes: int = None,
    threshold_ref: str = None,
    min_buffer: graphql_schema.ThresholdModifierInput = None,
    max_buffer: graphql_schema.ThresholdModifierInput = None,
    number_of_agg_periods: int = None,
    custom_rule_uuid: datetime = None,
    interval_minutes: int = None,
    interval_crontab: Iterable[str] = None,
    start_time: datetime = None,
    min_interval_minutes: int = None,
    dw_id: datetime = None,
    labels: Iterable[str] = None,
    notes: str = None,
    override: bool = None,
    interval_minutes: int = None,
    interval_crontab: Iterable[str] = None,
    start_time: datetime = None,
    min_interval_minutes: int = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a Volume SLO.

    Args:
        operator: None.
        schedule_type: None.
        description: Description of rule.
        schedule_type: None.
        timezone: Timezone.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        comparison_type: None.
        full_table_id: None.
        full_table_ids: None.
        mcon: None.
        field: None.
        metric: None.
        threshold: None.
        baseline_agg_function: None.
        baseline_interval_minutes: None.
        is_threshold_relative: None.
        threshold_lookback_minutes: None.
        threshold_ref: None.
        min_buffer: None.
        max_buffer: None.
        number_of_agg_periods: None.
        custom_rule_uuid: UUID of custom rule, to update existing rule.
        interval_minutes: None.
        interval_crontab: None.
        start_time: None.
        min_interval_minutes: None.
        dw_id: Warehouse the tables are contained in. Required when using
            fullTableIds.
        labels: The monitor labels.
        notes: Additional context for the rule.
        override: If override is set, it forces the dc schedule to run.
        interval_minutes: None.
        interval_crontab: None.
        start_time: None.
        min_interval_minutes: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_volume_rule(
            **strip_kwargs(
                operator=operator,schedule_type=schedule_type,description=description,schedule_type=schedule_type,timezone=timezone,comparison_type=comparison_type,full_table_id=full_table_id,full_table_ids=full_table_ids,mcon=mcon,field=field,metric=metric,threshold=threshold,baseline_agg_function=baseline_agg_function,baseline_interval_minutes=baseline_interval_minutes,is_threshold_relative=is_threshold_relative,threshold_lookback_minutes=threshold_lookback_minutes,threshold_ref=threshold_ref,min_buffer=min_buffer,max_buffer=max_buffer,number_of_agg_periods=number_of_agg_periods,custom_rule_uuid=custom_rule_uuid,interval_minutes=interval_minutes,interval_crontab=interval_crontab,start_time=start_time,min_interval_minutes=min_interval_minutes,dw_id=dw_id,labels=labels,notes=notes,override=override,interval_minutes=interval_minutes,interval_crontab=interval_crontab,start_time=start_time,min_interval_minutes=min_interval_minutes,
            )
        )
    )

    op_stack = ("createOrUpdateVolumeRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateVolumeRule"]



@task
async def create_or_update_volume_rule_custom_rule(  # noqa
    operator: graphql_schema.CustomRuleComparisonOperator,
    schedule_type: graphql_schema.ScheduleType,
    description: str,
    schedule_type: graphql_schema.ScheduleType,
    timezone: str,
    montecarlo_credentials: MontecarloCredentials,
    comparison_type: graphql_schema.ComparisonType = None,
    full_table_id: str = None,
    full_table_ids: Iterable[str] = None,
    mcon: str = None,
    field: str = None,
    metric: str = None,
    threshold: float = None,
    baseline_agg_function: graphql_schema.AggregationFunction = None,
    baseline_interval_minutes: int = None,
    is_threshold_relative: bool = None,
    threshold_lookback_minutes: int = None,
    threshold_ref: str = None,
    min_buffer: graphql_schema.ThresholdModifierInput = None,
    max_buffer: graphql_schema.ThresholdModifierInput = None,
    number_of_agg_periods: int = None,
    custom_rule_uuid: datetime = None,
    interval_minutes: int = None,
    interval_crontab: Iterable[str] = None,
    start_time: datetime = None,
    min_interval_minutes: int = None,
    dw_id: datetime = None,
    labels: Iterable[str] = None,
    notes: str = None,
    override: bool = None,
    interval_minutes: int = None,
    interval_crontab: Iterable[str] = None,
    start_time: datetime = None,
    min_interval_minutes: int = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a Volume SLO.

    Args:
        operator: None.
        schedule_type: None.
        description: Description of rule.
        schedule_type: None.
        timezone: Timezone.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        comparison_type: None.
        full_table_id: None.
        full_table_ids: None.
        mcon: None.
        field: None.
        metric: None.
        threshold: None.
        baseline_agg_function: None.
        baseline_interval_minutes: None.
        is_threshold_relative: None.
        threshold_lookback_minutes: None.
        threshold_ref: None.
        min_buffer: None.
        max_buffer: None.
        number_of_agg_periods: None.
        custom_rule_uuid: UUID of custom rule, to
            update existing rule.
        interval_minutes: None.
        interval_crontab: None.
        start_time: None.
        min_interval_minutes: None.
        dw_id: Warehouse the tables are contained
            in. Required when using fullTableIds.
        labels: The monitor labels.
        notes: Additional context for the rule.
        override: If override is set, it forces the
            dc schedule to run.
        interval_minutes: None.
        interval_crontab: None.
        start_time: None.
        min_interval_minutes: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_volume_rule(
            **strip_kwargs(
                operator=operator,schedule_type=schedule_type,description=description,schedule_type=schedule_type,timezone=timezone,comparison_type=comparison_type,full_table_id=full_table_id,full_table_ids=full_table_ids,mcon=mcon,field=field,metric=metric,threshold=threshold,baseline_agg_function=baseline_agg_function,baseline_interval_minutes=baseline_interval_minutes,is_threshold_relative=is_threshold_relative,threshold_lookback_minutes=threshold_lookback_minutes,threshold_ref=threshold_ref,min_buffer=min_buffer,max_buffer=max_buffer,number_of_agg_periods=number_of_agg_periods,custom_rule_uuid=custom_rule_uuid,interval_minutes=interval_minutes,interval_crontab=interval_crontab,start_time=start_time,min_interval_minutes=min_interval_minutes,dw_id=dw_id,labels=labels,notes=notes,override=override,interval_minutes=interval_minutes,interval_crontab=interval_crontab,start_time=start_time,min_interval_minutes=min_interval_minutes,
            )
        ).custom_rule(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createOrUpdateVolumeRule","customRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateVolumeRule"]["customRule"]




@task
async def update_user_authorization_group_membership(  # noqa
    group_names: Iterable[str],
    member_user_id: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update a user's authorization group membership. Authenticated user must have
    permission to manage users.

    Args:
        group_names: List of authorization group names the user should be a
            member of.
        member_user_id: User ID for the user whose membership is being updated.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.update_user_authorization_group_membership(
            **strip_kwargs(
                group_names=group_names,member_user_id=member_user_id,
            )
        )
    )

    op_stack = ("updateUserAuthorizationGroupMembership",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["updateUserAuthorizationGroupMembership"]



@task
async def update_user_authorization_group_membership_added_to_groups(  # noqa
    group_names: Iterable[str],
    member_user_id: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update a user's authorization group membership. Authenticated user must have
    permission to manage users.

    Args:
        group_names: List of
            authorization group names the user should be a member of.
        member_user_id: User ID for
            the user whose membership is being updated.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.update_user_authorization_group_membership(
            **strip_kwargs(
                group_names=group_names,member_user_id=member_user_id,
            )
        ).added_to_groups(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("updateUserAuthorizationGroupMembership","addedToGroups",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["updateUserAuthorizationGroupMembership"]["addedToGroups"]



@task
async def update_user_authorization_group_membership_removed_from_groups(  # noqa
    group_names: Iterable[str],
    member_user_id: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update a user's authorization group membership. Authenticated user must have
    permission to manage users.

    Args:
        group_names: List of
            authorization group names the user should be a member of.
        member_user_id: User ID for
            the user whose membership is being updated.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.update_user_authorization_group_membership(
            **strip_kwargs(
                group_names=group_names,member_user_id=member_user_id,
            )
        ).removed_from_groups(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("updateUserAuthorizationGroupMembership","removedFromGroups",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["updateUserAuthorizationGroupMembership"]["removedFromGroups"]



@task
async def create_collector_record(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    region: str = "us-east-1",
    template_provider: str = "cloudformation",
    template_variant: str = "hephaestus",
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create an additional collector record (with template) in the account.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        region: Region where the DC is hosted.
        template_provider: DC template IaC provider.
        template_variant: DC template variant.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_collector_record(
            **strip_kwargs(
                region=region,template_provider=template_provider,template_variant=template_variant,
            )
        )
    )

    op_stack = ("createCollectorRecord",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createCollectorRecord"]



@task
async def create_collector_record_dc(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    region: str = "us-east-1",
    template_provider: str = "cloudformation",
    template_variant: str = "hephaestus",
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create an additional collector record (with template) in the account.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        region: Region where the DC is hosted.
        template_provider: DC template IaC provider.
        template_variant: DC template variant.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_collector_record(
            **strip_kwargs(
                region=region,template_provider=template_provider,template_variant=template_variant,
            )
        ).dc(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createCollectorRecord","dc",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createCollectorRecord"]["dc"]



@task
async def delete_access_token(  # noqa
    token_id: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Delete an API Access Token by ID.

    Args:
        token_id: ID of the token to delete.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_access_token(
            **strip_kwargs(
                token_id=token_id,
            )
        )
    )

    op_stack = ("deleteAccessToken",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteAccessToken"]



@task
async def trigger_circuit_breaker_rule(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    namespace: str = None,
    rule_name: str = None,
    rule_uuid: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Run a custom rule as a circuit breaker immediately.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        namespace: Namespace.
        rule_name: Rule Name.
        rule_uuid: Rule UUID.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.trigger_circuit_breaker_rule(
            **strip_kwargs(
                namespace=namespace,rule_name=rule_name,rule_uuid=rule_uuid,
            )
        )
    )

    op_stack = ("triggerCircuitBreakerRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["triggerCircuitBreakerRule"]




@task
async def update_custom_metric_rule_notes(  # noqa
    custom_rule_uuid: datetime,
    montecarlo_credentials: MontecarloCredentials,
    notes: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update notes for custom metric rule.

    Args:
        custom_rule_uuid: UUID of custom rule, to update existing rule.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        notes: Additional context for the custom SQL rule.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.update_custom_metric_rule_notes(
            **strip_kwargs(
                custom_rule_uuid=custom_rule_uuid,notes=notes,
            )
        )
    )

    op_stack = ("updateCustomMetricRuleNotes",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["updateCustomMetricRuleNotes"]



@task
async def update_custom_metric_rule_notes_custom_rule(  # noqa
    custom_rule_uuid: datetime,
    montecarlo_credentials: MontecarloCredentials,
    notes: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update notes for custom metric rule.

    Args:
        custom_rule_uuid: UUID of custom rule,
            to update existing rule.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        notes: Additional context for the custom
            SQL rule.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.update_custom_metric_rule_notes(
            **strip_kwargs(
                custom_rule_uuid=custom_rule_uuid,notes=notes,
            )
        ).custom_rule(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("updateCustomMetricRuleNotes","customRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["updateCustomMetricRuleNotes"]["customRule"]




@task
async def toggle_disable_sampling(  # noqa
    disable: bool,
    dw_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Enable/disable the sampling data feature.

    Args:
        disable: If true, disable the sampling data feature.
        dw_id: The warehouse's UUID.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.toggle_disable_sampling(
            **strip_kwargs(
                disable=disable,dw_id=dw_id,
            )
        )
    )

    op_stack = ("toggleDisableSampling",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["toggleDisableSampling"]




@task
async def test_hive_credentials(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    auth_mode: str = None,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    database: str = None,
    host: str = None,
    port: int = None,
    username: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a hive sql based connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        auth_mode: Authentication mode to hive. If not set 'SASL' is used.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        database: Name of database.
        host: Hostname.
        port: Port.
        username: Username with access to hive.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_hive_credentials(
            **strip_kwargs(
                auth_mode=auth_mode,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,database=database,host=host,port=port,username=username,
            )
        )
    )

    op_stack = ("testHiveCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testHiveCredentials"]




@task
async def stop_monitor(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    monitor_id: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        monitor_id: None.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.stop_monitor(
            **strip_kwargs(
                monitor_id=monitor_id,
            )
        )
    )

    op_stack = ("stopMonitor",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["stopMonitor"]




@task
async def test_bq_credentials(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    service_json: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a BQ connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        service_json: Service account key file as a base64 string.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_bq_credentials(
            **strip_kwargs(
                dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,service_json=service_json,
            )
        )
    )

    op_stack = ("testBqCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testBqCredentials"]



@task
async def test_bq_credentials_warnings(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    service_json: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a BQ connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        service_json: Service account key file as a base64
            string.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_bq_credentials(
            **strip_kwargs(
                dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,service_json=service_json,
            )
        ).warnings(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("testBqCredentials","warnings",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testBqCredentials"]["warnings"]



@task
async def test_bq_credentials_validations(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    service_json: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a BQ connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        service_json: Service account key file as a base64
            string.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_bq_credentials(
            **strip_kwargs(
                dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,service_json=service_json,
            )
        ).validations(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("testBqCredentials","validations",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testBqCredentials"]["validations"]




@task
async def set_default_incident_group_interval(  # noqa
    dw_id: datetime,
    interval: int,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Set default incident grouping interval (in hours) for a warehouse.

    Args:
        dw_id: The warehouse's UUID.
        interval: Interval in hours.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.set_default_incident_group_interval(
            **strip_kwargs(
                dw_id=dw_id,interval=interval,
            )
        )
    )

    op_stack = ("setDefaultIncidentGroupInterval",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["setDefaultIncidentGroupInterval"]




@task
async def remove_connection(  # noqa
    connection_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Remove an integration connection and deschedule any associated jobs.

    Args:
        connection_id: ID of the connection to remove.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.remove_connection(
            **strip_kwargs(
                connection_id=connection_id,
            )
        )
    )

    op_stack = ("removeConnection",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["removeConnection"]




@task
async def create_or_update_domain(  # noqa
    name: str,
    montecarlo_credentials: MontecarloCredentials,
    assignments: Iterable[str] = None,
    name: str = None,
    value: str = None,
    uuid: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a domain.

    Args:
        name: Domain name.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        assignments: Objects assigned to domain (as MCONs).
        name: Domain name.
        value: None.
        uuid: UUID of domain to update.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_domain(
            **strip_kwargs(
                name=name,assignments=assignments,name=name,value=value,uuid=uuid,
            )
        )
    )

    op_stack = ("createOrUpdateDomain",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateDomain"]



@task
async def create_or_update_domain_domain(  # noqa
    name: str,
    montecarlo_credentials: MontecarloCredentials,
    assignments: Iterable[str] = None,
    name: str = None,
    value: str = None,
    uuid: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a domain.

    Args:
        name: Domain name.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        assignments: Objects assigned to domain (as
            MCONs).
        name: Domain name.
        value: None.
        uuid: UUID of domain to update.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_domain(
            **strip_kwargs(
                name=name,assignments=assignments,name=name,value=value,uuid=uuid,
            )
        ).domain(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createOrUpdateDomain","domain",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateDomain"]["domain"]




@task
async def save_event_onboarding_data(  # noqa
    config: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Save event onboarding configuration.

    Args:
        config: JSON Key/values with event config to store.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.save_event_onboarding_data(
            **strip_kwargs(
                config=config,
            )
        )
    )

    op_stack = ("saveEventOnboardingData",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["saveEventOnboardingData"]




@task
async def toggle_mute_datasets(  # noqa
    mute: bool,
    montecarlo_credentials: MontecarloCredentials,
    datasets: Iterable[graphql_schema.ToggleDatasetInputItem] = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Start/Stop getting notifications for the given datasets.

    Args:
        mute: True for muting the table, False for un-muting.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        datasets: The datasets being muted.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op
        .toggle_mute_datasets(
            **strip_kwargs(
                input=dict(
                    mute=mute,datasets=datasets,
                )
            )
        )
    )

    op_stack = ("toggleMuteDatasets",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["toggleMuteDatasets"]



@task
async def delete_unified_user_assignment(  # noqa
    object_mcon: str,
    unified_user_id: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Associate a UnifiedUser with a CatalogObject.

    Args:
        object_mcon: MCON of catalog object.
        unified_user_id: UUID of UnifiedUser.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_unified_user_assignment(
            **strip_kwargs(
                object_mcon=object_mcon,unified_user_id=unified_user_id,
            )
        )
    )

    op_stack = ("deleteUnifiedUserAssignment",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteUnifiedUserAssignment"]



@task
async def update_monitor_labels(  # noqa
    labels: Iterable[str],
    monitor_type: str,
    monitor_uuid: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        labels: Labels to insert on the monitor.
        monitor_type: Type of monitor.
        monitor_uuid: UUID of the metric monitor or custom rule.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.update_monitor_labels(
            **strip_kwargs(
                labels=labels,monitor_type=monitor_type,monitor_uuid=monitor_uuid,
            )
        )
    )

    op_stack = ("updateMonitorLabels",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["updateMonitorLabels"]




@task
async def migrate_collector_resources(  # noqa
    source_dc_id: datetime,
    target_dc_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    resource_ids: Iterable[datetime] = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Migrate resources (warehouses, BI) from one data collector to another.

    Args:
        source_dc_id: Source DC UUID.
        target_dc_id: Target DC UUID.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        resource_ids: List of resource UUIDs to migrate. By default all
            resources will be migrated.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.migrate_collector_resources(
            **strip_kwargs(
                source_dc_id=source_dc_id,target_dc_id=target_dc_id,resource_ids=resource_ids,
            )
        )
    )

    op_stack = ("migrateCollectorResources",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["migrateCollectorResources"]




@task
async def update_monitor_name(  # noqa
    monitor_type: str,
    monitor_uuid: datetime,
    name: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        monitor_type: Type of monitor.
        monitor_uuid: UUID of the metric monitor or custom rule.
        name: The new monitor name (the description field).
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.update_monitor_name(
            **strip_kwargs(
                monitor_type=monitor_type,monitor_uuid=monitor_uuid,name=name,
            )
        )
    )

    op_stack = ("updateMonitorName",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["updateMonitorName"]




@task
async def set_warehouse_name(  # noqa
    dw_id: datetime,
    name: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Set friendly name for a warehouse.

    Args:
        dw_id: UUID of the warehouse to update.
        name: Desired name.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.set_warehouse_name(
            **strip_kwargs(
                dw_id=dw_id,name=name,
            )
        )
    )

    op_stack = ("setWarehouseName",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["setWarehouseName"]



@task
async def set_warehouse_name_warehouse(  # noqa
    dw_id: datetime,
    name: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Set friendly name for a warehouse.

    Args:
        dw_id: UUID of the warehouse to update.
        name: Desired name.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.set_warehouse_name(
            **strip_kwargs(
                dw_id=dw_id,name=name,
            )
        ).warehouse(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("setWarehouseName","warehouse",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["setWarehouseName"]["warehouse"]




@task
async def test_presto_credentials(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    catalog: str = None,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    host: str = None,
    http_scheme: str = None,
    password: str = None,
    port: int = None,
    schema: str = None,
    ca: str = None,
    cert: str = None,
    key: str = None,
    mechanism: str = None,
    skip_verification: bool = None,
    user: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test connection to Presto.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        catalog: Mount point to access data source.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        host: Hostname.
        http_scheme: Scheme for authentication.
        password: User's password.
        port: HTTP port.
        schema: Schema to access.
        ca: None.
        cert: None.
        key: None.
        mechanism: None.
        skip_verification: None.
        user: Username with access to catalog/schema.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_presto_credentials(
            **strip_kwargs(
                catalog=catalog,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,host=host,http_scheme=http_scheme,password=password,port=port,schema=schema,ca=ca,cert=cert,key=key,mechanism=mechanism,skip_verification=skip_verification,user=user,
            )
        )
    )

    op_stack = ("testPrestoCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testPrestoCredentials"]




@task
async def toggle_mute_with_regex(  # noqa
    dw_id: datetime,
    rule_regex: str,
    mute: bool,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        dw_id: None.
        rule_regex: None.
        mute: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op
        .toggle_mute_with_regex(
            **strip_kwargs(
                input=dict(
                    dw_id=dw_id,rule_regex=rule_regex,mute=mute,
                )
            )
        )
    )

    op_stack = ("toggleMuteWithRegex",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["toggleMuteWithRegex"]




@task
async def snooze_custom_rule(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    snooze_minutes: int = None,
    uuid: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Snooze a custom rule. Data collection will continue, but no anomalies will be
    reported.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        snooze_minutes: Number of minutes to snooze rule.
        uuid: UUID for rule to snooze.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.snooze_custom_rule(
            **strip_kwargs(
                snooze_minutes=snooze_minutes,uuid=uuid,
            )
        )
    )

    op_stack = ("snoozeCustomRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["snoozeCustomRule"]



@task
async def snooze_custom_rule_custom_rule(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    snooze_minutes: int = None,
    uuid: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Snooze a custom rule. Data collection will continue, but no anomalies will be
    reported.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        snooze_minutes: Number of minutes to snooze rule.
        uuid: UUID for rule to snooze.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.snooze_custom_rule(
            **strip_kwargs(
                snooze_minutes=snooze_minutes,uuid=uuid,
            )
        ).custom_rule(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("snoozeCustomRule","customRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["snoozeCustomRule"]["customRule"]




@task
async def set_incident_owner(  # noqa
    incident_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    owner: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Set an owner for an existing incident.

    Args:
        incident_id: The incident's UUID.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        owner: Incident owner to set.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.set_incident_owner(
            **strip_kwargs(
                incident_id=incident_id,owner=owner,
            )
        )
    )

    op_stack = ("setIncidentOwner",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["setIncidentOwner"]



@task
async def set_incident_owner_incident(  # noqa
    incident_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    owner: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Set an owner for an existing incident.

    Args:
        incident_id: The incident's UUID.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        owner: Incident owner to set.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.set_incident_owner(
            **strip_kwargs(
                incident_id=incident_id,owner=owner,
            )
        ).incident(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("setIncidentOwner","incident",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["setIncidentOwner"]["incident"]




@task
async def update_databricks_notebook_job(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    connection_id: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update Databricks collection notebook and job.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        connection_id: A Databricks connection UUID.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.update_databricks_notebook_job(
            **strip_kwargs(
                connection_id=connection_id,
            )
        )
    )

    op_stack = ("updateDatabricksNotebookJob",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["updateDatabricksNotebookJob"]




@task
async def update_event_comment(  # noqa
    event_comment_id: datetime,
    event_text: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        event_comment_id: None.
        event_text: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.update_event_comment(
            **strip_kwargs(
                event_comment_id=event_comment_id,event_text=event_text,
            )
        )
    )

    op_stack = ("updateEventComment",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["updateEventComment"]




@task
async def update_databricks_notebook(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    connection_id: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update Databricks notebook.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        connection_id: A Databricks connection UUID.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.update_databricks_notebook(
            **strip_kwargs(
                connection_id=connection_id,
            )
        )
    )

    op_stack = ("updateDatabricksNotebook",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["updateDatabricksNotebook"]




@task
async def create_or_update_doc(  # noqa
    content: str,
    title: str,
    montecarlo_credentials: MontecarloCredentials,
    doc_mcon: str = None,
    parent_doc_mcon: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a Doc.

    Args:
        content: Content of Doc.
        title: Title of Doc.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        doc_mcon: mcon of Doc, required if updating existing doc.
        parent_doc_mcon: mcon of parent Doc.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_doc(
            **strip_kwargs(
                content=content,title=title,doc_mcon=doc_mcon,parent_doc_mcon=parent_doc_mcon,
            )
        )
    )

    op_stack = ("createOrUpdateDoc",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateDoc"]



@task
async def create_or_update_doc_doc(  # noqa
    content: str,
    title: str,
    montecarlo_credentials: MontecarloCredentials,
    doc_mcon: str = None,
    parent_doc_mcon: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a Doc.

    Args:
        content: Content of Doc.
        title: Title of Doc.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        doc_mcon: mcon of Doc, required if updating
            existing doc.
        parent_doc_mcon: mcon of parent Doc.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_doc(
            **strip_kwargs(
                content=content,title=title,doc_mcon=doc_mcon,parent_doc_mcon=parent_doc_mcon,
            )
        ).doc(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createOrUpdateDoc","doc",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateDoc"]["doc"]



@task
async def track_table(  # noqa
    track: bool,
    montecarlo_credentials: MontecarloCredentials,
    mcon: str = None,
    full_table_id: str = None,
    dw_id: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Add table to account's dashboard.

    Args:
        track: Enable or disable table tracking.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        mcon: Mcon of table to toggle tracking for.
        full_table_id: Deprecated - use mcon. Ignored if mcon is present.
        dw_id: Warehouse the table is contained in. Required when using a
            fullTableId.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op
        .track_table(
            **strip_kwargs(
                input=dict(
                    track=track,mcon=mcon,full_table_id=full_table_id,dw_id=dw_id,
                )
            )
        )
    )

    op_stack = ("trackTable",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["trackTable"]




@task
async def toggle_mute_dataset(  # noqa
    dw_id: datetime,
    ds_id: str,
    mute: bool,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        dw_id: None.
        ds_id: None.
        mute: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op
        .toggle_mute_dataset(
            **strip_kwargs(
                input=dict(
                    dw_id=dw_id,ds_id=ds_id,mute=mute,
                )
            )
        )
    )

    op_stack = ("toggleMuteDataset",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["toggleMuteDataset"]




@task
async def create_or_update_custom_rule(  # noqa
    operator: graphql_schema.CustomRuleComparisonOperator,
    description: str,
    schedule_type: graphql_schema.ScheduleType,
    timezone: str,
    montecarlo_credentials: MontecarloCredentials,
    comparison_type: graphql_schema.ComparisonType = None,
    full_table_id: str = None,
    full_table_ids: Iterable[str] = None,
    mcon: str = None,
    field: str = None,
    metric: str = None,
    threshold: float = None,
    baseline_agg_function: graphql_schema.AggregationFunction = None,
    baseline_interval_minutes: int = None,
    is_threshold_relative: bool = None,
    threshold_lookback_minutes: int = None,
    threshold_ref: str = None,
    min_buffer: graphql_schema.ThresholdModifierInput = None,
    max_buffer: graphql_schema.ThresholdModifierInput = None,
    number_of_agg_periods: int = None,
    custom_rule_uuid: datetime = None,
    dw_id: datetime = None,
    interval_minutes: int = None,
    labels: Iterable[str] = None,
    notes: str = None,
    interval_minutes: int = None,
    interval_crontab: Iterable[str] = None,
    start_time: datetime = None,
    min_interval_minutes: int = None,
    start_time: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a custom rule.

    Args:
        operator: None.
        description: Description of rule.
        schedule_type: None.
        timezone: Timezone.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        comparison_type: None.
        full_table_id: None.
        full_table_ids: None.
        mcon: None.
        field: None.
        metric: None.
        threshold: None.
        baseline_agg_function: None.
        baseline_interval_minutes: None.
        is_threshold_relative: None.
        threshold_lookback_minutes: None.
        threshold_ref: None.
        min_buffer: None.
        max_buffer: None.
        number_of_agg_periods: None.
        custom_rule_uuid: UUID of custom rule, to update existing rule.
        dw_id: Warehouse the tables are contained in. Required when using
            fullTableIds.
        interval_minutes: How often to run scheduled custom rule check
            (DEPRECATED, use schedule instead).
        labels: The monitor labels.
        notes: Additional context for the rule.
        interval_minutes: How often to run scheduled custom rule check
            (DEPRECATED, use schedule instead).
        interval_crontab: None.
        start_time: Start time of schedule (DEPRECATED, use schedule instead).
        min_interval_minutes: None.
        start_time: Start time of schedule (DEPRECATED, use schedule instead).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_custom_rule(
            **strip_kwargs(
                operator=operator,description=description,schedule_type=schedule_type,timezone=timezone,comparison_type=comparison_type,full_table_id=full_table_id,full_table_ids=full_table_ids,mcon=mcon,field=field,metric=metric,threshold=threshold,baseline_agg_function=baseline_agg_function,baseline_interval_minutes=baseline_interval_minutes,is_threshold_relative=is_threshold_relative,threshold_lookback_minutes=threshold_lookback_minutes,threshold_ref=threshold_ref,min_buffer=min_buffer,max_buffer=max_buffer,number_of_agg_periods=number_of_agg_periods,custom_rule_uuid=custom_rule_uuid,dw_id=dw_id,interval_minutes=interval_minutes,labels=labels,notes=notes,interval_minutes=interval_minutes,interval_crontab=interval_crontab,start_time=start_time,min_interval_minutes=min_interval_minutes,start_time=start_time,
            )
        )
    )

    op_stack = ("createOrUpdateCustomRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateCustomRule"]



@task
async def create_or_update_custom_rule_custom_rule(  # noqa
    operator: graphql_schema.CustomRuleComparisonOperator,
    description: str,
    schedule_type: graphql_schema.ScheduleType,
    timezone: str,
    montecarlo_credentials: MontecarloCredentials,
    comparison_type: graphql_schema.ComparisonType = None,
    full_table_id: str = None,
    full_table_ids: Iterable[str] = None,
    mcon: str = None,
    field: str = None,
    metric: str = None,
    threshold: float = None,
    baseline_agg_function: graphql_schema.AggregationFunction = None,
    baseline_interval_minutes: int = None,
    is_threshold_relative: bool = None,
    threshold_lookback_minutes: int = None,
    threshold_ref: str = None,
    min_buffer: graphql_schema.ThresholdModifierInput = None,
    max_buffer: graphql_schema.ThresholdModifierInput = None,
    number_of_agg_periods: int = None,
    custom_rule_uuid: datetime = None,
    dw_id: datetime = None,
    interval_minutes: int = None,
    labels: Iterable[str] = None,
    notes: str = None,
    interval_minutes: int = None,
    interval_crontab: Iterable[str] = None,
    start_time: datetime = None,
    min_interval_minutes: int = None,
    start_time: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a custom rule.

    Args:
        operator: None.
        description: Description of rule.
        schedule_type: None.
        timezone: Timezone.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        comparison_type: None.
        full_table_id: None.
        full_table_ids: None.
        mcon: None.
        field: None.
        metric: None.
        threshold: None.
        baseline_agg_function: None.
        baseline_interval_minutes: None.
        is_threshold_relative: None.
        threshold_lookback_minutes: None.
        threshold_ref: None.
        min_buffer: None.
        max_buffer: None.
        number_of_agg_periods: None.
        custom_rule_uuid: UUID of custom rule, to
            update existing rule.
        dw_id: Warehouse the tables are contained
            in. Required when using fullTableIds.
        interval_minutes: How often to run
            scheduled custom rule check (DEPRECATED, use schedule
            instead).
        labels: The monitor labels.
        notes: Additional context for the rule.
        interval_minutes: How often to run scheduled custom rule check
            (DEPRECATED, use schedule instead).
        interval_crontab: None.
        start_time: Start time of schedule (DEPRECATED, use schedule instead).
        min_interval_minutes: None.
        start_time: Start time of schedule
            (DEPRECATED, use schedule instead).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_custom_rule(
            **strip_kwargs(
                operator=operator,description=description,schedule_type=schedule_type,timezone=timezone,comparison_type=comparison_type,full_table_id=full_table_id,full_table_ids=full_table_ids,mcon=mcon,field=field,metric=metric,threshold=threshold,baseline_agg_function=baseline_agg_function,baseline_interval_minutes=baseline_interval_minutes,is_threshold_relative=is_threshold_relative,threshold_lookback_minutes=threshold_lookback_minutes,threshold_ref=threshold_ref,min_buffer=min_buffer,max_buffer=max_buffer,number_of_agg_periods=number_of_agg_periods,custom_rule_uuid=custom_rule_uuid,dw_id=dw_id,interval_minutes=interval_minutes,labels=labels,notes=notes,interval_minutes=interval_minutes,interval_crontab=interval_crontab,start_time=start_time,min_interval_minutes=min_interval_minutes,start_time=start_time,
            )
        ).custom_rule(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createOrUpdateCustomRule","customRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateCustomRule"]["customRule"]




@task
async def resend_user_invite(  # noqa
    emails: Iterable[str],
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Resend user invite.

    Args:
        emails: List of email addresses to resend the invitation.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.resend_user_invite(
            **strip_kwargs(
                emails=emails,
            )
        )
    )

    op_stack = ("resendUserInvite",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["resendUserInvite"]



@task
async def resend_user_invite_invites(  # noqa
    emails: Iterable[str],
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Resend user invite.

    Args:
        emails: List of email addresses to resend the
            invitation.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.resend_user_invite(
            **strip_kwargs(
                emails=emails,
            )
        ).invites(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("resendUserInvite","invites",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["resendUserInvite"]["invites"]



@task
async def delete_authorization_group(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    name: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Delete an authorization group.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        name: Unique to the account, human-readable name name (for use in
            code/policy reference).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_authorization_group(
            **strip_kwargs(
                name=name,
            )
        )
    )

    op_stack = ("deleteAuthorizationGroup",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteAuthorizationGroup"]



@task
async def delete_custom_rule(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    uuid: datetime = None,
    warehouse_uuid: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Delete a custom rule.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        uuid: UUID for rule to delete.
        warehouse_uuid: Deprecated.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_custom_rule(
            **strip_kwargs(
                uuid=uuid,warehouse_uuid=warehouse_uuid,
            )
        )
    )

    op_stack = ("deleteCustomRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteCustomRule"]




@task
async def test_self_hosted_credentials(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    assumable_role: str = None,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    connection_type: str = None,
    external_id: str = None,
    region: str = None,
    self_hosting_key: str = None,
    self_hosting_mechanism: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a connection of any type with self-hosted credentials.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        assumable_role: Role that can be assumed by the DC to access the self-
            hosting mechanism.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        connection_type: Type of connection.
        external_id: An external id, per assumable role conditions.
        region: Region where the credentials are hosted.
        self_hosting_key: Identifier for the credentials within the self-hosting
            mechanism (e.g. SecretManager secret ARN).
        self_hosting_mechanism: Type of credential self-hosting mechanism.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_self_hosted_credentials(
            **strip_kwargs(
                assumable_role=assumable_role,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,connection_type=connection_type,external_id=external_id,region=region,self_hosting_key=self_hosting_key,self_hosting_mechanism=self_hosting_mechanism,
            )
        )
    )

    op_stack = ("testSelfHostedCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testSelfHostedCredentials"]



@task
async def test_self_hosted_credentials_warnings(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    assumable_role: str = None,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    connection_type: str = None,
    external_id: str = None,
    region: str = None,
    self_hosting_key: str = None,
    self_hosting_mechanism: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a connection of any type with self-hosted credentials.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        assumable_role: Role that can be assumed by
            the DC to access the self-hosting mechanism.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        connection_type: Type of connection.
        external_id: An external id, per assumable
            role conditions.
        region: Region where the credentials are
            hosted.
        self_hosting_key: Identifier for the
            credentials within the self-hosting mechanism (e.g.
            SecretManager secret ARN).
        self_hosting_mechanism: Type of credential
            self-hosting mechanism.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_self_hosted_credentials(
            **strip_kwargs(
                assumable_role=assumable_role,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,connection_type=connection_type,external_id=external_id,region=region,self_hosting_key=self_hosting_key,self_hosting_mechanism=self_hosting_mechanism,
            )
        ).warnings(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("testSelfHostedCredentials","warnings",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testSelfHostedCredentials"]["warnings"]



@task
async def test_self_hosted_credentials_validations(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    assumable_role: str = None,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    connection_type: str = None,
    external_id: str = None,
    region: str = None,
    self_hosting_key: str = None,
    self_hosting_mechanism: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a connection of any type with self-hosted credentials.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        assumable_role: Role that can be assumed by
            the DC to access the self-hosting mechanism.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        connection_type: Type of connection.
        external_id: An external id, per assumable
            role conditions.
        region: Region where the credentials are
            hosted.
        self_hosting_key: Identifier for the
            credentials within the self-hosting mechanism (e.g.
            SecretManager secret ARN).
        self_hosting_mechanism: Type of credential
            self-hosting mechanism.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_self_hosted_credentials(
            **strip_kwargs(
                assumable_role=assumable_role,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,connection_type=connection_type,external_id=external_id,region=region,self_hosting_key=self_hosting_key,self_hosting_mechanism=self_hosting_mechanism,
            )
        ).validations(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("testSelfHostedCredentials","validations",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testSelfHostedCredentials"]["validations"]




@task
async def validate_cron(  # noqa
    cron: str,
    montecarlo_credentials: MontecarloCredentials,
    allow_multiple: bool = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Validate a CRON expression.

    Args:
        cron: CRON expression.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        allow_multiple: Allow multiple CRON expressions.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.validate_cron(
            **strip_kwargs(
                cron=cron,allow_multiple=allow_multiple,
            )
        )
    )

    op_stack = ("validateCron",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["validateCron"]



@task
async def cleanup_collector_record(  # noqa
    dc_id: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Deletes an unassociated collector record in the account. This does not delete
    the CloudFormation stack and will not succeed if the collector is active
    and/or associated with a warehouse.

    Args:
        dc_id: DC UUID.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.cleanup_collector_record(
            **strip_kwargs(
                dc_id=dc_id,
            )
        )
    )

    op_stack = ("cleanupCollectorRecord",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["cleanupCollectorRecord"]




@task
async def test_glue_credentials(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    assumable_role: str = None,
    aws_region: str = None,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    external_id: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a Glue connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        assumable_role: Assumable role ARN to use for accessing AWS resources.
        aws_region: Glue region.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        external_id: An external id, per assumable role conditions.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_glue_credentials(
            **strip_kwargs(
                assumable_role=assumable_role,aws_region=aws_region,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,external_id=external_id,
            )
        )
    )

    op_stack = ("testGlueCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testGlueCredentials"]



@task
async def test_glue_credentials_warnings(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    assumable_role: str = None,
    aws_region: str = None,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    external_id: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a Glue connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        assumable_role: Assumable role ARN to use for
            accessing AWS resources.
        aws_region: Glue region.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        external_id: An external id, per assumable role
            conditions.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_glue_credentials(
            **strip_kwargs(
                assumable_role=assumable_role,aws_region=aws_region,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,external_id=external_id,
            )
        ).warnings(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("testGlueCredentials","warnings",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testGlueCredentials"]["warnings"]



@task
async def test_glue_credentials_validations(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    assumable_role: str = None,
    aws_region: str = None,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    external_id: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test a Glue connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        assumable_role: Assumable role ARN to use for
            accessing AWS resources.
        aws_region: Glue region.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        external_id: An external id, per assumable role
            conditions.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_glue_credentials(
            **strip_kwargs(
                assumable_role=assumable_role,aws_region=aws_region,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,external_id=external_id,
            )
        ).validations(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("testGlueCredentials","validations",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testGlueCredentials"]["validations"]




@task
async def set_generates_incidents(  # noqa
    generates_incidents: bool,
    uuid: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Set whether a DBT project generates incidents.

    Args:
        generates_incidents: should generate incidents.
        uuid: dbt project uuid.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.set_generates_incidents(
            **strip_kwargs(
                generates_incidents=generates_incidents,uuid=uuid,
            )
        )
    )

    op_stack = ("setGeneratesIncidents",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["setGeneratesIncidents"]



@task
async def set_generates_incidents_dbt_project(  # noqa
    generates_incidents: bool,
    uuid: datetime,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Set whether a DBT project generates incidents.

    Args:
        generates_incidents: should generate incidents.
        uuid: dbt project uuid.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.set_generates_incidents(
            **strip_kwargs(
                generates_incidents=generates_incidents,uuid=uuid,
            )
        ).dbt_project(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("setGeneratesIncidents","dbtProject",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["setGeneratesIncidents"]["dbtProject"]




@task
async def create_or_update_lineage_node(  # noqa
    object_id: str,
    object_type: str,
    property_name: str,
    property_value: str,
    montecarlo_credentials: MontecarloCredentials,
    name: str = None,
    resource_id: datetime = None,
    resource_name: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a lineage node.

    Args:
        object_id: Object identifier.
        object_type: Object type.
        property_name: None.
        property_value: None.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        name: Object name (table name, report name, etc).
        resource_id: The id of the resource containing the node.
        resource_name: The name of the resource containing the node.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_lineage_node(
            **strip_kwargs(
                object_id=object_id,object_type=object_type,property_name=property_name,property_value=property_value,name=name,resource_id=resource_id,resource_name=resource_name,
            )
        )
    )

    op_stack = ("createOrUpdateLineageNode",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateLineageNode"]




@task
async def remove_user_from_account(  # noqa
    email: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Remove user from account.

    Args:
        email: Email address of user.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.remove_user_from_account(
            **strip_kwargs(
                email=email,
            )
        )
    )

    op_stack = ("removeUserFromAccount",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["removeUserFromAccount"]



@task
async def remove_user_from_account_user(  # noqa
    email: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Remove user from account.

    Args:
        email: Email address of user.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.remove_user_from_account(
            **strip_kwargs(
                email=email,
            )
        ).user(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("removeUserFromAccount","user",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["removeUserFromAccount"]["user"]



@task
async def create_or_update_object_property(  # noqa
    mcon_id: str,
    property_name: str,
    montecarlo_credentials: MontecarloCredentials,
    property_source_type: str = "dashboard",
    property_value: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update properties (tags) for objects (e.g. tables, fields, etc.).

    Args:
        mcon_id: Monte Carlo full identifier for an entity.
        property_name: Name of the property (AKA tag key).
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        property_source_type: Where property originated.
        property_value: Value of the property (AKA tag value).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_object_property(
            **strip_kwargs(
                mcon_id=mcon_id,property_name=property_name,property_source_type=property_source_type,property_value=property_value,
            )
        )
    )

    op_stack = ("createOrUpdateObjectProperty",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateObjectProperty"]



@task
async def create_or_update_object_property_object_property(  # noqa
    mcon_id: str,
    property_name: str,
    montecarlo_credentials: MontecarloCredentials,
    property_source_type: str = "dashboard",
    property_value: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    

    Args:
        mcon_id: Monte Carlo full identifier
            for an entity.
        property_name: Name of the property
            (AKA tag key).
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        property_source_type: Where property
            originated.
        property_value: Value of the property
            (AKA tag value).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op
        .create_or_update_object_property(
            **strip_kwargs(
                input=dict(
                    mcon_id=mcon_id,property_name=property_name,property_source_type=property_source_type,property_value=property_value,
                )
            )
        ).object_property(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createOrUpdateObjectProperty","objectProperty",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateObjectProperty"]["objectProperty"]



@task
async def delete_lineage_node(  # noqa
    mcon: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Delete a lineage node and any lineage edges connected to it.

    Args:
        mcon: The MCON of the node to be deleted.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_lineage_node(
            **strip_kwargs(
                mcon=mcon,
            )
        )
    )

    op_stack = ("deleteLineageNode",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteLineageNode"]



@task
async def save_table_importance_stats(  # noqa
    mcon: str,
    montecarlo_credentials: MontecarloCredentials,
    importance_score: float = None,
    is_important: bool = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Save custom table stats for a table.

    Args:
        mcon: The MCON of the table whose stats are being updated.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        importance_score: User-provided importance score.
        is_important: Whether the table is a key asset or not.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.save_table_importance_stats(
            **strip_kwargs(
                mcon=mcon,importance_score=importance_score,is_important=is_important,
            )
        )
    )

    op_stack = ("saveTableImportanceStats",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["saveTableImportanceStats"]



@task
async def save_table_importance_stats_stats(  # noqa
    mcon: str,
    montecarlo_credentials: MontecarloCredentials,
    importance_score: float = None,
    is_important: bool = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Save custom table stats for a table.

    Args:
        mcon: The MCON of the table whose stats are
            being updated.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        importance_score: User-provided importance
            score.
        is_important: Whether the table is a key
            asset or not.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.save_table_importance_stats(
            **strip_kwargs(
                mcon=mcon,importance_score=importance_score,is_important=is_important,
            )
        ).stats(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("saveTableImportanceStats","stats",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["saveTableImportanceStats"]["stats"]



@task
async def delete_doc(  # noqa
    doc_mcon: str,
    montecarlo_credentials: MontecarloCredentials,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Delete Doc.

    Args:
        doc_mcon: mcon of Doc.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.delete_doc(
            **strip_kwargs(
                doc_mcon=doc_mcon,
            )
        )
    )

    op_stack = ("deleteDoc",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["deleteDoc"]



@task
async def test_athena_credentials(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    assumable_role: str = None,
    aws_region: str = None,
    catalog: str = None,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    external_id: str = None,
    workgroup: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test an Athena connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        assumable_role: Assumable role ARN to use for accessing AWS resources.
        aws_region: Athena cluster region.
        catalog: Glue data catalog.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        external_id: An external id, per assumable role conditions.
        workgroup: Workbook for running queries and retrieving logs. If not
            specified the primary is used.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_athena_credentials(
            **strip_kwargs(
                assumable_role=assumable_role,aws_region=aws_region,catalog=catalog,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,external_id=external_id,workgroup=workgroup,
            )
        )
    )

    op_stack = ("testAthenaCredentials",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testAthenaCredentials"]



@task
async def test_athena_credentials_warnings(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    assumable_role: str = None,
    aws_region: str = None,
    catalog: str = None,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    external_id: str = None,
    workgroup: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test an Athena connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        assumable_role: Assumable role ARN to use for
            accessing AWS resources.
        aws_region: Athena cluster region.
        catalog: Glue data catalog.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        external_id: An external id, per assumable role
            conditions.
        workgroup: Workbook for running queries and
            retrieving logs. If not specified the primary is used.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_athena_credentials(
            **strip_kwargs(
                assumable_role=assumable_role,aws_region=aws_region,catalog=catalog,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,external_id=external_id,workgroup=workgroup,
            )
        ).warnings(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("testAthenaCredentials","warnings",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testAthenaCredentials"]["warnings"]



@task
async def test_athena_credentials_validations(  # noqa
    montecarlo_credentials: MontecarloCredentials,
    assumable_role: str = None,
    aws_region: str = None,
    catalog: str = None,
    dc_id: datetime = None,
    skip_validation: bool = None,
    skip_permission_tests: bool = None,
    test_options: graphql_schema.ValidatorTestOptions = None,
    external_id: str = None,
    workgroup: str = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test an Athena connection.

    Args:
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        assumable_role: Assumable role ARN to use for
            accessing AWS resources.
        aws_region: Athena cluster region.
        catalog: Glue data catalog.
        dc_id: None.
        skip_validation: None.
        skip_permission_tests: None.
        test_options: None.
        external_id: An external id, per assumable role
            conditions.
        workgroup: Workbook for running queries and
            retrieving logs. If not specified the primary is used.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.test_athena_credentials(
            **strip_kwargs(
                assumable_role=assumable_role,aws_region=aws_region,catalog=catalog,dc_id=dc_id,skip_validation=skip_validation,skip_permission_tests=skip_permission_tests,test_options=test_options,external_id=external_id,workgroup=workgroup,
            )
        ).validations(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("testAthenaCredentials","validations",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["testAthenaCredentials"]["validations"]




@task
async def create_or_update_freshness_custom_rule(  # noqa
    operator: graphql_schema.CustomRuleComparisonOperator,
    description: str,
    schedule_type: graphql_schema.ScheduleType,
    timezone: str,
    montecarlo_credentials: MontecarloCredentials,
    comparison_type: graphql_schema.ComparisonType = None,
    full_table_id: str = None,
    full_table_ids: Iterable[str] = None,
    mcon: str = None,
    field: str = None,
    metric: str = None,
    threshold: float = None,
    baseline_agg_function: graphql_schema.AggregationFunction = None,
    baseline_interval_minutes: int = None,
    is_threshold_relative: bool = None,
    threshold_lookback_minutes: int = None,
    threshold_ref: str = None,
    min_buffer: graphql_schema.ThresholdModifierInput = None,
    max_buffer: graphql_schema.ThresholdModifierInput = None,
    number_of_agg_periods: int = None,
    custom_rule_uuid: datetime = None,
    dw_id: datetime = None,
    interval_minutes: int = None,
    labels: Iterable[str] = None,
    notes: str = None,
    interval_minutes: int = None,
    interval_crontab: Iterable[str] = None,
    start_time: datetime = None,
    min_interval_minutes: int = None,
    start_time: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a freshness custom rule.

    Args:
        operator: None.
        description: Description of rule.
        schedule_type: None.
        timezone: Timezone.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        comparison_type: None.
        full_table_id: None.
        full_table_ids: None.
        mcon: None.
        field: None.
        metric: None.
        threshold: None.
        baseline_agg_function: None.
        baseline_interval_minutes: None.
        is_threshold_relative: None.
        threshold_lookback_minutes: None.
        threshold_ref: None.
        min_buffer: None.
        max_buffer: None.
        number_of_agg_periods: None.
        custom_rule_uuid: UUID of custom rule, to update existing rule.
        dw_id: Warehouse the tables are contained in. Required when using
            fullTableIds.
        interval_minutes: How often to run scheduled custom rule check
            (DEPRECATED, use schedule instead).
        labels: The monitor labels.
        notes: Additional context for the rule.
        interval_minutes: How often to run scheduled custom rule check
            (DEPRECATED, use schedule instead).
        interval_crontab: None.
        start_time: Start time of schedule (DEPRECATED, use schedule instead).
        min_interval_minutes: None.
        start_time: Start time of schedule (DEPRECATED, use schedule instead).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_freshness_custom_rule(
            **strip_kwargs(
                operator=operator,description=description,schedule_type=schedule_type,timezone=timezone,comparison_type=comparison_type,full_table_id=full_table_id,full_table_ids=full_table_ids,mcon=mcon,field=field,metric=metric,threshold=threshold,baseline_agg_function=baseline_agg_function,baseline_interval_minutes=baseline_interval_minutes,is_threshold_relative=is_threshold_relative,threshold_lookback_minutes=threshold_lookback_minutes,threshold_ref=threshold_ref,min_buffer=min_buffer,max_buffer=max_buffer,number_of_agg_periods=number_of_agg_periods,custom_rule_uuid=custom_rule_uuid,dw_id=dw_id,interval_minutes=interval_minutes,labels=labels,notes=notes,interval_minutes=interval_minutes,interval_crontab=interval_crontab,start_time=start_time,min_interval_minutes=min_interval_minutes,start_time=start_time,
            )
        )
    )

    op_stack = ("createOrUpdateFreshnessCustomRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateFreshnessCustomRule"]



@task
async def create_or_update_freshness_custom_rule_custom_rule(  # noqa
    operator: graphql_schema.CustomRuleComparisonOperator,
    description: str,
    schedule_type: graphql_schema.ScheduleType,
    timezone: str,
    montecarlo_credentials: MontecarloCredentials,
    comparison_type: graphql_schema.ComparisonType = None,
    full_table_id: str = None,
    full_table_ids: Iterable[str] = None,
    mcon: str = None,
    field: str = None,
    metric: str = None,
    threshold: float = None,
    baseline_agg_function: graphql_schema.AggregationFunction = None,
    baseline_interval_minutes: int = None,
    is_threshold_relative: bool = None,
    threshold_lookback_minutes: int = None,
    threshold_ref: str = None,
    min_buffer: graphql_schema.ThresholdModifierInput = None,
    max_buffer: graphql_schema.ThresholdModifierInput = None,
    number_of_agg_periods: int = None,
    custom_rule_uuid: datetime = None,
    dw_id: datetime = None,
    interval_minutes: int = None,
    labels: Iterable[str] = None,
    notes: str = None,
    interval_minutes: int = None,
    interval_crontab: Iterable[str] = None,
    start_time: datetime = None,
    min_interval_minutes: int = None,
    start_time: datetime = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create or update a freshness custom rule.

    Args:
        operator: None.
        description: Description of rule.
        schedule_type: None.
        timezone: Timezone.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        comparison_type: None.
        full_table_id: None.
        full_table_ids: None.
        mcon: None.
        field: None.
        metric: None.
        threshold: None.
        baseline_agg_function: None.
        baseline_interval_minutes: None.
        is_threshold_relative: None.
        threshold_lookback_minutes: None.
        threshold_ref: None.
        min_buffer: None.
        max_buffer: None.
        number_of_agg_periods: None.
        custom_rule_uuid: UUID of custom
            rule, to update existing rule.
        dw_id: Warehouse the tables are
            contained in. Required when using fullTableIds.
        interval_minutes: How often to
            run scheduled custom rule check (DEPRECATED, use schedule
            instead).
        labels: The monitor labels.
        notes: Additional context for the
            rule.
        interval_minutes: How often to run scheduled custom rule check
            (DEPRECATED, use schedule instead).
        interval_crontab: None.
        start_time: Start time of schedule (DEPRECATED, use schedule instead).
        min_interval_minutes: None.
        start_time: Start time of
            schedule (DEPRECATED, use schedule instead).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op.create_or_update_freshness_custom_rule(
            **strip_kwargs(
                operator=operator,description=description,schedule_type=schedule_type,timezone=timezone,comparison_type=comparison_type,full_table_id=full_table_id,full_table_ids=full_table_ids,mcon=mcon,field=field,metric=metric,threshold=threshold,baseline_agg_function=baseline_agg_function,baseline_interval_minutes=baseline_interval_minutes,is_threshold_relative=is_threshold_relative,threshold_lookback_minutes=threshold_lookback_minutes,threshold_ref=threshold_ref,min_buffer=min_buffer,max_buffer=max_buffer,number_of_agg_periods=number_of_agg_periods,custom_rule_uuid=custom_rule_uuid,dw_id=dw_id,interval_minutes=interval_minutes,labels=labels,notes=notes,interval_minutes=interval_minutes,interval_crontab=interval_crontab,start_time=start_time,min_interval_minutes=min_interval_minutes,start_time=start_time,
            )
        ).custom_rule(
            **strip_kwargs(
                
            )
        )
    )

    op_stack = ("createOrUpdateFreshnessCustomRule","customRule",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["createOrUpdateFreshnessCustomRule"]["customRule"]




@task
async def toggle_mute_tables(  # noqa
    mute: bool,
    montecarlo_credentials: MontecarloCredentials,
    tables: Iterable[graphql_schema.ToggleTableInputItem] = None,
    return_fields: Iterable[str] = None,
    
) -> Dict[str, Any]:  # pragma: no cover
    """
    Start/Stop getting notifications for the given tables.

    Args:
        mute: True for muting the table, False for un-muting.
        montecarlo_credentials: Credentials to use for authentication with
            Montecarlo.
        tables: The tables being muted.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.
        
    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = (
        op
        .toggle_mute_tables(
            **strip_kwargs(
                input=dict(
                    mute=mute,tables=tables,
                )
            )
        )
    )

    op_stack = ("toggleMuteTables",)
    op_selection = _subset_return_fields(op_selection, op_stack, return_fields, return_fields_defaults)

    result = await _execute_graphql_op(op, montecarlo_credentials)
    return result["toggleMuteTables"]