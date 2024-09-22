from fastapi import APIRouter, Depends


router = APIRouter( tags=['Документы'])


@router.get("/document/{document_id}", summary="Получить один документ")
async def get_document(document_id:int) -> str:
    # rez = await StudentDAO.find_one_or_none(**request_body.to_dict())
    # if rez is None:
    #     return {'message': f'Студент с указанными вами параметрами не найден!'}
    return "Документ"
#
#
# @router.post("/doc_upload/")
# async def add_student(student: SStudentAdd) -> dict:
#     check = await StudentDAO.add_student(**student.dict())
#     if check:
#         return {"message": "Студент успешно добавлен!", "student": student}
#     else:
#         return {"message": "Ошибка при добавлении студента!"}
#
#
# @router.delete("/doc_delete/{document_id}")
# async def dell_document_by_id(document_id: int) -> dict:
#     pass
#     # check = await StudentDAO.delete_student_by_id(student_id=student_id)
#     # if check:
#     #     return {"message": f"Студент с ID {student_id} удален!"}
#     # else:
#     #     return {"message": "Ошибка при удалении студента!"}