# AI Cover Letter Generator

The **AI Cover Letter Generator** is a Streamlit-based application that automates the creation of personalized cover letters for job applications. It uses advanced natural language processing (NLP) techniques powered by the **Groq API** (with the `llama-3.1-70b-versatile` model) to extract job details from a provided URL and generate tailored cover letters based on the user's resume and portfolio.

## Features
- **Job Description Extraction**: Extracts job details (role, experience, skills, and description) from a job posting URL.
- **Personalized Cover Letters**: Generates cover letters tailored to the job description and the user's skills, experience, and portfolio links.
- **Resume Parsing**: Reads and processes a Word document (`my_resume.docx`) to extract relevant information (e.g., skills, experience, education, and portfolio links).
- **Vector Database Integration**: Uses **ChromaDB** to store and query resume data for efficient retrieval.
- **Streamlit Interface**: Provides an intuitive and user-friendly web interface for generating cover letters.

---

## File Structure
```
.
├── __pycache__/                  # Python cache files
├── resource/                     # Contains user-specific resources
│   └── my_resume.docx            # User's resume in Word format
├── vectorstore/                  # ChromaDB vector database files
│   ├── a29e36c3-1a2e-41a8-b678-b1f67b0af0ad
│   └── chroma.sqlite3
├── .env                          # Environment variables (e.g., GROQ_API_KEY)
├── .gitignore                    # Specifies files to ignore in Git
├── LICENSE                       # License file (MIT License)
├── README.md                     # This file
├── chains.py                     # Contains logic for job extraction and cover letter generation
├── main.py                       # Streamlit app entry point
├── portfolio.py                  # Handles resume parsing and ChromaDB integration
├── requirements.txt              # Python dependencies
└── utils.py                      # Utility functions (e.g., text cleaning)
```

---

## How It Works
1. **Job Description Extraction**:
   - The user provides a URL to a job posting.
   - The application scrapes the webpage and extracts job details (role, experience, skills, and description) using the Groq API.

2. **Resume Parsing**:
   - The application reads the user's resume (`my_resume.docx`) and extracts relevant sections (e.g., skills, experience, education, and portfolio links).
   - The extracted data is stored in a **ChromaDB** vector database for efficient querying.

3. **Cover Letter Generation**:
   - The application matches the job requirements with the user's skills and experience.
   - It generates a personalized cover letter using the Groq API, incorporating relevant portfolio links and tailored content.

---

## Prerequisites
- Python 3.12 or higher
- A **Groq API key** (sign up at [Groq](https://groq.com/))
- A Word document (`my_resume.docx`) containing your resume in the following format:
  - **Headings**: Use headings like "Techstack", "Links", "Experience", and "Education" to structure your resume.
  - **Content**: Add relevant details under each heading.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Monish-Nallagondalla/AI_CoverLetter_generator.git
   cd AI_CoverLetter_generator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the root directory.
   - Add your Groq API key:
     ```plaintext
     GROQ_API_KEY=your_groq_api_key_here
     ```

4. Place your resume in the `resource` folder and name it `my_resume.docx`.

---

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

2. Open the app in your browser (usually at `http://localhost:8501`).

3. Enter the URL of a job posting and click **Submit**.

4. The app will generate a personalized cover letter based on the job description and your resume. The output will be displayed in Markdown format.

---

## Code Overview
### Key Files
- **`main.py`**: The entry point for the Streamlit app. Handles user input and displays the generated cover letter.
- **`chains.py`**: Contains the logic for extracting job details and generating cover letters using the Groq API.
- **`portfolio.py`**: Handles resume parsing and integrates with ChromaDB for storing and querying resume data.
- **`utils.py`**: Provides utility functions (e.g., cleaning text from web scrapes).

---

## Example
### Input
- **Job Posting URL**: `https://example.com/job-posting`
- **Resume**: `resource/my_resume.docx`

### Output
```markdown
Dear Hiring Manager,

I am excited to apply for the Data Scientist position at [Company Name]. With my expertise in analyzing data, developing machine learning models, and creating data-driven solutions, I am confident in my ability to contribute to your team.

In my previous role at [Previous Company], I successfully [specific achievement or project]. I have also worked on [another project], which aligns closely with the requirements of this role.

You can find more details about my work in my portfolio: [Portfolio Link].

Thank you for considering my application. I look forward to the opportunity to discuss how I can contribute to your team.

Best regards,
Monish
```

---

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contributing
Contributions are welcome! If you'd like to contribute, please:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request.

---

## Future Improvements
- Add support for PDF resumes.
- Allow users to customize the tone and style of the cover letter.
- Integrate with additional job boards for automated job posting retrieval.

---

## Questions or Issues?
If you have any questions or encounter issues, feel free to open an issue on the [GitHub repository](https://github.com/Monish-Nallagondalla/AI_CoverLetter_generator/issues).
```
