# BoTTS
## Dataset: OpenSLR SLR149 (TTS Data)

- **Source**: https://openslr.org/149/
- **Status**: Imported and tracked in this repository.
- **Location**: `data/`

### Description
This project uses the dataset distributed on OpenSLR as SLR149. The data has been downloaded from the link above and is included under the `data/` directory, preserving the original archive's folder structure when possible.

### Repository layout
- **Root folder for dataset**: `data/`
- **Example subfolder**: You may find subsets or transcriptions in subdirectories such as `data/tsang/` (e.g., `data/tsang/tsangsyl.txt`). Your exact structure may vary depending on what you extracted from the archive.

### How to use in this repo
- Reference dataset files via paths under `data/`.
- Keep any local preprocessing or generated artifacts within a separate folder (e.g., `data/processed/`) to avoid modifying the original files.

### Attribution and citation
- Please refer to the dataset page at https://openslr.org/149/ for the official description, license, and citation information.
- If you publish work based on this repository, include a citation to the dataset as directed on the OpenSLR page.
