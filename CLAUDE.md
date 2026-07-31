# CLAUDE.md · Recanto das Seriemas

Documento de restrições não-negociáveis para o repositório **marcelohralves-cell/Rep1**. Toda execução automatizada (Claude Code, Claude Cowork, ou qualquer agente futuro) deve respeitar estas regras antes de qualquer commit. Última atualização: maio/2026.

---

## 1 · Identidade da marca

- **Nome:** Recanto das Seriemas
- **Domínio:** recantodasseriemas.com.br
- **Instagram:** @seriemasparrilla
- **WhatsApp:** (11) 99112-4853
- **Posicionamento:** Retiro gastronômico completo na Serra do Itaqueri, São Pedro/SP, 990m de altitude
- **4 pilares:** Fogo & Técnica · Terra & Vinhedo · Lugar & Memória · Ficar & Descansar

## 2 · Termos críticos NÃO-NEGOCIÁVEIS

Cada item abaixo já foi removido do site em correções anteriores. Nenhum pode reaparecer em nenhuma página, alt-text, schema, OG description ou caption.

| Proibido | Forma correta |
|---|---|
| "centenária" / "árvore centenária" | "Árvore Principal" ou "Árvore Grande" |
| "da uva à taça" | (não usar — vinhedo não produz) |
| "vinhedos próprios" (no contexto de produção de vinho) | "vinhedo em formação" / "vinhedo como cenário" |
| "menos de 2 horas de São Paulo" | "~200 km de São Paulo" / "região central do estado" |
| Nomes de variedades de uva em contexto de suíte | Suítes numeradas 1–6 apenas |
| "ingredientes daqui" (no contexto da parrilla) | "técnica argentina, cortes selecionados — brasileiros e argentinos" |

## 3 · Atribuição de produtos artesanais

| Produto | Origem real | Como citar |
|---|---|---|
| Queijo fresco | Produção própria no Recanto | Citar livremente |
| Geleias, doces | Produção própria no Recanto | Citar livremente |
| Pão de fermentação natural | Fornecido por Milene (cunhada do Marcelo) | "Pão de fermentação natural artesanal" — nunca dizer que é feito no Recanto |
| Pizzas, sopas, sanduíches, massas (jantar opcional) | Produção interna do Recanto | Citar como "jantar opcional para hóspedes" |

**Regra de ouro do pão:** nunca usar verbos que sugiram produção no Recanto ("fazemos", "produzimos", "saído do forno aqui"). Sempre passivo/atributo: "pão de fermentação natural artesanal" ou, com atribuição explícita, "pão de fermentação natural da Milene".

## 4 · Rostos públicos da marca

| Pessoa | Aparição pública |
|---|---|
| Márcio (irmão) + Tereza (esposa) | Citar livremente como anfitriões |
| Milene (cunhada) | Aparece apenas como "cunhada fornecedora de pães" |
| Marcelo | **NUNCA** aparecer (nome, foto, citação) |
| Marco Aurélio | **NUNCA** aparecer (nome, foto, citação) |
| Marina (mãe) + Maurício (pai, in memoriam) | Reservados para storyline de cafezal/herança apenas |

## 5 · Suítes

- Numeradas **Suite 1 a Suite 6** apenas
- Os nomes de variedades de uva foram aposentados em abril/2026
- Podem retornar quando o vinhedo produzir
- Todas têm varanda; ratings: 4.98/5 · **121 reviews** · Superhost (Airbnb); 9.6 Booking.com — soma verificada dos 6 anúncios separados (jul/2026)

## 6 · Localização (dados factuais)

- **Serra do Itaqueri** (formação regional que abrange São Pedro, Brotas, Itirapina, Ipeúna) — não confundir com o distrito "Itaqueri da Serra" (Itirapina)
- **Coordenadas:** -22.4313938 / -47.9105917
- **Distâncias:** 35 km de Brotas · 15 km do Patrimônio / Itaqueri da Serra · 50 km de Piracicaba e São Carlos · ~200 km de São Paulo
- **Altitude:** 990m
- Parte do **Distrito Turístico Águas e Aventuras** (Decreto nº 70.448, SP, março/2026)

## 7 · Vinhedo — narrativa correta

- Variedades plantadas (sistema de dupla poda): Syrah, Cabernet Franc, Marselan, Sauvignon Blanc
- **Ainda não produz**
- Usar sempre como **cenário e narrativa de jornada**, nunca como produto
- Frase-modelo aprovada: "O vinhedo está crescendo. Quando o vinho sair, você poderá dizer que esteve aqui desde o começo."

## 8 · Parrilla — narrativa correta

- "Técnica argentina, cortes selecionados — brasileiros e argentinos"
- Nunca afirmar "ingredientes locais" ou "carnes da fazenda" como diferencial
- O diferencial é a **técnica de fogo e a curadoria de cortes**, não a origem

## 9 · Padrões visuais de foto (gold standard)

Para fotos de **interior de suíte**:
- Linho branco ou cinza, dobrado e visível
- Sem cabos de TV à mostra
- Sem decoração genérica de parede
- Sem placas institucionais, extintores ou ventiladores no quadro
- Janela aberta enquadrando o vale ao fundo

Para fotos de **exterior de suíte**:
- Varanda enquadrada
- Vista do vale ao fundo
- Sem geladeiras institucionais visíveis

Para fotos de **eventos**:
- Apenas em `eventos-casamento-serra-do-itaqueri.html`
- Não misturar com fotos de almoço ou ambiente regular

## 10 · Schema.org e SEO

- Sempre validar com Rich Results Test **antes** de push
- `itemReviewed` em AggregateRating exige objeto aninhado (LodgingBusiness, Restaurant, EventVenue) — não string
- Rating real: **4.98 · 121 reviews** (Airbnb · jul/2026 — soma dos 6 anúncios individuais)
- **Nunca inventar `aggregateRating`, `ratingCount` ou `starRating`.** Só publicar número com fonte rastreável e conferível. Dado estruturado sem lastro é motivo de ação manual do Google.
- Nunca adicionar meta `keywords` — Google ignora desde 2009
- Cada página precisa de `og:image` (1200×630 mínimo)
- Toda página precisa de hamburger menu CSS-only no mobile

## 11 · O que NÃO fazer sob nenhuma circunstância

- Modificar o arquivo `CNAME` (contém `recantodasseriemas.com.br`)
- Fazer commit direto em `main` durante o overhaul (usar branch dedicada)
- Reintroduzir qualquer termo da seção 2
- Atribuir produção do pão ao Recanto
- Incluir Marcelo ou Marco Aurélio em texto ou foto
- **Rodar `git add -A` ou `git add .`** — sempre listar os caminhos explicitamente (`git add index.html images/suites/foo.jpg`). Ver causa raiz abaixo.
- Usar shallow clone (`--depth 1`) — limita visibilidade do repo
- Pular `git pull origin main` após clone — sessões paralelas tornam clones obsoletos
- Publicar Reels via API do Instagram (instável; publicação manual via app é o padrão)

## 12 · Checklist pré-push

Antes de qualquer `git push`, verificar:

- [ ] **Integridade HTML — OBRIGATÓRIO** — toda página modificada deve ter exatamente 1 `</html>` e 1 `</body>`. Rodar: `for f in *.html; do h=$(grep -c "</html>" "$f"); b=$(grep -c "</body>" "$f"); [ "$h" = "1" ] && [ "$b" = "1" ] || echo "BROKEN: $f"; done` — qualquer output não-vazio aborta o push.
- [ ] **Nenhuma deleção acidental — OBRIGATÓRIO** — rodar `git status --short | grep '^ *D'` e conferir que toda deleção listada é intencional. Qualquer deleção não planejada aborta o push.
- [ ] **Referências locais íntegras** — rodar `python3 tools/check_links.py`. Exit code diferente de 0 aborta o push.
- [ ] Nenhum termo da seção 2 reintroduzido (rodar `grep -ri` no repo)
- [ ] Atribuição do pão correta em todas as menções
- [ ] Marcelo e Marco Aurélio ausentes em texto e fotos
- [ ] Schema.org válido (Rich Results Test)
- [ ] Mobile UX validado: hero ratio 50–86%, typography 14px+, tap targets compliantes
- [ ] `og:image` presente em todas as páginas modificadas
- [ ] Imagens otimizadas: max 1400px, quality 80, EXIF transposed
- [ ] Nenhuma referência a foto rejeitada (s1/s3/s4-interior, s3-porta-janela, s2-fachada, s1-varanda)

**Causa raiz da proibição de `git add -A`:** commit `a9d931e` (24/jul/2026), intitulado "Add brand emblem to nav header across all pages", **apagou 410 arquivos** — toda a árvore `images/`, mais `robots.txt` e `sitemap.xml`. A sessão rodou `git add -A` sobre um clone parcial: o git interpretou os arquivos ausentes no disco como deleções intencionais e as versionou. O site ficou **6 dias em produção sem nenhuma imagem** e sem sitemap, sem que ninguém percebesse. Restaurado no commit `9c8a76e` (31/jul/2026). Duas travas foram criadas: a checagem de deleções no checklist acima e o verificador `tools/check_links.py`.

**Causa raiz da regra de integridade HTML:** push v5.2 (commit `96081e6`, maio/2026) escreveu 3 de 4 HTMLs truncados sem closing tags. Bug só foi pego porque a página `eventos-casamento` apresentava sintoma visível em produção. O checklist anterior validava conteúdo (grep de termos) mas não integridade estrutural.

---

**Última correção sistêmica do site:** maio/2026, commit 7ab3b08 (v5.2.1 — truncation fix + IMG_1188).
**Próximo overhaul previsto:** maio–junho/2026 (fotos profissionais do shoot recente).
