---
title: Manifest
lang: en
slug: manifest
order: 2
layout: future
---


<div class="section-content">

Your project should contain a `manifest.json` file that defines your App's manifest, where you can configure your app. Refer to <a href="https://api.slack.com/reference/manifests" target="_blank">app manifest documentation</a> to learn the available manifest configurations.

Notably This file informs slack of the definitions for:

* [functions](/bolt-python/concepts#manifest-functions)
* [workflows](/bolt-python/concepts#manifest-workflows)

`manifest.json` should be located in a `manifest/` folder at the top level of your project.

<pre class="structure">
.
├── ...
├── manifest                      # folder with app manifest and triggers
│   ├── manifest.json             # app manifest definition
│   └── triggers                  # folder with trigger files
│       ├── sample_trigger.json   # trigger definition
│       └── ...
└── ...
</pre>

</div>

<div>
```json
{
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

##### parameters

* `properties`, [properties definition](#properties)
* `required`, `list` of `string` defining the property names required by the function

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

##### properties

`dictionary` with `key`:`value` pair

* `key`, `string` defining the property name
* `value`, [property definition](#property)

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

##### property

* `type`, `string` defining the property type
* `description`, `string` defining the property description

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
