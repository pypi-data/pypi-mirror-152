<a href="https://colab.research.google.com/github/PathwayCommons/pathway-abstract-classifier/blob/main/notebooks/tutorial.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/pathwaycommons/pathway-abstract-classifier/main/pathway_abstract_classifier/app.py)
![build](https://github.com/PathwayCommons/pathway-abstract-classifier/actions/workflows/ci-cd.yml/badge.svg)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/PathwayCommons/pathway-abstract-classifier/)
[![codecov](https://codecov.io/gh/PathwayCommons/pathway-abstract-classifier/branch/main/graph/badge.svg?token=uHxwRs5JzD)](https://codecov.io/gh/PathwayCommons/pathway-abstract-classifier)

# Pathway Abstract Classifier

A tool to classify articles with biological pathway information.

## Requirements

This project requires Python 3.8 or 3.9.

## Installation

Set up a virtual environment. Here, we use [miniconda](https://docs.conda.io/en/latest/miniconda.html) to create an environment named `testenv`:

```bash
$ conda create --name testenv python=3.8
$ conda activate testenv
```

```sh
pip install pathway-abstract-classifier
```

## Usage

### Example

Classify one article with biological pathway information and one that clearly does not.

```py
from pathway_abstract_classifier.pathway_abstract_classifier import Classifier

# Example articles
documents = [
    {
        'title': 'YTHDC1-mediated augmentation of miR-30d in repressing pancreatic tumorigenesis via attenuation of RUNX1-induced transcriptional activation of Warburg effect',
        'abstract': 'Pancreatic ductal adenocarcinoma (PDAC) is one of the most lethal human cancers. It thrives in a malnourished environment; however, little is known about the mechanisms by which PDAC cells actively promote aerobic glycolysis to maintain their metabolic needs. Gene Expression Omnibus (GEO) was used to identify differentially expressed miRNAs. The expression pattern of miR-30d in normal and PDAC tissues was studied by in situ hybridization. The role of miR-30d/RUNX1 in vitro and in vivo was evaluated by CCK8 assay and clonogenic formation as well as transwell experiment, subcutaneous xenograft model and liver metastasis model, respectively. Glucose uptake, ATP and lactate production were tested to study the regulatory effect of miR-30d/RUNX1 on aerobic glycolysis in PDAC cells. Quantitative real-time PCR, western blot, Chip assay, promoter luciferase activity, RIP, MeRIP, and RNA stability assay were used to explore the molecular mechanism of YTHDC1/miR-30d/RUNX1 in PDAC. Here, we discover that miR-30d expression was remarkably decreased in PDAC tissues and associated with good prognosis, contributed to the suppression of tumor growth and metastasis, and attenuation of Warburg effect. Mechanistically, the m6A reader YTHDC1 facilitated the biogenesis of mature miR-30d via m6A-mediated regulation of mRNA stability. Then, miR-30d inhibited aerobic glycolysis through regulating SLC2A1 and HK1 expression by directly targeting the transcription factor RUNX1, which bound to the promoters of the SLC2A1 and HK1 genes. Moreover, miR-30d was clinically inversely correlated with RUNX1, SLC2A1 and HK1, which function as adverse prognosis factors for overall survival in PDAC tissues. Overall, we demonstrated that miR-30d is a functional and clinical tumor-suppressive gene in PDAC. Our findings further uncover that miR-30d is a novel target for YTHDC1 through m6A modification, and miR-30d represses pancreatic tumorigenesis via suppressing aerobic glycolysis.'
    },
    {
        'title': 'Loss of 15-lipoxygenase disrupts T reg differentiation altering their pro-resolving functions',
        'abstract': 'Regulatory T-cells (Tregs) are central in the maintenance of homeostasis and resolution of inflammation. However, the mechanisms that govern their differentiation and function are not completely understood. Herein, we demonstrate a central role for the lipid mediator biosynthetic enzyme 15-lipoxygenase (ALOX15) in regulating key aspects of Treg biology. Pharmacological inhibition or genetic deletion of ALOX15 in Tregs decreased FOXP3 expression, altered Treg transcriptional profile and shifted their metabolism. This was linked with an impaired ability of Alox15-deficient cells to exert their pro-resolving actions, including a decrease in their ability to upregulate macrophage efferocytosis and a downregulation of interferon gamma expression in Th1 cells. Incubation of Tregs with the ALOX15-derived specilized pro-resolving mediators (SPM)s Resolvin (Rv)D3 and RvD5n-3 DPA rescued FOXP3 expression in cells where ALOX15 activity was inhibited. In vivo, deletion of Alox15 led to increased vascular lipid load and expansion of Th1 cells in mice fed western diet, a phenomenon that was reversed when Alox15-deficient mice were reconstituted with wild type Tregs. Taken together these findings demonstrate a central role of pro-resolving lipid mediators in governing the differentiation of naive T-cells to Tregs.'

    }
]

# Make predictions. Ktrain may throw a UserWarning which you can safely ignore.
classifier = Classifier()
predictions = classifier.predict(documents)

# Each Prediction contains fields: document, classification and probability
assert prediction[0].classification == 1
assert prediction[1].classification == 0
```

## Testing

From within the directory housing the GitHub repository:

```bash
$ poetry install
```

Run the test script:

```bash
$ ./test.sh
```

Under the hood, the tests are run with [pytest](https://docs.pytest.org/). The test script also does a lint check with [flake8](https://flake8.pycqa.org/) and type check with [mypy](http://mypy-lang.org/).


## Publishing a release

A GitHub workflow will automatically version and release this package to [PyPI](https://pypi.org/) following a push directly to `main` or when a pull request is merged into `main`. A push/merge to `main` will automatically bump up the patch version.

We use [Python Semantic Release (PSR)](https://python-semantic-release.readthedocs.io/en/latest/) to manage versioning. By making a commit with a well-defined message structure, PSR will scan commit messages and bump the version accordingly in accordance with [semver](https://python-poetry.org/docs/cli/#version).

For a patch bump:

```bash
$ git commit -m "fix(app): some comment for this patch version"
```

For a minor bump:

```bash
$ git commit -m "feat(pathway_abstract_classifier): some comment for this minor version bump"
```

For a release:

```bash
$ git commit -m "feat(pathway_abstract_classifier): some comment for this release\n\nBREAKING CHANGE: other footer text."
```


## Resources

See the [tutorial](https://github.com/PathwayCommons/pathway-abstract-classifier/blob/main/notebooks/tutorial.ipynb) (or open it in [Colab](https://colab.research.google.com/github/PathwayCommons/pathway-abstract-classifier/blob/main/notebooks/tutorial.ipynb)) for a more detailed guide on potential usage. Importantly, this tutorial shows how to conduct threshold-moving, which you can learn more about [here](https://deepchecks.com/glossary/classification-threshold/). Also consider taking a look at the Ktrain [documentation](https://amaiya.github.io/ktrain/index.html) and [repo](https://github.com/amaiya/ktrain) which contains some very good tutorials.


