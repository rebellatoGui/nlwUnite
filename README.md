# Especificações

✪ Pass.in

O pass.in é uma aplicação de **gestão de participantes em eventos presenciais**.

A ferramenta permite que o organizador cadastre um evento e abra uma página pública de inscrição.

Os participantes inscritos podem emitir uma credencial para check-in no dia do evento.

O sistema fará um scan da credencial do participante para permitir a entrada no evento.
![especs pass in](https://github.com/rebellatoGui/nlwUnite/assets/146299321/0950f230-5c25-4642-8644-d3e7a3fa15ff)

## Requisitos

### Requisitos funcionais

- [ ]  O organizador deve poder cadastrar um novo evento;
- [ ]  O organizador deve poder visualizar dados de um evento;
- [ ]  O organizador deve poser visualizar a lista de participantes;
- [ ]  O participante deve poder se inscrever em um evento;
- [ ]  O participante deve poder visualizar seu crachá de inscrição;
- [ ]  O participante deve poder realizar check-in no evento;

### Regras de negócio

- [ ]  O participante só pode se inscrever em um evento uma única vez;
- [ ]  O participante só pode se inscrever em eventos com vagas disponíveis;
- [ ]  O participante só pode realizar check-in em um evento uma única vez;

### Requisitos não-funcionais

- [ ]  O check-in no evento será realizado através de um QRCode;

## Banco de dados

Nessa aplicação vamos utilizar banco de dados relacional (SQL). Para ambiente de desenvolvimento seguiremos com o SQLite pela facilidade do ambiente.

![diagrama ERD](https://github.com/rebellatoGui/nlwUnite/assets/146299321/089f3e5c-2d73-416a-813d-9d33458de0df)
