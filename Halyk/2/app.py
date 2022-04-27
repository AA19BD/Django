import fitz

pdf_document = "source/image-segmentation-by-local-entropy-methods.pdf"
doc = fitz.open(pdf_document)

print(f'Num of pages {doc.pageCount}')
print(f'Metadata {doc.metadata}')
print("---------------")

for current_page in range(len(doc)):
    page = doc.loadPage(current_page)
    page_text = page.getText()
    print(page_text)
