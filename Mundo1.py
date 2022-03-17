{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Mundo1.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNliF1QdQT+3DPAr7ar+vOJ",
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
        "<a href=\"https://colab.research.google.com/github/triskler/Repositorio-de-codigos/blob/main/Mundo1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import math"
      ],
      "metadata": {
        "id": "Hu2EPdTzIbjW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Dois formatos de impressão"
      ],
      "metadata": {
        "id": "4IzfioNqDxK1"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "GQI7mVFgyEdY"
      },
      "outputs": [],
      "source": [
        "print(\"olá, mundo\")\n",
        "print(f'olá, mundo')"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# entrada de dados e saida de dados"
      ],
      "metadata": {
        "id": "QAdDzcYEDvdE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "name = input(\"Digite seu nome: \")\n",
        "print(\"É um prazer te conhecer \"+ name )"
      ],
      "metadata": {
        "id": "IJRaLFg7ybj0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#formato de função e saida em impressão, tambem pode ser retornado"
      ],
      "metadata": {
        "id": "boj4ZkO3EDXM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def soma (num1,num2):\n",
        "  return num1 + num2\n"
      ],
      "metadata": {
        "id": "St-AU6lp0XPn"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## funcoes nativas para analilse de variavel\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "NWMmkn0iEKf6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "var = input(\"Digite algo: \")\n",
        "print(f'É alfabético? {var.isalpha()}')\n",
        "print(f'É numerico? {var.isnumeric()}')\n",
        "print(f'É alfanumerico? {var.isalnum()}')\n",
        "print(f'Esta em maiuscula? {var.isupper()}')\n",
        "print(f'Esta em minuscula? {var.islower()}')\n",
        "print(f'Está capitalizada? {var.istitle()}')"
      ],
      "metadata": {
        "id": "eXCChykH20JH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "`Impressão com variabilidade `"
      ],
      "metadata": {
        "id": "C9FQDEzJFHRn"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data = int(input(\"Digite um numero: \"))\n",
        "print(f'Você digitou o numero {data}')\n",
        "print(f'Seu antecessor é {data-1} e seu sucessor é {data+1}')"
      ],
      "metadata": {
        "id": "R7BmFMT9DsY7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "`Operadores aritiméticos com variavel`"
      ],
      "metadata": {
        "id": "R0ZSl6bKFdXR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "data = int(input(\"Digite um numero: \"))\n",
        "sqrt = math.sqrt(data)\n",
        "print(f'O dobro de {data} é {data * 2}')\n",
        "print(f'O triplo de {data} é {data * 3}')\n",
        "print(f'Sua raiz quadrada é {int(sqrt)}')"
      ],
      "metadata": {
        "id": "JuPpwKNOHP-N"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Média aritimética com especificação de casas decimais"
      ],
      "metadata": {
        "id": "RVm9bpUJKpa7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "nota1 = float(input(\"Digite a primeira nota: \"))\n",
        "nota2 = float(input(\"Digite o segunda nota: \"))\n",
        "media = (nota1 + nota2) / 2\n",
        "print(f'A média do Aluno é: {media}')"
      ],
      "metadata": {
        "id": "xZsb3HNvKvKW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Conversor de medidas"
      ],
      "metadata": {
        "id": "iupsFdNML5lo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data = int(input(\"Digite a medida em metros: \"))\n",
        "print(f'{data} metros, corresponde a {data / 1000} kilometros')\n",
        "print(f'corresponde a {data / 100} Hectometros')\n",
        "print(f'corresponde a {data / 10} Decametros')\n",
        "print(f'corresponde a {data * 10} Decimetros')\n",
        "print(f'corresponde a {data * 100} Centímetros')\n",
        "print(f'corresponde a {data * 1000} Milímetros')\n"
      ],
      "metadata": {
        "id": "xrufwHNgL83c"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Tabuada do numero informado"
      ],
      "metadata": {
        "id": "-6jYbVuCUGxg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data = int(input(\"Digite um numero para ver sua tabuada: \"))\n",
        "print(f'A tabuada do {data} é: ')\n",
        "print(f'{data} x 1 = {data}')\n",
        "print(f'{data} x 2 = {data * 2}')\n",
        "print(f'{data} x 3 = {data * 3}')\n",
        "print(f'{data} x 4 = {data * 4}')\n",
        "print(f'{data} x 5 = {data * 5}')\n",
        "print(f'{data} x 6 = {data * 6}')\n",
        "print(f'{data} x 7 = {data * 7}')\n",
        "print(f'{data} x 8 = {data * 8}')\n",
        "print(f'{data} x 9 = {data * 9}')\n",
        "print(f'{data} x 10 = {data * 10}')\n",
        "print(\"-\" * 10)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "spDnvUSEULLO",
        "outputId": "dcb2f38e-d146-432f-fe68-b2024568b5ca"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um numero para ver sua tabuada: 8\n",
            "A tabuada do 8 é: \n",
            "8 x 1 = 8\n",
            "8 x 2 = 16\n",
            "8 x 3 = 24\n",
            "8 x 4 = 32\n",
            "8 x 5 = 40\n",
            "8 x 6 = 48\n",
            "8 x 7 = 56\n",
            "8 x 8 = 64\n",
            "8 x 9 = 72\n",
            "8 x 10 = 80\n",
            "----------\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Conversor de moeda"
      ],
      "metadata": {
        "id": "K-YDwhvLrSdl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data = float(input(\"Valor em reais: \"))\n",
        "print(f'R${data} correspondem a US${data / 5.08}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wx5-hHPCrWu8",
        "outputId": "d483c743-de56-46ca-d536-5ed536bf43e5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Valor em reais: 20\n",
            "R$20.0 correspondem a US$3.937007874015748\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Orçamento de pintura"
      ],
      "metadata": {
        "id": "7Zb86PK5us9A"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data = float(input(\"Digite a altura da parede: \"))\n",
        "data2 = float(input(\"Digite a largura da parede: \"))\n",
        "\n",
        "area = data * data2\n",
        "print(f'A área da parede é {area} m2')\n",
        "\n",
        "tinta = area / 2\n",
        "print(f'Serão necessários {tinta} litros para pintar esta parede.')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kfQn7JFKuyFY",
        "outputId": "5c152437-8495-4ed2-b9da-6d5b2e7fc3e4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a altura da parede: 1.8\n",
            "Digite a largura da parede: 3.75\n",
            "A área da parede é 6.75 m2\n",
            "Serão necessários 3.375 litros para pintar esta parede.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Calculo de desconto"
      ],
      "metadata": {
        "id": "jyqeXXFJwINs"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data = float(input(\"Digite o valor: \"))\n",
        "data2 = int(input(\"Digite o desconto: \"))\n",
        "\n",
        "valor = data * (data2/100)\n",
        "resultado = float(data - valor)\n",
        "\n",
        "print(f'O valor de R${data} com desconto de {data2}%:')\n",
        "print(f'R${resultado}')"
      ],
      "metadata": {
        "id": "h29Ecu6RwLNN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Reajuste salarial"
      ],
      "metadata": {
        "id": "7k27wfyCzo3o"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data = float(input(\"Digite o sálario do funcionario: \"))\n",
        "data2 = int(input(\"Digite o reajuste: \"))\n",
        "\n",
        "valor = data * (data2/100)\n",
        "resultado = data + valor\n",
        "print(f'O salário do funcionário passou de R${data} para R${resultado} aplicando {data2}% de reajuste.')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cQOVcpxFz1_2",
        "outputId": "3195002c-5d48-46c2-b929-755a4d3a2534"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o sálario do funcionario: 3452.67\n",
            "Digite o reajuste: 10\n",
            "O salário do funcionário passou de R$3452.67 para R$3797.937 aplicando 10% de reajuste.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Conversor de Temperatura"
      ],
      "metadata": {
        "id": "GiwNLec91IDi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data = float(input(\"Digite a temperatura em Celsius: \"))\n",
        "valor = (data * 1.8) + 32\n",
        "\n",
        "print(f'A temperatura de {data} Celcius corresponde a {valor} em graus Fahrenheit ')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K0rVHaZw1Ofl",
        "outputId": "b57b4e86-38f5-4e77-8914-abd202157e70"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a temperatura em Celsius: 38\n",
            "A temperatura de 38.0 Celcius corresponde a (100.4, 2) em graus Fahrenheit \n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Calculo de valor de locação de carro"
      ],
      "metadata": {
        "id": "WO3iC19h3WPP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data = int(input(\"Quantos dias estava em posse do carro: \"))\n",
        "data2 = float(input(\"Numero de kilometros rodados: \"))\n",
        "\n",
        "resultado = (60 * data) + (data2 * 0.15) \n",
        "print(f'O valor a pagar é de R${resultado}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "v_59xko13aqv",
        "outputId": "ab31131b-b45b-40e3-999f-378c286bb44f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Quantos dias estava em posse do carro: 33\n",
            "Numero de kilometros rodados: 200\n",
            "O valor a pagar é de R$2010.0 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Quebrar um float em inteiro e resto"
      ],
      "metadata": {
        "id": "0mnUFC-Z4mW1"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data = float(input(\"Digite um numero real: \"))\n",
        "\n",
        "inteiro = int(data)\n",
        "print(f'O numero {data} possui {inteiro} inteiros.')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "v2wa4Vlf4sb9",
        "outputId": "f9148bcc-7e8d-4205-cc76-8f5e204b4252"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um numero real: 67.567\n",
            "O numero 67.567 possui 67 inteiros.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Calculo do comprimento tode hipotenusa "
      ],
      "metadata": {
        "id": "ROP8BDjN5sGu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "data = float(input(\"Digite o comprimento do cateto oposto: \"))\n",
        "data2 = float(input(\"Digite o comprimento do cateto adjascente: \"))\n",
        "\n",
        "hipot = math.sqrt((data ** 2) + (data2 **2))\n",
        "\n",
        "print(f'O comprimento da hipotenusa é {hipot}')"
      ],
      "metadata": {
        "id": "e3CkNkIn5znc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Sorteio de pessoa aleatória"
      ],
      "metadata": {
        "id": "1k2ZvAth8B48"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "data = input(\"Digite o primeiro nome: \")\n",
        "data2 = input(\"Digite o segundo nome: \")\n",
        "data3 = input(\"Digite o terceiro nome: \")\n",
        "data4 = input(\"Digite o quarto nome: \")\n",
        "\n",
        "lista = [data, data2, data3, data4]\n",
        "escolhido = random.choice(lista)\n",
        "\n",
        "print(f'O escolhido foi {escolhido}')\n"
      ],
      "metadata": {
        "id": "RllA4QFG8Gpz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Verificador de numero"
      ],
      "metadata": {
        "id": "UxOjQlcmo84b"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data = input(\"Digite um numero: \")\n",
        "if(len(data) == 4):\n",
        "  print(f'Este numero tem: ')\n",
        "  print(f'{data[-1]} unidades')\n",
        "  print(f'{data[-2]} dezenas')\n",
        "  print(f'{data[-3]} centenas')\n",
        "  print(f'{data[-4]} milhares')\n",
        "elif(len(data) == 3):\n",
        "  print(f'Este numero tem: ')\n",
        "  print(f'{data[-1]} unidades')\n",
        "  print(f'{data[-2]} dezenas')\n",
        "  print(f'{data[-3]} centenas')\n",
        "elif(len(data) == 2):\n",
        "  print(f'Este numero tem: ')\n",
        "  print(f'{data[-1]} unidades')\n",
        "  print(f'{data[-2]} dezenas')\n",
        "else:\n",
        "  print(f'Este numero tem: ')\n",
        "  print(f'{data[-1]} unidades')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9qtgNJOqpyiR",
        "outputId": "34022902-2e67-4392-e456-3a2558bb4855"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um numero: 567\n",
            "Este numero tem: \n",
            "7 unidades\n",
            "6 dezenas\n",
            "5 centenas\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Verificador de string"
      ],
      "metadata": {
        "id": "tTqMPBS5xn6d"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data = input(\"Digite seu nome completo: \")\n",
        "data = data.upper()\n",
        "primeira = data.find('A')\n",
        "ultima = data.rfind('A')\n",
        "count = 0\n",
        "for palavra in data:\n",
        "  if(palavra == 'A'):\n",
        "    count += 1\n",
        "  else:\n",
        "    continue;\n",
        "print(f'A letra A aparece {count} vezes')\n",
        "print(f'A primeira ocorrencia foi no espaço {primeira +1}')\n",
        "print(f'A ultima ocorrencia foi na posição {ultima +1}')"
      ],
      "metadata": {
        "id": "kHzudlmdxsNV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Separação de primeiro e ultimo nomes"
      ],
      "metadata": {
        "id": "rFEoOb2C1DdY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data = (input(\"Digite o seu nome completo: \"))\n",
        "data = data.split()\n",
        "print(f'O seu primeiro nome é {data[0]} e seu ultimo nome é {data[-1]} ')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pcPrmkXm1Hvu",
        "outputId": "2ea97d04-809f-42a4-c0dd-0646f32a6484"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o seu nome completo: Rafael Brum da Fonseca\n",
            "O seu primeiro nome é Rafael e seu ultimo nome é Fonseca \n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Jogo de adivinhação"
      ],
      "metadata": {
        "id": "aR6n8oj33XcH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "data = int(input(\"Digite um numero de 0 a 3: \"))\n",
        "comp = random.randint(0,3)\n",
        "if(data == comp):\n",
        "  print(f'Você acertou! Escolhi o numero {comp}.')\n",
        "else:\n",
        "  print(f'Você errou! O numero escolhido foi {comp} e não {data}')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "li-vO2Rn3bxu",
        "outputId": "b4215aa9-1344-426c-d7ec-8430c162830d"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um numero de 0 a 3: 0\n",
            "Você acertou! Escolhi o numero 0.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Radar de velocidade"
      ],
      "metadata": {
        "id": "9kmwWiWUHC0B"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data = int(input(\"Insira a velocidade do veiculo: \"))\n",
        "limite = 90\n",
        "if data > limite +10:\n",
        "  print(f'MULTADO! Sua velocidade foi de {data} Km/h em uma via de {limite} km/h')\n",
        "elif data <= limite +10:\n",
        "  print(f'CUIDADO! sua velocidade é de {data} km/h numa via de {limite} km/h')\n",
        "else:\n",
        "  print(f'DIRIJA COM SEGURANÇA! Tenha uma boa viagem!')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "y8ZTa3nUHUi1",
        "outputId": "ae87e342-5ec9-4b6c-8075-0f5003831b83"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Insira a velocidade do veiculo: 99\n",
            "CUIDADO! sua velocidade é de 99 km/h numa via de 90 km/h\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Valor da passagem "
      ],
      "metadata": {
        "id": "2tb99kMxJhCS"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data = int(input(\"Digite o numero de pessoas: \"))\n",
        "data2 = float(input(\"Digite a distancia percorrida: \"))\n",
        "\n",
        "if data2 <= 100:\n",
        "  valor = 0.50\n",
        "elif data2 > 100:\n",
        "  valor = 0.40\n",
        "\n",
        "passagem = data * (data2 * valor)\n",
        "\n",
        "print(f' O valor da passagem para {data} pessoas, em uma distancia de {data2} Km,\\n custará {passagem:.2f}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b-znJVsuJlBC",
        "outputId": "f10bbdfb-c0e7-443f-ef2b-4b2f7900b4b9"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o numero de pessoas: 3\n",
            "Digite a distancia percorrida: 234\n",
            " O valor da passagem para 3 pessoas, em uma distancia de 234.0 Km,\n",
            " custará 280.80\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#calculo de ano bissexto"
      ],
      "metadata": {
        "id": "mwpUAdZMNKr4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data = int(input(\"Digite oano aser analisado: \"))\n",
        "\n",
        "if data % 4 == 0 and data % 100 != 0 or data % 400 == 0:\n",
        "  print(f'O ano {data} é BISSEXTO')\n",
        "else:\n",
        "  print(f'O ano {data} NÃO É BISSEXTO')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u4qcX-3tNQki",
        "outputId": "a027be20-6db2-4824-f160-bcfb7dea6a4b"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite oano aser analisado: 1700\n",
            "O ano 1700 NÃO É BISSEXTO\n"
          ]
        }
      ]
    }
  ]
}