# 🐍 PyFlunt: Domain Notification Pattern

Implementação Python inspirada no [Flunt](https://github.com/andrebaltieri/flunt) (.NET) desenvolvido por @andrebaltieri

[![Último Lançamento no PyPI](https://img.shields.io/pypi/v/flunt.svg)](https://pypi.org/project/flunt/)
[![Downloads](https://pepy.tech/badge/flunt)](https://pepy.tech/project/flunt)
[![Gitter](https://img.shields.io/badge/chat-on%20gitter-yellow.svg)](https://matrix.to/#/#pyflunt:gitter.im)


[![Avaliação de Segurança](https://sonarcloud.io/api/project_badges/measure?project=fazedordecodigo_PyFlunt&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=fazedordecodigo_PyFlunt)
[![Avaliação de Confiabilidade](https://sonarcloud.io/api/project_badges/measure?project=fazedordecodigo_PyFlunt&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=fazedordecodigo_PyFlunt)
[![Avaliação de Manutenibilidade](https://sonarcloud.io/api/project_badges/measure?project=fazedordecodigo_PyFlunt&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=fazedordecodigo_PyFlunt)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=fazedordecodigo_PyFlunt&metric=bugs)](https://sonarcloud.io/summary/new_code?id=fazedordecodigo_PyFlunt)
[![Vulnerabilidades](https://sonarcloud.io/api/project_badges/measure?project=fazedordecodigo_PyFlunt&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=fazedordecodigo_PyFlunt)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=fazedordecodigo_PyFlunt&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=fazedordecodigo_PyFlunt)


[English Version](./README_EN.md)


Flunt te auxilia a implementar Domain Notification Pattern em sua aplicação para centralizar erros e mudanças em determinadas ações e entidades.

Flunt surgiu de duas necessidades: implementar o Domain Notification Pattern para substituir exceções no nível de domínio da aplicação e reduzir a quantidade de IFs (complexidade) usando uma abordagem baseada em contratos.

Assim, basicamente o que o Flunt faz é adicionar uma lista de Notificações à sua classe e vários métodos para interagir com ela.

## ➡️ Como usar

### 🔧 Instalação

````bash
pip install flunt
````

### 🔔 Notifiable

````python
from flunt.notifiable import Notifiable
from flunt.notification import Notification

class Nome(Notifiable):
    def __init__(self, nome):
        super().__init__()

        if len(nome) > 3:
            self.add_notification(
                Notification(field='nome', message='nome inválido')
            )

        self._nome = nome
````

### 📜 Contract
````python
"""Módulo Objetos de Valor."""
from flunt.notifiable import Notifiable
from flunt.contract import Contract


class Nome(Notifiable):
    """Classe Objeto de Valor Nome."""

    def __init__(self, primeiro_nome, ultimo_nome):
        """Encontrar 'Construtor'."""
        super().__init__()
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.add_notifications(
            Contract()
            .requires(self.primeiro_nome, 'primeiro nome')
            .requires(self.ultimo_nome, 'último nome')
            .is_greater_than(
                value=self.primeiro_nome,
                comparer=3,
                key="primeiro_nome",
                message="Mínimo de 3 caracteres",
            )
            .is_greater_than(
                value=self.ultimo_nome,
                comparer=3,
                key="ultimo_nome",
                message="Mínimo de 3 caracteres",
            )
            .get_notifications()
        )


nome = Nome('Emerson', 'Delatorre')
if not nome.is_valid():
    for notification in nome.get_notifications():
        print(notification)

````

## 📄 Licença

Este projeto contém a licença MIT. Consulte o arquivo [LICENSE](LICENSE).

## Mods
* [Flunt para C# (Original)](https://github.com/andrebaltieri/Flunt)
* [Flunt.Br](https://github.com/lira92/flunt.br)
* [Flunt para Java](https://github.com/carlosbritojun/jflunt)
* [Flunt para JavaScript](https://github.com/jhonesgoncal/flunt)
* [Flunt para PHP](https://github.com/matheusbloise/flunt-php)
