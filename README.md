# 🚗 Locadora de Veículos

Sistema de gerenciamento de locadora de veículos desenvolvido em **Python** com foco em **Programação Orientada a Objetos (POO)**.

---

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como atividade prática da faculdade para aplicar os conceitos fundamentais de POO:

- **Classes** e **Objetos**
- **Atributos** e **Métodos**
- **Abstração**
- **Encapsulamento**
- **Herança**
- **Polimorfismo**

O sistema simula o funcionamento básico de uma locadora, permitindo cadastrar, listar, alugar e devolver veículos através de um menu interativo no terminal.

---

## 🧠 Conceitos de POO Aplicados

| Conceito | Onde está no código |
|----------|---------------------|
| **Classe** | `Veiculo`, `Carro`, `Moto` |
| **Objeto / Instância** | `veiculo = Carro(...)` |
| **Atributos** | `modelo`, `placa`, `valor`, `_disponivel`, `portas`, `cilindradas` |
| **Métodos** | `alugar()`, `devolver()`, `exibir_informacoes()`, `calcular_aluguel()` |
| **Abstração** | A classe `Veiculo` representa apenas o essencial para a locadora |
| **Encapsulamento** | O atributo `_disponivel` é controlado exclusivamente pelos métodos |
| **Herança** | `Carro` e `Moto` herdam de `Veiculo` |
| **Polimorfismo** | `calcular_aluguel()` tem comportamento diferente para carro e moto |

---

## 🏗️ Estrutura do Projeto
