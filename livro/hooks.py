import logging
import mkdocs.plugins
import os
import re


ADMONITION_PATTERN = re.compile(r'(!!! +(info|note) +"(.*?)".*?)')
ANCHOR_PATTERN = re.compile(r'\[id> +(.*?)\](\(.*?\))?')
CODE_BLOCK_NL_PATTERN = re.compile(r'``` +linguagem_natural +title="(.*?)".*?[\s\S]([.\s\S]*?)```')
INCLUDE_PATTERN = re.compile(r'[\s\S]{! +(.*?) +!}(?=[\s\S])')
MERMAID_PATTERN = re.compile(r'``` +mermaid +title="(.*?)"([.\s\S]*?)```')
MY_ADMONITION_PATTERN = re.compile(r'(([!!!|???]) +(\w+)(.*)[\s\S](\s {4}[.\s\S]*?))(?=\n{2}[^\s])')


def add_anchor_to_admonitions(markdown):
    def repl(match):
        content = match.group(1)
        sub = match.group(3).strip()
        return content.replace(sub, f'[id> {sub}]')

    return ADMONITION_PATTERN.sub(repl, markdown)


def code_block_NL(markdown):
    repl = r'<div class="language-text highlight" id="alg-\1">' \
           r'<span class="filename">\1</span>' \
           r'<pre style="white-space: pre-wrap;">' \
           r'<code class="linguagem-natural">\2</code></pre></div>'
    return CODE_BLOCK_NL_PATTERN.sub(repl, markdown)


def my_admonitions(markdown):
    def repl(match):
        full, block_start, block_type, title, body = match.groups()

        types = {'info': 'Definição',
                 'note': 'Dica',
                 'warning': 'Atenção',
                 'llm': 'Chat-bot',
                 }

        if block_type not in types or title:
            return full

        if block_type == 'llm':
            llms = ', '.join(["[ChatGPT](https://openai.com/chatgpt/)",
                              "[Gemini](https://gemini.google.com/)",
                              "[Claude](https://www.anthropic.com/claude)",
                              "[Llama](https://www.llama2.ai/)",
                              ])
            footer = (f'\n    Algumas opções são {llms}. **Estes modelos '
                      'podem cometer erros!** Verifique as informações '
                      'em fontes confiáveis.')
            body = f'{body}\n{footer}'

        return f'{block_start} {block_type} "{types[block_type]}"{body}'

    return MY_ADMONITION_PATTERN.sub(repl, markdown)


def set_anchors(markdown):
    def repl(match):
        text = match.group(1).strip()
        id = text.replace('  ', ' ').replace(' ', '-')
        if match.group(2):
            return f'[<span id="{id}">{text}</span>]{match.group(2)}'
        return f'<span id="{id}">{text}</span>'

    return ANCHOR_PATTERN.sub(repl, markdown)


def on_page_read_source(page, config):
    def repl(match):
        with open(os.path.join(docs_dir, match.group(1).strip())) as f:
            content = f.read()
        return f'\n{content}\n'

    with open(os.path.join(docs_dir, page.file.src_uri)) as f:
        source = f.read()

    if page.file.src_uri.endswith('.md'):
        while INCLUDE_PATTERN.search(source):
            source = INCLUDE_PATTERN.sub(repl, source)
    return source


def check_content(markdown, src_uri):
    sections = {'Citação': r'(!!! quote "\[(.*)\]\(.*\)"[\s\S])\n {4}\*(.*?)\*(?=\n\n)',
                'Introdução': r'---\n\n([.\s\S]*?)(?=\n---\n)',
                'Resumo': r'<h\d>Resumo</h\d>',
                'Exercícios': r'<h\d>Exercícios</h\d>',
                'Chat-bot': r'[!!!|???] llm ',
                }

    for section, regex in sections.items():
        if not re.search(regex, markdown):
            log.warning(f'"{src_uri}" sem seção "{section}".')

    for missing in re.findall(r'https://img\.shields\.io/badge/TODO-(.*?)-', markdown):
        log.warning(f'"{src_uri}" sem {missing}.')


def on_page_markdown(markdown, page, config, files):
    # markdown = include_files(markdown)
    markdown = my_admonitions(markdown)
    markdown = add_anchor_to_admonitions(markdown)
    markdown = set_anchors(markdown)
    markdown = code_block_NL(markdown)
    markdown = mermaid_title(markdown)
    src_uri = page.file.src_uri
    if src_uri != index_uri:  # and '/' not in src_uri:
        check_content(markdown, src_uri)
    return markdown


def mermaid_title(markdown):
    repl = r'<div class="language-text highlight" id="\1">' \
           r'<span class="filename">\1</span>\n\n' \
           r'``` mermaid\2```\n\n</div>'
    return MERMAID_PATTERN.sub(repl, markdown)


log = logging.getLogger('mkdocs')
with open('mkdocs.yml') as f:
    content = f.read()
    docs_dir = re.search(r'docs_dir: (.*)', content).group(1)
    index_uri = re.search(r'nav:[\s\S].*?: (.+)', content).group(1)
