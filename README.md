# Dog Show Entry Processor

A tool to process dog show entries from Excel and generate LaTeX formatted documents.

## Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd CSC26
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare your data file**
   - Copy `Entries_template.xlsx` to `Entries.xlsx`
   - Fill in your actual data in `Entries.xlsx`
   - `Entries.xlsx` is in `.gitignore` and won't be committed

## Excel File Format

The `Entries.xlsx` file should have 8 columns:
1. **Dog Name** - Name of the dog
2. **Handler** - Handler's name
3. **Registration Number** - ISDS or other registration number
4. **Sire** - Father's name
5. **Breeder** - Breeder's name
6. **Date of Birth** - DOB of the dog
7. **Dam** - Mother's name
8. **Photo Path** - Relative path to dog's photo (e.g., `pictures_orig/handler_dogname.jpg`)

## Usage

1. **Process the Excel file**
   ```bash
   python read_excel.py
   ```
   This will read `Entries.xlsx` and generate `entries.tex`

2. **Compile the LaTeX document**
   ```bash
   pdflatex draft_mit_arlo.tex
   ```

## File Structure

```
.
├── read_excel.py           # Python script to process Excel data
├── draft_mit_arlo.tex      # Main LaTeX document
├── Entries_template.xlsx   # Template file (committed to repo)
├── Entries.xlsx            # Your actual data (NOT committed - in .gitignore)
├── entries.tex             # Generated file (NOT committed - in .gitignore)
├── requirements.txt        # Python dependencies
├── pictures_orig/          # Directory for dog photos
└── README.md              # This file
```

## Security Note

**Never commit `Entries.xlsx` with real participant data!** 
- The template file `Entries_template.xlsx` contains only example data
- Your actual `Entries.xlsx` file is protected by `.gitignore`
- Always verify `.gitignore` is working before committing
