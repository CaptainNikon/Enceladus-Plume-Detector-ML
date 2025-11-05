## Enceladus Plume Detection with Cassini INMS Data

This repository now contains updated analysis scripts and notebooks focused on detecting Enceladus plume flybys in data from the **Cassini Ion and Neutral Mass Spectrometer (INMS)** instrument.

> **Note:** The original CDA dust-impact analysis pipeline and all legacy scripts remain available in this repository for reference and reproducibility. See the _Legacy CDA Analysis_ section below.

## Data Source

All INMS data used in this project are publicly available from NASA’s **Planetary Data System (PDS)**, specifically:

> NASA Planetary Data System (PDS), Cassini INMS  
> [https://pds-ppi.igpp.ucla.edu/collection/CO-S-INMS-2-PKT-U-V1.0:DATA](https://pds-ppi.igpp.ucla.edu/collection/CO-S-INMS-2-PKT-U-V1.0:DATA)

>Gell, D.,A., CO-S-INMS-2-PKT-U-V1.0, CASSINI S INMS TELEMETRY PACKET DATA V1.0, NASA Planetary Data System, 2018.
> [10.17189/1519604](https://doi.org/10.17189/1519604)

When using this repository or any derived data, please cite the original INMS instrument paper and acknowledge NASA’s PDS:

> Waite, J.H., Young, D.T., Cravens, T.E., *et al.* (2004).  
> _The Cassini Ion and Neutral Mass Spectrometer (INMS) Investigation._  
> **Space Science Reviews**, 114(1–4), 113–231.  
> [https://doi.org/10.1007/s11214-004-1408-2](https://doi.org/10.1007/s11214-004-1408-2)

## Legacy CDA Analysis

This repository previously centered on **dust impact detection** using Cassini’s Cosmic Dust Analyzer (CDA):

> Srama, R., Ahrens, T.J., Altobelli, N., *et al.* (2004).  
> _The Cassini Cosmic Dust Analyzer._ **Space Science Reviews**, 114(1–4), 465–518.  
> [https://doi.org/10.1023/B:SPAC.0000046755.70579.e6](https://doi.org/10.1023/B:SPAC.0000046755.70579.e6)

CDA scripts are retained in the `cda/` and `legacy_cda_analysis/` subfolders for replicability and as a reference for dust-based plume detection.

## Acknowledgment

This project uses data produced by the Cassini INMS and CDA instrument teams and archived in the NASA Planetary Data System (PDS).

## License

Unless otherwise stated, code in this repository is released under the MIT License. See the `LICENSE` file for details.

---

**Summary:**  
* Current analysis focuses on Enceladus plume detection via Cassini INMS data  
* Original CDA code and documentation is preserved for legacy research and comparison