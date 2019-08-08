import pytero

def test_client():
  natero_client = pytero.NateroClient("test_key", region="us")
  natero_client.get()

if __name__ == "__main__":
    test_client()