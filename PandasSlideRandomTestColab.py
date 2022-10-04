{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyP11p090t3KhOzU0DCNjG/G",
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
        "<a href=\"https://colab.research.google.com/github/DavidSilvaProgrammer/-Softex-Modulo-2/blob/main/PandasSlideRandomTestColab.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iO0W0YKtWGnO",
        "outputId": "8208d4ca-5f12-43c0-b501-92370cbfcbaa"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "     Aluno  nota1  nota2  Média      Estado\n",
            "0  aluno_1      7     10    8.5   Aprovação\n",
            "1  aluno_2      3     10    6.5  Reprovação\n",
            "2  aluno_3      9      4    6.5  Reprovação\n",
            "3  aluno_4     10      6    8.0   Aprovação\n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "biscoito=pd.read_csv(\"/content/MediaAlunos - Página1.csv\")\n",
        "\n",
        "biscoito['Média']=(biscoito['nota1']+biscoito['nota2'])/2\n",
        "biscoito.loc[biscoito['Média']>=7,\"Estado\"]=\"Aprovação\"\n",
        "biscoito.loc[biscoito['Média']<7,\"Estado\"]=\"Reprovação\"\n",
        "\n",
        "print(biscoito)"
      ]
    }
  ]
}