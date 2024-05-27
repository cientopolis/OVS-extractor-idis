# OVS-extractor-idis

Esta herramienta presenta diferentes enfoques de extracción de pares atributo-valor en descripciones inmobiliarias, utilizando técnicas de NLP

## 🌱 Instalación

Usando [pip](https://pip.pypa.io/en/stable/)

```bash
pip install -r requirements.txt
```

## 🌱 Uso

```python
py extractor -h
usage: [-h] -s {qa,rbm,ner} [-i | --inferences | --no-inferences]

Run an AI model for QA, NER and RBM and compute the results      

options:
  -h, --help            show this help message and exit
  -s {qa,rbm,ner}, --strategy {qa,rbm,ner}
                        Select the strategy
  -i, --inferences, --no-inferences
                        Run with inferences (default: False)
```
Extracción sin inferencias usando rule-based matching
```python
py extractor -s rbm
```

## 🌱 Licencia

[MIT](https://choosealicense.com/licenses/mit/)