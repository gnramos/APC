import logging
# import mkdocs.plugins
import os
import re


ANCHOR_PATTERN = re.compile(r'\[id> +(.*?)\](\(.*?\))?')
CODE_BLOCK_NL_PATTERN = re.compile(r'``` +linguagem_natural +title="(.*?)".*?[\s\S]([.\s\S]*?)```')
INCLUDE_PATTERN = re.compile(r'[\s\S]{! +(.*?) +!}(?=[\s\S])')
MERMAID_PATTERN = re.compile(r'``` +mermaid +title="(.*?)"([.\s\S]*?)```')
# ADMONITION_PATTERN = re.compile(r'((!!!|\?\?\?) +(\w+) (\w.*)[\s\S](\s {4}[.\s\S]*?))(?=\n{2}[^\s])')
ADMONITION_PATTERN = re.compile(r'(!!!|\?\?\?) +(\w+)(.*?\n)\n([.\s\S]*?)(?=\n\n)')


def code_block_NL(markdown):
    repl = r'<div class="language-text highlight" id="alg-\1">' \
           r'<span class="filename">\1</span>' \
           r'<pre style="white-space: pre-wrap;">' \
           r'<code class="linguagem-natural">\2</code></pre></div>'
    return CODE_BLOCK_NL_PATTERN.sub(repl, markdown)


def set_admonitions(markdown):
    def repl(match):
        block_start, block_type, title, body = match.groups()

        title = title.strip()
        if block_type == 'chatbot':
            body = (f'{body}\n\n    Algumas opções são '
                    '[ChatGPT](https://openai.com/chatgpt/), '
                    '[Gemini](https://gemini.google.com/), '
                    '[Claude](https://www.anthropic.com/claude) e '
                    '[Llama](https://www.llama2.ai/)'
                    '. **Estes modelos podem cometer erros!** Verifique as '
                    'informações em fontes confiáveis.')
        elif title and block_type in ('definição', 'dica'):
            title = f'"[id> {title[1:-1]}]"'

        return f'{block_start} {block_type} {title}\n{body}'

    return ADMONITION_PATTERN.sub(repl, markdown)


def set_anchors(markdown):
    def repl(match):
        text = match.group(1).strip()
        id = text.replace('  ', ' ').replace(' ', '-')
        if match.group(2):
            return f'"[<span id="{id}">{text}</span>]{match.group(2)}'
        return f'<span id="{id}">{text}</span>'

    return ANCHOR_PATTERN.sub(repl, markdown)


def on_page_read_source(page, config):
    def repl(match):
        with open(os.path.join(docs_dir, match.group(1).strip())) as f:
            content = f.read()
        return f'\n{content}\n'

    with open(os.path.join(docs_dir, page.file.src_uri)) as f:
        source = f.read()

    while INCLUDE_PATTERN.search(source):
        source = INCLUDE_PATTERN.sub(repl, source)

    return source


def check_content(markdown, src_uri):
    return
    sections = {'Citação': r'(!!! quote "\[(.*)\]\(.*\)"[\s\S])\n {4}\*(.*?)\*(?=\n\n)',
                'Introdução': r'---\n\n([.\s\S]*?)(?=\n---\n)',
                'Resumo': r'<h\d>Resumo</h\d>',
                'Chat-bot': r'(!!!|\?\?\?) chatbot',
                'Exercícios': r'^\?\?\? exercícios$',
                }

    for section, regex in sections.items():
        if not re.search(regex, markdown):
            log.warning(f'"{src_uri}" sem seção "{section}".')

    for missing in re.findall(r'https://img\.shields\.io/badge/TODO-(.*?)-', markdown):
        log.warning(f'"{src_uri}" sem {missing}.')


def on_page_markdown(markdown, page, config, files):
    src_uri = page.file.src_uri
    if src_uri != index_uri:
        markdown = set_admonitions(markdown)
    markdown = set_anchors(markdown)
    markdown = code_block_NL(markdown)
    markdown = mermaid_title(markdown)
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
