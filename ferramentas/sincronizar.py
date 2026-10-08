#!/usr/bin/env python3
"""Sincroniza os arquivos compartilhados nas skills, valida e empacota.

Uso (na raiz do repositório):
    python3 ferramentas/sincronizar.py              # todas as skills
    python3 ferramentas/sincronizar.py nome-skill   # só uma

Para cada pasta em skills/:
1. lê skills/<nome>/compartilhado.txt (um destino por linha, ex.:
   "references/guia-redacao.md") e copia o arquivo de mesmo nome de
   compartilhado/ para esse destino;
2. valida o SKILL.md (cabeçalho com name igual ao nome da pasta e description);
3. gera dist/<nome>.zip, pronto para instalar em claude.ai
   (Configurações > Capacidades > Skills).
"""

import os
import re
import shutil
import sys
import zipfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMPARTILHADO = os.path.join(RAIZ, "compartilhado")
SKILLS = os.path.join(RAIZ, "skills")
DIST = os.path.join(RAIZ, "dist")
IGNORAR = {"compartilhado.txt", "__pycache__", ".DS_Store"}


def sincronizar(nome):
    pasta = os.path.join(SKILLS, nome)
    lista = os.path.join(pasta, "compartilhado.txt")
    if os.path.exists(lista):
        for destino in open(lista, encoding="utf-8").read().split():
            origem = os.path.join(COMPARTILHADO, os.path.basename(destino))
            if not os.path.exists(origem):
                sys.exit(f"[{nome}] arquivo compartilhado inexistente: {origem}")
            alvo = os.path.join(pasta, destino)
            os.makedirs(os.path.dirname(alvo), exist_ok=True)
            shutil.copy2(origem, alvo)


def validar(nome):
    caminho = os.path.join(SKILLS, nome, "SKILL.md")
    texto = open(caminho, encoding="utf-8").read()
    cab = re.match(r"---\n(.*?)\n---\n", texto, re.S)
    if not cab:
        sys.exit(f"[{nome}] SKILL.md sem cabeçalho YAML")
    campos = dict(re.findall(r"^(\w+):\s*(.+)$", cab.group(1), re.M))
    if campos.get("name") != nome:
        sys.exit(f"[{nome}] name do SKILL.md ({campos.get('name')}) difere da pasta")
    if len(campos.get("description", "")) < 50:
        sys.exit(f"[{nome}] description ausente ou curta demais")
    if len(campos["description"]) > 1024:
        sys.exit(f"[{nome}] description com {len(campos['description'])} caracteres (máximo 1024)")
    for ref in set(re.findall(r"`((?:references|scripts|assets)/[^`\s]+)`", texto)):
        if not os.path.exists(os.path.join(SKILLS, nome, ref)):
            sys.exit(f"[{nome}] SKILL.md cita {ref}, que não existe")


def empacotar(nome):
    os.makedirs(DIST, exist_ok=True)
    destino = os.path.join(DIST, f"{nome}.zip")
    pasta = os.path.join(SKILLS, nome)
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for raiz, dirs, arquivos in os.walk(pasta):
            dirs[:] = [d for d in dirs if d not in IGNORAR]
            for arq in sorted(arquivos):
                if arq in IGNORAR:
                    continue
                completo = os.path.join(raiz, arq)
                z.write(completo, os.path.join(nome, os.path.relpath(completo, pasta)))
    return destino


def main():
    nomes = sys.argv[1:] or sorted(
        d for d in os.listdir(SKILLS) if os.path.isfile(os.path.join(SKILLS, d, "SKILL.md")))
    for nome in nomes:
        sincronizar(nome)
        validar(nome)
        print(f"{nome}: ok -> {os.path.relpath(empacotar(nome), RAIZ)}")


if __name__ == "__main__":
    main()
