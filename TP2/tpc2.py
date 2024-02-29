import re
import sys


def converter_cabecalhos(line):
    match = re.match(r'^(#{1,3})\s(.+)$', line)
    if match:
        nivel = len(match.group(1))
        texto = match.group(2)
        return r'<h{nivel}>{texto}</h{nivel}>'
    return line

def converter_bold(line):
    line = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', line)
    return line


def converter_italico(line):
    line = re.sub(r'\*(.*?)\*', r'<i>\1</i>', line)
    return line

def converterLink(line):
    return re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', line)

def converterImagem(line):
    return re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', line)

def converterLista(line):
    line = re.sub(r'^(\d+)\.? (.+)$', r'<li>\2</li>', line, flags=re.MULTILINE)
    return re.sub(r'(<li>.+</li>)', r'<ol>\n\1\n</ol>', line, flags=re.DOTALL)

def addSpaceToLi(line):
    return re.sub(r'<li>(.+?)</li>',r'  <li>\1</li>', line)

def main(args):
    input_file = args[1]
    output_file = args[2]

    with open(input_file, 'r') as f:
        markdown_content = f.read()

    markdown_content = converter_cabecalhos(markdown_content)
    markdown_content = converterImagem(markdown_content)
    markdown_content = converterLink(markdown_content)
    markdown_content = converterLista(markdown_content)
    markdown_content = converter_bold(markdown_content)
    markdown_content = converter_italico(markdown_content)
    markdown_content = addSpaceToLi(markdown_content)

    with open(output_file, 'w') as f:
        f.write(markdown_content)

    return 0

if __name__ == "__main__":
    main(sys.argv)


