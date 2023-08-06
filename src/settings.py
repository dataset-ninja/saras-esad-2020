from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "SARAS-ESAD 2020"
PROJECT_NAME_FULL: str = "SARAS Endoscopic Vision Challenge for Surgeon Action Detection 2020"

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_NC_SA_3_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Medical(), Industry.Robotics()]
CATEGORY: Category = Category.Medical(
    benchmark=True, extra=Category.Robotics(), sensitive_content=True
)

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = "2020-06-15"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://saras-esad.grand-challenge.org/Home/"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 695814
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/saras-esad-2020"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "Training_Dataset": "https://drive.google.com/file/d/1CnYAzZRVEDGK1TycGBb8SnMgyvzeZrie/view?usp=sharing",
    "Validation dataset": "https://drive.google.com/file/d/17rWwuWKFZFxQ0DTRs5cmUzU2Vb5PScol/view?usp=sharing",
    "Test dataset Images": "https://drive.google.com/file/d/1gho-oGzUbNgnZmBZ2GDKWWOcs1VI-z0O/view?usp=sharing",
    "Test dataset Labels": "https://drive.google.com/file/d/16srrq1NIso1mI2YKtHMIPyn5bZbcCyo3/view?usp=sharing",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "CuttingMesocolon": [0, 0, 255],
    "PullingVasDeferens": [255, 165, 0],
    "ClippingVasDeferens": [255, 192, 203],
    "CuttingVasDeferens": [210, 105, 30],
    "ClippingTissue": [139, 69, 19],
    "PullingSeminalVesicle": [127, 255, 0],
    "ClippingSeminalVesicle": [240, 230, 140],
    "CuttingSeminalVesicle": [127, 255, 212],
    "SuckingBlood": [218, 165, 32],
    "SuckingSmoke": [255, 0, 0],
    "PullingTissue": [0, 255, 0],
    "CuttingTissue": [255, 255, 0],
    "BaggingProstate": [255, 0, 255],
    "BladderNeckDissection": [0, 255, 255],
    "BladderAnastomosis": [128, 0, 0],
    "PullingProstate": [0, 128, 0],
    "ClippingBladderNeck": [0, 0, 128],
    "CuttingThread": [128, 128, 0],
    "UrethraDissection": [128, 0, 128],
    "CuttingProstate": [0, 128, 128],
    "PullingBladderNeck": [75, 0, 130],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = "https://arxiv.org/abs/2006.07164"
CITATION_URL: Optional[str] = "https://arxiv.org/abs/2006.07164"
AUTHORS: Optional[List[str]] = [
    "Vivek Singh Bawa",
    "Gurkirt Singh",
    "Francis KapingA",
    "Inna Skarga-Bandurova",
    "Alice Leporini",
    "Carmela Landolfo",
    "Armando Stabile",
    "Francesco Setti",
    "Riccardo Muradore",
    "Elettra Oleari",
    "Fabio Cuzzolin",
]

ORGANIZATION_NAME: Optional[
    Union[str, List[str]]
] = "Smart Autonomous Robotic Assistant Surgeon (SARAS) EU Consortium"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "http://saras-project.eu/"

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
