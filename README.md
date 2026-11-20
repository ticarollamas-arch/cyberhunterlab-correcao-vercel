<p align="center"><img src="assets/banner.svg" alt="CyberHuntLab — correção do build no Vercel" width="100%"></p>

# CyberHuntLab — correção do build no Vercel

Script Python de uma única tarefa: corrige um erro de sintaxe JSX em `src/app/studio/page.tsx` do projeto CyberHuntLab (Next.js) que impedia o **build no Vercel**. O arquivo tinha um `</div>` a mais antes do bloco `{providerError ...}`; o script remove esse fechamento excedente.

> Este repositório é um **patch**, não o projeto completo. Ele deve ser executado dentro do repositório do CyberHuntLab.

## Como funciona

- Procura o trecho com o `</div>` duplicado em `src/app/studio/page.tsx`.
- Só altera o arquivo se encontrar o trecho **exatamente uma vez**; caso contrário, sai com erro e não muda nada.
- Grava o arquivo em UTF-8 e informa o caminho corrigido.

## Instalação

Nenhuma dependência além do **Python 3** (só usa a biblioteca padrão). Copie `corrigir_studio.py` para a raiz do repositório do CyberHuntLab.

## Como usar

Na raiz do repositório que contém `src/app/studio/page.tsx`:

```bash
python3 corrigir_studio.py
```

Depois, valide o build localmente antes de publicar no Vercel:

```bash
npm install
npm run build
```

### Mensagens

| Saída | Significado |
|---|---|
| `OK: fechamento JSX excedente removido em src/app/studio/page.tsx` | Correção aplicada. |
| `ERRO: execute na raiz do repositorio que contem src/app/studio/page.tsx` | O script foi executado fora da raiz do projeto. |
| `ERRO: trecho esperado nao encontrado exatamente uma vez; arquivo nao modificado` | O arquivo já foi corrigido ou mudou; nada foi alterado. |

## Tecnologias

Python 3 (pathlib) · Next.js · React/JSX · TypeScript · Vercel

## Licença

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE).
