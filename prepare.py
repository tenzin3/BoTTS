from pathlib import Path 

class OpenSLR149:
    def __init__(self):
        self.data_dir = Path("data/tsang")
        self.transcript_file = self.data_dir / "tsangsyl.txt"

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
        
    def prepare(self):
        pass
        

if __name__ == "__main__":
    processor = OpenSLR149()
    rows = processor.read_transcript()
    print(f"Read {len(rows)} rows from transcript")