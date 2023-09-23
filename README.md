# Ngrok Tunnel Manager

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [How to Register for Ngrok and Get an API Key](#how-to-register-for-ngrok-and-get-an-api-key)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)

## Introduction

Ngrok Tunnel Manager is a simple graphical user interface (GUI) application that helps you manage [ngrok](https://ngrok.com/) tunnels. Ngrok is a service that allows you to expose your local web server to the internet for testing and development purposes. This tool allows you to create and manage ngrok tunnels with ease.

## Prerequisites

Before you can use Ngrok Tunnel Manager, you need to have the following prerequisites installed on your system:

- Python 3
- Tkinter library (usually included with Python)
- pyngrok library (pyngrok)
- webbrowser library (usually included with Python)

## How to Register for Ngrok and Get an API Key

To use this application, you will need an ngrok API key. Here's how to register for ngrok and obtain your API key:

1. Visit the [ngrok website](https://ngrok.com/) and sign up for an ngrok account if you don't already have one.

2. After signing in, go to the [ngrok dashboard](https://dashboard.ngrok.com/get-started).

3. Under the "Your Auth Token" section, you will find your API key. Copy this API key to use it in Ngrok Tunnel Manager.

## Installation

1. Clone this repository to your local machine:
```bash
git clone https://github.com/VargaBalazsAdam/Py-Publish-Localhost
```

2. Navigate to the project directory:
```bash
cd Py-Publish-Localhost
```

3. Install the required Python packages
```bash
pip install pyngrok
```


## Usage

1. Run the Ngrok Tunnel Manager application by executing the following command in the project directory:
```bash
main.py
```

2. The Ngrok Tunnel Manager GUI will open.

3. Set your ngrok API key:
- Enter your API key in the "API Key" field.
- Click the "Set API Key" button.

4. Select a port to create an ngrok tunnel for your local web server from the dropdown list or enter a custom port.

5. Click the "Create ngrok tunnel" button to create the tunnel.

6. The list of active tunnels will be displayed in the GUI. You can select a tunnel and click the "Open Tunnel in Browser" button to open it in your default web browser.

7. To exit the application, click the "Exit" button. This will also disconnect all ngrok tunnels.

## Features

- Set and save your ngrok API key.
- Create ngrok tunnels for various ports.
- List and manage active tunnels.
- Open tunnels in your default web browser.

## Contributing

Contributions to Ngrok Tunnel Manager are welcome. If you have any suggestions, bug reports, or feature requests, please open an issue on the [GitHub repository](https://github.com/VargaBalazsAdam/Py-Publish-Localhost).
