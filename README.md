# StoryCheck AI Agent

AI agent koji automatizuje analizu user story-ja za potrebe Product Owner-a i QA tima. Agent nije chatbot — na osnovu ulaznog user story-ja, kroz 6 koraka generiše kompletan strukturisan izveštaj.

## Funkcionalnosti

Agent kroz LangGraph workflow prolazi kroz sledeće korake:
1. **Analiza kvaliteta** user story-ja (INVEST principi) + predlog poboljšane verzije
2. **Generisanje Acceptance Criteria** (Given/When/Then format)
3. **Generisanje Test Cases** (pozitivni i negativni scenariji)
4. **Procena rizika** sa predlozima za ublažavanje
5. **Preporuke** za razvojni tim
6. **Čuvanje** kompletnog izveštaja u `output/report.md`

## Tehnologije

- Python
- LangChain / LangGraph
- Groq (LLM - llama-3.3-70b-versatile)
- python-dotenv

## Instalacija

```bash
git clone https://github.com/kristinarbc/storycheck-ai-agent_uriz.git
cd storycheck-ai-agent_uriz
python -m venv .venv
source .venv/Scripts/activate   # Git Bash na Windows-u
pip install -r requirements.txt
```

Napravi `.env` fajl u root folderu (ovaj fajl se ne pushuje na GitHub, samo za lokalno korišćenje):

```
GROQ_API_KEY=tvoj_licni_key_ovde
```

Key se generiše besplatno na [console.groq.com](https://console.groq.com) → API Keys → Create API Key.

## Pokretanje

```bash
python main.py
```

Agent nudi dve opcije unosa:
1. Učitavanje iz `data/stories.json` (bira se index story-ja)
2. Ručni unos user story-ja preko terminala

Rezultat se čuva u `output/report.md`.

## Primer

**Ulaz:**
```
As a registered user, I want to upload my artwork, so that I can share my paintings with other users.
```

**Izlaz (deo izveštaja):**
- Analiza kvaliteta i INVEST provera
- 4-6 Acceptance Criteria
- 3 pozitivna + 3 negativna test case-a
- 3-5 identifikovanih rizika sa mitigacijom
- 3 preporuke za tim

## Struktura projekta

```
storycheck-ai-agent_uriz/
├── main.py
├── requirements.txt
├── README.md
├── .env
├── agent/
│   ├── llm.py
│   ├── prompts.py
│   └── workflow.py
├── data/
│   └── stories.json
├── output/
│   └── report.md
└── services/
    └── loader.py
```

## Ograničenja

- Agent trenutno radi sa jednim user story-jem po pokretanju (nema batch obradu)
- Kvalitet izlaza zavisi od izabranog LLM modela
- Nema perzistentnu bazu podataka - izveštaji se čuvaju kao lokalni fajlovi

## Mogućnosti unapređenja

- Integracija sa JIRA API-jem za automatski unos generisanih task-ova
- Batch obrada više story-ja odjednom
- Web/GUI interfejs umesto terminala
```
