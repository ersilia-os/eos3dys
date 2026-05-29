This model has been financed by Project PID2023-148309OA-I00 funded by MICIU/AEI/10.13039/501100011033 and by ERDF, EU.
<img width="200" alt="MICIU+Cofinanciado+AEI" src="https://github.com/user-attachments/assets/aa3c3ed0-1eda-47fe-a7cb-478c4e3839a6" />
# CoADD antimicrobial prediction

Array of bioactivity ML models based on the CoADD data. We have built individual models for each organism and strain for which sufficient data (>100 compounds) is available. Additional cytotoxicity models have also been included. Cut-offs for binary activity are determined at 50% for percentage of inhibition and 25 uM for dose-response assays. All models achieved an AUROC > 0.7 using the LazyQSAR package. Detailed analysis is available in this [repository](https://github.com/ersilia-os/coadd-binary-tasks)

This model was incorporated on 2026-05-19.Last packaged on 2026-05-20.

## Information
### Identifiers
- **Ersilia Identifier:** `eos3dys`
- **Slug:** `coadd-antimicrobial-activity`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Antimicrobial resistance`
- **Target Organism:** `Acinetobacter baumannii`, `Candida albicans`, `Klebsiella pneumoniae`, `Pseudomonas aeruginosa`, `Staphylococcus aureus`, `Cryptococcus neoformans`, `Candida glabrata`, `Cryptococcus deuterogattii`, `Homo sapiens`
- **Tags:** `Antimicrobial activity`, `ESKAPE`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `22`
- **Output Consistency:** `Fixed`
- **Interpretation:** Classification score (rank) for pathogen inhibition, with higher scores indicating stronger predicted activity.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| abaumannii_ATCC19606_inhib_50 | float | high | Classification score (rank) for bioactivity in Acinetobacter baumannii ATCC19606 |
| abaumannii_ATCC19606_mic_25 | float | high | Classification score (rank) for bioactivity in Acinetobacter baumannii ATCC19606 |
| calbicans_ATCC90028_inhib_50 | float | high | Classification score (rank) for bioactivity in Candida albicans ATCC90028 |
| calbicans_ATCC90028_mic_25 | float | high | Classification score (rank) for bioactivity in Candida albicans ATCC90028 |
| cdeuterogattii_CBS7750_mic_25 | float | high | Classification score (rank) for bioactivity in Cryptococcus deuterogattii CBS7750 |
| cglabrata_ATCC90030_mic_25 | float | high | Classification score (rank) for bioactivity in Candida glabrata ATCC90030 |
| cneoformans_H99_inhib_50 | float | high | Classification score (rank) for bioactivity in Cryptococcus neoformans H99 |
| cneoformans_H99_mic_25 | float | high | Classification score (rank) for bioactivity in Cryptococcus neoformans H99 |
| ecoli_ATCC25922_inhib_50 | float | high | Classification score (rank) for bioactivity in Escherichia coli ATCC25922 |
| ecoli_ATCC25922_mic_25 | float | high | Classification score (rank) for bioactivity in Escherichia coli ATCC25922 |

_10 of 22 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos3dys](https://hub.docker.com/r/ersiliaos/eos3dys)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos3dys.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos3dys.zip)

### Resource Consumption
- **Model Size (Mb):** `600`
- **Environment Size (Mb):** `1888`
- **Image Size (Mb):** `3214.14`

**Computational Performance (seconds):**
- 10 inputs: `56.28`
- 100 inputs: `48.55`
- 10000 inputs: `1357.18`

### References
- **Source Code**: [https://github.com/ersilia-os/coadd-binary-tasks](https://github.com/ersilia-os/coadd-binary-tasks)
- **Publication**: [https://co-add.org](https://co-add.org)
- **Publication Type:** `Other`
- **Publication Year:** `2026`
- **Ersilia Contributor:** [GemmaTuron](https://github.com/GemmaTuron)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-only](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos3dys
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos3dys
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
