import sys

if __name__ == "__main__":
    dados = [{'idade': int(l[5]), 'modalidade': l[8], 'resultado': l[-1].strip().lower()} for l in (linha.split(',') for linha in sys.stdin.readlines()[1:])]

    modalidades = sorted(set(d['modalidade'] for d in dados))
    print("Modalidades desportivas:", modalidades)

    total_atletas = len(dados)
    aptos = sum(1 for row in dados if 'resultado' in row and row['resultado'] == 'true')
    percentagem_aptos, percentagem_inaptos = (aptos / total_atletas) * 100 if total_atletas > 0 else 0, ((total_atletas - aptos) / total_atletas) * 100 if total_atletas > 0 else 0

    print("Percentagem de atletas aptos:", percentagem_aptos)
    print("Percentagem de atletas inaptos:", percentagem_inaptos)

    distribuicao = {idade: sum(1 for d in dados if (d['idade'] >= idade and d['idade'] < idade + 5)) for idade in range(18, 40, 5)}

    print("Distribuição de atletas por escalão etário:")
    [print(f"[{escalao}-{escalao+4}]:", quantidade) for escalao, quantidade in distribuicao.items()]
