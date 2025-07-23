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
def playbook_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_3() called")

    inputs = {}

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "local/playbook", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/playbook", container=container, name="playbook_3", callback=decision_1, inputs=inputs)

    return


@phantom.playbook_block()
def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("decision_1() called")

    # check for 'else' condition 2
    format_warning_msg(action=action, success=success, container=container, results=results, handle=handle)

    return


@phantom.playbook_block()
def format_warning_msg(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_warning_msg() called")

    template = """WARNING! URL Found in http_intel threat list!!!\n\nURL: {0}\nThreat Key: {1}\nTime Created: {2}"""

    # parameter list for template variable replacement
    parameters = [
        "",
        "",
        ""
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_warning_msg")

    add_comment_3(container=container)

    return


@phantom.playbook_block()
def add_comment_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_comment_3() called")

    format_warning_msg = phantom.get_format_data(name="format_warning_msg")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment=format_warning_msg)

    set_severity_5(container=container)

    return


@phantom.playbook_block()
def format_url_not_found_msg(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_url_not_found_msg() called")

    template = """URL not found in http_intel threat list.\n\nURL: {0}"""

    # parameter list for template variable replacement
    parameters = [
        ""
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_url_not_found_msg")

    add_comment_4(container=container)

    return


@phantom.playbook_block()
def add_comment_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_comment_4() called")

    format_url_not_found_msg = phantom.get_format_data(name="format_url_not_found_msg")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment=format_url_not_found_msg)

    ask_to_add_to_threat_list(container=container)

    return


@phantom.playbook_block()
def set_severity_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("set_severity_5() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.set_severity(container=container, severity="high")

    container = phantom.get_container(container.get('id', None))

    return


@phantom.playbook_block()
def ask_to_add_to_threat_list(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("ask_to_add_to_threat_list() called")

    # set approver and message variables for phantom.prompt call

    user = None
    role = "Administrator"
    message = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "format_url_not_found_msg:formatted_data"
    ]

    # responses
    response_types = [
        {
            "prompt": "Would you like to add the URL to the http_intel threat list?",
            "options": {
                "type": "list",
                "required": True,
                "choices": [
                    "Yes",
                    "No"
                ],
            },
        }
    ]

    phantom.prompt2(container=container, user=user, role=role, message=message, respond_in_mins=5, name="ask_to_add_to_threat_list", parameters=parameters, response_types=response_types, callback=decision_2)

    return


@phantom.playbook_block()
def decision_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("decision_2() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["ask_to_add_to_threat_list:action_result.summary.responses.0", "==", "Yes"]
        ],
        conditions_dps=[
            ["ask_to_add_to_threat_list:action_result.summary.responses.0", "==", "Yes"]
        ],
        name="decision_2:condition_1",
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        format_threat_key_value(action=action, success=success, container=container, results=results, handle=handle)
        return

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

    # call playbook "preconf/playbook", returns the playbook_run_id
    playbook_run_id = phantom.playbook("preconf/playbook", container=container, name="playbook_2", callback=playbook_2_callback, inputs=inputs)

    return


@phantom.playbook_block()
def playbook_2_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_2_callback() called")

    
    # Downstream End block cannot be called directly, since execution will call on_finish automatically.
    # Using placeholder callback function so child playbook is run synchronously.


    return


@phantom.playbook_block()
def format_threat_key_value(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_threat_key_value() called")

    template = """local intel"""

    # parameter list for template variable replacement
    parameters = []

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_threat_key_value")

    format_record_user_field(container=container)

    return


@phantom.playbook_block()
def format_record_user_field(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_record_user_field() called")

    template = """nobody"""

    # parameter list for template variable replacement
    parameters = []

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_record_user_field")

    datetime_modify_7(container=container)

    return


@phantom.playbook_block()
def datetime_modify_7(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("datetime_modify_7() called")

    parameters = []

    parameters.append({
        "input_datetime": None,
        "amount_to_modify": None,
        "modification_unit": None,
        "input_format_string": None,
        "output_format_string": None,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/datetime_modify", parameters=parameters, name="datetime_modify_7", callback=format_time)

    return


@phantom.playbook_block()
def format_time(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_time() called")

    template = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "datetime_modify_7:custom_function_result.data.epoch_time"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_time")

    playbook_2(container=container)

    return


@phantom.playbook_block()
def playbook_string_split_extract_url_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("playbook_string_split_extract_url_1() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.requestURL"])

    container_artifact_cef_item_0 = [item[0] for item in container_artifact_data]

    inputs = {
        "url": container_artifact_cef_item_0,
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "preconf/String_split_extract_url", returns the playbook_run_id
    playbook_run_id = phantom.playbook("preconf/String_split_extract_url", container=container, name="playbook_string_split_extract_url_1", callback=playbook_3, inputs=inputs)

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