---
title: App manifest
lang: en
slug: app-manifests
order: 1
---


<div class="section-content">

An app's manifest is where you can configure its name and scopes, declare the functions your app will use, and more.

</div>

<div>
```json
{
  "_metadata": {
    "major_version": 2,
    "minor_version": 2
  },
  "display_information": {
    "name": "Bolt Template App TEST"
  },
  "features": {
    "app_home": {
      "home_tab_enabled": false,
      "messages_tab_enabled": true,
      "messages_tab_read_only_enabled": true
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
        "chat:write.public"
      ]
    }
  },
  "settings": {
    "interactivity": {
      "is_enabled": true
    },
    "org_deploy_enabled": true,
    "socket_mode_enabled": true,
    "token_rotation_enabled": false
  },
  "functions": {},
  "types": {},
  "workflows": {},
  "outgoing_domains": []
}
```
</div>
