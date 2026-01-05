from pathlib import Path

from utils import Phenomer

class OpenSLR149:
    def __init__(self):
        self.data_dir = Path("data/tsang")
        self.transcript_file = self.data_dir / "tsangsyl.txt"

        self.output_dir = Path("processed")

    def read_transcript(self) -> list[tuple[str, str]]:
        content = self.transcript_file.read_text(encoding='utf-8')
        rows = content.strip().split('\n')
        rows = [row for row in rows if row.strip()]

        data = []
        for row in rows:
            file_name = row.split()[0]
            syls = ' '.join(row.split()[1:])
            data.append((file_name, syls))
        return data
        
    def transform(self):
        """
        Transform data to LJSpeech format.(For training VITS model)
        Output format: <file_name> <phoneme_sequence>
        """
        phenomer = Phenomer()
        rows = self.read_transcript()
        
        output_rows = []
        unique_symbols = set()
        for file_name, syls in rows:
            phoneme_seq = phenomer.run(syls)
            unicode_bo_text = "་".join(syls.split())
            output_rows.append(f"{file_name}|{unicode_bo_text}")
            unique_symbols.update(phoneme_seq.split())
        
        # Ensure the output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # 1. Write the metadata file
        metadata_file = self.output_dir / "metadata.csv"
        metadata_file.write_text('\n'.join(output_rows), encoding='utf-8')
        
        # 2. Write unique symbols to a file
        # Sorting them makes the list easier to read and verify
        sorted_symbols = sorted(list(unique_symbols))
        symbols_file = self.output_dir / "unique_symbols.txt"
        
        # Joining with spaces as needed for your VITS config
        symbols_file.write_text(' '.join(sorted_symbols), encoding='utf-8')


if __name__ == "__main__":
    processor = OpenSLR149()
    processor.transform()
    print("Transformation complete!")
    