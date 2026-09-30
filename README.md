# Text Categorization Based on Fine-tuning of Pre-trained Language Models

*Ταξινόμηση Κειμένων με Προσαρμογή Προ-εκπαιδευμένων Γλωσσικών Μοντέλων*

[![Status: archived](https://img.shields.io/badge/status-archived%20%282019%29-lightgrey)](#)
[![Follow-up: genre-and-authorship-bench](https://img.shields.io/badge/follow--up-genre--and--authorship--bench-2a78d6)](https://github.com/athanbonis/genre-and-authorship-bench)

Undergraduate thesis, Department of Information and Communication Systems Engineering,
University of the Aegean, September 2019.

- **Authors:** Athanasios Bonis, Georgios Dimopoulos
- **Supervisor:** Efstathios Stamatatos, Associate Professor
- **Thesis (PDF):** [`docs/thesis.pdf`](docs/thesis.pdf) (in Greek) ·
  [Hellanicus institutional repository](https://hellanicus.lib.aegean.gr/items/f79c6c6c-fcf2-4985-b396-8a1117c06b4b)

> **Archived.** This repository is kept as the 2019 record of the thesis and is not maintained.
>
> **Follow-up work:** the questions studied here are being rebuilt from scratch as an open,
> reproducible benchmark in
> [athanbonis/genre-and-authorship-bench](https://github.com/athanbonis/genre-and-authorship-bench),
> with a plain-language explainer at [whowrotethis.athanbonis.com](https://whowrotethis.athanbonis.com).

## Abstract

Text Categorization is an important study in the field of Text-Mining, with a wide range of
applications. In recent years, through the development of Neural Networks, many techniques
have been developed such as pre-trained language models, which are applicable to Natural
Language Processing (NLP). Currently, the best practice for categorizing texts, e.g. writer
recognition, is the application of Pre-Trained Language Models through Fine-Tuning. In
this research, we analyze and present the application of the Universal Language Model
Fine Tuning technique (ULMFiT) in some text categorization applications, which is developed
by NLP's fast.ai research team. Furthermore, we compare this technique with others, and
we conclude, presenting the results of this comparison.

**Keywords:** Text Mining, NLP, Authorship Attribution, Fine-Tuning, ULMFiT.

## Results reported in the thesis

ULMFiT (fastai v1, AWD-LSTM pre-trained on WikiText-103) compared with the best
previously published result on each dataset (Chapter 6 of the thesis):

| Task | Dataset | Best prior result | ULMFiT |
|---|---|---|---|
| Authorship attribution, single domain | C10 (10 authors, 500 test texts) | 80.6% (character n-grams) | 70.7% |
| Authorship attribution, cross domain | PAN-18 fanfiction (problems 1–4, English) | 0.697 (PAN-18 baseline, English) | 0.11–0.31 accuracy per problem |
| Web genre identification (10-fold CV) | 7-genre (Santini) | 96.5% (textual + structural) | 99.1% |
| Web genre identification (10-fold CV) | KI-04 | 84.1% (textual + structural) | 92.6% |

Main conclusion of the thesis: the fine-tuned language model outperformed earlier approaches on
web genre identification, but fell behind character n-gram methods on authorship attribution,
and did not work on the non-English PAN-18 problems.

### Known caveats

These were found when the thesis was reviewed in 2026. They are listed so that the numbers
are not used without them.

- **Genre results may be inflated.** Mean test accuracy is higher than validation accuracy
  (99.1 vs 95.2 on 7-genre, 92.6 vs 78.6 on KI-04). A likely cause is that the language model
  was fine-tuned on text that included each fold's test documents.
- **PAN-18 numbers are inconsistent.** Table 6.3 lists 97 correct out of 40 texts for problem 3.
  The per-problem accuracies average about 0.19, while Table 6.4 reports 0.376. PAN-18 is
  officially scored with macro-F1, not accuracy.
- **English-only model.** The pre-trained model was English-only, which explains the failure on
  the French, Italian, Polish and Spanish problems.
- **Swapped captions.** The captions of Tables 6.2 (C10) and 6.8 (KI-04) are swapped.

## Repository contents

| Path | Contents |
|---|---|
| `docs/thesis.pdf` | The thesis |
| `Text Mining Test.ipynb` | First ULMFiT test on the IMDB sample dataset |
| `pan-baseline.py` | Official PAN-18 cross-domain authorship attribution baseline (character n-grams + linear SVM), by E. Stamatatos |
| `pan18/` | PAN-18 cross-domain authorship attribution development corpus (20 problems, 5 languages) and the baseline's answers |
| `funficts_predict.py`, `unknown_tocsv.py` | Convert PAN-18 problems to CSV files |
| `fastai_funficts.py` | ULMFiT language-model fine-tuning on PAN-18 problem 1 |
| `answers/`, `unknown_dsets/` | Generated CSV files for PAN-18 |
| `website-genres-classification/` | 7-genre and KI-04 corpora, and the scripts that convert them to CSV |

### Reproducibility

This repository contains only part of the code behind the thesis:

- The C10 experiment, the 10-fold cross-validation genre experiments and the PAN-18 classifier
  training shown in Chapter 6 are **not** included.
- The code uses the fastai v1 API (`TextLMDataBunch`, etc.), which does not run on current fastai.
  See `requirements.txt` for the original environment.
- Known bugs: `unknown_tocsv.py` reads from `pan18/<problem>` instead of
  `pan18/datasets/<problem>`, `funficts_predict.py` computes a validation split that it never
  writes, and the genre scripts use hard-coded Windows paths.

## Datasets and credits

The datasets belong to their creators and are included only for the record of the thesis.
Check each dataset's terms before reusing it.

- **PAN-18 cross-domain authorship attribution:** Kestemont et al., *Overview of the Author
  Identification Task at PAN-2018*, CLEF 2018.
- **7-genre:** M. Santini, web genre corpus.
- **KI-04:** S. Meyer zu Eissen and B. Stein, *Genre Classification of Web Pages*, KI 2004.
- **ULMFiT:** J. Howard and S. Ruder, *Universal Language Model Fine-tuning for Text
  Classification*, ACL 2018.

## Citation

```bibtex
@thesis{bonis2019textcategorization,
  title       = {Text Categorization Based on Fine-tuning of Pre-trained Language Models},
  author      = {Bonis, Athanasios and Dimopoulos, Georgios},
  type        = {Undergraduate thesis},
  institution = {University of the Aegean, Department of Information and Communication Systems Engineering},
  year        = {2019},
  month       = sep,
  url         = {https://hellanicus.lib.aegean.gr/items/f79c6c6c-fcf2-4985-b396-8a1117c06b4b}
}
```
