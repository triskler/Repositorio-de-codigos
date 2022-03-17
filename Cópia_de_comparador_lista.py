{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Cópia de comparador_lista.py",
      "provenance": [],
      "authorship_tag": "ABX9TyO4PHp0uDQUIGFNck5aEf5C",
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
        "<a href=\"https://colab.research.google.com/github/triskler/Repositorio-de-codigos/blob/main/C%C3%B3pia_de_comparador_lista.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xt5x1DzoJ8Hc"
      },
      "source": [
        "def common_letters(string_one, string_two):\n",
        "  common = []\n",
        "  for letter in string_one:\n",
        "    if (letter in string_two) and not (letter in common):\n",
        "      common.append(letter)\n",
        "  return common\n",
        "  # Código que compara os dois grupos e imprimi os contidos "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "oPy0uxFPKYo0"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}