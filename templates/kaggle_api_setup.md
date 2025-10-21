# Kaggle API Setup (macOS/Linux)

1) Create a Kaggle account and go to **Account** -> **Create New API Token**.
   This downloads `kaggle.json`.

2) Move the file and fix permissions:
```bash
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

3) Test:
```bash
kaggle competitions list | head
```

4) Download a competition dataset (example: Titanic):
```bash
cd competitions/titanic
make download COMP=titanic
unzip -d data/ data/titanic.zip
```

5) Submit (example):
```bash
make submit COMP=titanic SUB=submissions/sub_v1.csv MSG="lgbm baseline 5fold"
```
