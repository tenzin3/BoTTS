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
        phenomer = Phenomer(    )
        rows = self.read_transcript()
        
        output_rows = []
        for file_name, syls in rows:
            phoneme_seq = phenomer.run(syls)
            output_rows.append(f"{file_name}|{phoneme_seq}|tsang")
        
        # Write to output file
        self.output_dir.mkdir(parents=True, exist_ok=True)
        output_file = self.output_dir / "metadata.csv"
        output_file.write_text('\n'.join(output_rows), encoding='utf-8')
        

if __name__ == "__main__":
    processor = OpenSLR149()
    processor.transform()
    print("Transformation complete!")
    