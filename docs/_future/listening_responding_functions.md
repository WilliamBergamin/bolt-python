---
title: Listening & responding to functions
lang: en
slug: functions
order: 5
layout: future
---

<div class="section-content">

Your app can use the `function()` method to listen to incoming function requests. The method requires a function `callback_id` of type `str`. Functions must eventually be completed with `complete()` to inform Slack that your app has processed the function request. There are two ways to complete a function with `complete()` which requires **one of two** keyword arguments `outputs` or `error`.

* `outputs` of type `dict` completes your function **successfully** and provide a dictionary containing the outputs of your function as defined in the apps manifest.
* `error` of type `str` completes your function **unsuccessfully** and provides a message containing information regarding why your function was not successful.

</div>

<div>
<span class="annotation">Refer to <a href="https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html" target="_blank">the module document</a> to learn the available listener arguments.</span>
```python
# The sample function simply outputs an input
@app.function("sample_function")
def sample_func(event, complete: Complete):
    try:
        message = event["inputs"]["message"]
        complete(outputs={"updatedMsg": f":wave: You submitted the following message: \n\n>{message}"})
    except Exception as e:
        complete(error="Cannot submit the message")
        raise e
```
</div>

<details class="secondary-wrapper">
<summary markdown="0">
<h4 class="secondary-header">Function Interactivity</h4>
</summary>

<div class="secondary-content">

The `function()` method returns a `SlackFunction` decorator object. This object can be used by your app to set up listeners for interactive behaviors such as [actions](/bolt-python/concepts#action-respond) and [views](/bolt-python/concepts#view_submissions). These interactive behaviors will be scoped to your function.

These listeners behave similarly to the ones assigned directly to your app. the notable difference is that `complete()` must be called once your function is completed.

</div>

```python
@app.function("sample_function")
def sample_func(event, complete: Complete):
    try:
        client.chat_postMessage(
            channel="a-channel-id",
            text="A new button appears",
            blocks=[
                {
                    "type": "actions",
                    "block_id": "approve-button",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Click",
                            },
                            "action_id": "sample_action",
                            "style": "primary",
                        },
                    ],
                },
            ],
        )
    except Exception as e:
        complete(error="Cannot post message")
        raise e

@sample_func.action("sample_action")
def update_message(ack, body, client, complete):
    try:
        ack()
        if "container" in body and "message_ts" in body["container"]:
            client.reactions_add(
                name="white_check_mark",
                channel=body["channel"]["id"],
                timestamp=body["container"]["message_ts"],
            )
        complete()
    except Exception as e:
        logger.error(e)
        complete(error="Cannot react to message")
        raise e
```

</details>
