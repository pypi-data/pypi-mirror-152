# Robustness Evaluation of Pre-trained Language Models in the Russian Language

This is a repo with experiments for *Robustness Evaluation of Pre-trained Language Models in the Russian Language* and a tool `ru_attacker` for attacking Russian NLP models

### Installation
```
pip install ru_attacker
```
### Usage example

Set model
```
>>> from ru_attacker.models import RobertaModel
>>> roberta_checkpoints = "Roberta_checkpoints"
>>> ruRoberta = RobertaModel(roberta_checkpoints)
```

Set dataset
```
>>> from ru_attacker.models.set_dataset import get_data
>>> data_dir = "TERRa/val.jsonl" 
>>> data = get_data(data_dir)
```

Set attack

You have to define `transformation`, `goal_function` and `type_perturbation`. `constraints` and `search_method` are optional
```
>>> from ru_attacker.attacks.transformations import BackTranslation  # transformation
>>> from ru_attacker.attacks.goal_function import LabelPreserving  # goal function
>>> from ru_attacker.attacks.constraints import GrammarAcceptability, SemanticSimilarity  # constraints
>>> from ru_attacker.attacks.search_method import GreedySearch  # search method
>>> from ru_attacker.attacks import Attack  # attack wrapper
>>> backtranslation = Attack(
        transformation=BackTranslation(languages=["en", "fr", "de"]),  # you can set languages manually or use the default ones
        goal_function=LabelPreserving(),
        type_perturbation="hypothesis",  # to what part perturbation is applied {"hypothesis", "premise"}
        constraints=[GrammarAcceptability(), SemanticSimilarity()],
        search_method=GreedySearch()
    )
```

Attack model and view results
```
>>> results = backtranslation.attack(ruRoberta, data)
                  [Succeeded / Failed / Skipped / Total] 0 / 1 / 0 / 1:
                  entailment --> entailment
                  original premise: """Решение носит символический характер, так как взыскать компенсацию практически невозможно"", - отмечается в сообщении."
                  original hypothesis: Взыскать компенсацию не получится.

                  transformed: Компенсации не будет.

                  

                  [Succeeded / Failed / Skipped / Total] 1 / 1 / 0 / 2:
                  entailment --> not_entailment
                  original premise: Об этом вечером во вторник, 17 января, сообщила пресс-служба Спасательного департамента, отметив, что немецкую противотанковую мину Tellermine 42 обнаружили в на улице Кеэвисе в ходе земляных работ. Спасатели эвакуировали жителей окрестных домов, офисов и складских помещений. Уничтожать мину на месте не стали, поскольку это угрожало повреждению трассы трубопровода.
                  original hypothesis: На улице Кеэвисе жителей эвакуировали из-за мины.

                  transformed: На улице Касери эвакуировали жителей из мин.
```
Convert results to DataFrame
```
>>> import pandas as pd
>>> dataframe = pd.DataFrame(results)
```

Here is [`Tutorial`](https://github.com/yuliya1324/ru_attacker/blob/main/Tutorial.ipynb)

### Experiments

All the data used in experiments and the results are in 
[`data`](https://github.com/yuliya1324/ru_attacker/tree/main/data) 
folder ([`TERRa`](https://github.com/yuliya1324/ru_attacker/tree/main/data/TERRa) and 
[`results`](https://github.com/yuliya1324/ru_attacker/tree/main/data/results) correspondingly).

All experiments can be reproduced in [`Experiments.ipynb`](https://github.com/yuliya1324/ru_attacker/blob/main/Experiments.ipynb).

Models checkpoints are available via:
- [ruT5-large](https://drive.google.com/file/d/1NmyPu_VCgR4IO3PIcyV4BHMShYGhqtSJ/view?usp=sharing)
- [ruRoberta-large](https://drive.google.com/file/d/1llS2LbnW9KREFAHGCS1EteIUOKE6WO7U/view?usp=sharing)

