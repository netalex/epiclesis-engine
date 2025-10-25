# Porto delle Due Rive — Seedbook di Ambientazione

_Stampabile, con asset testuali e ganci di campagna. Versione: 2025-10-25._

## Sinossi
Polis costiera con **porto conteso** tra **Riva Nord** (commerci) e **Riva Sud** (pescatori). Un **corridoio neutro** di **Ermes** garantisce passaggio e dialogo. **Atena** sigilla cariche e leggi dalla **Acropoli**; **Poseidone** tutela il **Faro** e i confini marini; **Zeus Horkios** custodisce i **giuramenti**. L’equilibrio vacilla a ogni tempesta, scandalo o carestia.

### Palette e tono
- Civico, tecnico-rituale, niente miracoli antirealistici.
- Conflitti **regolati** (Ares) e feste di **charis** (Afrodite) come valvole di sicurezza.
- **Anánkē**: limiti fisici rispettati; il divino **orienta** traiettorie plausibili.

## Tīmē/Miasma di base (città)
- **T**≈5, **M**≈2 (calano con spergiuri pubblici, salgono con restituzioni reali).

## Fazioni
riva_nord:
  nome: Consorzio delle Tre Ancore
  agenda:
  - Controllo banchine 1-3
  - Tariffe preferenziali
  - Monopolio scarico spezie
  domini:
  - passaggio
  - scambio
  - polis
  patroni:
  - deity:ermes@1.0.0
  - deity:athena@1.0.0
  t_m:
    T: 4
    M: 2
riva_sud:
  nome: Gilda dei Pescatori del Levante
  agenda:
  - Accesso alba
  - Ripristino banchi ittici
  - Dazi equi
  domini:
  - mare
  - ciclo
  - fertilita
  patroni:
  - deity:poseidone@1.0.0
  - deity:demetra@1.0.0
  t_m:
    T: 3
    M: 2
custodi_neutrali:
  nome: Collegio dei Kerykes
  agenda:
  - Mantenere corridoio Ermes
  - Proteggere messaggeri
  - Arbitrare liti minori
  domini:
  - passaggio
  - confini
  - sovranita
  patroni:
  - deity:ermes@1.0.0
  - deity:zeus@1.0.0
  t_m:
    T: 5
    M: 1


## Luoghi chiave
- id: location:porto-conteso-acropoli@1.0.0
  name: Acropoli — Santuario di Atena Polias
  tm:
    T: 5
    M: 1
  note: Assemblee, sigilli civici, viste sul porto.
- id: location:porto-conteso-faro@1.0.0
  name: Faro del Promontorio — Altare di Poseidone
  tm:
    T: 4
    M: 1
  note: Segnali, tempeste, confini marini.
- id: location:porto-conteso-mercato@1.0.0
  name: Mercato alle Banchine
  tm:
    T: 3
    M: 2
  note: Scambi, rivalità, occasioni.
- id: location:porto-conteso-sala-trattato@1.0.0
  name: Sala del Trattato — Pietre di Ermes
  tm:
    T: 5
    M: 1
  note: Tregue, giuramenti, audit pubblici.


## Calendario rituale (ridotto)
- mese: Alimo
  evento: Benedizione delle Reti
  epiclesi: epiclesis:poseidone-enosichthon@1.0.0
  IE_atteso: 6
- mese: Spighia
  evento: Processione di Demetra
  epiclesi: epiclesis:demetra-thesmophoros@1.0.0
  IE_atteso: 6
- mese: Agoraio
  evento: Tregua dei Mercanti
  epiclesi: epiclesis:ermes-kerykeios@1.0.0
  IE_atteso: 6
- mese: Poliade
  evento: Sigillo delle Cariche
  epiclesi: epiclesis:athena-polias@1.0.0
  IE_atteso: 8


## Oracoli locali
- titolo: La Scaglia nell’Olio
  testo: Quando l’olio rifletterà una scaglia che non appartiene al mare, il patto
    non reggerà se non sarà riconsegnato il debito non nominato.
  budget_chiarezza: medio
  condizioni: restituzione + testimoni
- titolo: Tre Pietre e una Voce
  testo: Se tre pietre restano mute, aprite la bocca del quarto segno e la merce contesa
    troverà tre padri.
  budget_chiarezza: basso
  condizioni: atto pubblico nel corridoio


## Ganci di campagna
- **GdR — Scambio alla cieca**: una nave carica attracca fuori calendario. Chi viola la tregua perde +2 IE a scena; con **herma** firmata dal Collegio, si negozia.
- **GdR — Il faro sordo**: il promontorio non risponde; per riaccendere serve un voto pubblico al Faro e **tridente simbolico**.
- **Romanzo — Le spighe e il sale**: un matrimonio politico (Era Gamelia) minaccia la tregua; il protagonista deve scegliere tra amore e pace cittadina.
- **Romanzo — Il Keryx caduto**: un messaggero muore in zona neutra; la città rischia il collasso della tīmē finché non si celebra una **catarsi** in Sala del Trattato.

## Mappe (PNG)
- `maps/overview.png` — schema d’insieme del porto
- `maps/distretto_neutrale.png` — detail del corridoio di **Ermes**

## Riti consigliati (link alla KB)
- Tregua dei mercanti → `ritual:trattato-del-messaggero@1.0.0` (Ermes Kerykeios)
- Mozione del profondo → `ritual:mozione-del-profondo@1.0.0` (Poseidone Enosichthon)
- Sigillo delle cariche → `ritual:sigillo-sobrio@1.0.0` (Atena Polias)
- Patto nuziale pubblico → `ritual:patto-nuziale@1.0.0` (Era Teleia)

## Artefatti utili
- `artifact:herma@1.0.0`, `artifact:tridente-simbolico@1.0.0`, `artifact:aigis@1.0.0`, `artifact:keraunos@1.0.0`

## Struttura in 3 Atti (campagna)
1. **Tensione**: guasti al Faro, libello calunnioso, nave fuori calendario. IE medio 5–6.

2. **Catarsi**: restituzioni, duello regolato, festa di **charis**. IE 6–8.

3. **Sigillo**: giuramento pubblico in Sala del Trattato; fulmine simbolico (**Zeus**) se IE≥10.


## Scene "se… allora…" (pronte)
- Se **la Dogana** blocca la merce **senza testimoni**, allora **M+1** e i kerykes perdono autorità finché non si convoca un **rito di verità** (Atena).

- Se **una tempesta** danneggia le banchine, allora la **Mozione del Profondo** chiarisce i confini e protegge i soccorsi (Poseidone) **ma** richiede **voto di manutenzione** (Efesto/Atena).

- Se **un keryx** è ferito in zona neutra, allora **Lex Stygia** impone **restituzione** o **bando**; l’**Apsis Nomia** crea campo sicuro per l’indagine (Ares).


## Epiloghi possibili
- **Concordia**: le Rive accettano una **quota rotante** sulle banchine e un **registro pubblico** (IE alto, teofania simbolica).

- **Rigidità**: eccesso di forma (Era) senza misura (Apollo) → fragilità futura (IE alto ma T↓ nel tempo).

- **Rottura**: violata la neutralità di Ermes → **M+2** e guardiano punitivo (mostro) finché non avviene catarsi.

