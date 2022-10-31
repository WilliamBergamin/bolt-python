---
title: Getting started
order: 1
slug: getting-started-future
lang: en
layout: tutorial
permalink: /tutorial/getting-started-future
---

## Getting started <span class="label-beta">BETA</span>

<div class="section-content">
This guide will cover how to get started with your next-gen platform using Bolt for Python by setting up the Slack CLI and also installing the required dependencies.
</div>

---

### What is the next-generation platform? {#next-gen}

You can find all the answers to this question on Slack's <a href="https://api.slack.com/future/intro" target="_blank">official introduction page.</a>

<p class="alert alert_info"><ts-icon class="ts_icon_info_circle"></ts-icon>Our next-generation platform is currently in beta. <a href="https://api.slack.com/future/survey" target="_blank">Your feedback is most welcome.</a> - all feedback will help shape the future platform experience!</p>

---

### Setting up the CLI {#setting-up-cli}

To build a next-generation app with Bolt for Python, you'll need to get the Slack CLI.

**Install the Slack Cli** by following this [Quickstart Guide](https://api.slack.com/future/quickstart).

---

### Install dependencies {#install-dependencies}

Once the CLI is set up, make sure your machine has the most recent version of [Python](https://www.python.org/) installed. you can either install Python through a package manager (such as [Homebrew](https://brew.sh/) for Mac) or directly from the website.

---

### Accept the Beta Terms of Service {#accept-tos}

In order to use the next-generation platform features, you'll need to accept a Terms of Service for Slack Platform Beta. To do so, go to the Workspace Settings of the workspace you'll be developing with, then go to the Permissions tab. Find the "Slack Platform Beta" heading, then select the checkbox that says "I have read and agree to the Slack Platform Beta Service Terms" and save the section. Once you have accepted, the section will look like this:

![Beta Terms of Service](https://slack.dev/bolt-js/assets/beta-tos-future.png "Beta Terms of Service")

> 💡 You must be an admin of your workspace to be able to access the Workspace Settings and accept the Terms of Service.

Congratulations! You're now ready to start building using the next-generation Platform. 🎉 You can now proceed with either creating a new app by following the instructions below or <a href="/bolt-python/tutorial/migrate-existing-app" target="_blank">migrating an existing app</a>.

---

### Create a new app {#create-app}

Before you start developing with Bolt, you'll want to create a Slack app.

To create the app, you'll run the following command:

```zsh
slack create my-app -t slack-samples/bolt-python-starter-template -b future
```

This command creates an app through the CLI by cloning a specified template. In this case, the template is the <a href="https://github.com/slack-samples/bolt-python-starter-template/tree/future" target="_blank">Bolt for Python Starter Template</a> on the `future` branch. This starter template includes a "Hello World" example that demonstrates how to use <a href="/bolt-python/future/concepts#manifest-workflows" target="_blank">built-in</a> and <a href="/bolt-python/future/concepts#functions" target="_blank">custom</a> Functions, <a href="https://api.slack.com/future/triggers" target="_blank">Triggers</a> and <a href="/bolt-python/future/concepts#manifest-workflows" target="_blank">Workflows</a>.

Once the app is successfully created, you should see a message like this:

```txt
✨ my-app successfully created

🧭 Explore your project's README.md for documentation and code samples, and at any time run slack help to display a list of available commands

🧑‍🚀 Follow the steps below to try out your new project

1️⃣  Change into your project directory with: cd my-app

2️⃣  Develop locally and see changes in real-time with: slack run

3️⃣  When you're ready to deploy for production use: slack deploy

🔔 If you leave the workspace, you won’t be able to manage any apps you’ve deployed to it. Apps you deploy will belong to the workspace even if you leave the workspace
```

---

### Set up your trigger {#setup-trigger}

As mentioned, this app comes with preexisting functionality - it uses Functions, Workflows and a Trigger set up to kick things off. Let's run a command to initialize that Trigger via the CLI.

First, make sure you're in the project directory in your command line: `cd my-app`

Then, run the following command to create a Trigger:

```bash
slack triggers create --trigger-def "triggers/sample-trigger.json"      
```

The above command will create a trigger for the selected workspace. Make sure to select the workspace you want and that it is appended by `(dev)`. This will create a dev instance of your app. Once the trigger is successfully created, you should see an output like this:

```bash
⚡ Trigger created
   Trigger ID:   [ID]
   Trigger Type: shortcut
   Trigger Name: Sample Trigger
   URL: https://slack.com/shortcuts/[ID]/[Some ID]
```

The provided URL will be what you use to run your Trigger. Copy this URL and save it somewhere; you'll need it for later.

---

### Run your app {#run-your-app}

Now that your app and Trigger are successfully created, let's try running it!

```bash
# install the required project dependencies
pip install -r requirements.txt

# start a local development server
slack run
```

Executing `pip install -r requirements.txt` installs all the project requirements to your machine.

Executing `slack run` starts a local development server, syncing changes to your workspace's development version of your app.

You'll be prompted to select a workspace to install the app to&mdash;select the development instance of your workspace (you'll know it's the development version because the name has the string `(dev)` appended).

> 💡 If you don't see the workspace you'd like to use in the list, you can `CTRL + C` out of the `slack run` command and run `slack auth login`. This will allow you to authenticate in your desired workspace to have it show up in the list for `slack run`.

Once the app is successfully ran, you'll see output in your Terminal to indicate it's running, similar to what you would see with any other Bolt for Python app. You can search for the `⚡️ Bolt app is running! ⚡️` message to make sure that your app has successfully started up.

### Trigger your app's workflow {#trigger-workflow}

With your app running, access your workspace and paste the URL from the Trigger you created in the [previous step](/bolt-python/tutorial/getting-started-future#setup-trigger) into a message in a public channel.

> 💡 App Triggers are automatically saved as a channel bookmark under "Workflows" for easy access.

Send the message and click the "Run" button that appears. A modal will appear prompting you to enter information to greet someone in your Slack workspace. Fill out the requested information.

![Hello World modal](https://slack.dev/bolt-js/assets/hello-world-modal.png "Hello World modal")

Then, submit the form. In the specified channel submitted in the form, you should receive a message from the app tagging the submitted user. The message will also contain a randomly generated greeting and the message you wrote in the form.

The full app flow can be seen here:
![Hello World app](https://slack.dev/bolt-js/assets/hello-world-demo.gif "Hello World app")

---

### Next steps {#next-steps}

Now we have a working instance of a next-generation app in your workspace and you've seen it in action! You can explore on your own and dive into the code yourself here or continue your learning journey by diving into [App Manifests](/bolt-python/future/concepts#manifests) or looking into adding more [Functions](/bolt-python/future/concepts#functions), [Workflows](/bolt-python/future/concepts#manifest-workflows), and [Triggers](#setup-trigger) to your app!
