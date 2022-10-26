---
title: Manifest functions
order: 3
slug: manifest-functions
lang: en
layout: future
---

<div class="section-content">
Your App can [listen to custom functions](/bolt-python/concepts#functions). Your functions must be defined in your [App Manifest](/bolt-python/concepts#manifest) in order for Slack to know of their existence.

`manifest.json` is where you define your functions. `functions` is a `dictionary` with `key`:`value` pair:

- `key`, `string` containing the function `callback_id`
- `value`, [function object](#function)
  
##### function

- `title`, `string` containing the title
- `description`, `string` containing the description
- `input_parameters`, [parameters object](#parameters) defining the inputs
- `output_parameters`, [parameters object](#parameters) defining the outputs

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
