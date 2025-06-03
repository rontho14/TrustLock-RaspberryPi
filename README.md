# 🔒 TrustLock – Fechadura Eletrônica com Raspberry Pi Pico

Projeto desenvolvido para a disciplina de Microcontroladores do curso de Engenharia de Computação no Instituto Mauá de Tecnologia.

## 📌 Visão Geral

O **TrustLock** é uma fechadura eletrônica inteligente com foco em segurança residencial, utilizando o microcontrolador **Raspberry Pi Pico**. A autenticação pode ser feita por **senha numérica** ou **cartão RFID**, com feedback visual via display OLED e sonoro via buzzer.

---

## 🛠️ Componentes Utilizados

### 🔧 Hardware

- Raspberry Pi Pico
- Display OLED (I2C)
- Teclado 4x4
- Sensor RFID (MFRC522)
- Buzzer piezoelétrico
- Trava solenoide 5V
- Caixa impressa em 3D

### 💻 Software

- MicroPython
- Thonny IDE
- Bibliotecas: `machine`, `utime`, drivers para OLED, RFID e teclado
- Git/GitHub para versionamento

---

## ✅ Funcionalidades

- Autenticação por senha (via teclado)
- Autenticação por RFID
- Feedback visual no OLED
- Feedback sonoro com buzzer
- Controle físico da trava
- Caixa 3D para organização e proteção

---

## 📋 Requisitos

### Requisitos de Usuário (UR)

- UR-1: Autenticar acesso por senha
- UR-2: Autenticar via RFID
- UR-3: Segurança contra acessos não autorizados
- UR-5: Feedback visual
- UR-6: Feedback sonoro

### Requisitos Técnicos (TR)

- TR-1: Alimentação constante em laboratório
- TR-3: Alimentar o Pico com 12V
- TR-4: Alimentar solenoide com 5V
- TR-6: GPIO para todos os sensores/atuadores
- TR-8: Uso de MicroPython

---

## 🧠 Estratégia de Desenvolvimento

1. Levantamento de requisitos
2. Escolha e teste dos componentes
3. Prototipação individual dos dispositivos
4. Integração dos módulos com MicroPython
5. Montagem final em perfboard e caixa 3D
6. Testes de validação

---

## 🎯 Resultados

- Prototipagem funcional validada
- Interface clara e intuitiva
- Sistema estável e seguro
- Projeto pronto para expansão com app, banco de dados e biometria

---

## 🔮 Melhorias Futuras

- Integração com app ou web para cadastro de usuários
- Banco de dados para logs de acesso
- Fonte portátil (bateria)
- Autenticação multifator ou biometria

---

## 📚 Autores

- André Freire Prino – 21.00476-5
- Guilherme Thomasi Ronca – 22.00522-6  
- Matheus Santos Feitosa – 20.00628-4
- João Vitor Ferrenha – 22.00085-2  

---

## 📅 Versão

**V1.0.0 – 2025**