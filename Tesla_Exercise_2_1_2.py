{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Tesla Exercise 2.1.2.ipynb",
      "provenance": [],
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
        "<a href=\"https://colab.research.google.com/github/TobAde/Tesla_Exercise/blob/main/Tesla_Exercise_2_1_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZTzfZyRNe5pD",
        "outputId": "5ed640f8-3589-4f28-82ad-27f966c1891c"
      },
      "source": [
        "# Installing pytest using pip\n",
        "!pip install pytest ipython_pytest"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: pytest in /usr/local/lib/python3.7/dist-packages (3.6.4)\n",
            "Collecting ipython_pytest\n",
            "  Downloading ipython_pytest-0.0.1.tar.gz (3.5 kB)\n",
            "Requirement already satisfied: more-itertools>=4.0.0 in /usr/local/lib/python3.7/dist-packages (from pytest) (8.8.0)\n",
            "Requirement already satisfied: atomicwrites>=1.0 in /usr/local/lib/python3.7/dist-packages (from pytest) (1.4.0)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.7/dist-packages (from pytest) (57.2.0)\n",
            "Requirement already satisfied: py>=1.5.0 in /usr/local/lib/python3.7/dist-packages (from pytest) (1.10.0)\n",
            "Requirement already satisfied: six>=1.10.0 in /usr/local/lib/python3.7/dist-packages (from pytest) (1.15.0)\n",
            "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.7/dist-packages (from pytest) (21.2.0)\n",
            "Requirement already satisfied: pluggy<0.8,>=0.5 in /usr/local/lib/python3.7/dist-packages (from pytest) (0.7.1)\n",
            "Building wheels for collected packages: ipython-pytest\n",
            "  Building wheel for ipython-pytest (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for ipython-pytest: filename=ipython_pytest-0.0.1-py3-none-any.whl size=3635 sha256=f18bb52e29fa087de73ba760a7a50b6b064e3b2da77ba893c8469c21e62cb3ad\n",
            "  Stored in directory: /root/.cache/pip/wheels/20/ee/88/a9c38f1db92e33abf00a2dde912e4488ac175f2113953fd16a\n",
            "Successfully built ipython-pytest\n",
            "Installing collected packages: ipython-pytest\n",
            "Successfully installed ipython-pytest-0.0.1\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2fd5oKVge8HI",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5dc8c3e4-7e4a-4c2d-c7f8-173548372ca8"
      },
      "source": [
        "import ipython_pytest\n",
        "%load_ext ipython_pytest"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "The ipython_pytest extension is already loaded. To reload it, use:\n",
            "  %reload_ext ipython_pytest\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5olo7VUermlM"
      },
      "source": [
        "  class Tesla:\n",
        "\n",
        "    def __init__(self, model: str, color: str, autopilot: bool = False, efficiency: float = 0.3):\n",
        "        self.__model = model\n",
        "        self.__color = color\n",
        "        self.__battery_charge = 99.9\n",
        "        self.__is_locked = True\n",
        "        self.__seats_count = 5\n",
        "        self.__autopilot = autopilot\n",
        "        self.__efficiency = 0.3\n",
        "     \n",
        "    @property\n",
        "    def seats_count(self) -> str:\n",
        "        return self.__seats_count\n",
        "\n",
        "    def autopilot(self, obsticle: str) -> str:\n",
        "        if self.__autopilot==False:\n",
        "            return \"Autopilot is not available\"\n",
        "        return f\"Tesla model {self.__model} avoids {obsticle}\"\n",
        "    \n",
        "    @seats_count.setter\n",
        "    def seats_count(self, new_seats: int) -> None:\n",
        "      '''\n",
        "      Sets the seats count to a new number not less than 2.\n",
        "\n",
        "      Parameters\n",
        "      ----------\n",
        "      new_seats:str \n",
        "      new number of seats\n",
        "\n",
        "      Return\n",
        "      ------\n",
        "      None\n",
        "      '''\n",
        "      if new_seats <2:\n",
        "          return self.seats_count  \n",
        "      else: \n",
        "            self.__seats_count = new_seats   \n",
        "            \n",
        "    def welcome(self) -> str:\n",
        "        raise NotImplementedError\n",
        "\n",
        "    def open_doors(self) -> str:\n",
        "        '''\n",
        "        Opens the door of the car if car is not locked\n",
        "\n",
        "        Parameters\n",
        "        -----------\n",
        "        None\n",
        "\n",
        "        Returns\n",
        "        -------\n",
        "        Str\n",
        "        '''  \n",
        "        if self.__is_locked ==True:\n",
        "            return \"Car is locked!\"\n",
        "        return \"Doors opens sideways\"\n",
        "\n",
        "    def unlock(self) -> bool:\n",
        "        self.__is_locked = False\n",
        "        return self.__is_locked \n",
        "\n",
        "    def check_battery_level(self) -> str:\n",
        "        return f\"Battery charge level is {self.__battery_charge}%\"\n",
        " \n",
        "    def charge_battery(self):\n",
        "        '''\n",
        "        Charges the battery_charge of the tesla to 100%\n",
        "        Calls the check_battery_level function\n",
        "\n",
        "        Parameters\n",
        "        ----------\n",
        "        None\n",
        "\n",
        "        Returns\n",
        "        -------\n",
        "        None\n",
        "  \n",
        "        '''\n",
        "        self.__battery_charge = 100   \n",
        "        self.check_battery_level() \n",
        "\n",
        "    def drive(self, travel_range: float):\n",
        "        battery_discharge_percent = travel_range * self.__efficiency\n",
        "        if self.__battery_charge - battery_discharge_percent >= 0:\n",
        "           self.__battery_charge -= battery_discharge_percent \n",
        "        return self.check_battery_level()\n",
        "            "
      ],
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "F3RgoWykgN-a"
      },
      "source": [
        "Unit tests"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9rKK0PzmfNrT",
        "outputId": "7e98ab6a-dfae-4aec-e4a9-376fedd7cc85"
      },
      "source": [
        "%%pytest\n",
        "def can_unlock_car():\n",
        "  tesla = Tesla('S', 'Black')\n",
        "  assert tesla.open_doors() == \"Car is locked!\"\n",
        "  tesla.unlock()\n",
        "  assert tesla.open_doors() == \"Doors opens sideways\"\n",
        "\n",
        "def check_battery_charge():\n",
        "  tesla = Tesla(\"S\", \"red\")\n",
        "  assert tesla.check_battery_level() == \"Battery charge level is 99.9%\"\n",
        "  assert tesla.drive(100) == \"Battery charge level is 69.9%\"\n",
        "  assert tesla.drive(420) == \"Battery charge level is 69.9%\"\n",
        "  tesla.charge_battery()\n",
        "  assert tesla.check_battery_level() == \"Battery charge level is 100%\""
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "============================= test session starts ==============================\n",
            "platform linux -- Python 3.7.11, pytest-3.6.4, py-1.10.0, pluggy-0.7.1\n",
            "rootdir: /tmp/tmpawdkysk1, inifile:\n",
            "plugins: typeguard-2.7.1\n",
            "collected 0 items\n",
            "\n",
            "=============================== warnings summary ===============================\n",
            "<undetermined location>\n",
            "  Module already imported so cannot be rewritten: typeguard\n",
            "\n",
            "-- Docs: http://doc.pytest.org/en/latest/warnings.html\n",
            "========================== 1 warnings in 0.07 seconds ==========================\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}