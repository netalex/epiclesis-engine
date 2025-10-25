# Porto delle Due Rive — Pacchetto Pre‑Sessione & Minicampagna

> Ambientazione: polis costiera con **porto conteso** tra Riva Nord (commerci) e Riva Sud (pescatori). Corridoio **neutrale** di **Ermes**. Santuario di **Atena** sull’acropoli, **Faro** di **Poseidone** sul promontorio. Regole di lore: **Anánkē**, **tīmē/miasma (T/M)**, **Indice di Epifania (IE)**, **Lex Stygia**. 
> Formula IE (promemoria): `IE = T + A + C + O + V + E − M` (Tīmē + Ancoraggio + Coerenza epiclesi + Offerta + Voto/Giuramento + Emergenza di dominio − Miasma).

---

## SESSIONE 0 — Kit del Facilitatore

### 1) Pitch & Tono
- **Genere**: epico‑civico, tecnico‑rituale, zero miracoli che violano la fisica.
- **Temi**: patti, confini, tregue, restituzione, festa e misura.
- **Segnali di sicurezza**: X‑Card / Lines & Veils / OK Check‑in. Scene su religione/sesso/conflitto trattate **con misura** (Era/Apollo). 

### 2) Domande ai giocatori (aggancio)
1. **Che legame** hai con il porto (famiglia, bottega, tempeste, trattati)?
2. Qual è il **debito** che devi restituire (economico, affettivo, civico)?
3. A quale **epiclesi** sei più vicino (Ermes Kerykeios, Poseidone Enosichthon, Atena Polias, Era Teleia, Apollo Paian, Ares Enyalios, Afrodite Pandemos, Efesto Chalkeus, Artemide Agrotera)? Perché?
4. Indica una **soglia** che difendi (banchina, strada, casa, faro, mercato).

### 3) Creazione rapida PG (system‑agnostic)
- **Patroni** (1–2): scegli domini coerenti.
- **T/M iniziali**: T=3, M=1 (aggiusta ±1 se background forte/debito grave).
- **Voti**: 1 voto *leggero* (impegno realistico), 1 *forte* (Lex Stygia facoltativa). 
- **Relazioni**: scrivi 2 legami: uno **di Peithō/Charis** (Afrodite) e uno **civico** (Atena/Ermes).

### 4) Strumenti del GM
- **Clocks/Fronti** (6 segmenti ciascuno):
  - *Tempesta a Levante* (Poseidone) — avanza quando si ignorano i segnali del faro.
  - *Dogana Opaca* (Atena/Ermes) — avanza con transazioni senza testimoni.
  - *Keryx Ferito* (Zeus/Ermes) — avanza se la neutralità viene violata.
- **Riti chiave**: 
  - `ritual:trattato-del-messaggero@1.0.0` (Ermes, IE 6) — corridoi di tregua.
  - `ritual:mozione-del-profondo@1.0.0` (Poseidone, IE 8) — chiarire confini.
  - `ritual:sigillo-sobrio@1.0.0` (Atena, IE 10) — riforme/sigilli civici.
  - `ritual:giuramento-stige@1.0.0` (Zeus, IE 7) — vincolo ontologico ai patti.
  - `ritual:purificazione-paian@1.0.0` (Apollo, IE 7) — bonifica di M.
  - `ritual:duello-regolato@1.0.0` (Ares, IE 6) — scontro con limiti.
  - `ritual:festa-di-charis@1.0.0` (Afrodite, IE 6) — coesione.
  - `ritual:sigillo-di-officina@1.0.0` (Efesto, IE 6) — strumenti/mandati.
- **Artefatti utili**: `artifact:herma@1.0.0`, `artifact:tridente-simbolico@1.0.0`, `artifact:aigis@1.0.0`, `artifact:keraunos@1.0.0`.

### 5) Risoluzione rapida (senza sistema)
- **Prova Mitica**: definisci *Obiettivo → Dominio → Epiclesi*
  - *Basso* (compito civile semplice) → IE target 5
  - *Medio* (tregua/bonifica locale) → IE target 6–7
  - *Alto* (confini, riforme, tempeste) → IE target 8–10
- Per alzare IE: +A (luogo giusto), +C (epiclesi precisa), +O (offerta reale), +V (voto/testimoni), +E (urgenza coerente), ridurre M (confessione/restituzione).

---

## MINICAMPAGNA — Trilogia del Porto

> Struttura in 3 atti: **Tensione → Catarsi → Sigillo**. Ogni episodio fornisce scene con *setup, obiettivo, ostacoli, rito consigliato, IE target, conseguenze*. Usa i **Fronti** per scandire il ritmo.

### EP1 — *Il Faro Sordo* (Tensione)
**Setup**: mare in aumento, un mercantile fuori calendario pretende priorità. La luce del faro è intermittente.

**Scene**
1. **Dogana Opaca**  
   - Obiettivo: impedire che la merce entri senza registro.  
   - Ostacoli: pressioni politiche, libelli calunniosi.  
   - Rito: `trattato-del-messaggero` (IE 6).  
   - IE Boost: testimoni pubblici (+V), *herma* su banchina (+A), pegno dei capitani (+O).  
   - Esito: se IE≥6, corridoio attivo; altrimenti *Dogana Opaca +1* e M+1.
2. **Il Promontorio Muto**  
   - Obiettivo: riaccendere il faro in sicurezza.  
   - Ostacoli: attrezzatura guasta, disputa Nord/Sud.  
   - Rito: `mozione-del-profondo` (IE 8) con `tridente-simbolico`.  
   - Esito: se IE≥8, confini e segnali stabilizzati (Tempesta −1); se <8, attiva *Tempesta +1*.
3. **Voci nel Corridoio**  
   - Obiettivo: disinnescare provocazioni nella zona neutra.  
   - Rito: `duello-regolato` (IE 6) **oppure** `purificazione-paian` (IE 7) se c’è colpa riconosciuta.  
   - Esito: successi riducono M di 1; fallimenti aumentano *Keryx Ferito*.

**Chiusura atto**: se due fronti sono ≥3/6, il porto rischia la crisi → EP2 parte sotto pressione (M+1).

---

### EP2 — *Sale e Spighe* (Catarsi)
**Setup**: calendario rituale intreccia *Processione di Demetra* e *Tregua dei Mercanti*. Si propone un **matrimonio politico**.

**Scene**
1. **Redistribuzione del Raccolto**  
   - Obiettivo: evitare carestia locale.  
   - Rito: `mietitura-ritorno` (IE 6) + `festa-di-charis` (IE 6).  
   - Boost: impegno scritto alla redistribuzione (+V), liste pubbliche (+A).  
   - Esito: IE≥6 → T+1, M−1; altrimenti agitazioni (Dogana +1).
2. **Patto Nuziale Pubblico**  
   - Obiettivo: legittimare l’alleanza Nord/Sud.  
   - Rito: `patto-nuziale` (IE 6) o `giuramento-stige` (IE 7) per blindare clausole.  
   - Conflitto: ex‑alleato tenta sabotaggio → *duello‑regolato*.  
   - Esito: se il patto è formale ma non giusto → T aumenta poco e M non scende (segnala rigidità di Era senza misura di Apollo).
3. **Epistola del Keryx**  
   - Obiettivo: riparare un’offesa in zona neutra.  
   - Rito: `trattato-del-messaggero` + `purificazione-paian`.  
   - Esito: se riconosciuta colpa → M−1 extra, altrimenti *Keryx Ferito +1*.

**Chiusura atto**: se T≥5 e M≤2, la città è pronta al **Sigillo**; altrimenti servono ulteriori restituzioni.

---

### EP3 — *Il Fulmine sul Trattato* (Sigillo)
**Setup**: si propone una **riforma delle banchine** e un **corridoio permanente**.

**Scene**
1. **Assemblea sull’Acropoli**  
   - Obiettivo: deliberare fondazioni giuste.  
   - Rito: `sigillo-sobrio` (IE 10) — Atena Polias, controfirma `keraunos` (Zeus) se IE≥10.  
   - Boost: voto dei magistrati (+V), oli e lane non tinte (+O), festa cittadina (+A/C).  
   - Esito: IE≥10 → teofania simbolica (fulmine) e riforma; 8–9 → riforma parziale (T+1, M invariata); ≤7 → rinvio (Dogana +1).
2. **Giuramenti sullo Stige**  
   - Obiettivo: vincolare capi banchina e kerykes.  
   - Rito: `giuramento-stige` (IE 7).  
   - Esito: spergiuro futuro → T−2 per 9 cicli e ban civico automatico.
3. **Ultima Prova**  
   - Obiettivo: verificare la neutralità del corridoio durante una tempesta.  
   - Rito: `mozione-del-profondo` + `trattato-del-messaggero`.  
   - Esito: successo → fronti a 0, porto stabilizzato; fallimento → *Guardiano Punitivo* (mostro) appare finché non avviene catarsi pubblica.

**Epiloghi**
- **Concordia**: quote rotanti, audit pubblici, *fulmine simbolico* sancisce il patto.
- **Rigidità**: forma senza misura → problemi futuri, seme per nuova stagione.
- **Rottura**: neutralità violata → M+2, *Vuoto di Soglia* finché non si rammenda.

---

## STATI & MONITORAGGIO (GM)
- **Fronti**: avanza 1 segmento su fallimenti rilevanti o ignorare segnali; riduci 1 su catarsi/verità pubblica.
- **T/M cittadino**: aggiorna a fine scena; dichiara sempre **costi** di artefatti/teofanie.
- **Oracoli (budget di chiarezza)**: basso=allusivo; medio=condizionale con 1 condizione esplicita; alto=2–3 condizioni esplicite.

---

## HANDOUTS & RISORSE
- Ordinanza di Neutralità (Sala del Trattato) — *handout*.
- Oracolo “Tre Pietre e una Voce” — *handout*.
- Mappa testuale del porto — *handout*.
- PNG mappe (overview, distretto neutrale) sono disponibili nel pacchetto asset.

---

## RICETTE VELOCI "SE… ALLORA…"
- Se una transazione avviene **senza testimoni**, allora **M+1** e *Dogana Opaca +1*, finché non c’è rito di verità (`trattato-del-messaggero`).
- Se un giuramento è **rimandato**, allora `giuramento-stige` richiederà +1 IE al prossimo tentativo (la città diffida).
- Se un duello eccede i limiti, allora **M+1** e serve `purificazione-paian` per bonificare.
- Se un artefatto è usato **fuori firma**, allora effetto dimezzato e **M+1**.

---

## PROMEMORIA LORE
- **Competenza**: chiama l’**epiclesi corretta** (Atena→polis/leggi; Ermes→tregue/strade; Poseidone→mare/confini; Era→patti/matrimonio; Apollo→verità/misura; Ares→conflitto regolato; Afrodite→charis/peithō; Efesto→firma/strumenti; Artemide→selvatico/confini naturali).
- **Lex Stygia**: giuramenti pubblici con costo reale; spergiuro → T−2 per 9 cicli e limite IE max 7 locale.
- **Niente violazioni di Anánkē**: il divino **orienta** traiettorie plausibili, non crea energia dal nulla.
