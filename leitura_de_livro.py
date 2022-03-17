{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/triskler/Repositorio-de-codigos/blob/main/leitura_de_livro.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "background_save": true
        },
        "id": "UwQ_NBEVzgf1"
      },
      "outputs": [],
      "source": [
        "#abertura do arquivo\n",
        "name = input('Insira o arquivo:')\n",
        "handle = open(name)\n",
        "\n",
        "#separando linhas e palavras\n",
        "#montando dicionario e contando palavras\n",
        "counts = dict()\n",
        "for line in handle:\n",
        "  words = line.split()\n",
        "  for word in words:\n",
        "    counts[word] = counts[word].get(word, 0) + 1\n",
        "#Neste ponto já temos um histograma ==>\n",
        "#selecionando a palavra mais mencionada \n",
        "\n",
        "bigWord = None\n",
        "bigCount = None\n",
        "for word,count in counts.items():\n",
        "  if bigCount is None or count > bigCount:\n",
        "    bigWord = word\n",
        "    bigCount = count\n",
        "\n",
        "#saida de dados\n",
        "\n",
        "print(bigWord, bigCount)\n",
        "\n",
        "\n",
        "\n"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "leitura de livro",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMAZ1obd/qpe3VfOgCFZVDr",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}