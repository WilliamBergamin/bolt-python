---
title: Manifest
lang: en
slug: manifest
order: 2
layout: future
---


<div class="section-content">

Your project should contain a `manifest.json` file that defines your App's manifest, where you can configure your app. Refer to [app manifest documentation](https://api.slack.com/reference/manifests) to learn the available manifest configurations.

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
