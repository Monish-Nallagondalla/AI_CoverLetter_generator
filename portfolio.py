import pandas as pd
import chromadb
import uuid
import docx


class Portfolio:
    def __init__(self, file_path="resource/my_resume.docx"):
        self.file_path = file_path
        self.data = self._read_word_file(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def _read_word_file(self, file_path):
        doc = docx.Document(file_path)
        text = []
        sections = {'Techstack': [], 'Links': [], 'Experience': [], 'Education': []}
        current_section = None

        for paragraph in doc.paragraphs:
            if paragraph.style.name.startswith('Heading'):
                # Identify sections based on headings
                heading = paragraph.text.lower()
                if 'skills' in heading or 'tech' in heading:
                    current_section = 'Techstack'
                elif 'links' in heading or 'portfolio' in heading:
                    current_section = 'Links'
                elif 'experience' in heading:
                    current_section = 'Experience'
                elif 'education' in heading:
                    current_section = 'Education'
            elif current_section and paragraph.text.strip():
                sections[current_section].append(paragraph.text)

        return pd.DataFrame([{
            'Techstack': '\n'.join(sections['Techstack']),
            'Links': '\n'.join(sections['Links']),
            'Experience': '\n'.join(sections['Experience']),
            'Education': '\n'.join(sections['Education'])
        }])

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=[row["Techstack"], row["Experience"]],
                    metadatas=[
                        {"type": "skills", "links": row["Links"]},
                        {"type": "experience", "education": row["Education"]}
                    ],
                    ids=[str(uuid.uuid4()), str(uuid.uuid4())]
                )

    def query_links(self, skills):
        results = self.collection.query(
            query_texts=skills,
            n_results=2,
            where={"type": "skills"}
        )
        return results.get('metadatas', [])

    def get_experience(self):
        results = self.collection.query(
            query_texts=["experience"],
            n_results=1,
            where={"type": "experience"}
        )
        return results.get('metadatas', [])

    def get_education(self):
        results = self.collection.query(
            query_texts=["education"],
            n_results=1,
            where={"type": "experience"}
        )
        return results.get('metadatas', [])
