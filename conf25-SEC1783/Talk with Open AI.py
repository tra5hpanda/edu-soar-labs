"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'format_open_ai_text_and_prompt' block
    format_open_ai_text_and_prompt(container=container)

    return

@phantom.playbook_block()
def format_open_ai_text_and_prompt(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_open_ai_text_and_prompt() called")

    template = """{{\"model\": \"{0}\", \"input\": \"{1}\" }}"""

    # parameter list for template variable replacement
    parameters = [
        "playbook_input:model",
        "playbook_input:input"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_open_ai_text_and_prompt")

    format_endpoint_open_ai(container=container)

    return


@phantom.playbook_block()
def format_endpoint_open_ai(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_endpoint_open_ai() called")

    template = """responses"""

    # parameter list for template variable replacement
    parameters = []

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_endpoint_open_ai")

    format_headers(container=container)

    return


@phantom.playbook_block()
def format_headers(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_headers() called")

    template = """{\"Content-Type\": \"application/json\"}\n"""

    # parameter list for template variable replacement
    parameters = []

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_headers")

    ask_open_ai(container=container)

    return


@phantom.playbook_block()
def ask_open_ai(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("ask_open_ai() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    format_open_ai_text_and_prompt = phantom.get_format_data(name="format_open_ai_text_and_prompt")
    format_headers = phantom.get_format_data(name="format_headers")
    format_endpoint_open_ai = phantom.get_format_data(name="format_endpoint_open_ai")

    parameters = []

    if format_endpoint_open_ai is not None:
        parameters.append({
            "body": format_open_ai_text_and_prompt,
            "headers": format_headers,
            "location": format_endpoint_open_ai,
            "verify_certificate": False,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("post data", parameters=parameters, name="ask_open_ai", assets=["open ai"])

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ask_open_ai_result_data = phantom.collect2(container=container, datapath=["ask_open_ai:action_result.summary.status_code"])

    ask_open_ai_summary_status_code = [item[0] for item in ask_open_ai_result_data]

    output = {
        "update_kv_store_status": ask_open_ai_summary_status_code,
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