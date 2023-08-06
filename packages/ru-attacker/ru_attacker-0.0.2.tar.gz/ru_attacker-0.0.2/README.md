# ru_attacker

This is a tool for attacking Russian NLP models

### Installation
```
pip install ru_attacker
```
### Usage example

Set model
```
>>> from ru_attacker.models import RobertaModel
>>> roberta_checkpoints =  "Roberta_checkpoints"
>>> ruRoberta = RobertaModel(roberta_checkpoints)
```

Set dataset
```
>>> from ru_attacker.models.set_dataset import get_data
>>> data_dir = "TERRa/val.jsonl" 
>>> data = get_data(data_dir)
```

Set attack
```
>>> from ru_attacker.ru_attacker.attacks import WordOrder
>>> word_order_attack = WordOrder()
```

Attack model and view results
```
>>> results = word_order_attack.attack(ruT5, data)
                  [Succeeded / Failed / Skipped / Total] 0 / 1 / 0 / 1:
                  entailment --> not_entailment
                  original premise: """Решение носит символический характер, так как взыскать компенсацию практически невозможно"", - отмечается в сообщении."
                  original hypothesis: Взыскать компенсацию не получится.
                  
                  transformed: не компенсацию Взыскать получится .
```
Convert results to DataFrame
```
>>> dataframe = pd.DataFrame(results)
```
