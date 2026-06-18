from pypdf import PdfReader


def read_txt_file(uploaded_file):
    """
    Read text from an uploaded .txt file.
    """

    return uploaded_file.read().decode("utf-8")


def read_pdf_file(uploaded_file):
    """
    Read text from an uploaded PDF file.
    """

    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_text_from_file(uploaded_file):
    """
    Extract text from uploaded .txt or .pdf file.
    """

    if uploaded_file is None:
        return ""

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".txt"):
        return read_txt_file(uploaded_file)

    if file_name.endswith(".pdf"):
        return read_pdf_file(uploaded_file)

    return ""