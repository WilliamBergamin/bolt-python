---
title: Manifest functions
order: 3
slug: manifest-functions
lang: en
layout: future
---

<div class="section-content">
Your app can [listen to custom functions](/bolt-python/concepts#functions). Your functions must be defined in your [app manifest](/bolt-python/concepts#manifest) in order for Slack to know of their existence.

`manifest.json` is where you define your functions.

<table id="functions_dict">
  <tr>
    <th>
      <h5 id="functions_dict">functions</h5>
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
      <a href="#function">function object</a>
    </td>
    <td>defines the function</td>
  </tr>
</table>

<table id="function">
  <tr>
    <th>
      <h5>function</h5>
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
      <code>output_parameters</code>
    </td>
    <td>
      <a href="#parameters">parameters object</a>
    </td>
    <td>defines the outputs</td>
  </tr>
</table>

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
