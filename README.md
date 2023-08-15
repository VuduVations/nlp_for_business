# Stoked Delivery Chat

Welcome to the GitHub repository of the Stoked Delivery Chat! This repository contains a code snippet that leverages Vertex AI and Gradio to deploy a conversational model that can assist with various inquiries related to Stoked Delivery.

# Prerequisites

Python 3.6 or later: If you do not have Python installed, download it from here.

Google Colab: This code is tailored to run on Google Colab. If you wish to run it locally, you might need to adjust the authentication mechanism.

# Dependencies: Install the required packages using pip:

```bash
pip install vertexai gradio google-colab
```

# How to Use

Clone this repository:

```bash
git clone [<repository-url>](https://github.com/botvoodoo/nlp_for_business/edit/main/README.MD)
```

Navigate to the cloned directory:

```bash
cd <repository-dir>
```

If you're running the code locally, make sure to provide the appropriate authentication credentials for Vertex AI and set your GOOGLE_APPLICATION_CREDENTIALS.

# Run the code:

```bash
python food_delivery_genchat.py
```

Access the Gradio interface that will be displayed in the terminal. If running on Google Colab, you'll get a public link to access the interface.

# Features

Customizable Parameters: You can adjust the conversation's parameters like temperature, token limit, etc., to suit your requirements.

Interactive UI: Gradio offers an interactive interface for you to communicate with the model.

Secure: The allow_screenshots parameter is set to False, ensuring the interface is not captured inadvertently.

# Contributing

If you would like to contribute to the development of this chat model or spot any bugs, please raise an issue or submit a pull request!

# License

This project is licensed under the GNU GENERAL PUBLIC LICENSE. See the LICENSE.md file for details.

# Acknowledgments

Vertex AI for providing the language model capabilities.
Gradio for offering an easy-to-use interface for model interactions.
