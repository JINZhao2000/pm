import uvicorn
import threading
from utils.utils import fhost, fport, chost, cport
import client.main as cli
import fournisseur.main as four


def run_uvicorn(app, host, port):
    uvicorn.run(app, host=host, port=port)


if __name__ == '__main__':
    t1 = threading.Thread(target=run_uvicorn, args=(cli.app, chost, cport))
    t2 = threading.Thread(target=run_uvicorn, args=(four.app, fhost, fport))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
