---
title: Overview of steps from apps
lang: en
slug: /concepts/steps
---

:::danger

Steps from apps are a deprecated feature.

Steps from apps are different than, and not interchangeable with, Slack automation workflows. We encourage those who are currently publishing steps from apps to consider the new [Slack automation features](https://api.slack.com/automation), such as custom steps for Bolt.

Please [read the Slack API changelog entry](https://api.slack.com/changelog/2023-08-workflow-steps-from-apps-step-back) for more information.

:::

Steps from apps for legacy workflows are now deprecated. Use new [custom steps](https://api.slack.com/automation/functions/custom-bolt).

Steps from apps allow your app to create and process steps that users can add using [Workflow Builder](https://api.slack.com/workflows).

Steps from apps are made up of three distinct user events:

- Adding or editing the step in a Workflow
- Saving or updating the step's configuration
- The end user's execution of the step

All three events must be handled for a step from app to function.

Read more about steps from apps in the [API documentation](https://api.slack.com/workflows/steps).