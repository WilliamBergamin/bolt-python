---
title: Manifest workflows
order: 4
slug: manifest-workflows
lang: en
layout: future
---

<div class="section-content">

Your app can use functions by referencing them in workflows. Your functions and the ones provided by slack can be used as a step in workflow definitions.

Workflows are invoked by [Triggers](/bolt-python/future/triggers). You will need to set up a trigger to use your workflow.

trigger → workflow → step → function

`manifest.json` is where you define your workflows.

<table id="workflows">
  <tr>
    <th>
      <h5>workflows</h5>
    </th>
    <th>
      <code>dictionary</code>
    </th>
    <th></th>
  </tr>
  <tr>
    <td>
      <code>key</code>
    </td>
    <td>
      <code>string</code>
    </td>
    <td>defines the function <code>callback_id</code></td>
  </tr>
  <tr>
    <td>
      <code>value</code>
    </td>
    <td>
      <a href="#workflow">workflow object</a>
    </td>
    <td>defines the function</td>
  </tr>
</table>

<table id="workflow">
  <tr>
    <th>
      <h5>workflow</h5>
    </th>
    <th>
      <code>object</code>
    </th>
    <th></th>
  </tr>
  <tr>
    <td>
      <code>title</code>
    </td>
    <td>
      <code>string</code>
    </td>
    <td>defines the title</td>
  </tr>
  <tr>
    <td>
      <code>description</code>
    </td>
    <td>
      <code>string</code>
    </td>
    <td>defines the description</td>
  </tr>
  <tr>
    <td>
      <code>input_parameters</code>
    </td>
    <td>
      <a href="#parameters">parameters object</a>
    </td>
    <td>defines the inputs</td>
  </tr>
  <tr>
    <td>
      <code>steps</code>
    </td>
    <td>
      <code>list[<a href="#parameters">parameters object</a>]</code>
    </td>
    <td>defines the steps</td>
  </tr>
</table>

<table id="step">
  <tr>
    <th>
      <h5>step</h5>
    </th>
    <th>
      <code>object</code>
    </th>
    <th></th>
  </tr>
  <tr>
    <td>
      <code>id</code>
    </td>
    <td>
      <code>string</code>
    </td>
    <td>defines the order of the steps</td>
  </tr>
  <tr>
    <td>
      <code>function_id</code>
    </td>
    <td>
      <code>string</code>
    </td>
    <td>defines the <code>function_id</code> of the function to evoke</td>
  </tr>
  <tr>
    <td>
      <code>inputs</code>
    </td>
    <td>
      <code>dict[string:string]</code>
    </td>
    <td>defines the inputs to provide to the function</td>
  </tr>
</table>

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
