import photoshop.api as ps
from photoshop import Session

app = ps.Application()
app.load("E:/US/TSHIRT/9.5/IARTGROUP_F_M-BLACK_20230904162610_KXMJRODAY_1-1_front.pdf")

with Session() as sess:
    doc = sess.active_document
    options = sess.PDFSaveOptions()
    doc.saveAs(
        "F:/Input2/IARTGROUP_F_M-BLACK_20230904162610_KXMJRODAY_1-1_front.pdf",
        options,
        True,
    )
