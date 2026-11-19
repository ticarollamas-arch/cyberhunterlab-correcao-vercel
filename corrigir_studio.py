from pathlib import Path
p = Path("src/app/studio/page.tsx")
if not p.exists():
    raise SystemExit("ERRO: execute na raiz do repositorio que contem src/app/studio/page.tsx")
s = p.read_text(encoding="utf-8")
old = '              </div>\n            </div>\n            </div>\n\n            {providerError'
new = '              </div>\n            </div>\n\n            {providerError'
if s.count(old) != 1:
    raise SystemExit("ERRO: trecho esperado nao encontrado exatamente uma vez; arquivo nao modificado")
p.write_text(s.replace(old,new),encoding="utf-8")
print("OK: fechamento JSX excedente removido em",p)
