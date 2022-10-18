---
title: App manifest
order: 1
slug: app-manifests
lang: en
layout: tutorial
permalink: /future/app-manifests
---
# App manifests <span class="label-beta">BETA</span>

<div class="section-content">
An app's manifest is where you can configure its name and scopes, declare the functions your app will use, and more.
</div>

---

## Configuring an app {#configuring-an-app}

Locate the file named `manifest.json` within your application. This will likely be in your project's root directory or a `manifest` folder.

Inside the manifest file, you will find an `module.exports = Manifest({})` block that defines the app's configuration. For the [Hello World application](https://github.com/slack-samples/bolt-python-starter-template/tree/future) in the Bolt for JavaScript Starter Template, it will look something like this:

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

---

## Next steps {#next-steps}

Now that you're acquainted with the Manifest, you can dive into the world of [built-in functions](/bolt-python/future/built-in-functions) and [custom functions](/bolt-python/future/custom-functions)!
