---
title: Manifest
lang: en
slug: manifest
order: 2
layout: future
---


<div class="section-content">

Your project should contain a `manifest.json` file that defines your app's manifest, where you can configure your app. Refer to <a href="https://api.slack.com/reference/manifests" target="_blank">app manifest documentation</a> to learn the available manifest configurations.

Notably this file informs slack of the definitions for:

* [functions](/bolt-python/concepts#manifest-functions)
* [workflows](/bolt-python/concepts#manifest-workflows)

`manifest.json` should be located at the top level of your project.

<pre class="structure">
.
├── ...
├── manifest.json             # app manifest definition
├── triggers                  # folder with trigger files
│   ├── sample_trigger.json   # trigger definition
│   └── ...
└── ...
</pre>

---

Be sure to include the following line in your `manifest.json` file in order to get type prediction & validation in your IDE.

```json
{
  "$schema": "https://raw.githubusercontent.com/slackapi/manifest-schema/main/manifest.schema.json",
  ...
}
```

</div>

<div>
```json
{
  "$schema": "https://raw.githubusercontent.com/slackapi/manifest-schema/main/manifest.schema.json",
  "_metadata": {
    "major_version": 2,
  },
  "display_information": {
    "name": "Bolt Template App TEST"
  },
  "features": {
    "app_home": {
      "home_tab_enabled": false,
    },
    "bot_user": {
      "display_name": "Bolt Template App TEST",
      "always_online": false
    }
  },
  "oauth_config": {
    "scopes": {
      "bot": [
        "chat:write",
      ]
    }
  },
  "settings": {
    "socket_mode_enabled": true,
  },
  "functions": {},
  "types": {},
  "workflows": {},
  "outgoing_domains": []
}
```
</div>

<details id="common-manifest-types" class="secondary-wrapper" >
  
<summary class="section-head" markdown="0">
  <h4 class="section-head">Common Manifest Types</h4>
</summary>

<div>

<div class="secondary-content">

<table id="parameters">
  <tr>
    <th>
      <h5>parameters</h5>
    </th>
    <th>
      <code>object</code>
    </th>
    <th></th>
  </tr>
  <tr>
    <td>
      <code>properties</code>
    </td>
    <td>
      <a href="#properties">properties object</a>
    </td>
    <td>defines the properties</td>
  </tr>
  <tr>
    <td>
      <code>required</code>
    </td>
    <td>
      <code>list[string]</code>
    </td>
    <td>defines the properties required by the function</td>
  </tr>
</table>

</div>

```json
  "$comment": "sample parameters object"
  "*_parameters":{
    "properties": {
      "property_0_name": {
        "type": "string",
        "description": "this is my first property"
      }
    },
    "required": [
      "property_name"
    ]
  }
```

</div>

<div>

<div class="secondary-content">

<table id="properties">
  <tr>
    <th>
      <h5>properties</h5>
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
    <td>defines the property name</td>
  </tr>
  <tr>
    <td>
      <code>value</code>
    </td>
    <td>
      <a href="#property">property object</a>
    </td>
    <td>defines the property</td>
  </tr>
</table>

</div>

```json
  "$comment": "sample properties dictionary"
  "properties": {
    "property_0_name": {
      "type": "string",
      "description": "this is my first property"
    },
    "property_1_name": {
      "type": "integer",
      "description": "this is my second property"
    }
  }
  
```

</div>

<div>

<div class="secondary-content">

<table id="property">
  <tr>
    <th>
      <h5>property</h5>
    </th>
    <th>
      <code>object</code>
    </th>
    <th></th>
  </tr>
  <tr>
    <td>
      <code>type</code>
    </td>
    <td>
      <code>string</code>
    </td>
    <td>defines the property type</td>
  </tr>
  <tr>
    <td>
      <code>description</code>
    </td>
    <td>
      <code>string</code>
    </td>
    <td>defines the property description</td>
  </tr>
</table>

</div>

```json
  "$comment": "sample property object"
  "property_0_name": {
    "type": "string",
    "description": "this is my first property"
  }
  
```

</div>

</details>
