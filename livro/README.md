# Algoritmos e Programação de Computadores

O livro é gerado com o [mkdocs](https://www.mkdocs.org/).

# ATENÇÃO!

O conteúdo está em sendo construído, este material está incompleto e não é apropriado para ser uma referência bibliográfica (ainda).

## Desenvolvimento do conteúdo

O conteúdo é dividido em uma estrutura de diretórios:

```
.
├── docs          # conteúdo
│   ├── diretório # markdown
│   ├── img       # imagens
│   └── src       # código
└── overrides     # configurações

Para melhor organizar os arquivos, tópicos de primeiro nível estão organizados em arquivos Markdown, e podem incluir (recursivamente) outros arquivos. Para evitar os avisos do mkdocs de arquivos processados mas não inclusos no menu de navegação, os arquivos de segundo nível em diante têm um `.` extra ao final do nome.
```

Cada capítulo tem uma estrutura definida:

1. Citação: uma citação relacionada ao tópico.
1. Resumo: um resumo do conteúdo a ser apresentado.
1. Conteúdo: o conteúdo.
1. Resumo: um destaque dos pontos mais relevantes.
1. Chat-bot: prompts para desenvolvimento de certos pontos do conteúdo com agentes de IA.
1. Exercícios: questões para reforçar o aprendizado.

Há uma verificação automatizada da estrutura dentro de [`hooks.py`](../hooks.py). Partes ausentes são indicadas com [medalhas](https://img.shields.io) com o texto *TODO-???* (com *???* indicando o que falta).
