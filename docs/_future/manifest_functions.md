---
title: Manifest functions
order: 3
slug: manifest-functions
lang: en
layout: future
---

<div class="section-content">
Your App can [listen to custom functions](/bolt-python/concepts#functions). Your functions must be defined in your [App Manifest](/bolt-python/concepts#manifest) in order for Slack to know of its existence.

`manifest.json` is where you define your functions. `functions` is a `dictionary` with `key`:`value` pair:

- `key` is the function `callback_id`
- `value` a [function definition](#function)
  
##### function

- `title` a string containing the title
- `description` a string containing the description
- `input_parameters` a [parameters](#parameters) defining the inputs
- `output_parameters` a [parameters](#parameters) defining the outputs

##### parameters

- `properties` is a [properties definition](#properties)
- `required` is a list of strings containing the property names required by the function

##### properties

`dictionary` with `key`:`value` pair

- `key` is the property name
- `value` is a [property definition](#property)

##### property

- `type` a string defining the property type
- `description` a string containing the property description

</div>

<div>
```json
    "functions": {
      "sample_function": {
        "title": "Sample function",
        "description": "A sample function",
        "input_parameters": {
          "properties": {
            "message": {
              "type": "string",
              "description": "Message to be posted"
            }
          },
          "required": [
            "message"
          ]
        },
        "output_parameters": {
          "properties": {
            "updatedMsg": {
              "type": "string",
              "description": "Updated message to be posted"
            }
          },
          "required": [
            "updatedMsg"
          ]
        }
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

- [Send message](https://api.slack.com/future/functions#send-message)
- [Open a form](https://api.slack.com/future/functions#send-message)
- [Create channel](https://api.slack.com/future/functions)

Refer to [the built-in functions document](https://api.slack.com/future/functions) to learn the available built-in functions.
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
