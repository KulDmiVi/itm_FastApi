from fastapi import APIRouter, UploadFile
from app.documents.models import Documents
from app.documents.dao import DocumentsDAO
router = APIRouter( tags=['Докуметы'])





@router.post("/doc_upload/", summary="Загрузка документов")
async def add_document(file: UploadFile) -> dict:
    try:
        file_path = f"{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        new_document = Documents()
        new_document.path = file_path
        new_document_id = await DocumentsDAO.add_document(new_document)
        return {"200 OK": new_document_id}
    except Exception as e:
        return {"message": e.args}


@router.delete("/doc_delete/{document_id}", summary="Удаление документа по id")
async def del_document(document_id: int) -> dict:
    check = await DocumentsDAO.delete_document_by_id(document_id)
    if check:
        return {"message": f"Документ с ID {document_id} удален!"}
    else:
        return {"message": "Ошибка при удалении документа!"}


#
# @router.get("/doc_analyz/", summary="Получение документов")
# async def get_document(document_id:int) -> str:
#     # rez = await StudentDAO.find_one_or_none(**request_body.to_dict())
#     # if rez is None:
#     #     return {'message': f'Студент с указанными вами параметрами не найден!'}
#     return "Описание"