"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'string_split' block
    string_split(container=container)

    return

@phantom.playbook_block()
def string_split(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("string_split() called")

    playbook_input_url = phantom.collect2(container=container, datapath=["playbook_input:url"])

    parameters = []

    # build parameters list for 'string_split' call
    for playbook_input_url_item in playbook_input_url:
        parameters.append({
            "delimiter": "?",
            "input_string": playbook_input_url_item[0],
            "strip_whitespace": True,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/string_split", parameters=parameters, name="string_split", callback=string_split_callback)

    return


@phantom.playbook_block()
def string_split_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("string_split_callback() called")

    
    debug_5(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)
    regex_extract_url(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)


    return


@phantom.playbook_block()
def debug_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("debug_5() called")

    string_split_data = phantom.collect2(container=container, datapath=["string_split:custom_function_result.data.*.item"])
    string_split__result = phantom.collect2(container=container, datapath=["string_split:custom_function_result.success","string_split:custom_function_result.message"])

    string_split_data___item = [item[0] for item in string_split_data]
    string_split_success = [item[0] for item in string_split__result]
    string_split_message = [item[1] for item in string_split__result]

    parameters = []

    parameters.append({
        "input_1": string_split_data___item,
        "input_2": string_split_success,
        "input_3": string_split_message,
        "input_4": ["from String Split"],
        "input_5": None,
        "input_6": None,
        "input_7": None,
        "input_8": None,
        "input_9": None,
        "input_10": None,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_5")

    return


@phantom.playbook_block()
def regex_extract_url(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("regex_extract_url() called")

    string_split_data = phantom.collect2(container=container, datapath=["string_split:custom_function_result.data.*.item"])

    parameters = []

    # build parameters list for 'regex_extract_url' call
    for string_split_data_item in string_split_data:
        parameters.append({
            "input_string": string_split_data_item[0],
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/regex_extract_url", parameters=parameters, name="regex_extract_url", callback=regex_extract_url_callback)

    return


@phantom.playbook_block()
def regex_extract_url_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("regex_extract_url_callback() called")

    
    debug_7(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)
    filter_out_none(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)


    return


@phantom.playbook_block()
def debug_7(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("debug_7() called")

    regex_extract_url__result = phantom.collect2(container=container, datapath=["regex_extract_url:custom_function_result.data.extracted_url","regex_extract_url:custom_function_result.data.input_string"])

    regex_extract_url_data_extracted_url = [item[0] for item in regex_extract_url__result]
    regex_extract_url_data_input_string = [item[1] for item in regex_extract_url__result]

    parameters = []

    parameters.append({
        "input_1": regex_extract_url_data_extracted_url,
        "input_2": ["from"],
        "input_3": regex_extract_url_data_input_string,
        "input_4": ["debug from Regex Extract"],
        "input_5": None,
        "input_6": None,
        "input_7": None,
        "input_8": None,
        "input_9": None,
        "input_10": None,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_7")

    return


@phantom.playbook_block()
def filter_out_none(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("filter_out_none() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["regex_extract_url:custom_function_result.data.extracted_url", "!=", None]
        ],
        conditions_dps=[
            ["regex_extract_url:custom_function_result.data.extracted_url", "!=", None]
        ],
        name="filter_out_none:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        debug_2(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def debug_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("debug_2() called")

    filtered_cf_result_0 = phantom.collect2(container=container, datapath=["filtered-data:filter_out_none:condition_1:regex_extract_url:custom_function_result.data.extracted_url"])

    filtered_cf_result_0_data_extracted_url = [item[0] for item in filtered_cf_result_0]

    parameters = []

    parameters.append({
        "input_1": ["from filter"],
        "input_2": filtered_cf_result_0_data_extracted_url,
        "input_3": None,
        "input_4": None,
        "input_5": None,
        "input_6": None,
        "input_7": None,
        "input_8": None,
        "input_9": None,
        "input_10": None,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_2")

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    filtered_cf_result_0 = phantom.collect2(container=container, datapath=["filtered-data:filter_out_none:condition_1:regex_extract_url:custom_function_result.data.extracted_url"])

    filtered_cf_result_0_data_extracted_url = [item[0] for item in filtered_cf_result_0]

    output = {
        "url": filtered_cf_result_0_data_extracted_url,
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_playbook_output_data(output=output)

    return