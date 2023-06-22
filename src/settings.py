from typing import Dict, List, Optional, Union

from dataset_tools.templates import AnnotationType, CVTask, Industry, License

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "SARAS-ESAD 2020"
PROJECT_NAME_FULL: str = "SARAS endoscopic vision challenge for surgeon action detection 2020"

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_NC_SA_3_0()
INDUSTRIES: List[Industry] = [Industry.Medical()]
CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_YEAR: int = 2020
HOMEPAGE_URL: str = "https://saras-esad.grand-challenge.org/Home/"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 740115
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
    "CuttingMesocolon":[128, 128, 128],
    "PullingVasDeferens":[255, 165, 0],
    "ClippingVasDeferens":[255, 192, 203],
    "CuttingVasDeferens":[210,105,30],
    "ClippingTissue":[139,69,19],
    "PullingSeminalVesicle":[112,128,144],
    "ClippingSeminalVesicle":[240,230,140],
    "CuttingSeminalVesicle":[176,196,222],
    "SuckingBlood":[218,165,32],
    "SuckingSmoke":[255, 0, 0],
    "PullingTissue":[0, 255, 0],
    "CuttingTissue":[255, 255, 0],
    "BaggingProstate":[255, 0, 255],
    "BladderNeckDissection":[0, 255, 255],
    "BladderAnastomosis":[128, 0, 0],
    "PullingProstate":[0, 128, 0],
    "ClippingBladderNeck":[0, 0, 128],
    "CuttingThread":[128, 128, 0],
    "UrethraDissection":[128, 0, 128],
    "CuttingProstate":[0, 128, 128],
    "PullingBladderNeck":[192, 192, 192],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = "https://arxiv.org/abs/2006.07164"
CITATION_URL: Optional[str] = None
ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "(SARAS) Smart Autonomous Robotic Assistant Surgeon EU consortium"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "http://saras-project.eu/"
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "industries": INDUSTRIES,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["tags"] = TAGS if TAGS is not None else []

    return settings
