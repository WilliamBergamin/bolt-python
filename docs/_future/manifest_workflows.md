---
title: Manifest workflows
order: 4
slug: manifest-workflows
lang: en
layout: future
---

<div class="section-content">
On the next-generation platform, you can build **custom functions**, reusable building blocks of automation that are deployed to our infrastructure and accept inputs, perform some calculations, and provide outputs. Functions can be used as steps in [Workflows](/bolt-python/future/workflows)&mdash;and Workflows are invoked by [Triggers](/bolt-python/future/triggers).

To create a function, we need to do the following:

- [define the function](#define) in the Manifest;
- [implement the function](#implement) in its respective source file;

</div>

<details class="secondary-wrapper" >
  
<summary class="section-head" markdown="0">
  <h4 class="section-head">Built in functions</h4>
</summary>

<div class="secondary-content">
Slack provides built in functions your work

</div>

```python
# Matches all modified messages
@app.event({
    "type": "message",
    "subtype": "message_changed"
})
def log_message_change(logger, event):
    user, text = event["user"], event["text"]
    logger.info(f"The user {user} changed the message to {text}")
```

</details>
