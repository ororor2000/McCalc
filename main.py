import json
from pathlib  import Path

from models.McManager import McManager

try:
    base_path = Path(__file__).parent
    path = (base_path / "data/data.json").resolve()

    file = open(path, "r", encoding="utf-8")

    data = json.loads(file.read())

    manager = McManager(data)
    
    a = manager.build_order([1,8,9], 2)
    x=5

except Exception as err:
    print(err)