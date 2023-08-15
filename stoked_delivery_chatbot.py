{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNt707Uke75f2NTyoitTlAf",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/botvoodoo/nlp_for_business/blob/main/stoked_delivery_chatbot.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "RIfiyv0tc0Mr"
      },
      "outputs": [],
      "source": [
        "!pip install \"shapely<2.0.0\"\n",
        "!pip install google-cloud-aiplatform>=1.29.0\n",
        "!pip install streamlit"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import auth as google_auth\n",
        "google_auth.authenticate_user()\n",
        "\n",
        "import vertexai\n",
        "from vertexai.language_models import TextGenerationModel\n",
        "\n",
        "vertexai.init(project=\"bionic-water-394610\", location=\"us-central1\")\n",
        "parameters = {\n",
        "    \"temperature\": 0.5,\n",
        "    \"max_output_tokens\": 256,\n",
        "    \"top_p\": 0.8,\n",
        "    \"top_k\": 40\n",
        "}\n",
        "model = TextGenerationModel.from_pretrained(\"text-bison@001\")\n",
        "response = model.predict(\n",
        "    'Who are Stoked Delivery?',\n",
        "    **parameters\n",
        ")\n",
        "print(f\"Response from Model: {response.text}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fb2U_leDc2Za",
        "outputId": "e1aba821-9f6c-42ec-ff07-a1786cf7a220"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Response from Model: Stoked Delivery is a delivery company that specializes in delivering food, drinks, and other items from local businesses to customers' homes. We offer a fast, reliable, and affordable delivery service that is perfect for busy people who don't have time to go out to get their own food.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import vertexai\n",
        "from vertexai.language_models import TextGenerationModel\n",
        "\n",
        "# Initialize Vertex AI\n",
        "vertexai.init(project=\"bionic-water-394610\", location=\"us-central1\")\n",
        "parameters = {\n",
        "    \"temperature\": 0.5,\n",
        "    \"max_output_tokens\": 256,\n",
        "    \"top_p\": 0.8,\n",
        "    \"top_k\": 40\n",
        "}\n",
        "model = TextGenerationModel.from_pretrained(\"text-bison@001\")\n",
        "\n",
        "# Streamlit app\n",
        "st.title('Vertex AI Chatbot')\n",
        "\n",
        "user_input = st.text_input(\"You: \", \"\")\n",
        "if user_input:\n",
        "    response = model.predict(user_input, **parameters)\n",
        "    st.write(f\"Bot: {response.text}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "50kG2f-1fLRh",
        "outputId": "46cfe300-ef2d-48c6-e912-c81e8001a695"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2023-08-15 18:02:44.103 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.10/dist-packages/ipykernel_launcher.py [ARGUMENTS]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "zsqq8Wkev4J7"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}