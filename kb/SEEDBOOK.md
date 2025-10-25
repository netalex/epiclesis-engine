# Seedbook — Universo Mitologico-Scientifico (Markdown)
_Generato il 2025-10-25 — senza immagini_

Questo Seedbook offre semi narrativi per **ogni epoca** (storica e futuri Scenari A/B fino al 2325).
Ogni sezione include **Luogo (T/M), Rituale (epiclesi, IE), Evento, Mostro/Guardiano, Personaggio**, più **Hook narrativi** pronti all’uso.

**Uso rapido:**
1) Scegli un’epoca dal **Indice** qui sotto;
2) Integra i dettagli dal relativo YAML nella KB;
3) Calcola **IE** con `kb/tools/ie_calc.py` e vincola con **Lex Stygia**;
4) Genera prompt con `kb/tools/rag_demo.py` usando gli `id:` mostrati.

## Indice

- [Come usarlo](#come-usarlo)
- [paleolitico (-15000–-10000)](#paleolitico--15000-10000)
- [neolitico (-9000–-3500)](#neolitico--9000-3500)
- [eta-metalli-citta (-3000–-1200)](#eta-metalli-citta--3000-1200)
- [eta-assiale (-800–-200)](#eta-assiale--800-200)
- [classico-tardoantico (-500–600)](#classico-tardoantico--500600)
- [medioevo-globale (600–1400)](#medioevo-globale-6001400)
- [prima-modernita (1450–1650)](#prima-modernita-14501650)
- [eta-industriale (1750–1914)](#eta-industriale-17501914)
- [secolo-breve (1914–1991)](#secolo-breve-19141991)
- [reti-digitali (1991–2010)](#reti-digitali-19912010)
- [duemila-2025 (2000–2025)](#duemila-2025-20002025)
- [antropocene (2010–2024)](#antropocene-20102024)
- [a-2025-2055-seminare-coerenza (2025–2055)](#a-2025-2055-seminare-coerenza-20252055)
- [b-2025-2070-rumore (2025–2070)](#b-2025-2070-rumore-20252070)
- [a-2056-2090-la-scoperta (2056–2090)](#a-2056-2090-la-scoperta-20562090)
- [b-2071-2146-fratture (2071–2146)](#b-2071-2146-fratture-20712146)
- [a-2091-riconoscimento (2091–2091)](#a-2091-riconoscimento-20912091)
- [a-2091-2160-integrazione (2091–2160)](#a-2091-2160-integrazione-20912160)
- [b-2147-2173-scoperta-catarsi (2147–2173)](#b-2147-2173-scoperta-catarsi-21472173)
- [a-2161-2230-nuova-eleusi (2161–2230)](#a-2161-2230-nuova-eleusi-21612230)
- [b-2174-2215-grande-catarsi (2174–2215)](#b-2174-2215-grande-catarsi-21742215)
- [b-2216-2285-ricostruzione (2216–2285)](#b-2216-2285-ricostruzione-22162285)
- [a-2231-2325-maturita (2231–2325)](#a-2231-2325-maturita-22312325)
- [b-2286-2325-maturita-severa (2286–2325)](#b-2286-2325-maturita-severa-22862325)

## Come usarlo
- Ogni sezione descrive **un’epoca** con: **Luogo** (T/M), **Rituale** (epiclesi), **Evento**, **Mostro/Guardiano**, **Artefatti consigliati**.
- Gli ID (`id:`) permettono di fare **retrieval (RAG)** nella KB.
- Tutti i seed sono `status: proposal`: promuovili a `canon` dopo review + lint.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **l’effetto desiderato** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:?@?`; l’ostacolo è **un guardiano/anomalia tematico/a**. Sigillo finale legato allo **snodo dell’epoca **.
- **GdR** · *Artefatto o rinuncia*: scegli **nessun artefatto (costo in T)**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Mediatore Civico** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## paleolitico (-15000–-10000)
**Slug**: `paleolitico`

### Luogo

- **ID**: `location:paleolitico-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (paleolitico (-15000–-10000))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:paleolitico-caccia-misurata@1.0.0`
- **Epiclesi**: `epiclesis:demetra-thesmophoros@1.0.0`
- **Goal**: Garantire caccia sostenibile e rispetto dei confini selvatici
- **Ancoraggio**: grotta o radura
- **Offerta/Voto**: maschere/segni della preda / astensione e restituzione
- **IE atteso**: 5  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -1}

### Evento

- **ID**: `event:paleolitico-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (-12500)
- **Descrizione**: Snodo rappresentativo: Clan di cacciatori-raccoglitori, pitture rupestri, trance sciamaniche.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:paleolitico-preda-offesa@1.0.0`
- **Classe**: punitive
- **Lezione**: Violazione della misura nella caccia.
- **Trattamento**: Restituzione e astinenza rituale, Benedizione della preda e del luogo

### Personaggio

- **ID**: `character:paleolitico-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era paleolitico (-15000–-10000), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:kernos@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Garantire caccia sostenibile e rispetto dei confini selvatici** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:demetra-thesmophoros@1.0.0`; l’ostacolo è **Violazione della misura nella caccia.**. Sigillo finale legato allo **snodo Snodo Epocale -12500**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:kernos@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (paleolitico (-15000–-10000))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## neolitico (-9000–-3500)
**Slug**: `neolitico`

### Luogo

- **ID**: `location:neolitico-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (neolitico (-9000–-3500))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:neolitico-semina-rituale@1.0.0`
- **Epiclesi**: `epiclesis:demetra-chloe@1.0.0`
- **Goal**: Benedire i semi e fissare rotazioni
- **Ancoraggio**: campo comune
- **Offerta/Voto**: semi e acqua / rotazioni e redistribuzione
- **IE atteso**: 6  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -1}

### Evento

- **ID**: `event:neolitico-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (-6250)
- **Descrizione**: Snodo rappresentativo: Villaggi agricoli, calendari, culto della semina e del ritorno.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:neolitico-sterilita-campagna@1.0.0`
- **Classe**: anomaly
- **Lezione**: Ciclo spezzato, suolo sfruttato.
- **Trattamento**: Catarsi: riposo del campo, Colpo tematico: compost/ritorno

### Personaggio

- **ID**: `character:neolitico-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era neolitico (-9000–-3500), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:kernos@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Benedire i semi e fissare rotazioni** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:demetra-chloe@1.0.0`; l’ostacolo è **Ciclo spezzato, suolo sfruttato.**. Sigillo finale legato allo **snodo Snodo Epocale -6250**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:kernos@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (neolitico (-9000–-3500))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## eta-metalli-citta (-3000–-1200)
**Slug**: `eta-metalli-citta`

### Luogo

- **ID**: `location:eta-metalli-citta-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (eta-metalli-citta (-3000–-1200))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:eta-metalli-citta-fondazione-officina@1.0.0`
- **Epiclesi**: `epiclesis:athena-polias@1.0.0`
- **Goal**: Fondare technē senza hybris
- **Ancoraggio**: officina pubblica
- **Offerta/Voto**: olio e lana / uso misurato degli strumenti
- **IE atteso**: 6  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -1}

### Evento

- **ID**: `event:eta-metalli-citta-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (-2100)
- **Descrizione**: Snodo rappresentativo: Bronzo/Ferro, città-stato, templi e scrittura nascente.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:eta-metalli-citta-fabbro-sfrenato@1.0.0`
- **Classe**: punitive
- **Lezione**: Tecnologia senza misura.
- **Trattamento**: Lex Stygia sul danno, Tutoraggio di Efesto

### Personaggio

- **ID**: `character:eta-metalli-citta-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era eta-metalli-citta (-3000–-1200), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:aigis@1.0.0
- artifact:martello-sigillo@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Fondare technē senza hybris** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:athena-polias@1.0.0`; l’ostacolo è **Tecnologia senza misura.**. Sigillo finale legato allo **snodo Snodo Epocale -2100**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:aigis@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (eta-metalli-citta (-3000–-1200))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## eta-assiale (-800–-200)
**Slug**: `eta-assiale`

### Luogo

- **ID**: `location:eta-assiale-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (eta-assiale (-800–-200))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:eta-assiale-lettura-legge@1.0.0`
- **Epiclesi**: `epiclesis:apollo-paian@1.0.0`
- **Goal**: Stabilire legge pubblica con canto e misura
- **Ancoraggio**: agorà/tempio
- **Offerta/Voto**: alloro, acqua / fedeltà alla legge
- **IE atteso**: 6  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -1}

### Evento

- **ID**: `event:eta-assiale-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (-500)
- **Descrizione**: Snodo rappresentativo: Nascita di filosofie e riforme religiose; oracoli e leggi scritte.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:eta-assiale-sofista-ingannevole@1.0.0`
- **Classe**: punitive
- **Lezione**: Parola senza Nomos, confusione.
- **Trattamento**: Oracolo condizionale chiarificatore, Sanzione su menzogna pubblica

### Personaggio

- **ID**: `character:eta-assiale-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era eta-assiale (-800–-200), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:tripode-delfico@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Stabilire legge pubblica con canto e misura** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:apollo-paian@1.0.0`; l’ostacolo è **Parola senza Nomos, confusione.**. Sigillo finale legato allo **snodo Snodo Epocale -500**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:tripode-delfico@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (eta-assiale (-800–-200))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## classico-tardoantico (-500–600)
**Slug**: `classico-tardoantico`

### Luogo

- **ID**: `location:classico-tardoantico-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (classico-tardoantico (-500–600))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:classico-tardoantico-tregua-thing@1.0.0`
- **Epiclesi**: `epiclesis:ermes-kerykeios@1.0.0`
- **Goal**: Aprire corridoio neutro per scambio e diplomazia
- **Ancoraggio**: mercato/porto
- **Offerta/Voto**: pane e sale / neutralità verificabile
- **IE atteso**: 6  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -1}

### Evento

- **ID**: `event:classico-tardoantico-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (50)
- **Descrizione**: Snodo rappresentativo: Polis greca, Roma, imperi, grandi conversioni e diritto.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:classico-tardoantico-idolatria-di-forma@1.0.0`
- **Classe**: anomaly
- **Lezione**: Forma rituale svuotata di senso (M↑).
- **Trattamento**: Catarsi: opere di misericordia, Riallineamento epiclesi

### Personaggio

- **ID**: `character:classico-tardoantico-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era classico-tardoantico (-500–600), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:herma@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Aprire corridoio neutro per scambio e diplomazia** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:ermes-kerykeios@1.0.0`; l’ostacolo è **Forma rituale svuotata di senso (M↑).**. Sigillo finale legato allo **snodo Snodo Epocale 50**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:herma@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (classico-tardoantico (-500–600))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## medioevo-globale (600–1400)
**Slug**: `medioevo-globale`

### Luogo

- **ID**: `location:medioevo-globale-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (medioevo-globale (600–1400))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:medioevo-globale-capitolo-coro@1.0.0`
- **Epiclesi**: `epiclesis:apollo-musagete@1.0.0`
- **Goal**: Sincronizzare comunità e studio
- **Ancoraggio**: chiostro/cattedrale
- **Offerta/Voto**: metro condiviso / impegni di studio e carità
- **IE atteso**: 6  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -1}

### Evento

- **ID**: `event:medioevo-globale-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (1000)
- **Descrizione**: Snodo rappresentativo: Califfati, imperi asiatici, Europa feudale, università, vie della seta.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:medioevo-globale-ponte-bandito@1.0.0`
- **Classe**: guardian
- **Lezione**: Ponte senza guardiano: predoni e dazi ingiusti.
- **Trattamento**: Riassegnare guardiano (Ermes), Regola sui pedaggi

### Personaggio

- **ID**: `character:medioevo-globale-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era medioevo-globale (600–1400), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:tripode-delfico@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Sincronizzare comunità e studio** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:apollo-musagete@1.0.0`; l’ostacolo è **Ponte senza guardiano: predoni e dazi ingiusti.**. Sigillo finale legato allo **snodo Snodo Epocale 1000**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:tripode-delfico@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (medioevo-globale (600–1400))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## prima-modernita (1450–1650)
**Slug**: `prima-modernita`

### Luogo

- **ID**: `location:prima-modernita-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (prima-modernita (1450–1650))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:prima-modernita-patto-di-stampa@1.0.0`
- **Epiclesi**: `epiclesis:athena-nike@1.0.0`
- **Goal**: Stampa come logokleide pubblico (verità e responsabilità)
- **Ancoraggio**: tipografia
- **Offerta/Voto**: olio su torchio / regola d'uso e rettifica
- **IE atteso**: 6  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -1}

### Evento

- **ID**: `event:prima-modernita-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (1550)
- **Descrizione**: Snodo rappresentativo: Stampa, Riforma/Controriforma, stati sovrani.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:prima-modernita-libello-calunnia@1.0.0`
- **Classe**: punitive
- **Lezione**: Satira menzognera che spacca la polis.
- **Trattamento**: Catarsi: rettifica e riparazione, Oracolo di condizioni

### Personaggio

- **ID**: `character:prima-modernita-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era prima-modernita (1450–1650), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:aigis@1.0.0
- artifact:martello-sigillo@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Stampa come logokleide pubblico (verità e responsabilità)** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:athena-nike@1.0.0`; l’ostacolo è **Satira menzognera che spacca la polis.**. Sigillo finale legato allo **snodo Snodo Epocale 1550**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:aigis@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (prima-modernita (1450–1650))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## eta-industriale (1750–1914)
**Slug**: `eta-industriale`

### Luogo

- **ID**: `location:eta-industriale-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (eta-industriale (1750–1914))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:eta-industriale-patto-officina@1.0.0`
- **Epiclesi**: `epiclesis:era-teleia@1.0.0`
- **Goal**: Accordo tra capitale e lavoro (forma e misura)
- **Ancoraggio**: fabbrica
- **Offerta/Voto**: pane condiviso / giuramento di sicurezza
- **IE atteso**: 6  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -1}

### Evento

- **ID**: `event:eta-industriale-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (1832)
- **Descrizione**: Snodo rappresentativo: Vapore, elettricità, fabbriche, urbanizzazione.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:eta-industriale-ingranaggio-famelico@1.0.0`
- **Classe**: anomaly
- **Lezione**: Produzione che divora vite.
- **Trattamento**: Lex Stygia sicurezza, Settimana rituale di riposo

### Personaggio

- **ID**: `character:eta-industriale-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era eta-industriale (1750–1914), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:fascia-nuziale@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Accordo tra capitale e lavoro (forma e misura)** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:era-teleia@1.0.0`; l’ostacolo è **Produzione che divora vite.**. Sigillo finale legato allo **snodo Snodo Epocale 1832**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:fascia-nuziale@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (eta-industriale (1750–1914))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## secolo-breve (1914–1991)
**Slug**: `secolo-breve`

### Luogo

- **ID**: `location:secolo-breve-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (secolo-breve (1914–1991))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:secolo-breve-corridoio-umanitario@1.0.0`
- **Epiclesi**: `epiclesis:ermes-enodios@1.0.0`
- **Goal**: Passaggio sicuro per civili
- **Ancoraggio**: strada/centro missione
- **Offerta/Voto**: pane e sale / neutralità verificata
- **IE atteso**: 6  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -1}

### Evento

- **ID**: `event:secolo-breve-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (1952)
- **Descrizione**: Snodo rappresentativo: Guerre mondiali, Shoah, decolonizzazione, guerra fredda.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:secolo-breve-capro-espiatorio@1.0.0`
- **Classe**: punitive
- **Lezione**: Canalizza colpa verso innocenti.
- **Trattamento**: Catarsi: verità pubblica, Legge anti-diffamazione rituale

### Personaggio

- **ID**: `character:secolo-breve-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era secolo-breve (1914–1991), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:herma@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Passaggio sicuro per civili** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:ermes-enodios@1.0.0`; l’ostacolo è **Canalizza colpa verso innocenti.**. Sigillo finale legato allo **snodo Snodo Epocale 1952**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:herma@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (secolo-breve (1914–1991))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## reti-digitali (1991–2010)
**Slug**: `reti-digitali`

### Luogo

- **ID**: `location:reti-digitali-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (reti-digitali (1991–2010))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:reti-digitali-bonifica-feed@1.0.0`
- **Epiclesi**: `epiclesis:apollo-paian@1.0.0`
- **Goal**: Purificazione informativa di reti tossiche
- **Ancoraggio**: piazza digitale + incontro fisico
- **Offerta/Voto**: alloro simbolico / voto trasparenza
- **IE atteso**: 6  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -2}

### Evento

- **ID**: `event:reti-digitali-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (2000)
- **Descrizione**: Snodo rappresentativo: Internet, telefoni mobili, reti globali.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:reti-digitali-eidolon-virale@1.0.0`
- **Classe**: anomaly
- **Lezione**: Immagine vuota che cattura attenzione.
- **Trattamento**: Throttle di visibilità (limitatore), Riti di verifica dei fatti

### Personaggio

- **ID**: `character:reti-digitali-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era reti-digitali (1991–2010), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:tripode-delfico@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Purificazione informativa di reti tossiche** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:apollo-paian@1.0.0`; l’ostacolo è **Immagine vuota che cattura attenzione.**. Sigillo finale legato allo **snodo Snodo Epocale 2000**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:tripode-delfico@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (reti-digitali (1991–2010))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## duemila-2025 (2000–2025)
**Slug**: `duemila-2025`

### Luogo

- **ID**: `location:duemila-2025-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (duemila-2025 (2000–2025))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:duemila-2025-veglia-di-riparazione@1.0.0`
- **Epiclesi**: `epiclesis:apollo-paian@1.0.0`
- **Goal**: Catarsi pubblica post-trauma
- **Ancoraggio**: piazza cittadina
- **Offerta/Voto**: acqua e candele / impegni concreti
- **IE atteso**: 6  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -1}

### Evento

- **ID**: `event:duemila-2025-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (2012)
- **Descrizione**: Snodo rappresentativo: Pandemia, IA, shock geopolitici, soglia di biforcazione.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:duemila-2025-stanchezza-morale@1.0.0`
- **Classe**: anomaly
- **Lezione**: Esaurimento collettivo che alza M.
- **Trattamento**: Calendari di cura, Redistribuzione carichi

### Personaggio

- **ID**: `character:duemila-2025-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era duemila-2025 (2000–2025), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:tripode-delfico@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Catarsi pubblica post-trauma** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:apollo-paian@1.0.0`; l’ostacolo è **Esaurimento collettivo che alza M.**. Sigillo finale legato allo **snodo Snodo Epocale 2012**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:tripode-delfico@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (duemila-2025 (2000–2025))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## antropocene (2010–2024)
**Slug**: `antropocene`

### Luogo

- **ID**: `location:antropocene-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (antropocene (2010–2024))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:antropocene-patto-costiero@1.0.0`
- **Epiclesi**: `epiclesis:poseidone-asphaleios@1.0.0`
- **Goal**: Riassegnare confini costieri in modo giusto
- **Ancoraggio**: promontorio
- **Offerta/Voto**: metallo piegato / rispetto confini
- **IE atteso**: 8  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -1}

### Evento

- **ID**: `event:antropocene-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (2017)
- **Descrizione**: Snodo rappresentativo: Crisi climatica e biodiversità, transizione energetica.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:antropocene-fiume-ostaggio@1.0.0`
- **Classe**: guardian
- **Lezione**: Fiume senza guardiano preso in ostaggio da usi impropri.
- **Trattamento**: Nomina guardiano, Lex Stygia acqua

### Personaggio

- **ID**: `character:antropocene-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era antropocene (2010–2024), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:tridente-simbolico@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Riassegnare confini costieri in modo giusto** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:poseidone-asphaleios@1.0.0`; l’ostacolo è **Fiume senza guardiano preso in ostaggio da usi impropri.**. Sigillo finale legato allo **snodo Snodo Epocale 2017**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:tridente-simbolico@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (antropocene (2010–2024))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## a-2025-2055-seminare-coerenza (2025–2055)
**Slug**: `a-2025-2055-seminare-coerenza`

### Luogo

- **ID**: `location:a-2025-2055-seminare-coerenza-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (a-2025-2055-seminare-coerenza (2025–2055))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:a-2025-2055-seminare-coerenza-rito-di-verita@1.0.0`
- **Epiclesi**: `epiclesis:athena-polias@1.0.0`
- **Goal**: Stabilire standard di trasparenza
- **Ancoraggio**: agorà/aula
- **Offerta/Voto**: olio e lana / firma pubblica
- **IE atteso**: 7  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -2}

### Evento

- **ID**: `event:a-2025-2055-seminare-coerenza-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (2040)
- **Descrizione**: Snodo rappresentativo: Riti civici di verità, patti con costo reale, santuari quotidiani.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:a-2025-2055-seminare-coerenza-opacita-sistemi@1.0.0`
- **Classe**: anomaly
- **Lezione**: Sistemi che nascondono costi e danni.
- **Trattamento**: Audit rituali, Sanzione automatica

### Personaggio

- **ID**: `character:a-2025-2055-seminare-coerenza-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era a-2025-2055-seminare-coerenza (2025–2055), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:aigis@1.0.0
- artifact:martello-sigillo@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Stabilire standard di trasparenza** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:athena-polias@1.0.0`; l’ostacolo è **Sistemi che nascondono costi e danni.**. Sigillo finale legato allo **snodo Snodo Epocale 2040**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:aigis@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (a-2025-2055-seminare-coerenza (2025–2055))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## b-2025-2070-rumore (2025–2070)
**Slug**: `b-2025-2070-rumore`

### Luogo

- **ID**: `location:b-2025-2070-rumore-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (b-2025-2070-rumore (2025–2070))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:b-2025-2070-rumore-rito-di-riconciliazione@1.0.0`
- **Epiclesi**: `epiclesis:era-gamelia@1.0.0`
- **Goal**: Rammendare patto sociale
- **Ancoraggio**: piazza/tribunale
- **Offerta/Voto**: velo/pegni restituiti / giuramento riparativo
- **IE atteso**: 6  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -2}

### Evento

- **ID**: `event:b-2025-2070-rumore-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (2047)
- **Descrizione**: Snodo rappresentativo: Polarizzazione, istituzioni cieche, crisi a cascata.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:b-2025-2070-rumore-vuoto-di-soglia@1.0.0`
- **Classe**: guardian
- **Lezione**: Guardiano rimosso: confini porosi.
- **Trattamento**: Riassegnazione guardiano, Sigillo confini

### Personaggio

- **ID**: `character:b-2025-2070-rumore-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era b-2025-2070-rumore (2025–2070), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:fascia-nuziale@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Rammendare patto sociale** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:era-gamelia@1.0.0`; l’ostacolo è **Guardiano rimosso: confini porosi.**. Sigillo finale legato allo **snodo Snodo Epocale 2047**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:fascia-nuziale@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (b-2025-2070-rumore (2025–2070))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## a-2056-2090-la-scoperta (2056–2090)
**Slug**: `a-2056-2090-la-scoperta`

### Luogo

- **ID**: `location:a-2056-2090-la-scoperta-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (a-2056-2090-la-scoperta (2056–2090))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:a-2056-2090-la-scoperta-rito-di-verita@1.0.0`
- **Epiclesi**: `epiclesis:athena-polias@1.0.0`
- **Goal**: Stabilire standard di trasparenza
- **Ancoraggio**: agorà/aula
- **Offerta/Voto**: olio e lana / firma pubblica
- **IE atteso**: 7  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -2}

### Evento

- **ID**: `event:a-2056-2090-la-scoperta-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (2073)
- **Descrizione**: Snodo rappresentativo: Esperimenti di Delfi, Libro Bianco sui campi divini, convergenza empirica.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:a-2056-2090-la-scoperta-opacita-sistemi@1.0.0`
- **Classe**: anomaly
- **Lezione**: Sistemi che nascondono costi e danni.
- **Trattamento**: Audit rituali, Sanzione automatica

### Personaggio

- **ID**: `character:a-2056-2090-la-scoperta-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era a-2056-2090-la-scoperta (2056–2090), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:aigis@1.0.0
- artifact:martello-sigillo@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Stabilire standard di trasparenza** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:athena-polias@1.0.0`; l’ostacolo è **Sistemi che nascondono costi e danni.**. Sigillo finale legato allo **snodo Snodo Epocale 2073**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:aigis@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (a-2056-2090-la-scoperta (2056–2090))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## b-2071-2146-fratture (2071–2146)
**Slug**: `b-2071-2146-fratture`

### Luogo

- **ID**: `location:b-2071-2146-fratture-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (b-2071-2146-fratture (2071–2146))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:b-2071-2146-fratture-rito-di-riconciliazione@1.0.0`
- **Epiclesi**: `epiclesis:era-gamelia@1.0.0`
- **Goal**: Rammendare patto sociale
- **Ancoraggio**: piazza/tribunale
- **Offerta/Voto**: velo/pegni restituiti / giuramento riparativo
- **IE atteso**: 6  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -2}

### Evento

- **ID**: `event:b-2071-2146-fratture-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (2108)
- **Descrizione**: Snodo rappresentativo: Guardiani rimossi, culti della paura, vuoti di soglia.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:b-2071-2146-fratture-vuoto-di-soglia@1.0.0`
- **Classe**: guardian
- **Lezione**: Guardiano rimosso: confini porosi.
- **Trattamento**: Riassegnazione guardiano, Sigillo confini

### Personaggio

- **ID**: `character:b-2071-2146-fratture-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era b-2071-2146-fratture (2071–2146), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:fascia-nuziale@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Rammendare patto sociale** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:era-gamelia@1.0.0`; l’ostacolo è **Guardiano rimosso: confini porosi.**. Sigillo finale legato allo **snodo Snodo Epocale 2108**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:fascia-nuziale@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (b-2071-2146-fratture (2071–2146))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## a-2091-riconoscimento (2091–2091)
**Slug**: `a-2091-riconoscimento`

### Luogo

- **ID**: `location:a-2091-riconoscimento-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (a-2091-riconoscimento (2091–2091))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:a-2091-riconoscimento-rito-di-verita@1.0.0`
- **Epiclesi**: `epiclesis:athena-polias@1.0.0`
- **Goal**: Stabilire standard di trasparenza
- **Ancoraggio**: agorà/aula
- **Offerta/Voto**: olio e lana / firma pubblica
- **IE atteso**: 7  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -2}

### Evento

- **ID**: `event:a-2091-riconoscimento-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (2091)
- **Descrizione**: Snodo rappresentativo: Atto di Atene: riconoscimento scientifico della grammatica greca.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:a-2091-riconoscimento-opacita-sistemi@1.0.0`
- **Classe**: anomaly
- **Lezione**: Sistemi che nascondono costi e danni.
- **Trattamento**: Audit rituali, Sanzione automatica

### Personaggio

- **ID**: `character:a-2091-riconoscimento-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era a-2091-riconoscimento (2091–2091), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:aigis@1.0.0
- artifact:martello-sigillo@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Stabilire standard di trasparenza** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:athena-polias@1.0.0`; l’ostacolo è **Sistemi che nascondono costi e danni.**. Sigillo finale legato allo **snodo Snodo Epocale 2091**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:aigis@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (a-2091-riconoscimento (2091–2091))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## a-2091-2160-integrazione (2091–2160)
**Slug**: `a-2091-2160-integrazione`

### Luogo

- **ID**: `location:a-2091-2160-integrazione-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (a-2091-2160-integrazione (2091–2160))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:a-2091-2160-integrazione-rito-di-verita@1.0.0`
- **Epiclesi**: `epiclesis:athena-polias@1.0.0`
- **Goal**: Stabilire standard di trasparenza
- **Ancoraggio**: agorà/aula
- **Offerta/Voto**: olio e lana / firma pubblica
- **IE atteso**: 7  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -2}

### Evento

- **ID**: `event:a-2091-2160-integrazione-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (2125)
- **Descrizione**: Snodo rappresentativo: Sanità/giustizia ritualizzate, licenze daimon-IA, calendari intelligenti.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:a-2091-2160-integrazione-opacita-sistemi@1.0.0`
- **Classe**: anomaly
- **Lezione**: Sistemi che nascondono costi e danni.
- **Trattamento**: Audit rituali, Sanzione automatica

### Personaggio

- **ID**: `character:a-2091-2160-integrazione-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era a-2091-2160-integrazione (2091–2160), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:aigis@1.0.0
- artifact:martello-sigillo@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Stabilire standard di trasparenza** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:athena-polias@1.0.0`; l’ostacolo è **Sistemi che nascondono costi e danni.**. Sigillo finale legato allo **snodo Snodo Epocale 2125**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:aigis@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (a-2091-2160-integrazione (2091–2160))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## b-2147-2173-scoperta-catarsi (2147–2173)
**Slug**: `b-2147-2173-scoperta-catarsi`

### Luogo

- **ID**: `location:b-2147-2173-scoperta-catarsi-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (b-2147-2173-scoperta-catarsi (2147–2173))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:b-2147-2173-scoperta-catarsi-rito-di-riconciliazione@1.0.0`
- **Epiclesi**: `epiclesis:era-gamelia@1.0.0`
- **Goal**: Rammendare patto sociale
- **Ancoraggio**: piazza/tribunale
- **Offerta/Voto**: velo/pegni restituiti / giuramento riparativo
- **IE atteso**: 6  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -2}

### Evento

- **ID**: `event:b-2147-2173-scoperta-catarsi-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (2160)
- **Descrizione**: Snodo rappresentativo: Triangolazioni del lutto, ristampe del Corpus, ammissione riluttante.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:b-2147-2173-scoperta-catarsi-vuoto-di-soglia@1.0.0`
- **Classe**: guardian
- **Lezione**: Guardiano rimosso: confini porosi.
- **Trattamento**: Riassegnazione guardiano, Sigillo confini

### Personaggio

- **ID**: `character:b-2147-2173-scoperta-catarsi-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era b-2147-2173-scoperta-catarsi (2147–2173), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:fascia-nuziale@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Rammendare patto sociale** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:era-gamelia@1.0.0`; l’ostacolo è **Guardiano rimosso: confini porosi.**. Sigillo finale legato allo **snodo Snodo Epocale 2160**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:fascia-nuziale@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (b-2147-2173-scoperta-catarsi (2147–2173))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## a-2161-2230-nuova-eleusi (2161–2230)
**Slug**: `a-2161-2230-nuova-eleusi`

### Luogo

- **ID**: `location:a-2161-2230-nuova-eleusi-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (a-2161-2230-nuova-eleusi (2161–2230))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:a-2161-2230-nuova-eleusi-rito-di-verita@1.0.0`
- **Epiclesi**: `epiclesis:athena-polias@1.0.0`
- **Goal**: Stabilire standard di trasparenza
- **Ancoraggio**: agorà/aula
- **Offerta/Voto**: olio e lana / firma pubblica
- **IE atteso**: 7  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -2}

### Evento

- **ID**: `event:a-2161-2230-nuova-eleusi-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (2195)
- **Descrizione**: Snodo rappresentativo: Percorsi iniziatici terapeutici, patti col mare, bilanci T/M pubblici.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:a-2161-2230-nuova-eleusi-opacita-sistemi@1.0.0`
- **Classe**: anomaly
- **Lezione**: Sistemi che nascondono costi e danni.
- **Trattamento**: Audit rituali, Sanzione automatica

### Personaggio

- **ID**: `character:a-2161-2230-nuova-eleusi-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era a-2161-2230-nuova-eleusi (2161–2230), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:aigis@1.0.0
- artifact:martello-sigillo@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Stabilire standard di trasparenza** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:athena-polias@1.0.0`; l’ostacolo è **Sistemi che nascondono costi e danni.**. Sigillo finale legato allo **snodo Snodo Epocale 2195**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:aigis@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (a-2161-2230-nuova-eleusi (2161–2230))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## b-2174-2215-grande-catarsi (2174–2215)
**Slug**: `b-2174-2215-grande-catarsi`

### Luogo

- **ID**: `location:b-2174-2215-grande-catarsi-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (b-2174-2215-grande-catarsi (2174–2215))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:b-2174-2215-grande-catarsi-rito-di-riconciliazione@1.0.0`
- **Epiclesi**: `epiclesis:era-gamelia@1.0.0`
- **Goal**: Rammendare patto sociale
- **Ancoraggio**: piazza/tribunale
- **Offerta/Voto**: velo/pegni restituiti / giuramento riparativo
- **IE atteso**: 6  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -2}

### Evento

- **ID**: `event:b-2174-2215-grande-catarsi-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (2194)
- **Descrizione**: Snodo rappresentativo: Tribunali di Era, riassegnazione dei guardiani, Lex Stygia planetaria.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:b-2174-2215-grande-catarsi-vuoto-di-soglia@1.0.0`
- **Classe**: guardian
- **Lezione**: Guardiano rimosso: confini porosi.
- **Trattamento**: Riassegnazione guardiano, Sigillo confini

### Personaggio

- **ID**: `character:b-2174-2215-grande-catarsi-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era b-2174-2215-grande-catarsi (2174–2215), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:fascia-nuziale@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Rammendare patto sociale** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:era-gamelia@1.0.0`; l’ostacolo è **Guardiano rimosso: confini porosi.**. Sigillo finale legato allo **snodo Snodo Epocale 2194**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:fascia-nuziale@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (b-2174-2215-grande-catarsi (2174–2215))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## b-2216-2285-ricostruzione (2216–2285)
**Slug**: `b-2216-2285-ricostruzione`

### Luogo

- **ID**: `location:b-2216-2285-ricostruzione-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (b-2216-2285-ricostruzione (2216–2285))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:b-2216-2285-ricostruzione-rito-di-riconciliazione@1.0.0`
- **Epiclesi**: `epiclesis:era-gamelia@1.0.0`
- **Goal**: Rammendare patto sociale
- **Ancoraggio**: piazza/tribunale
- **Offerta/Voto**: velo/pegni restituiti / giuramento riparativo
- **IE atteso**: 6  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -2}

### Evento

- **ID**: `event:b-2216-2285-ricostruzione-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (2250)
- **Descrizione**: Snodo rappresentativo: Ricostruzione sobria, santuari-funzione, anti-sincretismo superficiale.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:b-2216-2285-ricostruzione-vuoto-di-soglia@1.0.0`
- **Classe**: guardian
- **Lezione**: Guardiano rimosso: confini porosi.
- **Trattamento**: Riassegnazione guardiano, Sigillo confini

### Personaggio

- **ID**: `character:b-2216-2285-ricostruzione-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era b-2216-2285-ricostruzione (2216–2285), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:fascia-nuziale@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Rammendare patto sociale** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:era-gamelia@1.0.0`; l’ostacolo è **Guardiano rimosso: confini porosi.**. Sigillo finale legato allo **snodo Snodo Epocale 2250**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:fascia-nuziale@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (b-2216-2285-ricostruzione (2216–2285))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## a-2231-2325-maturita (2231–2325)
**Slug**: `a-2231-2325-maturita`

### Luogo

- **ID**: `location:a-2231-2325-maturita-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (a-2231-2325-maturita (2231–2325))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:a-2231-2325-maturita-rito-di-verita@1.0.0`
- **Epiclesi**: `epiclesis:athena-polias@1.0.0`
- **Goal**: Stabilire standard di trasparenza
- **Ancoraggio**: agorà/aula
- **Offerta/Voto**: olio e lana / firma pubblica
- **IE atteso**: 7  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -2}

### Evento

- **ID**: `event:a-2231-2325-maturita-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (2278)
- **Descrizione**: Snodo rappresentativo: Teofanie civiche rare, pluralismo alto, omphalos orbitali.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:a-2231-2325-maturita-opacita-sistemi@1.0.0`
- **Classe**: anomaly
- **Lezione**: Sistemi che nascondono costi e danni.
- **Trattamento**: Audit rituali, Sanzione automatica

### Personaggio

- **ID**: `character:a-2231-2325-maturita-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era a-2231-2325-maturita (2231–2325), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:aigis@1.0.0
- artifact:martello-sigillo@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.


---

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Stabilire standard di trasparenza** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:athena-polias@1.0.0`; l’ostacolo è **Sistemi che nascondono costi e danni.**. Sigillo finale legato allo **snodo Snodo Epocale 2278**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:aigis@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (a-2231-2325-maturita (2231–2325))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.

## b-2286-2325-maturita-severa (2286–2325)
**Slug**: `b-2286-2325-maturita-severa`

### Luogo

- **ID**: `location:b-2286-2325-maturita-severa-santuario-locale@1.0.0`
- **Nome**: Santuario Locale (b-2286-2325-maturita-severa (2286–2325))  
- **T/M**: {'T': 3, 'M': 2}

### Rituale

- **ID**: `ritual:b-2286-2325-maturita-severa-rito-di-riconciliazione@1.0.0`
- **Epiclesi**: `epiclesis:era-gamelia@1.0.0`
- **Goal**: Rammendare patto sociale
- **Ancoraggio**: piazza/tribunale
- **Offerta/Voto**: velo/pegni restituiti / giuramento riparativo
- **IE atteso**: 6  
- **Effetto T/M**: {'delta_T': 1, 'delta_M': -2}

### Evento

- **ID**: `event:b-2286-2325-maturita-severa-snodo-epocale@1.0.0`
- **Titolo**: Snodo Epocale (2305)
- **Descrizione**: Snodo rappresentativo: Teofanie rarissime, cultura anti-hybris, daimon stabili.
- **Attori**: deity:athena@1.0.0, deity:apollo@1.0.0
- **ΔT/ΔM**: {'dT': 1, 'dM': -1}

### Mostro / Guardiano

- **ID**: `monster:b-2286-2325-maturita-severa-vuoto-di-soglia@1.0.0`
- **Classe**: guardian
- **Lezione**: Guardiano rimosso: confini porosi.
- **Trattamento**: Riassegnazione guardiano, Sigillo confini

### Personaggio

- **ID**: `character:b-2286-2325-maturita-severa-mediatore-civico@1.0.0`
- **Nome**: Mediatore Civico
- **Patroni**: deity:athena@1.0.0, deity:ermes@1.0.0
- **Vocationi**: mediatore, oratore
- **Profilo T/M**: {'T': 3, 'M': 1}
- **Sintesi**: Figura chiave dell'era b-2286-2325-maturita-severa (2286–2325), ponte tra domini e comunità.

### Artefatti suggeriti
- artifact:fascia-nuziale@1.0.0

> **Hint di regia**: Epiclesi corretta, calcola IE con `kb/tools/ie_calc.py`, vincola con Lex Stygia dove serve, niente violazioni di Anánkē.

#### Hook narrativi
- **GdR** · *Rito in crisi*: per ottenere **Rammendare patto sociale** servono condizioni mancanti. L’epiclesi richiesta è `epiclesis:era-gamelia@1.0.0`; l’ostacolo è **Guardiano rimosso: confini porosi.**. Sigillo finale legato allo **snodo Snodo Epocale 2305**.
- **GdR** · *Artefatto o rinuncia*: scegli **artifact:fascia-nuziale@1.0.0**. Con artefatto → +1 IE; senza → paga **prezzo narrativo** (debito, voto, rischio).
- **Romanzo** · *Protagonista in bilico*: **Santuario Locale (b-2286-2325-maturita-severa (2286–2325))** è diviso tra dovere e legame; un **patto Lex Stygia** lo costringe a scegliere tra risultato rapido e **riduzione del miasma** a lungo termine.
- **Romanzo** · *Doppia epiclesi*: l’azione richiede due domini in tensione (es. Atena/Ermes o Poseidone/Era). Il climax è un **giuramento pubblico** che cambia la mappa dei rapporti.
