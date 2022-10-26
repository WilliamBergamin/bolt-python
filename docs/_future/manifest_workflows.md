---
title: Manifest workflows
order: 4
slug: manifest-workflows
lang: en
layout: future
---

<div class="section-content">

Your app can use functions by referencing them in a Workflow. Your functions and the ones provided by slack can be used as a step in Workflows.

Workflows are invoked by [Triggers](/bolt-python/future/triggers). You will need to set up a trigger to use your workflow.

trigger → workflow → step → function

`manifest.json` is where you define your workflows. `workflows` is a dictionary with `key:value` pair

- `key`, `string` defining the `workflow_id`
- `value`, [workflow object](#workflow)
  
##### workflow

- `title`, `string` defining the title
- `description`, `string` defining the description
- `input_parameters`, [parameters object](#parameters) defining the inputs
- `steps`, `list` of [step objects](#step) defining the steps

##### step

- `id`, `string` defining the order of the steps
- `function_id`, `string` defining the `function_id` of the function to evoke
- `inputs`, `dict[string:string]` of the inputs to provide to the function

</div>

<div>
```json
  "workflows": {
    "sample_workflow": {
      "title": "Sample workflow",
      "description": "A sample workflow",
      "input_parameters": {
        "properties": {
          "channel": {
            "type": "slack#/types/channel_id"
          }
        },
        "required": [
          "channel"
        ]
      },
      "steps": [
        {
          "id": "0",
          "function_id": "#/functions/sample_function",
          "inputs": {
            "message": "{{inputs.channel}}"
          }
        },
        {
          "id": "1",
          "function_id": "slack#/functions/send_message",
          "inputs": {
            "channel_id": "{{inputs.channel}}",
            "message": "{{steps.0.updatedMsg}}"
          }
        }
      ]
    }
  }
```
</div>

<details class="secondary-wrapper" >
  
<summary class="section-head" markdown="0">
  <h4 class="section-head">Built in functions</h4>
</summary>

<div class="secondary-content">
Slack provides built in functions that can be used by a workflow to accomplish simple tasks, add these functions to your workflow steps in order to use them.

- <a href="https://api.slack.com/future/functions#send-message" target="_blank">Send message</a>
- <a href="https://api.slack.com/future/functions#open-a-form" target="_blank">Open a form</a>
- <a href="https://api.slack.com/future/functions#create-channel" target="_blank">Create channel</a>

Refer to <a href="https://api.slack.com/future/functions" target="_blank">the built-in functions document</a> to learn the available built-in functions.
</div>

```json
    "$comment": "A step to post the user name to a channel"
    "steps": [
      {
        "id": "0",
        "function_id": "slack#/functions/send_message",
        "inputs": {
          "channel_id": "{{inputs.channel}}",
          "message": "{{inputs.user_name}}"
        }
      }
    ]
```

</details>
