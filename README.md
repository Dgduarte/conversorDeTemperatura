# 🌡️ Conversor de Temperatura em Python

Um conversor interativo de escalas termométricas via linha de comando (CLI) desenvolvido em Python. O programa permite converter valores entre as três principais escalas de temperatura do mundo: **Celsius**, **Fahrenheit** e **Kelvin**, com tratamento de erros e validação física de limites.

---

## 🚀 Funcionalidades

- **Conversão Bidirecional:** Converta de qualquer escala para qualquer outra (Celsius $\leftrightarrow$ Fahrenheit $\leftrightarrow$ Kelvin).
- **Entrada Flexível:** Aceita separadores decimais com ponto (`.`) ou vírgula (`,`).
- **Validação de Erros:** Não trava caso o usuário digite texto onde deveria ser número ou pressione `Enter` em branco.
- **Validação Física:** Alerta o usuário caso a temperatura informada esteja abaixo do **Zero Absoluto** ($0\text{ K}$ ou $-273.15\text{ °C}$).
- **Interface no Terminal:** Menus claros com animação de carregamento e formatação de casas decimais.

---

## 📐 Fórmulas Utilizadas

| Conversão | Fórmula |
| :--- | :--- |
| **Celsius para Fahrenheit** | $F = (C \times \frac{9}{5}) + 32$ |
| **Fahrenheit para Celsius** | $C = (F - 32) \times \frac{5}{9}$ |
| **Celsius para Kelvin** | $K = C + 273.15$ |
| **Kelvin para Celsius** | $C = K - 273.15$ |

> **Nota:** De acordo com o Sistema Internacional de Unidades (SI), a escala Kelvin é absoluta e não utiliza o símbolo de grau (`°`), apenas a letra **K**.

---

## 🛠️ Pré-requisitos

- **Python 3.7+** instalado na máquina.
- Não requer a instalação de bibliotecas externas (utiliza apenas os módulos nativos do Python).

---

## 💻 Como Executar

1. Clone ou baixe este repositório:
   ```bash
   git clone https://github.com/seu-usuario/conversor-temperatura.git
