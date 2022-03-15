{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "web browser",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyM+7FGzN4/NzoFamQA5Wuuf",
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
        "<a href=\"https://colab.research.google.com/github/triskler/Repositorio-de-codigos/blob/main/web_browser.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import socket\n",
        "\n",
        "mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n",
        "mysock.connect(('data.pr4e.org', 80))\n",
        "cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\\r\\n\\r\\n'.encode()\n",
        "mysock.send(cmd)\n",
        "\n",
        "while True:\n",
        "    data = mysock.recv(512)\n",
        "    if len(data) < 1:\n",
        "        break\n",
        "    print(data.decode(),end='')\n",
        "mysock.close()\n",
        "\n"
      ],
      "metadata": {
        "id": "UwQ_NBEVzgf1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f4085963-9c3a-45cd-8281-515a73da66ae"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "HTTP/1.1 200 OK\r\n",
            "Date: Tue, 15 Mar 2022 17:26:10 GMT\r\n",
            "Server: Apache/2.4.18 (Ubuntu)\r\n",
            "Last-Modified: Sat, 13 May 2017 11:22:22 GMT\r\n",
            "ETag: \"a7-54f6609245537\"\r\n",
            "Accept-Ranges: bytes\r\n",
            "Content-Length: 167\r\n",
            "Cache-Control: max-age=0, no-cache, no-store, must-revalidate\r\n",
            "Pragma: no-cache\r\n",
            "Expires: Wed, 11 Jan 1984 05:00:00 GMT\r\n",
            "Connection: close\r\n",
            "Content-Type: text/plain\r\n",
            "\r\n",
            "But soft what light through yonder window breaks\n",
            "It is the east and Juliet is the sun\n",
            "Arise fair sun and kill the envious moon\n",
            "Who is already sick and pale with grief\n"
          ]
        }
      ]
    }
  ]
}