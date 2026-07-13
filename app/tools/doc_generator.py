from datetime import datetime
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from xml.sax.saxutils import escape

from app.config import OUTPUT_DIR


def create_document(content: str, title: str = "Generated Document") -> str:
    """Create a simple Word document from the provided content without native dependencies."""
    output_dir = Path(OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_title = "".join(
        ch if ch.isalnum() or ch in "-_" else "_" for ch in title.lower()
    )
    document_path = output_dir / f"{safe_title}_{timestamp}.docx"

    paragraphs = []
    for line in [title, ""] + content.splitlines():
        paragraphs.append(f"<w:p><w:r><w:t>{escape(line)}</w:t></w:r></w:p>")

    document_xml = f"""<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
    <w:document xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\">
      <w:body>
        {''.join(paragraphs)}
        <w:sectPr>
          <w:pgSz w:w=\"12240\" w:h=\"15840\"/>
          <w:pgMar w:top=\"1440\" w:right=\"1440\" w:bottom=\"1440\" w:left=\"1440\" w:header=\"708\" w:footer=\"708\" w:gutter=\"0\"/>
        </w:sectPr>
      </w:body>
    </w:document>"""

    content_types = """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
    <Types xmlns=\"http://schemas.openxmlformats.org/package/2006/content-types\">
      <Default Extension=\"rels\" ContentType=\"application/vnd.openxmlformats-package.relationships+xml\"/>
      <Default Extension=\"xml\" ContentType=\"application/xml\"/>
      <Override PartName=\"/word/document.xml\" ContentType=\"application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml\"/>
    </Types>"""

    relationships = """<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>
    <Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\">
      <Relationship Id=\"rId1\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument\" Target=\"word/document.xml\"/>
    </Relationships>"""

    with ZipFile(document_path, "w", ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", content_types)
        archive.writestr("_rels/.rels", relationships)
        archive.writestr("word/document.xml", document_xml)

    return str(document_path)
