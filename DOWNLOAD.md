Dataset **SARAS-ESAD 2020** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/p/r/kz/eHeXvQwxQSB38OZuf2eOQDjVzsKKGqGMDLHZuC9qvh9SApTeAa4tKh9GKpcrjtAnc5IuZl7u9duukXipIKdEQe19AmjujEfTg6mgpKrmCbw89KlOoE7xSdTMk3M2.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='SARAS-ESAD 2020', dst_path='~/dtools/datasets/SARAS-ESAD 2020.tar')
```
The data in original format can be downloaded here:

- 🔗[Training_Dataset](https://drive.google.com/file/d/1CnYAzZRVEDGK1TycGBb8SnMgyvzeZrie/view?usp=sharing)
- 🔗[Validation dataset](https://drive.google.com/file/d/17rWwuWKFZFxQ0DTRs5cmUzU2Vb5PScol/view?usp=sharing)
- 🔗[Test dataset Images](https://drive.google.com/file/d/1gho-oGzUbNgnZmBZ2GDKWWOcs1VI-z0O/view?usp=sharing)
- 🔗[Test dataset Labels](https://drive.google.com/file/d/16srrq1NIso1mI2YKtHMIPyn5bZbcCyo3/view?usp=sharing)
