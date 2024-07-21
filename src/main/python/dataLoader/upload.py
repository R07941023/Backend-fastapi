from fastapi import UploadFile

async def decode_file(files: list) -> list:
    res = []
    ext_type = get_ext_type()
    for file in files:
        if any(file.filename.endswith(ext) for ext in ext_type['utf8_type']):
            res += [await txt_decode(file)]
        else:
            print('file extention can not be support')  
    return res    

def get_ext_type() -> dict:
    res = {}
    res['utf8_type'] = ['.sh', '.txt', 'ini']
    return res


async def txt_decode(file: UploadFile) -> dict:
    file_binary = await file.read()
    data = {"filename": file.filename, "data": file_binary.decode("utf-8")}
    return data

