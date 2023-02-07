import subprocess
subprocess.call(['pip', 'install', 'pyotritonclient', 'kaibu-utils'])

import io
from PIL import Image
import numpy as np
from pyotritonclient import execute

image = np.random.randint(0, 255, size=(1, 1, 256, 256), dtype=np.uint8).astype(
    "float32"
)
kwargs = {
    "inputs": [image],
    "model_id": "affable-shark",
    "return_rdf": True,
}

async def run():
    ret = await execute(
        [kwargs],
        server_url='http://127.0.0.1:9520/triton', # <-------------change the server url here
        model_name="bioengine-model-runner",
        serialization="imjoy",
    )
    result = ret["result"]
    assert "rdf" in result
    assert result["success"] == True, result["error"]
    print("Test passed", result["outputs"][0].shape)

if __name__ == "__main__":
    import asyncio
    asyncio.run(run())