# upload_openpecha_ljspeech_to_hub.py
import os
import pandas as pd
from datasets import Dataset, DatasetDict, Audio, Features, Value

DATA_DIR = "data/tsang_LJSpeech"            
META_PATH = os.path.join(DATA_DIR, "metadata.csv")
WAV_DIR = os.path.join(DATA_DIR, "wavs")

HF_DATASET_REPO = "tenzin3/openslr_149_tsang"  
SEED = 456
TEST_SIZE = 0.05

df = pd.read_csv(
    META_PATH,
    sep="|",
    header=None,
    names=["id", "uni"],
    dtype=str,
    keep_default_na=False,
)

# Build wav path: wavs/<id>.wav
df["audio"] = df["id"].apply(lambda x: os.path.join(WAV_DIR, f"{x}.wav"))

# Optional: validate file existence (highly recommended)
missing = df.loc[~df["audio"].apply(os.path.exists)]
if len(missing) > 0:
    print("Missing audio files for these ids (showing up to 20):")
    print(missing[["id", "audio"]].head(20).to_string(index=False))
    raise FileNotFoundError(f"Found {len(missing)} missing audio files. Fix paths before upload.")

# Keep only the columns your trainer expects
df = df[["audio", "uni"]]

# Create HF dataset with proper types
features = Features({
    "audio": Audio(),         # HF audio feature
    "uni": Value("string"),   # Tibetan text
})
ds = Dataset.from_pandas(df, features=features, preserve_index=False)

# Create splits (train/test) for your config
ds = ds.train_test_split(test_size=TEST_SIZE, seed=SEED)
dd = DatasetDict(train=ds["train"], test=ds["test"])

# Push to hub (make sure you've done: huggingface-cli login)
dd.push_to_hub(HF_DATASET_REPO)
print("Uploaded dataset to:", HF_DATASET_REPO)
