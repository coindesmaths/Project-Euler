from pathlib import Path


class Data:

    def init(n):
        data_directory = Path("data")

        s = str(n).zfill(4)

        for file in data_directory.iterdir():
            if not file.is_file():
                continue
            if file.name.startswith(s):
                with open(file.absolute(), "r", encoding="utf-8") as f:
                    return f.read()
        raise ValueError("Pas de données pour ce problème.")


if __name__ == "__main__":
    data = Data.init(22)
    print(data.split(","))
