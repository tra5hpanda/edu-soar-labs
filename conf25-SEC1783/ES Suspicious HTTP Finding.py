"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'playbook_string_split_extract_url_1' block
    playbook_string_split_extract_url_1(container=container)

    return

@phantom.playbook_block()
def playbook_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_2() called")

    inputs = {}

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "local/playbook", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/playbook", container=container, name="playbook_2", callback=decision_1, inputs=inputs)

    return


@phantom.playbook_block()
def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("decision_1() called")

    # check for 'else' condition 2
    open_status_and_set_urgency_to_critical(action=action, success=success, container=container, results=results, handle=handle)

    return


@phantom.playbook_block()
def open_status_and_set_urgency_to_critical(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("open_status_and_set_urgency_to_critical() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    finding_data = phantom.collect2(container=container, datapath=["finding:finding_id"])

    parameters = []

    # build parameters list for 'open_status_and_set_urgency_to_critical' call
    for finding_data_item in finding_data:
        if finding_data_item[0] is not None:
            parameters.append({
                "id": finding_data_item[0],
                "status": "In Progress",
                "urgency": "Critical",
                "description": "",
                "disposition": "",
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("update finding or investigation", parameters=parameters, name="open_status_and_set_urgency_to_critical", assets=["builtin_mc_connector"], callback=create_risk_modifier_of_a_risk_entity_1)

    return


@phantom.playbook_block()
def close_status_and_set_informational_urgency(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("close_status_and_set_informational_urgency() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    finding_data = phantom.collect2(container=container, datapath=["finding:finding_id"])

    parameters = []

    # build parameters list for 'close_status_and_set_informational_urgency' call
    for finding_data_item in finding_data:
        if finding_data_item[0] is not None:
            parameters.append({
                "id": finding_data_item[0],
                "status": "Closed",
                "urgency": "Informational",
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("update finding or investigation", parameters=parameters, name="close_status_and_set_informational_urgency", assets=["builtin_mc_connector"])

    return


@phantom.playbook_block()
def create_risk_modifier_of_a_risk_entity_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("create_risk_modifier_of_a_risk_entity_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    finding_data = phantom.collect2(container=container, datapath=["finding:consolidated_findings.risk_object_identity","finding:consolidated_findings.risk_object_type"])

    parameters = []

    # build parameters list for 'create_risk_modifier_of_a_risk_entity_1' call
    for finding_data_item in finding_data:
        if finding_data_item[0] is not None:
            parameters.append({
                "entity": finding_data_item[0],
                "entity_type": finding_data_item[1],
                "risk_modifier": 1003,
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("create risk modifier of a risk entity", parameters=parameters, name="create_risk_modifier_of_a_risk_entity_1", assets=["builtin_mc_connector"], callback=update_disposition)

    return


@phantom.playbook_block()
def playbook_string_split_extract_url_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_string_split_extract_url_1() called")

    finding_data = phantom.collect2(container=container, datapath=["finding:consolidated_findings.dest"])

    finding_consolidated_findings_dest = [item[0] for item in finding_data]

    inputs = {
        "url": finding_consolidated_findings_dest,
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "preconf/String_split_extract_url", returns the playbook_run_id
    playbook_run_id = phantom.playbook("preconf/String_split_extract_url", container=container, name="playbook_string_split_extract_url_1", callback=playbook_2, inputs=inputs)

    return


@phantom.playbook_block()
def update_disposition(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("update_disposition() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    finding_data = phantom.collect2(container=container, datapath=["finding:finding_id"])

    parameters = []

    # build parameters list for 'update_disposition' call
    for finding_data_item in finding_data:
        if finding_data_item[0] is not None:
            parameters.append({
                "id": finding_data_item[0],
                "disposition": "True Positive - Suspicious Activity",
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("update finding or investigation", parameters=parameters, name="update_disposition", assets=["builtin_mc_connector"])

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    return