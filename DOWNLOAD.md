Dataset **SARAS-ESAD 2020** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMTEyNF9TQVJBUy1FU0FEIDIwMjAvc2FyYXMtZXNhZC0yMDIwLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogIkUyOEgwaldnN3JYWURtZFc4VVd6MW9sRjJneWlFak5zZVhkdUFtYW9MZEU9In0=?response-content-disposition=attachment%3B%20filename%3D%22saras-esad-2020-DatasetNinja.tar%22)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='SARAS-ESAD 2020', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [Training_Dataset](https://drive.google.com/file/d/1CnYAzZRVEDGK1TycGBb8SnMgyvzeZrie/view?usp=sharing)
- [Validation dataset](https://drive.google.com/file/d/17rWwuWKFZFxQ0DTRs5cmUzU2Vb5PScol/view?usp=sharing)
- [Test dataset Images](https://drive.google.com/file/d/1gho-oGzUbNgnZmBZ2GDKWWOcs1VI-z0O/view?usp=sharing)
- [Test dataset Labels](https://drive.google.com/file/d/16srrq1NIso1mI2YKtHMIPyn5bZbcCyo3/view?usp=sharing)
