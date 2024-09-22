from fastapi import APIRouter


router = APIRouter( tags=['Докуметы'])


@router.get("/document_text/{document_id}", summary="Получить один документ")
async def get_document(document_id:int) -> str:
    # rez = await StudentDAO.find_one_or_none(**request_body.to_dict())
    # if rez is None:
    #     return {'message': f'Студент с указанными вами параметрами не найден!'}
    return "Описание"
#